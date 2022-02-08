#imports
import pymem
import pymem.process
import time
import keyboard
import numpy as np
from threading import Thread
import psutil
import secrets
import ctypes
from colorama import init, Fore, Back
init(autoreset=True)
#import config
from CONFIG import *
#import offsets;
from offsets import *



#this is a memory reading bunnyhop for csgo :D
def main():

#wait if game is running and start hopping when it is
    os.system("cls")
    print(f"{Fore.LIGHTMAGENTA_EX}PLS PRESS ENTER WHEN YOU ARE IN THE CS:GO MAIN MENU:")
    input("")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    
    os.system("cls")
    
    ctypes.windll.kernel32.SetConsoleTitleW("External csgo memory reading bunnyhopper; by cookie0_o (cookie0o on github)!")


    print (f"{Fore.CYAN}External csgo memory reading bunnyhopper;")
    print(f"{Fore.LIGHTBLUE_EX}by: cookie0_o (cookie0o on github)")
    print(" ")
    print(f"{Fore.GREEN}TOGGLE KEY; {Toggle_key}")

    #main hop part

    start = 0

    while True:
        if keyboard.is_pressed(Toggle_key) and start == 0:
            start = 1
        if keyboard.is_pressed(Toggle_key) and start == 1:
            start = 0
        while start == 1:
            if keyboard.is_pressed(Toggle_key) and start == 1:
                start = 0
            try:      
                #HOP
                if pm.read_int(client + dwLocalPlayer):
                    player = pm.read_int(client + dwLocalPlayer)
                    force_jump = client + dwForceJump
                    on_ground = pm.read_int(player + m_fFlags)
                    velocity = pm.read_float(player + m_vecVelocity)
                    if keyboard.is_pressed("space") and on_ground == 257:
                        if velocity < 1 and velocity > -1:
                            pass
                        else:
                            pm.write_int(force_jump, 5)
                            time.sleep(0.17)
                            pm.write_int(force_jump, 4)

                            if keyboard.is_pressed(Toggle_key) and start == 1:
                                start = 0
            except:
                time.sleep(0.001)
                pass
main()