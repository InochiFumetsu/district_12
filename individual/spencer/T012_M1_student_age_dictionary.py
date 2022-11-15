# STUDENT AGE DICTIONARY FILE

# AUTHOR: SPENCER HISCOX
# STUDENT NO.: 101230073


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


# MAIN SCRIPT (CALLING FUNCTION)
student_age_dictionary = student_age_dictionary('student-mat.csv')
