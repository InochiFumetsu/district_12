from typing import Tuple, Dict, List


def check_equal(description: str, actual: any, expected: any) -> bool:
    """
    Print a "passed" message if actual and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    actual.
    
    Parameters "actual" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    actual_type = type(actual)
    expected_type = type(expected)
    if actual_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but actual ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      actual, str(actual_type).strip('<class> ')))
        return False
    elif actual != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, actual))
        return False
    else:
        print("{0} PASSED".format(description))
    print("------")
    return True
    


#Spencer's check (test 2).
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
    Number of entries, by key in student_school_dictionary():   PASSED
    ------
    Number of entries, by key in student_health_dictionary():   PASSED
    ------
    Number of entries, by key in student_age_dictionary():      PASSED
    ------
    Number of entries, by key in student_failures_dictionary(): PASSED
    ------
    True
    >>>check_no_entries_by_key(student_age_dictionary("student-mat.csv"),
    "data_file_missing_entries_under_key_18.csv")
    Number of entries, by key in student_age_dictionary():      FAILED: expected 
    {18.0: 82, 17.0: 98, 15.0: 82, 16.0: 104, 19.0: 24, 22.0: 1, 20.0: 3, 21.0: 1}, 
    got {18: 81, 17: 98, 15: 82, 16: 104, 19: 24, 22: 1, 20: 3, 21: 1}
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
                    if abs(int(
                    adjusted[-1].rstrip(".")) / 10 - float(key)) > 0.0001:
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
                    if abs(int(line[index].rstrip(".")) / 10 - 
                           float(line[index])) > 0.0001:
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

#Milan's function (test 4).
def check_add_average(original_dict: dict) -> bool:
    """
    Return True if ALL of the following series of tests pass:
    1) The number of students in the original dictionary is the same as the number 
    of students in the dictionary returned by the add_average() function.
    2) The G_Avg key was successfully added to the new dictionary for all students. 
    3) Lastly, one random student is selected and their average of
    G1, G2, and G3 is compared to the calculated average from the modified dictionary.
    Otherwise, return False.
    Precondition: The dictionary passed must come from data from "student-mat.csv"
    and as such the original dictionary is properly formatted with correct key-value pairs.

    >>>check_add_average(sorted_student_school_dictionary)
    Number of students remains the same in either dictionary: PASSED
    G_Avg key was successfully added to the new dictionary: PASSED
    Correct Average Calculated for random sample: PASSED
    True

    """
    # assumes all test cases have failed
    same_number = False
    added_successfully = False
    random_avg = False
    counter_original = 0

    modified_dict = T012_M1_load_data.add_average(original_dict)
    for lists in original_dict.values():  # counts the number of students in original dictionary
        counter_original += len(lists)

    # random sample number generated
    random_student = random.randint(1, counter_original)

    counter_modified = 0

    counter_G_Avg = 0

    for lists in modified_dict.values():

        for i in range(len(lists)):
            counter_modified += 1  # counts the number of students in updated dictionary
            if "G_Avg" in lists[i]:  # checks if "G_Avg" has been added
                counter_G_Avg += 1
            if random_student == counter_modified:  # random sample average compared to actual given average
                sample_avg = round(
                    (lists[i]["G1"] + lists[i]["G2"] + lists[i]["G3"]) / 3, 2)
                actual_avg = lists[i]["G_Avg"]

    if check_equal("Number of students remains the same in either dictionary:", counter_original, counter_modified):
        same_number = True
    if check_equal("G_Avg key was successfully added to the new dictionary:", counter_original, counter_G_Avg):
        added_successfully = True
    if check_equal("Correct Average Calculated for random sample:", sample_avg, actual_avg):
        random_avg = True

    if same_number and added_successfully and random_avg:  # All three cases must be correct to return True
        return True
    else:  # Failure in any one of the checks
        return False