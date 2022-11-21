#LOAD DATA MODULE
#AUTHORS:
#   Spencer Hiscox    101230073
#   Jack Roberts      101261505
#   Esteban Heidrich  101267959
#   Milan Djordjevic  101262178



import string
from typing import List, Dict


def student_school_dictionary(filepath: str) ->Dict[int or str, List[dict]]:
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

  
  
def student_health_dictionary(file_name: str) -> Dict[int or str, List[dict]]:
    """This function takes student information and sorts them by their health 
    condition. 
    
    precondtions: file_name must be an existing file in the same folder as 
    this function
    
    >>>student_health_dictionary("student_info.txt")
    {'3': [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Failures': '0',
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another element},
    ...], 
    {'5': [{'School': 'GP', 'Age': '15', 'StudyTime': '3', 'Failures': '0',
    'Absences': '2', 'G1': '15', 'G2': '14', 'G3': '15'}, {another element},
    ...], 
    ...}
    """
    health_dictionary = {}
    first_run = True
    counter = 0
    raw_data = []
    file_content = open(file_name, "r")
    for line in file_content:
        if first_run:           
            student_dict_keys = line.strip().split(",")
            first_run = False
        raw_data += [0]
        raw_data[counter] = line.strip()
        counter += 1
    del raw_data[0]
    for j in raw_data:
        student_stat = j.split(",")
        health = int(student_stat[4])
        if not health in health_dictionary:
            health_dictionary[health] = []
        health_dictionary[health].append({
            student_dict_keys[0]: student_stat[0],
            student_dict_keys[1]: int(student_stat[1]),
            student_dict_keys[2]: float(student_stat[2]),
            student_dict_keys[3]: int(student_stat[3]),
            student_dict_keys[5]: int(student_stat[5]),
            student_dict_keys[6]: float(student_stat[6]),
            student_dict_keys[7]: float(student_stat[7]),
            student_dict_keys[8]: float(student_stat[8]),
        })
        file_content.close()
    return health_dictionary
  
  

