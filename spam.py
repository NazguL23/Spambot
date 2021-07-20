# By NazguL


### IMPORTS ###
import os
import sys
import colorama
import pyautogui
import time

colorama.init(autoreset=False)
  

### STYLE ###
class colors:   

    LIGHTRED = colorama.Fore.LIGHTRED_EX
    LIGHTCYAN = colorama.Fore.LIGHTCYAN_EX
    LIGHTGREEN = colorama.Fore.LIGHTGREEN_EX
    LIGHTYELLOW = colorama.Fore.LIGHTYELLOW_EX
    LIGHTBLUE = colorama.Fore.BLUE



def banner(defaultcolor):

    print(defaultcolor + """
       .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. ▄▄▄▄·       ▄▄▄▄▄
       ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪▐█ ▀█▪▪     •██  
       ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█▀▀█▄ ▄█▀▄  ▐█.▪
       ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██▄▪▐█▐█▌.▐▌ ▐█▌·
        ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 
                        By NazguL    """)


class menus:

    def main(defaultcolor):

        print(defaultcolor + """
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█

            [0] :  Change Color
            [1] :  Start Spamming
            [2] :  Exit 

    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█    
    """)

    def changecolor(defaultcolor):

        print(defaultcolor + """
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█

        [0] :  Blue     [3] : Green
        [1] :  Red      [4] : Cyan
        [2] :  Yellow   [5] : Exit 

    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█    
    """) 
    def spammenu(defaultcolor):

        print(defaultcolor + """
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█

        [0] : Setup Bot  
        [1] : Back to Menu     

    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█    
    """) 

    def spammenu1(defaultcolor,msg,timebtw):

        print(defaultcolor + f"""
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█

        Message  : {msg}
        TBetween : {str(timebtw)}

    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█    
    """)


### FEATURES ###
def changecolor(newcolor):

    return newcolor




if __name__ == '__main__':

    
    # VARS #
    color = colors.LIGHTCYAN

    print(sys.platform)
    if sys.platform == "win32" or sys.platform == "win64":
        systemclear = "cls"
    
    else:
        systemclear = "clear"


    
    
    while True:

        os.system(systemclear)
        banner(color)
        menus.main(color)
        command = input(color + "[*] " + "Options : ")

        if command == "0":
            
            os.system(systemclear)
            banner(color)
            menus.changecolor(color)
            command1 = input(color + "[*] " + "Options : ")

            if command1 == "0":

                color = changecolor(colors.LIGHTBLUE)

            elif command1 == "1":

                color = changecolor(colors.LIGHTRED)
            
            elif command1 == "2":

                color = changecolor(colors.LIGHTYELLOW)
            
            elif command1 == "3":

                color = changecolor(colors.LIGHTGREEN)
            
            elif command1 == "4":

                color = changecolor(colors.LIGHTCYAN)
            
            elif command1 == "5":

                pass

            else:

                print("Error : Unknown Command")
                input("Press any Key to Continue ")


        if command == "1":

            os.system(systemclear)
            banner(color)
            menus.spammenu(color)
            command2 = input(color + "[*] " + "Options : ")

            
            if command2 == "0":
                
                os.system(systemclear)
                banner(color)
                print("")
                message = input(color + "[*] Message : ")
                try:

                    timebetween = float(input(color + "[*] Time between Messages : "))

                except Exception:

                    print("Error : Please enter a float")
                    sys.exit()

                try:
                    amount = int(input(color + "[*] Amount of Message/s : "))

                except Exception:
                    print("Error : Please enter a integer")
                    sys.exit()

                    

                input("Press any Key to Start ")
                os.system(systemclear)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                os.system(systemclear)
                banner(color)
                menus.spammenu1(color,message,timebetween)
                print("")

                count = 0
                for i in range(amount):
                    
                    pyautogui.typewrite(message + "\n")
                    count += 1
                    time.sleep(timebetween)


                print("")
                input(color + f"Finished sending {str(count)} Messages ")
                

            elif command2 == "1":
                 
                pass

        if command == "2":
            
            os.system(systemclear)
            input("Press any key to exit ")
            os.system(systemclear)
            sys.exit()
    
