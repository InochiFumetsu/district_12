from typing import Tuple, Dict, List
import check_equal
import T012_M1_load_data


def check_no_entries_by_key(i_dict: Dict[str or int, List[dict]], 
                            file_name: str) -> Tuple[list]:
    """Return true if number of data entries contained under each key in the 
    dictionary being tested (i_dict) is equal to the number of lines whose value
    is that key in the file from which i_dict was created (file_name), and false
    otherwise.

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

    expected = {}
    metric = ''
    with open(file_name, 'r') as file:
        keys = file.readline().strip("\n ").split(sep=",")
        for dict_key in iter(i_dict):
            for key in keys:
                if key in i_dict[dict_key][0]:
                    continue
                else:
                    metric = key
                    break
            break
        index = keys.index(metric)
        key = 0
        for line in file:
            line = line.strip("\n ").split(sep=",")
            if line[index].isdigit():
                if (len(line[index].rsplit(sep=".")) - 1):
                    key = float(line[index])
                else:
                    key = int(line[index])
            else:
                key = line[index]
            if key in expected:
                expected[key] += 1
            else:
                expected[key] = 1

    actual = {}
    for key in iter(i_dict):
        actual[key] = len(i_dict[key])

    test_identifier = ("Number of data entries by key for " 
                      f"student_{metric.lower()}_dictionary()")
    
    if len(actual) == len(expected):
        for key in expected:
            if key in actual:
                if check_equal.check_equal(test_identifier + f", key = {key}", 
                                           actual[key], expected[key]):
                    continue
            print(test_identifier + f"FAILED: expected {key} key in dict," +
                  f"found {None}")
            return False
        return True

    print(test_identifier + f"FAILED: expected {len(expected)} keys in dict, " +
          f"got {len(actual)}")
    return False


dictionaries = [T012_M1_load_data.student_school_dictionary("student-mat.csv"), 
               T012_M1_load_data.student_health_dictionary("student-mat.csv"), 
               T012_M1_load_data.student_age_dictionary("student-mat.csv"), 
               T012_M1_load_data.student_failures_dictionary("student-mat.csv")]

checks_passed = 0
for dictionary in dictionaries:
    checks_passed += int(check_no_entries_by_key(dictionary,
                         "student-mat.csv"))
print(f"\n\n\nChecks passed: {checks_passed} / 4")