def student_age_dictionary(file_name: str) -> dict:
    """Return dictionary object with student ages as keys and a list of 
    dictionaries of the student information of students who are the age 
    indicated by the key as the values. The dataset is imported from the
    .csv file specified by argument 1: 'file_name'.

    Preconditions: file_name must exist. file_name must not be empty. file_name
    must be a .csv file-type.

    >>>student_age_dictionary('student-mat.csv')
    {'18': [{' School': 'GP', 'StudyTime': '2.0', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5.0', 'G2': '6.0', 'G3': '6.0'},..., {' School': 'MS', 
    'StudyTime': '1.0', 'Failures': '0', 'Health': '5', 'Absences': '0', 'G1': 
    '11.0', 'G2': '12.0', 'G3': '10.0'}], 
    '17': [{' School': 'GP', 'StudyTime': '2.0', 'Failures': '0', 'Health': '3', 
    'Absences': '4', 'G1': '5.0', 'G2': '5.0', 'G3': '6.0'}, ..., {' School': 'MS', 
    'StudyTime': '1.0', 'Failures': '0', 'Health': '2', 'Absences': '3', 'G1': 
    '14.0', 'G2': '16.0', 'G3': '16.0'}],
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
    float_values = ['StudyTime', 'G1', 'G2', 'G3']
    for i in range(len(raw_import)):
        amalgam = dict()
        for j in range(len(keys)):
            if raw_import[i][j].isdigit():
                if keys[j] in float_values:
                    amalgam[keys[j]] = float(raw_import[i][j])
                else:
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

  
  
def student_failures_dictionary(filename: str) -> Dict[int or str, List[dict]]:
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
  


def load_data(file_name: str, dict_key: str) -> Dict[int or str, List[dict]]:
    """This function takes two inputs: the file name and the dictionary key 
    that the user wants and returns the chosen dictionary
    
    preconditions: file_name exists and is the right format and dict_key is one
    of the existing dictionaries
    
    >>>load_data(data-mat.csv, Health)
    {'3': [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Failures': '0',
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another element},
    ...], 
    {'5': [{'School': 'GP', 'Age': '15', 'StudyTime': '3', 'Failures': '0',
    'Absences': '2', 'G1': '15', 'G2': '14', 'G3': '15'}, {another element},
    ...], 
    ...}
    >>>load_data('student-mat.csv', 'Health')
    'Invalid Key'
    """

    chosen_dictionary = {}
    if dict_key.lower() == "school":
        chosen_dictionary = student_school_dictionary(file_name)
    elif dict_key.lower() == "age":
        chosen_dictionary = student_age_dictionary(file_name)
    elif dict_key.lower() == "health":
        chosen_dictionary = student_health_dictionary(file_name)
    elif dict_key.lower() == "failures":
        chosen_dictionary = student_failures_dictionary(file_name)
    else:
        print("Invalid Key")
    return chosen_dictionary
  
  
  
def add_average(i_dict: Dict[int or str, List[dict]]) -> Dict[int or str, List[dict]]:
    """Return i_dict with average grade, with precision of 2, appended to all 
    dictionary-type list entries using 'G_avg' as the key.

    Preconditions: 
        1) i_dict must be of type Dict[int or str, List[dict]] and have been
         generated from any of functions:
            student_school_dictionary()
            student_health_dictionary()
            student_age_dictionary()
            student_failures_dictionary()
        2) i_dict dictionary-type list entries must contain keys 'G1', 'G2' and 
         'G3'representative of grades achieved by student whose data is 
         represented by entry.

    >>>add_average(student_age_dictionary('student-mat.csv'))
    {18: [{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'School': 'MB', 
    'StudyTime': 1, 'Failures': 2, 'Health': 4, 'Absences': 0, 'G1': 7, 'G2': 4, 
    'G3': 0, 'G_Avg': 3.67}, ..., {'School': 'MS', 'StudyTime': 1, 'Failures': 
    0, 'Health': 5, 'Absences': 0, 'G1': 11, 'G2': 12, 'G3': 10, 'G_Avg': 
    11.0}],
    17: {'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 
    4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}, 
    ...]
    ...}
    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument: argument must be of type dict.")

    first_run = True
    i_dict_clone = i_dict.copy()
    for key in iter(i_dict_clone):
        if first_run:
            first_run = False
            if type(i_dict[key]) != list:
                raise TypeError(
                    "Invalid argument: dictionary values must be of type list.")

        for i in range(len(i_dict_clone[key])):
            if not i:
                if type(i_dict[key][i]) != dict:
                    raise TypeError(
                        "Invalid argument: dict-value list entries must be of "
                        "type dict.")

                if not 'G1' in i_dict[key][i] \
                        or not 'G2' in i_dict[key][i] \
                        or not 'G3' in i_dict[key][i]:
                    raise KeyError(
                        "Invalid argument: dataset incompatible. Grades keys "
                        "not found: \"G1\"/\"G2\"/\"G3\" not found.")

                if type(i_dict[key][i]['G1']) != int \
                   or type(i_dict[key][i]['G2']) != int \
                   or type(i_dict[key][i]['G3']) != int:
                    raise ValueError(
                        "Invalid argument: list-entry dicts must contain "
                        "integer values at grades keys.")

            grade_keys = ['G1', 'G2', 'G3']
            average = 0
            for grade_key in grade_keys:
                average += i_dict_clone[key][i][grade_key]
            average = round(average / 3, 2)
            i_dict_clone[key][i]['G_Avg'] = average

    return i_dict_clone



# MAIN() SCRIPT
sorted_student_school_dictionary = student_school_dictionary("student-mat.csv")
sorted_student_health_dictionary = student_health_dictionary("student-mat.csv")
sorted_student_age_dictionary = student_age_dictionary('student-mat.csv')
sorted_student_failures_dictionary = student_failures_dictionary('student-mat.csv')

loaded_data_example = load_data("student-mat.csv", "Health")
loaded_data_ex2 = load_data("student-mat.csv", "Age")
loaded_data_ex3 = load_data("student-mat.csv", "School")
loaded_data_ex4 = load_data("student-mat.csv", "Failures")

dict_with_grade_average_added = add_average(sorted_student_failures_dictionary)
dict_with_grade_average_added2 = add_average(sorted_student_school_dictionary)
dict_with_grade_average_added3 = add_average(sorted_student_health_dictionary)
dict_with_grade_average_added4 = add_average(sorted_student_age_dictionary)

