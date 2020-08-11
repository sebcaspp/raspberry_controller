from controller.main import main
from controller.test import test

import sys
import asyncio

if __name__ == "__main__":
    if sys.argv[1]=="test" :
        asyncio.run( test() )
    else: 
        main()
    