import pyfiglet
import sys
import random
from pyfiglet import Figlet
s = input("Enter a string of text: ")
f = pyfiglet.Figlet()

if len(sys.argv) == 1:
        rndm = random.choice(pyfiglet.FigletFont.getFonts())
        f.setFont(font=rndm)
        print(f.renderText(s))
        
elif len(sys.argv) == 3:
    if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid font")
    f.setFont(font=sys.argv[2])
    print(f.renderText(s))
else:
    
    sys.exit("Invalid font")


    


     

 

