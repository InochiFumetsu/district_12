import string
from typing import List

#LOAD DATA MODULE
#AUTHORS:
#   Spencer Hiscox
#   Jack Roberts
#   Esteban Heidrich
#   Milan Djordjevic

def student_school_dictionary(filepath: str) -> dict[list]:
    """
    Return a dictionary with loaded data given a filepath of a .csv file.
    Precondition: filepath is a correct and existing file path to a .csv file
    >>>student_school_dictionary("student-mat.csv")
    {'GP': [{'Age': 18, 'StudyTime': 2, 'Failure': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},
            {'Age': 17, 'StudyTime': 2, 'Failure': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},
            ...],
     'MB': [{'Age': 18, 'StudyTime': 2, 'Failure': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},
            {'Age': 17, 'StudyTime': 2, 'Failure': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}
            ...],
      ...}
    """
    KEY_TYPE = 'School'
    file = open(filepath, "r")
    master_dictionary = {}
    first_run = True

    for line in file:
        temp_dict = {}
        if first_run:
            first_line = line.strip()
            key_list = first_line.split(",")
            # finds index of "School" key to avoid hard coding the index 0 (ex: suppose the column "School" was not the first column)
            for i in range(len(key_list)):
                if key_list[i] == KEY_TYPE:
                    index = i

            # get list of keys for inner and removes "School"
            key_list.remove(KEY_TYPE)
            first_run = False
        else:  # not first line
            line = line.strip()
            rows = line.split(",")
            # removes 'GP, or 'MP' from dictionary...
            copy_rows = rows.copy()
            rows.remove(rows[index])
            student_dictionary = {}

            for i in range(len(key_list)):  # creates the subset dictionary
                student_dictionary[key_list[i]] = int(rows[i])
            # make line a dictionary minus KEY_TYPE DATA (remove)

            if copy_rows[index] in master_dictionary:
                # add onto pre-existing list if key already exists
                master_dictionary[copy_rows[index]].append(
                    student_dictionary)

            else:  # the key does not exist yet, so add a key and a new list as its value; add dictionary to this list

                master_dictionary[copy_rows[index]] = []
                master_dictionary[copy_rows[index]].append(
                    student_dictionary)

    file.close()
    return master_dictionary  # loaded_dictionary
"""
● Copy the four functions developed in Task 1 into this file. Ensure that the functions are one after the other and the main script 
  (i.e., all function calls, a combination of the main scripts of the four individual files) are at the end of the file.
● Run Txxx_M1_load_data.py and ensure that there are no errors.

1. Follow the FDR to implement a function called load_data. This function must be placed below the four individual functions in the file Txxx_M1_load_data.py
Function Description:
  ● The function lets the user choose how the data will be loaded (i.e., which of the four functions you developed should be used).
  ● It takes two input parameters: (1) the file name where the data is stored, and (2) a string describing the key of the dictionary to be returned 
    ('School', 'Age', 'Health', 'Failures').
  ● It returns a dictionary with the data loaded using the key based on the input parameter. If the key provided is not valid, the function will print the error 
    message “Invalid Key” and return an empty dictionary.
2. Test your function. For this lab, you can just call your function to ensure that the data is loaded correctly. For testing purposes, use student-mat.csv. 
Ensure that the function calls are added to the end of the main script.

1. Follow the FDR to implement a function called add_average. This function must be placed inside the file Txxx_M1_load_data.py below load_data.
Function Description:
● The function will add the average of the student’s grades (G1, G2 and G3) as an additional attribute to the dictionary.
● It takes one input parameter (regardless of the key): (1) a dictionary
● It returns the dictionary updated with the average grade. Sample output (assuming school as key):
{ 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 },
{another element},
… ],
'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33 },
{another element},
… ],
… }
2. Test your function. For this lab, you can just call your function to ensure that the data is loaded correctly. For testing purposes, use student-mat.csv. 
Ensure that the function calls are added to the end of the main script.

1. Submit your module (Txxx_M1_load_data.py) on Brightspace (One submission per team). Before you submit, ensure:
  a. All the active team members’ names are at the top of the file as a Python comment. If a name is missing, that person will receive zero. We will assume that 
     the person did not participate in the task.
  b. The functions have the proper names.
  c. You have included type annotations and docstrings. Do not forget to include the preconditions, if any.
  d. At the end of the file, you have the main script in which the functions are called, and all testing scenarios are covered. For this lab, function calls are 
     enough to ensure that the data is properly loaded.
  e. The file name is correct.
  f. Run Txxx_M1_load_data.py one more time to ensure that there are no errors!
"""

#!! BELOW ALL OTHER FUNCTIONS!!
def add_average():
