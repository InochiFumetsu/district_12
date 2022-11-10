import random
import os
import re
#import importlib as imp
from rand_ass_classes import member_list
from rand_ass_classes import group


def user_interface()->None:
    members, quit, current_group = member_list(), False, group(hard_code)
    
    while not quit:
        os.system('cls')
        print("RANDOM ASSIGNMENT GENERATOR\n"
              "1. Enter / Change group members' names\n"
              "2. Generate random assignments\n"
              "3. Display most recent random assignments generated\n"
              "4. Delete group member list\n"
              "5. Quit\n\n")
        user_choice = input("Enter the number corresponding with your selection from the menu above: ")
        if not user_choice:
            os.system('cls')
            input("Invalid entry. You must make a selection.\n\n"
                  "Press <ENTER> to continue.")
            continue
        if not re.findall(r'(.+)?[^\d](.+)?', user_choice):
            user_choice = int(float(user_choice))
        else:
            os.system('cls')
            input("Invalid entry. Please make a selection from the menu options listed.\n\n"
                  "Press <ENTER> to continue. ")
            continue
        if 0 < user_choice < 6:
            if user_choice == 2 and not members.members:
                while True:
                    os.system('cls')
                    print("Please note: if you run random assignment generator without\n"
                          "entering names of group members, generator will run with hardcoded\n"
                          "member names. Currently, the hard-coded member names are:\n")
                    hard_code.display_members()
                    user_choice = input("\nPress <ENTER> to continue, or type \"menu\" to go back to the menu. ")
                    if not user_choice:
                        os.system('cls')
                        current_group = group(hard_code)
                        current_group.generate_random_assignments()
                        input("\nPress <ENTER> to continue.")
                        break
                    elif user_choice == "menu":
                        break
                    else:
                        os.system('cls')
                        input(f"Invalid entry. Please either type \"menu\" to return to the menu or hit <ENTER>\n"
                              "without typing anything to run random assignment generator with hardcoded member names.\n\n"
                              "Press <ENTER> to continue. ")
                        continue
            elif user_choice == 2:
                os.system('cls')
                current_group = group(members)
                current_group.generate_random_assignments()
                input("\nPress <ENTER> to continue. ")
                continue
            elif user_choice == 3:
                os.system('cls')
                current_group.display_results()
                input("\nPress <ENTER> to continue.")
                continue
            elif user_choice == 4:
                while True:
                    os.system('cls')
                    user_choice = input("Are you sure you want to delete the current group members\n"
                          "list?? This action cannot be undone. [Y/N]: ")
                    if user_choice.lower() == 'y':
                        members.delete_group()
                        break
                    elif user_choice.lower() == 'n':
                        break
                    else:
                        os.system('cls')
                        input("Invalid entry. Please enter Y or N.\n\n"
                              "Press <ENTER> to continue.")
                        continue
                continue
            elif user_choice == 5:
                quit = True
                continue
            else:
                if not members.members:
                    members.new_member_list()
                else:
                    while True:
                        os.system('cls')
                        print("The current group member list is:\n")
                        members.display_members()
                        user_choice = input("\n1. Update group member list\n"
                                            "2. Create new group member list (current list will be erased)\n"
                                            "3. Cancel\n\n"
                                            "Enter the number corresponding to your selection from the menu above: ")
                        if not user_choice:
                            os.system('cls')
                            input("Invalid entry. You must make a selection.\n\n"
                                  "Press <ENTER> to continue.")
                            continue                        
                        if not re.findall(r'(.+)?[^\d](.+)?', user_choice):
                            user_choice = int(float(user_choice))
                        else:
                            os.system('cls')
                            print("\nInvalid selection. Please select from the menu choices listed.\n\n")
                            input("Press <ENTER> to continue.")
                            continue                            
                        if 0 < user_choice < 4:
                            if user_choice == 2:
                                members.new_member_list()
                                break
                            elif user_choice == 3:
                                break
                            else:
                                members.update_members()
                                break
                        else:
                            os.system('cls')
                            print("\nInvalid selection. Please select from the menu choices listed.\n\n")
                            input("Press <ENTER> to continue.")
                            continue
                    continue
        else:
            os.system('cls')
            input("Invalid entry. Please make a selection from the menu options listed.\n\n"
                  "Press <ENTER> to continue. ")
            continue        
    os.system('cls')
    print("Thank you for using random assignment generator.")
    input("Press <ENTER> to exit the program. ")
    os.system('cls')




# MAIN CODE BODY:
hard_code = member_list(("Esteban", "Jack", "Milan", "Spencer"))
user_interface()
