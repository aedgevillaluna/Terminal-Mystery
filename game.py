import os
import sys
import random
import time

def clr():
    os.system('cls' if os.name == "nt" else "clear")

def blank():
    print("")

def cont_input():
    input("\033[3mPress enter to continue.\033[0m")

def info(game_data):
    clr()
    game_data["sign_time"] = time.strftime("%H:%M.%S")
    game_data["username"] = input("\033[3mWhat is your username?\033[0m\n")
    time.sleep(1)

def print_hacked_prompt(error_msg=""):
    clr()
    print("\033[1;4;31m[WARNING]\033[0m")
    print("\033[1mYour terminal was hacked.\033[0m")
    blank()
    time.sleep(2)
    if error_msg:
        print(error_msg)
        blank()
    return input(
        "What do you do?\n"
        "   1. Check the logs.\n"
        "   2. Keep programming.\n"
        "   3. Shut off everything.\n"
    )

def print_admin_blocked(error_msg=""):
    clr()
    print("\033[1;4;31m[ERROR: ACCESS BLOCKED BY ADMIN]\033[0m")
    time.sleep(1)
    print("┏\n"
          "  POTENTIAL COMMANDS:\n"
          "  log_access = false\n"
          "  is_admin = false\n"
          "  in_session = true     ┛\n")
    time.sleep(2)
    if error_msg:
        print(error_msg)
    return input(
        "Type one of the following commands?\n"
        "   log_access = true\n"
        "   is_admin = true\n"
        "   in_session = false\n"
    )

def directory_view(error_msg="", menu_item=0):
    clr()
    print("\033[1m[ADMIN DIRECTORY]\033[0m")

    menu_items = [
        ("┏", "[USER PROFILE]"),
        ("┣", "[ACCESS LOGS]"),
        ("┣", "[SECURITY SETTINGS]"),
        ("┗", "[LOG OUT]"),
    ]

    for index, (prefix, label) in enumerate(menu_items):
        if menu_item == index:
            print(f"{prefix} \033[47;30m{label}\033[0m")
        else:
            print(f"{prefix} {label}")

    if error_msg:
        print(error_msg)

    return input(
        "Select a menu. Use W or S to go up or down or leave it blank to select when you press enter.\n"
    )

def log_view(game_data, error_msg="", log_item=0):
    username = game_data["username"]
    clr()
    print("\033[1m[TERMINAL LOGS]\033[0m")

    log_items = [
        ("┏", f"[{game_data['log_time']}] {username} visits logs."),
        ("┣", f"[{game_data['accessed_time']}] {username} accessed admin panel."),
        ("┣", f"[{game_data['admin_blocked_time']}] {username} blocked from admin panel."),
        ("┣", f"[{game_data['hacked_time']}] [ERROR] session cannot be detected. (View for more info)"),
        ("┣", f"[{game_data['programming_time']}] {username} starts programming."),
        ("┗", f"[{game_data['sign_time']}] {username} signs in."),
    ]

    for index, (prefix, label) in enumerate(log_items):
        if log_item == index:
            print(f"{prefix} \033[47m\033[30m{label}\033[0m")
        else:
            print(f"{prefix} {label}")
            
    if error_msg:
        print(error_msg)
            
    return input(
        "Navigate the logs. Use W or S to go up or down or leave it blank to select when you press enter.\n"
        )

def run_loading():
    for percentage in range(0, 105, 5):
        clr()
        print("\033[1;33m[ACCESSING PANEL]\033[0m")
        print("Loading...")
        
        hashes = percentage // 5
        dashes = 20 - hashes
        bar = "#" * hashes + "-" * dashes
            
        print(f"[{bar}] // {percentage}%")
        blank()
        time.sleep(random.uniform(0.125, 0.75))

def end_text(text):
    clr()
    print(text)
    time.sleep(2)
    cont_input()

