# STUDENT FAILURES DICTIONARY FILE

# AUTHOR: Jack Roberts 101261505

import string
from typing import List


def student_failures_dictionary(filename: str) -> dict[list]:
    """
    Examples: student_failures_dictionary('student-mat_test.csv')  **student-mat_test.csv contains the first student listed in the original student-mat file from each school.

    {0: [{' School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {' School': 'MB', 'Age': 16, 'StudyTime': 2, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {' School': 'MS', 'Age': 18, 'StudyTime': 2, 'Health': 5, 'Absences': 2, 'G1': 11, 'G2': 11, 'G3': 11}], 1: [{' School': 'CF', 'Age': 16, 'StudyTime': 2, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {' School': 'BD', 'Age': 18, 'StudyTime': 2, 'Health': 2, 'Absences': 0, 'G1': 7, 'G2': 7, 'G3': 0}]}


    Function: The function student_failures_dictionary takes an input parameter which is supposed to be a csv file name as a string, and returns a dictionary of lists of dictionaries (the values in each row of the csv file).

    Parameters: The only input parameter is the filename parameter. This parameter expects a string containing a csv file name that is located in the same folder as this module.

    Preconditions: Past failures must range from 0-10, filename must contain no spaces and be of the format .csv, the file must not be empty, the file must contain a key of columns in the first row that contains a cell with 'Failures'.
    """

    infile = open(filename, "r")  # Open the file name of the input parameter

    # Create a list that holds a string of every line of the input parameter
    basic_import = []
    for i in infile:  # For loop that indexes through the file and append each line to the list
        basic_import.append(i)

    keys = []  # List for they keys of the csv file
    # Seperate the keys with commas and remove the new line at the end
    basic_import[0] = basic_import[0].strip('\n').split(sep=',')
    # For loop that loops through the first line of the csv file and appends the keys
    for i in basic_import[0]:
        keys.append(i)

    info = []  # List for the values of each cell in each line below index 0
    # For loop that loops through each line of the csv file and appends the values of each cell in a line to info
    for i in basic_import[1:]:
        info.append(i)

    # Loop through info and properly format it so it can be used later
    for i in range(len(info)):
        info[i] = info[i].strip('\n').split(sep=',')

    for i in range(len(info)):  # Loop through the info list and convert all values under each key to the type integer, except values under the key 'School'
        for j in range(len(info[0])):
            if j == 0:
                (info[i])[j] = str((info[i])[j])
            else:
                (info[i])[j] = int((info[i])[j])

    students = []  # Create list of students that holds each student's info
    # For each row in the length of the info list, create a hold dictionary
    for row in range(len(info)):
        hold = {}
        # For each column of each row for the lengths of the keys list, pull the value from the cell at row and column and assign it to hold at index
        for col in range(len(keys)):
            hold[keys[col]] = info[row][col]
        # Upload values for each student from hold dictionary
        students.append(hold)

    failures_dict = {}  # Create the dictionary with the key being number of failures

    # For loop that loops through the lengths of the students list
    for i in range(len(students)):
        # If statement that checks to see if the current number of failures for the student at index is alright a failures list in the failures dict dictionary
        if students[i]['Failures'] in failures_dict:
            # Adds the student and their info to the list that corresponds with their failures inside the dictionary
            failures_dict[students[i]['Failures']].append(students[i])
            del failures_dict[students[i]['Failures']][len(
                failures_dict[students[i]['Failures']]) - 1]['Failures']  # Deletes the failures key inside the student's info

        else:
            # Creates a list that corresponds to the number of failures of the student at index, and adds the rest of that students info to the dictionary
            failures_dict[students[i]['Failures']] = [students[i]]
            del failures_dict[students[i]['Failures']][len(
                failures_dict[students[i]['Failures']]) - 1]['Failures']  # Deletes the failures key inside the student's info

    infile.close()  # Close the csv file
    return failures_dict
