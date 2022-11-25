from typing import Tuple, Dict, List
import check_equal
import T012_M1_load_data


def check_no_entries_by_key(i_dict: Dict[str or int, List[dict]], 
                            file_name: str) -> bool:
    """Return true if number of data entries contained under each key in the 
    dictionary being tested (i_dict) is equal to the number of lines whose value
    is that key in the file from which i_dict was created (file_name), and false
    otherwise.
    
    Preconditions: 
        1) file name passed in as 'file_name' must be the original data file 
               from which the dictionary passed in as 'i_dict' was generated.
        2) file_name must be a .csv or .txt file extension and the first line of 
               the file must contain the headers of the data columns of the file
               (used as keys in the dicitonary generated from that file).

    >>>check_no_entries_by_key(student_age_dictionary("student-mat.csv"), 
    "student-mat.csv")
    Number of data entries by key for student_age_dictionary(), key = 18 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 17 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 15 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 16 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 19 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 22 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 20 PASSED
    -----
    Number of data entries by key for student_age_dictionary(), key = 21 PASSED
    -----
    True
    >>>check_no_entries_by_key(student_age_dictionary("student-mat.csv"),
    "some-other-data-file.csv"
    Number of data entries by key for student_age_dictionary(), key = 18 FAILED:
     expected 82, got 0"
    False
    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument: argument must be of type dict.")
    for key in i_dict:
        if type(i_dict[key]) != list:
            raise TypeError(
                "Invalid argument: dictionary values must be of type list.")
        for entry in i_dict[key]:
            if type(entry) != dict:
                raise TypeError(
                    "Invalid argument: dict-value list entries must be of type "
                    "dict.")
            break
        break

    if type(file_name) != str:
        raise TypeError(f"Invalid argument: {file_name}. "
                        "Argument must be of type <string>.")
    if file_name[-4:] != ".csv" and file_name[-4:] != ".txt":
        raise ValueError(f"Invalid argument: {file_name} is not a text file or"
                         " a comma-separated-value (.csv) file.")

    expected = {}
    metric = ''
    actual = {}
    key_fail = False
    with open(file_name, 'r') as file:
        keys = file.readline().strip("\n ").split(sep=",")
        for dict_key in iter(i_dict):
            adjusted = []
            for key in i_dict[dict_key][0]:
                adjusted.append(str(key.strip(" \n").replace(" ", "")))
                if adjusted[-1].isdigit():
                    if abs(int(adjusted[-1].rstrip(".")) - float(key)) > 0.0001:
                        adjusted[-1] = float(adjusted)
                    else:
                        adjusted[-1] = int(adjusted)
                if adjusted[-1] != key:
                    actual = key.replace(" ", "_")
                    expected = adjusted[-1]
                    key_fail = True
            for key in keys:
                if key in adjusted:
                    if keys.index(key) == len(keys) - 1:
                        metric = expected
                    continue
                else:
                    metric = key
                    break
            break
        if not key_fail:
            index = keys.index(metric)
            key = 0
            for line in file:
                line = line.strip("\n").replace(" ", "").split(sep=",")
                if line[index].isdigit():
                    if abs(int(
                        line[index].rstrip(".")) - float(line[index])) > 0.0001:
                        key = float(line[index])
                    else:
                        key = int(line[index])
                else:
                    key = line[index]
                if key in expected:
                    expected[key] += 1
                else:
                    expected[key] = 1

    if key_fail:
        i_dict = f"student_{metric.lower()}_dictionary()"
        test_id = (f"{i_dict}, key check:")
        fmt_tid = (f'{test_id:<59}')        
        return check_equal.check_equal(fmt_tid, actual, expected)        

    for key in iter(i_dict):
        actual[key] = len(i_dict[key])
    
    i_dict = f"student_{metric.lower()}_dictionary()"
    test_id = (f"Number of entries, by key in {i_dict}:")
    fmt_tid = (f'{test_id:<59}')
    
    return check_equal.check_equal(fmt_tid, actual, expected)



dictionaries = [T012_M1_load_data.student_school_dictionary("student-mat.csv"), 
               T012_M1_load_data.student_health_dictionary("student-mat.csv"), 
               T012_M1_load_data.student_age_dictionary("student-mat.csv"), 
               T012_M1_load_data.student_failures_dictionary("student-mat.csv")]

checks_passed = 0
for dictionary in dictionaries:
    checks_passed += int(check_no_entries_by_key(dictionary, "student-mat.csv"))

print("\n")
print(f'{f"Checks PASSED: {checks_passed}":>66}')
print(f'{f"Checks FAILED: {4 - checks_passed}":>66}')