def main():
    game_data = {}
    info(game_data)
    clr()
    print("\033[1;3;4;31mTerminal Mystery\033[0m")
    blank()
    input("Press enter to play.\n")

    clr()
    print("Welcome to the terminal! Let's get programming!")
    time.sleep(2)
    cont_input()

    game_data["programming_time"] = time.strftime("%H:%M.%S")

    for _ in range(random.randint(3,5)):
        for dots in [".", "..", "..."]:
            clr()
            print(f"\033[3mYou start programming{dots}\033[0m")
            blank()
            time.sleep(0.5)

    time.sleep(1.5)
    game_data["hacked_time"] = time.strftime("%H:%M.%S")
    input_2 = print_hacked_prompt()
    blank()

    while True:
        if input_2 == "1":
            clr()
            print("\033[3mYou decide to check the logs.\033[0m")
            break
        elif input_2 == "2":
            clr()
            print("\033[3mYou decide to keep programming.\033[0m")
            print("\033[3mUnaware of what is happening, the hacker kills your session.\033[0m")
            time.sleep(2)
            sys.exit()
        elif input_2 == "3":
            clr()
            print("\033[3mYou, in a panic, shut off everything.\033[0m")
            time.sleep(2)
            sys.exit()
        else:
            input_2 = print_hacked_prompt(error_msg="Invalid input. Type 1, 2, or 3.")
            blank()

    time.sleep(2)
    cont_input()

    run_loading()

    game_data["admin_blocked_time"] = time.strftime("%H:%M.%S")
    input_3 = print_admin_blocked()
    blank()

    while True:
        if input_3 in ("log_access = true", "log_access = false", "is_admin = false", "in_session = true"):
            clr()
            print("\033[3mNothing happened.\033[0m")
            time.sleep(2)
            cont_input()
            input_3 = print_admin_blocked()
            blank()
        elif input_3 == "is_admin = true":
            clr()
            print("\033[1;32m[ADMIN ACCESS GRANTED]\033[0m")
            time.sleep(2)
            cont_input()
            break
        elif input_3 == "in_session = false":
            clr()
            print("\033[1;31m[SESSION TERMINATED]\033[0m")
            time.sleep(2)
            print("\033[3mYou accidentally ended your session.\033[0m")
            time.sleep(2)
            sys.exit()
        else:
            input_3 = print_admin_blocked(error_msg="Invalid input.\n")
            blank()

    game_data["accessed_time"] = time.strftime("%H:%M.%S")
    menu_nav = 0
    input_4 = directory_view()
    blank()

    while True:
        if input_4.lower() == "w":
            if menu_nav > 0:
                menu_nav += -1
            input_4 = directory_view(menu_item=menu_nav)
            
        elif input_4.lower() == "s":
            if menu_nav < 3:
                menu_nav += 1
            input_4 = directory_view(menu_item=menu_nav)

        elif input_4 == "":
            if menu_nav in [0, 2]:
                clr()
                print("\033[3mNothing happened.\033[0m")
                time.sleep(2)
                cont_input()
                input_4 = directory_view(game_data, menu_item = 0)
                menu_nav = 0

            elif menu_nav == 1:
                clr()
                print("[CHECKING LOGS...]")
                time.sleep(2)
                cont_input()
                break

            elif menu_nav == 3:
                clr()
                print("[LOGGING OUT]")
                time.sleep(2)
                sys.exit()
                
        else:
            input_4 = directory_view(error_msg = 
                                     "Invalid input. Type W or S to go up or down, or leave blank when pressing enter to select.", 
                                     menu_item=menu_nav)
            blank()

    game_data["log_time"] = time.strftime("%H:%M.%S")
    log_nav = 0
    input_5 = log_view(game_data, log_item=log_nav)
    blank()

    while True:
        if input_5.lower() == "w":
            if log_nav > 0:
                log_nav += -1
            input_5 = log_view(game_data, log_item=log_nav)
            
        elif input_5.lower() == "s":
            if log_nav < 5:
                log_nav += 1
            input_5 = log_view(game_data, log_item=log_nav)

        elif input_5 == "":
            if log_nav in [0, 1, 2, 4, 5]:
                clr()
                print("\033[3mNothing happened.\033[0m")
                time.sleep(2)
                cont_input()
                input_5 = log_view(game_data, log_item = 0)
                log_nav = 0

            elif log_nav == 3:
                clr()
                print("[LOADING...]")
                time.sleep(2)
                cont_input()
                break
                
        else:
            input_5 = log_view(game_data, error_msg = 
                               "Invalid input. Type W or S to go up or down, or leave blank when pressing enter to select.",
                               log_item=log_nav)
            blank()

    end_text("\033[3mYou accessed the log...\033[0m")
    end_text("\033[3mYou read through the log...\033[0m")
    end_text("\033[3mSuddenly, your terminal starts to glitch again.\033[0m")

    clr()
    print("#########################################")
    print("########################")

    end_text("\033[3mThe 'hacker' left a message.\033[0m")
    clr()
    for i in range(50):
        print("I'll be here.")
        time.sleep(0.01)

    clr()
    print("\033[1;3;4;31mTerminal Mystery\033[0m\n")
    time.sleep(2)
    print("\033[1mA Mini Terminal-Based Game By Aeden Villaluna\033[0m")
    time.sleep(2)
    end_text("Game Over.")
    sys.exit()
    

if __name__ == "__main__":
    main()