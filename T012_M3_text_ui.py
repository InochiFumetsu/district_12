"""
Copyright © 2022, Esteban Heidrich, Jack Roberts, Milan Djordjevic, Spencer Hiscox. All rights reserved. Study-PY™ is a trademark of district_12™ developers.

Copyright © 2005-2022, NumPy Developers. All rights reserved.

Copyright © 2001-2002 Enthought, Inc. 2003-2022, SciPy Developers. All rights reserved.

Copyright © 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012–2022 The Matplotlib development team.

For full licensing information, see the README.md file in the root folder of the master branch of this repository:
https://github.com/InochiFumetsu/district_12/blob/master/README.md
"""


import T012_M1_load_data
import T012_M2_sort_plot
import T012_M3_optimization


def text_ui() -> None:
    """
    Examples:
    ** On open:
        The available commands are:
            1. L) oad Data
            2. S) ort Data
                    'School'    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'    'G1'    'G2'    'G3'    'G_Avg'
            3. H) istogram
                    'School'    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'
            4. W) orst ____ for Grades
                    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'
            5. B) est ____ for Grades
                    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'
            6. Q) uit

        Please type your command (Options: L, S, H, W, B, Q): 

    ** Upon the user entering "L" for load data
        Please type your command (Options: L, S, H, W, B, Q): L
        Please enter the name of the file: student-mat.csv
        Please enter the attribute to use as key (Options: Failures, Health, Age, School): Failures
        Data loaded

    ** Upon the user entering "S" for sort data (Assuming user has already loaded data, or else an error message will print informing user)
        Please type your command (Options: L, S, H, W, B, Q): S
        Please enter the attribute you want to use for sorting (Options: School, Age, StudyTime, Failures, Health, Absences, G1, G2, G3, G_Avg): G_Avg
        sorted_data loaded, and sorted by Failures. Do you want to display the data? (Options: Yes or No): Yes
        [{'School': 'MB', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 4.0, 'G2': 0.0, 'G3': 0.0, 'G_Avg': 1.33, 'Failures': 2}, {'School': 'MB', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 5.0, 'G2': 0.0, 'G3': 0.0, 'G_Avg': 1.67, 'Failures': 3}, {'School': 'MB', 'Age': 19, 'StudyTime': 1.0, 'Health': 4, 'Absences': 0, 'G1': 5.0, 'G2': 0.0, 'G3': 0.0, 'G_Avg': 1.67, 'Failures': 3}, ...

    ** Upon the user entering "W" for worst-for-grades (Assuming user has already loaded data, or else an error message will print informing user)
        Please type your command (Options: L, S, H, W, B, Q): W
        Please enter the attribute you want to calculate the worse value of the attribute for in terms of grades (Options: Age, StudyTime, Failures, Health, Absences): StudyTime
        The worst value for the attribute StudyTime is 1.0 and the average grade they received is 10.15

    ** Upon the user entering "B" for best-for-grades (Assuming user has already loaded data, or else an error message will print informing user)
        Please type your command (Options: L, S, H, W, B, Q): B
        Please enter the attribute you want to calculate the best value of the attribute for in terms of grades (Options: Age, StudyTime, Failures, Health, Absences): Age
        The best value for the attribute Age is 16.89 and the average grade they received is 11.15

    The interface function displays an interface for the user to navigate through using the shell and given prompts. This interface allows the user to load data, sort data, display a histogram, show the worst-for-grades of an attribute, the best-for-grades for an attribute, and finally to quit the program. This interface is a combination of all the previous lab's functions.

    The interface function takes no input parameters.

    Preconditions: The interface function calls many of our previous lab's files, so all files submitted alongside this one must be in the same folder for the function to run. The initial command asking if you want to load data and so forth allows uppercase or lowercase letters, but the sections where the function prompts you to enter in an attribute is case sensitive. The file name the user enters in the "Load Data" prompt must be a real file, and must be in the same folder as this text_ui program.
    """
    supported_cmds = ["L", "S", "H", "W", "B", "Q", "School", "Age",
                      "StudyTime", "Failures", "Health", "Absences", "G1", "G2", "G3", "G_Avg", "Yes", "No"]  # Create the list of supported commands for throughout the lab
    filename = ""  # Create the variable for the filename which will be accessed throughout the function
    loaded_data = {}  # Create the a variable that stores the data loaded from the load data command to be accessed throughout the function
    while True:  # Loop until quit

        # Print interface
        tab = "\t"
        print("The available commands are:")
        print(tab + "1. L) oad Data")
        print(tab + "2. S) ort Data")
        print(tab + tab + "'School'    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'    'G1'    'G2'    'G3'    'G_Avg'")
        print(tab + "3. H) istogram")
        print(tab + tab + "'School'    'Age'    'StudyTime'    'Failures'    'Health'    'Absences'")
        print(tab + "4. W) orst ____ for Grades")
        print(tab + tab + "'Age'    'StudyTime'    'Failures'    'Health'    'Absences'")
        print(tab + "5. B) est ____ for Grades")
        print(tab + tab + "'Age'    'StudyTime'    'Failures'    'Health'    'Absences'")
        print(tab + "6. Q) uit\n")

        # Get initial command
        # Convert user input to uppercase, allowing user to enter upper or lower and not display errors
        cmd = (input("Please type your command (Options: L, S, H, W, B, Q): ")).upper()
        # If the user input was invalid, prompt the user to retry.
        while (cmd not in supported_cmds):
            cmd = (input(
                "Invalid command. Please type your command: ")).upper()

        # Perform initial command
        if (cmd == "Q"):  # Quit command
            break  # Break out of while loop, essentially ending the program

        elif (cmd == "L"):  # Load Data command
            # Get the file name from the user
            filename = input("Please enter the name of the file: ")
            cmd2 = (input(
                "Please enter the attribute to use as key (Options: Failures, Health, Age, School): ")).capitalize()  # Get the attribute the user wants to load the data by
            # If the attribute the user entered is invalid, prompt user to try again
            while (cmd2 not in supported_cmds):
                cmd2 = (input(
                    "Invalid command. Please enter the attribute to use as key for loading the data: ")).capitalize()
            # Sort through and find which attribute the user wanted to load data by, and then print a statement letting the user know the data has been loaded
            if cmd2 == "Failures":
                loaded_data = T012_M1_load_data.add_average(
                    T012_M1_load_data.student_failures_dictionary(filename))
                print("Data loaded" + "\n")
            elif cmd2 == "Health":
                loaded_data = T012_M1_load_data.add_average(
                    T012_M1_load_data.student_health_dictionary(filename))
                print("Data loaded" + "\n")
            elif cmd2 == "School":
                loaded_data = T012_M1_load_data.add_average(
                    T012_M1_load_data.student_school_dictionary(filename))
                print("Data loaded" + "\n")
            elif cmd2 == "Age":
                loaded_data = T012_M1_load_data.add_average(
                    T012_M1_load_data.student_age_dictionary(filename))
                print("Data loaded" + "\n")
            else:
                # If an error occurs, print that an error occured
                print("\n" + "Load data error" + "\n")

        elif (cmd == "S"):  # Sort Data command
            # Create a variable of the sorted data to be accessed throughout this if statement
            sorted_data = []
            if loaded_data == {}:  # Error preventative if statement incase loaded data hasn't been loaded yet
                print("File not loaded. Please, load a file first.")
            else:
                cmd3 = input(
                    "Please enter the attribute you want to use for sorting (Options: School, Age, StudyTime, Failures, Health, Absences, G1, G2, G3, G_Avg): ")  # Get sorting attribute from the user
                # If the attribute the user entered is invalid, prompt user to try again
                while (cmd3 not in supported_cmds):
                    cmd3 = input(
                        "Invalid command. Please enter the attribute to use as key for sorting: ")
                sorted_data = (T012_M2_sort_plot.sort_students_selection(
                    loaded_data, cmd3))  # Store the sorted data
                cmd4 = (input("sorted_data loaded, and sorted by " + str(cmd3) +
                              ". Do you want to display the data? (Options: Yes or No): ")).capitalize()  # Ask the user if they want to display the data
                # If user enters invalid command, prompt to retry
                while (cmd4 not in supported_cmds):
                    cmd4 = (input(
                        "Invalid command. Do you want to display the data? (Options: Yes or No): ")).capitalize()
                if cmd4 == "Yes":
                    # If the user wants to display the data, print the sorted data.
                    print(str(sorted_data) + "\n")
                else:
                    print()

        elif (cmd == "H"):  # Histogram command
            if loaded_data == {}:  # Error preventative if statement incase loaded data hasn't been loaded yet
                print("File not loaded. Please, load a file first.\n")
            else:
                cmd5 = input(
                    "Please enter the attribute you want to use for the histogram (Options: School, Age, StudyTime, Failures, Health, Absences, G1, G2, G3, G_Avg): ")  # Get the attribute the user wants to display the histogram by
                # If user enters invalid command, prompt to retry
                while (cmd5 not in supported_cmds):
                    cmd5 = input(
                        "Invalid command. Please enter the attribute you want to use for the histogram (Options: School, Age, StudyTime, Failures, Health, Absences, G1, G2, G3, G_Avg): ")
                T012_M2_sort_plot.histogram(
                    dict(loaded_data), cmd5)  # Display the histogram

        elif (cmd == "W"):  # Worst for grades
            if loaded_data == {}:  # Error preventative if statement incase loaded data hasn't been loaded yet
                print("File not loaded. Please, load a file first.\n")
            else:
                atb = input(
                    "Please enter the attribute you want to calculate the worse value of the attribute for in terms of grades (Options: Age, StudyTime, Failures, Health, Absences): ")  # Get the attribute the user wants to calculate the worst-for-grades by
                # Calculate the worst-for-grades by the attribute used the loaded_data dictionary and add it to the atb_val variable
                atb_val = (T012_M3_optimization.minimum(loaded_data, atb))
                print("The worst value for the attribute " +
                      str(atb) + " is " + str(atb_val[0]) + " and the average grade they received is " + str(atb_val[1]) + "\n")  # Print the worst-for-grades values

        elif (cmd == "B"):  # Best for grades
            if loaded_data == {}:  # Error preventative if statement incase loaded data hasn't been loaded yet
                print("File not loaded. Please, load a file first.\n")
            else:
                atb2 = input(
                    "Please enter the attribute you want to calculate the best value of the attribute for in terms of grades (Options: Age, StudyTime, Failures, Health, Absences): ")  # Get the attribute the user wants to calculate the best-for-grades by
                # Calculate the best-for-grades by the attribute used the loaded_data dictionary
                atb_val2 = (T012_M3_optimization.maximum(loaded_data, atb2))
                print("The best value for the attribute " +
                      str(atb2) + " is " + str(atb_val2[0]) + " and the average grade they received is " + str(atb_val2[1]) + "\n")  # Print the best-for-grades values

        else:
            print()

    return


# Main
if __name__ == "__main__":
    text_ui()
