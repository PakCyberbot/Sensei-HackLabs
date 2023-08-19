import os, sys, subprocess
from colorama import Fore, Back, Style, init
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from rich import print as printr


console = Console()


banner =rf"""{Fore.MAGENTA}{Style.BRIGHT}
  _________                            __   /\   /\                __    ___           ___            
 /   _____/ ____   ____   ______ ____ |__| /  |_|  \_____    ____ |  | __   |   _____  \_ |__   ______
 \_____  \_/ __ \ /    \ /  ___// __ \|  |/         \__  \ _/ ___\|  |/ /   |   \__  \  | __ \ /  ___/
 /        \  ___/_   |  \\___ \\  ___/_  |\    _    // __ \_  \___|    \|   |___ / __ \_| \_\ \\___ \ 
/_______  /\___  /___|  /____  \\___  /__| \  | |  /(____  /\___  /__|_ \______ \____  /|___  /____  \
        \/     \/     \/     \/     \/      \/   \/      \/     \/     \/      \/    \/     \/     \/ 
{Style.RESET_ALL}
Developed by: {Fore.GREEN}{Style.BRIGHT}PakCyberbot (https://github.com/PakCyberbot)
{Style.RESET_ALL}
"""

print(banner)

def show_menu():
    current_available_envs = os.listdir()
    current_available_envs.remove("SenseiHackLabs.py")
    current_available_envs.remove("README.md")
    current_available_envs.remove("requirements.txt")

    
    total_envs = len(current_available_envs)
    print(f"{Fore.BLUE}> Select any Environment to Install or Get Info{Style.RESET_ALL}\n")
    for i, env in enumerate(current_available_envs):
        print(f"{i+1}) {env}")
    
    print("0) Exit")
    return current_available_envs

options = -1
install = -1
envs = show_menu()
while(options != 0):
    try:
        options = int(input(f"\n{Fore.CYAN}Select an Environment from the Menu:{Style.RESET_ALL}"))
    except TypeError:
        print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")
        continue
    except KeyboardInterrupt:
        print("\nEXITING FROM PROGRAM\nDon't forget to show some support to PakCyberbot for more interesting updates!")
        exit()
    
    if options == 0:
        print("\nEXITING FROM PROGRAM\nDon't forget to show some support to PakCyberbot for more interesting updates!")
        exit()
    
    while(install != 0):
        print(f"\n1) Install {envs[options - 1]}")
        print(f"2) Get an Info about {envs[options - 1]}")
        print(f"0) Go Back")
        try:
            install = int(input(f'\n{Fore.CYAN}Enter option:{Style.RESET_ALL}'))
        except TypeError:
            print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")
            continue
        except KeyboardInterrupt:
            print("\nEXITING FROM PROGRAM\nDon't forget to show some support to PakCyberbot for more interesting updates!")
            exit()

        if install == 0:
            break
        elif install == 2:
            with open(f"{envs[options - 1]}/info", "r") as info:
                print(f"{Fore.GREEN}="*20,f" INFO ABOUT {envs[options - 1]} ","="*20,Style.RESET_ALL)
                console.print(Markdown(info.read()))
                print(f"{Fore.GREEN}="*25,f" INFO END ","="*25,Style.RESET_ALL)
        elif install == 1:
            new_dir = os.path.join(os.getcwd(),envs[options - 1])
            subprocess.call(f"./setup.sh", shell=True, cwd=f"{new_dir}")
            results_path = f"{envs[options - 1]}/result"
            if os.path.exists(results_path):
                with open(results_path,"r") as output:
                    output = output.read()
                    printr(f"{output}")
                os.remove(results_path)
            else:
                print("Failed to Setup your Lab")

    show_menu()
