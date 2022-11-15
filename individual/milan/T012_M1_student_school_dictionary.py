import string
from typing import List


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
