	
import sys, getopt
from Argument import *

if __name__ == "__main__":
    handler = ArgumentsHandler(Argument("help","help","h",False,"provides Help"),Argument("test","test","t",description="Testing"))
    result = handler.resolve(sys.argv)
    print(result)

