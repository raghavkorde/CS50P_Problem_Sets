import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()


if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if arg2 not in figlet.getFonts() or arg1 not in ['-f', '--font']:
        sys.exit('Invalid usage')
    else:
        text = input('Input:')
        figlet.setFont(font = arg2)
        print(f'Output:')
        print(figlet.renderText(text))
elif len(sys.argv) == 1:
    text = input('Input:')
    select = choice(figlet.getFonts())
    figlet.setFont(font = select)
    print(f'Output:')
    print(figlet.renderText(text))
else :
    sys.exit('Invalid usage')