import sys,getopt

class Argument:

    value = ""
    description = ""
    def __init__(self,key, longForm, shortForm="", hasInput=True,description = ""):
        self.hasLongForm = not longForm == ""
        self.hasShortForm = not shortForm == ""
        self.hasDesc = not description == ""

        self.forms=[]
        if self.hasShortForm:
            self.forms.append("-" + shortForm)
            
        if self.hasLongForm:
            self.forms.append("--" + longForm)
            
        print(self.forms)
        self.longForm = longForm
        self.shortForm = shortForm
        self.key = key

        if self.hasDesc:
            self.setDesc(description)

        self.hasInput = hasInput
        if (hasInput):
            self.longForm+="="
            self.shortForm += ":"

    def setDesc(self, description):
        args = ",".join(self.forms)
        self.description = '{:20}, {}'.format(args, description)
        

class ArgumentsHandler:
    arguments = []

    header = ""
    def __init__(self, *args):
        for arg in args:
            self.arguments.append(arg)

    def printHelp(self):
        print(self.header)
        for arg in self.arguments:
            print(arg.description)
        print("\n")

    def resolve(self,argv):
        self._argv = argv[1:]
        print(self._argv)
        print(self.getLongForms())
        print(self.getShortForms())
        try:
            opts, args = getopt.getopt(self._argv,self.getShortForms(),self.getLongForms())
        except getopt.GetoptError:
            self.printHelp()
            sys.exit(2)

        out = {}
        for opt, arg in opts:
            for argument in self.arguments:
                if opt in argument.forms:
                    argument.value = arg
                    out[argument.key] = argument
        return out


    def getShortForms(self):
        forms = []
        for arg in self.arguments:
            if arg.hasShortForm:
                forms.append(arg.shortForm)
        return "".join(forms)                

    def getLongForms(self):
        forms = []
        for arg in self.arguments:
            if arg.hasLongForm:
                forms.append(arg.longForm)
        return forms   