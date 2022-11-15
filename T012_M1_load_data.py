#LOAD DATA MODULE
#AUTHORS:
#   Spencer Hiscox    101230073
#   Jack Roberts
#   Esteban Heidrich
#   Milan Djordjevic  101262178

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



def student_age_dictionary(file_name: str) -> dict:
    """Return dictionary object with student ages as keys and a list of 
    dictionaries of the student information of students who are the age 
    indicated by the key as the values. The dataset is imported from the
    .csv file specified by argument 1: 'file_name'.

    Preconditions: file_name must exist. file_name must not be empty. file_name
    must be a .csv file-type.

    >>>student_age_dictionary('student-mat.csv')
    {'18': [{' School': 'GP', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'},..., {' School': 'MS', 
    'StudyTime': '1', 'Failures': '0', 'Health': '5', 'Absences': '0', 'G1': 
    '11', 'G2': '12', 'G3': '10'}], 
    '17': [{' School': 'GP', 'StudyTime': '2', 
    'Failures': '0', 'Health': '3', 'Absences': '4', 'G1': '5', 'G2': '5', 'G3': 
    '6'}, ..., {' School': 'MS', 'StudyTime': '1', 'Failures': '0', 'Health': 
    '2', 'Absences': '3', 'G1': '14', 'G2': '16', 'G3': '16'}],
    ...
    }
    """
    if type(file_name) != str:
        raise TypeError(
            f"Invalid argument: {file_name}. "
            "Argument must be of type <string>.")

    if len(file_name) < 4:
        raise ValueError(
            f"[Errno X1] {file_name} is not a valid file name.")

    if file_name[-4:] != ".csv":
        raise ValueError(f"Invalid file type: {file_name} is not a "
                         "comma-separated value file. "
                         "(File is not .csv extension)")

    with open(file_name, 'r') as data_file:
        raw_import = []
        for line in data_file:
            raw_import.append(line)

    if not raw_import:
        raise EOFError(f"[Errno X2] {file_name}: file is empty.")

    keys = raw_import[0].strip("\n ").split(sep=",")
    del raw_import[0]

    if len(keys) == 1:
        raise RuntimeError(
            f"[Errno X3] {file_name} contains only one data field per entry.")

    if 'Age' not in keys:
        raise KeyError(
            f"{file_name}: dataset not compatible. \"Age\" field not found.")
    del file_name

    for i in range(len(raw_import)):
        raw_import[i] = raw_import[i].strip("\n ").split(sep=",")

    entries = []
    for i in range(len(raw_import)):
        amalgam = dict()
        for j in range(len(keys)):
            if raw_import[i][j].isdigit():
                amalgam[keys[j]] = int(raw_import[i][j])
            else:
                amalgam[keys[j]] = raw_import[i][j]
        entries.append(amalgam)
    del raw_import, keys

    age_dictionary = dict()
    for i in range(len(entries)):
        if entries[i]['Age'] in age_dictionary:
            age_dictionary[entries[i]['Age']].append(entries[i])
        else:
            age_dictionary[entries[i]['Age']] = [entries[i]]
        del age_dictionary[entries[i]['Age']][-1]['Age']
    del entries

    return age_dictionary

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
            # removes 'GP, or 'MP' from dictionary after making a copy of the original list...
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




#!! BELOW ALL OTHER FUNCTIONS!!
def load_data():
def add_average():



# MAIN SCRIPT (CALLING FUNCTION)
student_age_dictionary = student_age_dictionary('student-mat.csv')
student_school_dictionary = student_school_dictionary("student-mat.csv")
