import modules.selUI as selUI
import modules.uniKey as uniKey
import modules.ANSIcolour as ansi 
import os
import sys


def escape():
    while True:
        print("\n"+"—"*18+"\nProgramm stopped")
        quit()



os.chdir("/media/HDD/programmier8/control/autoAur/")


args = sys.argv
if len(args)>1:
    if args[1] in "-Ss":
        url=args[2]
        os.chdir("./wrk")
        os.system("rm -rf ./*")
        os.system("git clone "+url)
        pkgName = os.listdir("./")[0]
        os.chdir("./"+pkgName)
        os.system("makepkg -si")
        print("Installed package: "+pkgName+"\nDo you want to add the package to the update file? (Y,n)")
        inp=input("——>")
        if inp in "yYjJ":
            os.chdir("../../")
            if not url in open("./update", "r").read():
                open("./update", "a").write(url+"\n")
        escape()


opt = ["Install", "Install with manual flag", "Update package" "Quit"]
menu = selUI.SelectionMenu.create(opt, "Main menu", selUI.SelectionMenu.normalOptions)



def run():
    cui = "Please enter url or git clone command: \n-->"
    print(cui, end="")
    url = input()
    url = url.replace("git clone", "").replace(" ", "")
    os.chdir("./wrk")
    os.system("rm -rf ./*")
    os.system("git clone "+url)
    pkgName = os.listdir("./")[0]
    os.chdir("./"+pkgName)
    os.system("makepkg -si")
    print("Installed package: "+pkgName+"\nDo you want to add the package to the update file? (Y,n)")
    inp=input("——>")
    if inp in "yYjJ":
        os.chdir("../../")
        open("./update", "a").write(url+"\n")
    
    




os.system("clear")
while True:
    print(menu.refresh())
    inp = uniKey.Getch.getch()
    os.system("clear")
    if inp in ["w", "w", "8"]:
        menu.selDown()
    elif inp in ["s", "S", "2"]:
        menu.selUp()
    elif inp in ["D", "d", "6", "\n", " "]:
        sel = menu.select()
        if sel == opt[0]:
            try:
                run()
            except KeyboardInterrupt:
                escape()
        elif sel == opt[1]:
            run_with_flag()
        elif sel == opt[2]:
            run_archive()
        elif sel == opt[3]:
            escape()
        escape()
