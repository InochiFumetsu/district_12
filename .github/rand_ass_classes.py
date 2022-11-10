import random
import os
import re


class member_list:
    def __init__(self, members: tuple = ())->None:
        if type(members) != list \
        and type(members) != tuple \
        and type(members) != set:
            raise TypeError("Class object: Invalid Argument. Argument must be a tuple, list or set.")
        elif type(members) != tuple:
            members = tuple(members)
        self.members = members
    
    def delete_group(self)->None:
        self.members = ()    
    
    def display_members(self)->None:
        if self.members:
            for i in range(len(self.members)):
                print(i + 1, self.members[i], sep=" ")
        else:
            print("<No members to display>")
        print("")
    
    def new_member_list(self)->None:
        complete, first_run, temp_list = False, True, []
        while not complete:
            os.system('cls')
            print("Enter individual group members' names one at a time below.\n"
                  "Any name / identifier may be entered, as long as you are able to\n"
                  "identify the group member based on what you enter.\n"
                  "Once you have entered all group members' names / identifiers\n"
                  "press <ENTER> without typing a name to submit the list.\n"
                  "If you have made a mistake, you may enter \"CANCEL\" to exit\n"
                  "without making changes to the existing group list.\n\n"
                  "The current group member list is:")
            if first_run:
                first_run = False
                self.display_members()
            else:
                for i in range(len(temp_list)):
                    print(i + 1, temp_list[i], sep=" ")
            user_choice = input("\nEnter a group member's name / identifier: ")          
            if user_choice:
                if user_choice.lower() == "cancel":
                    while True:
                        os.system('cls')
                        confirm_exit = input("Are you sure you want to exit? Your changes will be discarded. [Y/N]: ")
                        if confirm_exit.lower() == 'y':
                            return
                        elif confirm_exit.lower() == 'n':
                            break
                        else:
                            os.system('cls')
                            input("Invalid response. Please enter Y or N.\n\n"
                                  "Press <ENTER> to continue. ")
                            continue
                    continue
                temp_list += [user_choice]
                continue
            else:
                while True:
                    os.system('cls')
                    print("The current group member list is:")
                    for i in range(len(temp_list)):
                        print(i + 1, temp_list[i], sep=" ")
                    user_choice = input("\nPress <ENTER> to continue, or type \"add\" to add another group member: ")
                    if not user_choice:
                        complete = True
                        break
                    if user_choice.lower() != "add":
                        os.system('cls')
                        input("Invalid entry. Please either press <ENTER> to accept the\n"
                              "changes or type \"add\" to continue adding group members.\n\n"
                              "Press <ENTER> to continue. ")                        
                        continue
                    else:
                        break
        self.members = tuple(temp_list)
        
    def update_members(self)->None:
        if self.members:
            self.members = list(self.members)
            while True:
                os.system('cls')
                print("The current group member list is:\n")
                self.display_members()
                print("\nBelow, you may enter the number corresponding with the group\n"
                      "member you would like to update. When you are finished, simply\n"
                      "press <ENTER> without typing anything.\n") 
                user_choice = input("\nEnter the number corresponding with the group member\n"
                      "you would like to update: ")
                if not user_choice:
                    break
                elif not re.findall(r'(.+)?[^\d](.+)?', user_choice):
                    user_choice = int(float(user_choice))
                else:
                    os.system('cls')
                    input(f"Invalid selection. \"{user_choice}\" is not a number from 1 to {len(self.members)}."
                          "\n\nPress <ENTER> to continue.")
                    continue            
                if  0 < user_choice < len(self.members) + 1:
                    index = user_choice - 1
                    print("\nIf you do not wish to change the member name you have\n"
                          "selected, press <ENTER> without typing anything.\n")
                    user_choice = input(f"\nEnter the name / identifier of the group member to replace \"{self.members[user_choice - 1]}\": ")
                    if not user_choice:
                        continue
                    else:
                        self.members[index] = user_choice
                        continue
                else:
                    os.system('cls')
                    input(f"Invalid selection. \"{user_choice}\" is not a number from 1 to {len(self.members)}."
                          "\n\nPress <ENTER> to continue.")
                    continue                               
            self.members = tuple(self.members)
        else:
            while True:
                os.system('cls')
                user_input = input("Member list is empty. No members to update.\n"
                                   "Creating new member list... press <ENTER> to continue\n"
                                   "or type \"exit\" to return to previous menu: ")
                if not user_input:
                    self.new_member_list()
                if user_input.lower() != "exit":
                    os.system('cls')
                    input("Invalid entry. Please either press <ENTER> to proceed with\n"
                          "creating a new member list or type \"exit\" and press\n"
                          "<ENTER> to return to the previous menu.\n\n"
                          "Press <ENTER> to continue.")
                    continue
                break



class group:
    def __init__(self, members: member_list = member_list(), noassignments: tuple = (0,))->None:
        if type(members) != member_list:
            raise TypeError("Class object: Invalid Argument. First position argument must be of type member_list (class object).")
        if type(noassignments) != tuple and type(noassignments) != int:
            raise TypeError("Class object: Invalid Argument. Second position argument must be of type tuple or type int.")
        
        #here's where you add if len(noassignments) != 1
            #for i in range(len(noassignments)):
                #if type(noassignments[i]) != int:
                    #if type(noassignments[i] != str:
                        #raise TypeError("Class object: Invalid Argument. Second position argument (tuple) must have elements of type string or int.")
                    #else:
                        #<complicated code block or maybe just calls a diff method?>
            #self.assignments = noassignments <-- FIGURE OUT IMPLICATIONS OF THIS IN GENERATE_RANDOM_ASSIGNMENTS()
            
        if noassignments[0]:
            #Gonna remove noassignments input parameter.. need to just write a 
            #def config_assignments()->None: function for this additional functionality.
            self.assignments = tuple(range(1, noassignments[0]))
        else:
            self.assignments = tuple(range(1, len(members.members) + 1))
        self.members = tuple(members.members)
        self.results = ()

    def display_results(self)->None:
        if self.results:
            for i in range(len(self.results)):
                print(self.results[i])
        else:
            print("<No results to display>", end="")

    def generate_random_assignments(self):
        members = list(self.members)
        assignments = list(self.assignments)
        results = []
        if not members:
            print("Error: Member list is empty. Cannot generate random assignments\n"
                  "for zero group members.")
            return
        for i in range(len(members)):
            assignee = members[random.randint(0, len(members) - 1)]
            members = set(members)
            members.remove(assignee)
            members = list(members)
            assignment = assignments[random.randint(0, len(assignments) - 1)]
            assignments = set(assignments)
            assignments.remove(assignment)
            assignments = list(assignments)
            results.append(f"{assignee}: {assignment}")
        self.results = tuple(results)
        self.display_results()