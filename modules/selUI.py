from collections import namedtuple
import os



"""
class 2axes
(object):


    clock_ison = True
    lenLeft = 14
    lenRight =14
    seperator = " | "


    def __init__(self, clock_ison, ):

        if clock_ison:
            self.heading = (("_"*(lenLeft+lenRight+len(seperator)))
            + "\n")






def build2axesSelectionMenutoString(config):
"""


class SelectionMenu:

##     How to create a SelectionMenu-Object
    #  It takes the options to choose from, a heading, and an array containing cosmetic specifications
    #  The object should be initialized as following:
    #
    #  seperator, selection-flag, null-flag, startpoint, subHeading, maxLen
#Index:    0    | |     1       | |    2   | |    3    | |    4   |  |  5 |
    #
    # The seperator represents the string between the selection flag, and the option, (in 'O|this is an option' the '|' is the seperator)
    # The seperator can contain more than one character ('O<>this is an option')
    #
    # The selection flag (refered to as selFlag in the code) indicates the users current selection ('O|this is an option', the 'O' is the
    # selection flag)
    #
    # The null flag will be used on options not currently selected by the user (' |this is an option', the ' ' is the null flag)
    #
    # The startpoint specifies the index of the entry, the user selection should start at
    #
    # The subHeading describes the char, that should be used to build the seperator under the heading
    # ('This is the title
    #   -------------------
    #   |this is an option', the '-' char)
    #
    # The maxLen describes the length to cut any line of the menu
    #
    #
    seperator = "|"
    selFlag = "O"
    nulFlag = " "
    sel = 0
    subHeading = "-"
    maxLen = 1024
    normalOptions=["|", "O", " ", 0, "", 16]

    def __init__(self, entrys, title, seperator, selFlag, nullFlag, sel, subHeading, maxLen):
        self.entrys = entrys
        self.title = title
        self.seperator = seperator
        self.selFlag = selFlag
        self.nullFlag = nullFlag
        self.sel = sel
        self. subHeading = subHeading
        self.maxLen = maxLen




    def create(entr, title, options):
        #menu = namedtuple('menu', ['entrys', 'title', 'seperator', 'selFlag', 'nullFlag', 'sel', 'subHeading', 'maxLen'])


        return SelectionMenu(entr, title, options[0], options[1], options[2], options[3], options[4], options[5])

    def selUp(menu):
        if menu.sel+1<len(menu.entrys):
            menu.sel+=1
        return menu


    def selDown(menu):
        if menu.sel-1>=0:
            menu.sel-=1
        return menu



    def refresh(menu):
        output = menu.title+"\n" + (menu.subHeading*menu.maxLen) + "\n"
        for i in range(0, len(menu.entrys)):
            if menu.sel == i:
                output += (menu.selFlag+menu.seperator+menu.entrys[i])[:menu.maxLen]
            else:
                output += (menu.nullFlag+menu.seperator+menu.entrys[i])[:menu.maxLen]
            output+="\n"
        return output

    def select(menu):
        return menu.entrys[menu.sel]







##        Testing:


"""
mymen = SelectionMenu(["Option1", "Option2", "Option3"], "Nice Heading", "|", "O", " ", 0, "_", 24)

while True:
    print(SelectionMenu.refresh(mymen))
    inp = input()
    if inp == "w":
        SelectionMenu.selDown(mymen)
    if inp == "s":
        mymen.selUp()
        #SelectionMenu.selUp(mymen)
    if inp == "d":
        print(SelectionMenu.select(mymen))
"""




