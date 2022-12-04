import sys, termios,tty


class Getch:

    def getch():
        try:
            orig_settings = termios.tcgetattr(sys.stdin)
            tty.setcbreak(sys.stdout)
            inp = sys.stdin.read(1)[0]
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
            return inp
        except KeyboardInterrupt:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
            quit()
        except:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
	




##Testing:


"""
while True:
    inp = Getch.getch()
    print(inp)
    if inp == "q":
        exit()
        """