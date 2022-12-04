RESET = '\033[0m'


BOLD = '\033[1m'
BOLD_OFF = '\033[22m'

ITALICS = '\033[3m'
ITALICS_OFF = '\23m'

UNDERLINE = '\033[4m'
UNDERLINE_OFF = '\033[24m'

BLACK = '\033[0,30m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'

def black(txt, normal = RESET):
    return BLACK+txt+normal
def red(txt, normal = RESET):
    return RED+txt+normal
def green(txt, normal = RESET):
    return GREEN+txt+normal
def yellow(txt, normal = RESET):
    return YELLOW+txt+normal
def blue(txt, normal = RESET):
    return BLUE+txt+normal
def purple(txt, normal = RESET):
    return PURPLE+txt+normal
def cyan(txt, normal = RESET):
    return CYAN+txt+normal
def white(txt, normal = RESET):
    return WHITE+txt+normal
class Bold:
    BLACK = '\033[1;30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'

    def black(txt, normal = RESET):
        return BLACK+txt+normal
    def red(txt, normal = RESET):
        return RED+txt+normal
    def green(txt, normal = RESET):
        return GREEN+txt+normal
    def yellow(txt, normal = RESET):
        return YELLOW+txt+normal
    def blue(txt, normal = RESET):
        return BLUE+txt+normal
    def purple(txt, normal = RESET):
        return PURPLE+txt+normal
    def cyan(txt, normal = RESET):
        return CYAN+txt+normal
    def white(txt, normal = RESET):
        return WHITE+txt+normal

class Underlined:
    BLACK = '\033[4;30m'
    RED = '\033[4;31m'
    GREEN = '\033[4;32m'
    YELLOW = '\033[4;33m'
    BLUE = '\033[4;34m'
    PURPLE = '\033[4;35m'
    CYAN = '\033[4;36m'
    WHITE = '\033[4;37m'

    def black(txt, normal = RESET):
        return BLACK+txt+normal
    def red(txt, normal = RESET):
        return RED+txt+normal
    def green(txt, normal = RESET):
        return GREEN+txt+normal
    def yellow(txt, normal = RESET):
        return YELLOW+txt+normal
    def blue(txt, normal = RESET):
        return BLUE+txt+normal
    def purple(txt, normal = RESET):
        return PURPLE+txt+normal
    def cyan(txt, normal = RESET):
        return CYAN+txt+normal
    def white(txt, normal = RESET):
        return WHITE+txt+normal

class Background:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'

    def black(txt, normal = RESET):
        return BLACK+txt+normal
    def red(txt, normal = RESET):
        return RED+txt+normal
    def green(txt, normal = RESET):
        return GREEN+txt+normal
    def yellow(txt, normal = RESET):
        return YELLOW+txt+normal
    def blue(txt, normal = RESET):
        return BLUE+txt+normal
    def purple(txt, normal = RESET):
        return PURPLE+txt+normal
    def cyan(txt, normal = RESET):
        return CYAN+txt+normal
    def white(txt, normal = RESET):
        return WHITE+txt+normal

    class HighIntensity:
        BLACK = '\033[0;100m'
        RED = '\033[0;101m'
        GREEN = '\033[0;102m'
        YELLOW = '\033[0;103m'
        BLUE = '\033[0;104m'
        PURPLE = '\033[0;105m'
        CYAN = '\033[0;106m'
        WHITE = '\033[0;107m'

        def black(txt, normal = RESET):
            return BLACK+txt+normal
        def red(txt, normal = RESET):
            return RED+txt+normal
        def green(txt, normal = RESET):
            return GREEN+txt+normal
        def yellow(txt, normal = RESET):
            return YELLOW+txt+normal
        def blue(txt, normal = RESET):
            return BLUE+txt+normal
        def purple(txt, normal = RESET):
            return PURPLE+txt+normal
        def cyan(txt, normal = RESET):
            return CYAN+txt+normal
        def white(txt, normal = RESET):
            return WHITE+txt+normal

class HighIntensity:
    BLACK = '\033[0;90m'
    RED = '\033[0;91m'
    GREEN = '\033[0;92m'
    YELLOW = '\033[0;93m'
    BLUE = '\033[0;94m'
    PURPLE = '\033[0;95m'
    CYAN = '\033[0;96m'
    WHITE = '\033[0;97m'

    def black(txt, normal = RESET):
        return BLACK+txt+normal
    def red(txt, normal = RESET):
        return RED+txt+normal
    def green(txt, normal = RESET):
        return GREEN+txt+normal
    def yellow(txt, normal = RESET):
        return YELLOW+txt+normal
    def blue(txt, normal = RESET):
        return BLUE+txt+normal
    def purple(txt, normal = RESET):
        return PURPLE+txt+normal
    def cyan(txt, normal = RESET):
        return CYAN+txt+normal
    def white(txt, normal = RESET):
        return WHITE+txt+normal
