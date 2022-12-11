"""
© Copyright 2022, Esteban Heidrich, Jack Roberts, Milan Djordjevic, Spencer Hiscox. All rights reserved. Study-PY™ is a trademark of district_12™ developers.

Copyright © 2005-2022, NumPy Developers. All rights reserved.

Copyright © 2001-2002 Enthought, Inc. 2003-2022, SciPy Developers. All rights reserved.

© Copyright 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012–2022 The Matplotlib development team.

For full licensing information, see the README.md file in the root folder of the master branch of this repository:
https://github.com/InochiFumetsu/district_12/blob/master/README.md
"""


from typing import Tuple, Dict, List
import T012_M1_load_data
import random


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



#Esteban's check (test 1).
def check_equal_dict_keys(file_name: str, dict_name: str) -> bool:
    """this function prepares two lists that are tested by the check_equal
    function and returns how many dictionaries passed the test
    
    precondtitions: file_name must be an existing file in the same folder as 
    this function
    
    >>>check_equal_dict_keys(student-mat.csv, student_school_dictionary)
    True
    """
    if dict_name == "student_school_dictionary":
        dictionary = T012_M1_load_data.student_school_dictionary(file_name)
        dict_num = 0
    elif dict_name == "student_health_dictionary":
        dictionary = T012_M1_load_data.student_health_dictionary(file_name)
        dict_num = 3
    elif dict_name == "student_age_dictionary":
        dictionary = T012_M1_load_data.student_age_dictionary(file_name)
        dict_num = 1
    elif dict_name == "student_failures_dictionary":
        dictionary = T012_M1_load_data.student_failures_dictionary(file_name)
        dict_num = 2
    descrip = f'{f"Checking whether keys in {dict_name} should exist:":<66}'
    score = 0
    expected_keys = set()
    actual_keys = []
    counter = 0
    first_run = True
    file_content = open(file_name, "r")
    for line in file_content:
        if first_run:
            first_run = False
        else:
            raw_line = line.split(",")
            for z in range(4):
                del raw_line[-1]
            del raw_line[2]
            expected_keys.add(raw_line[dict_num])
            counter += 1
    expected_keys = list(expected_keys)
    if not dict_name == "student_school_dictionary":
        for i in range(0, len(expected_keys)):
            expected_keys[i] = int(expected_keys[i])
    for x in iter(dictionary.keys()):
            actual_keys.append(x)
    for l in range(len(actual_keys)):
        index = actual_keys.index(expected_keys[l])
        result = check_equal(descrip, expected_keys[l], 
                                         actual_keys[index])
        if result:
            score += 1
    if score == len(expected_keys):
        return True
    else:
        return False

    

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
    {18.0: 82, 17.0: 98, 15.0: 82, 16.0: 104, 19.0: 24, 22.0: 1, 20.0: 3, 
    21.0: 1}, got {18: 43, 17: 98, 15: 82, 16: 104, 19: 24, 22: 1, 20: 3, 21: 1}
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
                    adjusted[-1].replace(".", "")) / 
                           10 - float(key)) > 0.0001:
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
                    if abs(int(line[index].replace(".", "")) / 10 - 
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
        fmt_tid = (f'{test_id:<66}')        
        return check_equal(fmt_tid, actual, expected)        

    for key in iter(i_dict):
        actual[key] = len(i_dict[key])
    
    i_dict = f"student_{metric.lower()}_dictionary()"
    test_id = (f"Number of entries, by key in {i_dict}:")
    fmt_tid = (f'{test_id:<66}')
    
    return check_equal(fmt_tid, actual, expected)



#Test 3 - Jack (Testing value types)
def type_test() -> bool:
    """
    Example:
    Failures dictionary: Test 1 <class 'str'> PASSED
    ------
    Failures dictionary: Test 2 <class 'int'> PASSED
    ------
    Failures dictionary: Test 3 <class 'float'> PASSED
    ------
    Failures dictionary: Test 4 <class 'int'> PASSED
    ------
    Failures dictionary: Test 5 <class 'int'> PASSED
    ------
    Failures dictionary: Test 6 <class 'float'> PASSED
    ------
    Failures dictionary: Test 7 <class 'float'> PASSED
    ------
    Failures dictionary: Test 8 <class 'float'> PASSED
    ------
    
    Age dictionary: Test 1 <class 'str'> PASSED
    ------
    Age dictionary: Test 2 <class 'float'> PASSED
    ------
    Age dictionary: Test 3 <class 'int'> PASSED
    ------
    Age dictionary: Test 4 <class 'int'> PASSED
    ------
    Age dictionary: Test 5 <class 'int'> PASSED
    ------
    Age dictionary: Test 6 <class 'float'> PASSED
    ------
    Age dictionary: Test 7 <class 'float'> PASSED
    ------
    Age dictionary: Test 8 <class 'float'> PASSED
    ------
    
    Health dictionary: Test 1 <class 'str'> PASSED
    ------
    Health dictionary: Test 2 <class 'int'> PASSED
    ------
    Health dictionary: Test 3 <class 'float'> PASSED
    ------
    Health dictionary: Test 4 <class 'int'> PASSED
    ------
    Health dictionary: Test 5 <class 'int'> PASSED
    ------
    Health dictionary: Test 6 <class 'float'> PASSED
    ------
    Health dictionary: Test 7 <class 'float'> PASSED
    ------
    Health dictionary: Test 8 <class 'float'> PASSED
    ------
    
    School dictionary: Test 1 <class 'int'> PASSED
    ------
    School dictionary: Test 2 <class 'float'> PASSED
    ------
    School dictionary: Test 3 <class 'int'> PASSED
    ------
    School dictionary: Test 4 <class 'int'> PASSED
    ------
    School dictionary: Test 5 <class 'int'> PASSED
    ------
    School dictionary: Test 6 <class 'float'> PASSED
    ------
    School dictionary: Test 7 <class 'float'> PASSED
    ------
    School dictionary: Test 8 <class 'float'> PASSED
    ------
    
    Failures Pass count: 8
    Failures Error count: 0
    Age Pass count: 8
    Age Error count: 0
    Health Pass count: 8
    Health Error count: 0
    School Pass count: 8
    School Error count: 0
    
    (True, True, True, True)

    The function type_test takes the type of the values for each key for the 
    first student in each dictionary, and compares it to a hardcoded set of 
    expected types for the corresponding dictionary.

    This function takes no input parameters.

    Preconditions: This T012_TM1_3 file must be in the same folder as the 
    check_equals file on the computer's hard drive. The check_equals file must
    be the modified file I submitted alongside this file.
    """

    print("")  # Skip a printing line for clarity of reading

    types_failureskey_expected = [
        str, int, float, int, int, float, float, float]  # Create the failure dictionary expected key
    dic = (T012_M1_load_data.student_failures_dictionary(
        'student-mat.csv'))  # Make dic the variable assigned to the student_failures_dictionary
    pass_count_failures = 0  # Create test pass counter
    error_count_failures = 0  # Create test error counter
    for key in dic:  # Create loop for the keys in the dic variable
        # For every "student" (row) in the dictionary at the key
        for student in dic[key]:
            data_types = []  # Create list for types at each key
            # For each key in the "student" (row) list
            for key in student:
                # Append the type of the value of the student at the key
                data_types.append(type(student[key]))
            # For the length of the keys in dic, compare types by calling check_equal
            for i in range(len(data_types)):
                # checks if the elements of data_types match the values you hard coded in types_failureskey_expected below
                if check_equal(f'{f"Failures dictionary: Test {str(i + 1)} {str(data_types[i])}:":<66}', data_types[i], types_failureskey_expected[i]) == True:
                    pass_count_failures += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types[i]) + "=="
                          + str(types_failureskey_expected[i]) + "  ERROR failures")  # Print what line the error was at for debugging purposes
                    error_count_failures += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student

    if pass_count_failures == 8:  # If the test passed for the whole length of keys, set the whole test equal to True
        bool_failures = True
    else:  # Else, set the test equal to False
        bool_failures = False

    # Create the failure dictionary expected key
    types_agekey_expected = [str, float,
                             int, int, int, float, float, float]
    # Make dic the variable assigned to the student_failures_dictionary
    dic_a = (T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    pass_count_age = 0  # Create test pass counter
    error_count_age = 0  # Create test error counter
    for key in dic_a:  # Create loop for the keys in the dic variable
        # For every "student" (row) in the dictionary at the key
        for student in dic_a[key]:
            data_types_a = []  # Create list for types at each key
            # For each key in the "student" (row) list
            for key in student:
                # Append the type of the value of the student at the key
                data_types_a.append(type(student[key]))
            # For the length of the keys in dic_a, compare types by calling check_equal
            for i in range(len(data_types_a)):
                # checks if the elements of data_types match the values you hard coded in types_agekey_expected below
                if check_equal(f'{f"Age dictionary: Test {str(i + 1)} {str(data_types_a[i])}:":<66}', data_types_a[i], types_agekey_expected[i]) == True:
                    pass_count_age += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types_a[i]) + "=="
                          + str(types_agekey_expected[i]) + "  ERROR age")  # Print what line the error was at for debugging purposes
                    error_count_age += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student

    if pass_count_age == 8:  # If the test passed for the whole length of keys, set the whole test equal to True
        bool_age = True
    else:  # Else, set the test equal to False
        bool_age = False

    types_healthkey_expected = [
        str, int, float, int, int, float, float, float]  # Create the failure dictionary expected key
    # Make dic the variable assigned to the student_failures_dictionary
    dic_h = (T012_M1_load_data.student_health_dictionary('student-mat.csv'))
    pass_count_health = 0  # Create test pass counter
    error_count_health = 0  # Create test error counter
    for key in dic_h:  # Create loop for the keys in the dic variable
        # For every "student" (row) in the dictionary at the key
        for student in dic_h[key]:
            data_types_h = []  # Create list for types at each key
            # For each key in the "student" (row) list
            for key in student:
                # Append the type of the value of the student at the key
                data_types_h.append(type(student[key]))
            # For the length of the keys in dic_a, compare types by calling check_equal
            for i in range(len(data_types_h)):
                # checks if the elements of data_types match the values you hard coded in types_healthkey_expected below
                if check_equal(f'{f"Health dictionary: Test {str(i + 1)} {str(data_types_h[i])}:":<66}', data_types_h[i], types_healthkey_expected[i]) == True:
                    pass_count_health += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types_h[i]) + "=="
                          + str(types_healthkey_expected[i]) + "  ERROR health")  # Print what line the error was at for debugging purposes
                    error_count_health += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student

    if pass_count_health == 8:  # If the test passed for the whole length of keys, set the whole test equal to True
        bool_health = True
    else:  # Else, set the test equal to False
        bool_health = False

    types_schoolkey_expected = [
        int, float, int, int, int, float, float, float]  # Create the failure dictionary expected key
    # Make dic the variable assigned to the student_failures_dictionary
    dic_s = (T012_M1_load_data.student_school_dictionary('student-mat.csv'))
    pass_count_school = 0  # Create test pass counter
    error_count_school = 0  # Create test error counter
    for key in dic_s:  # Create loop for the keys in the dic variable
        # For every "student" (row) in the dictionary at the key
        for student in dic_s[key]:
            data_types_s = []  # Create list for types at each key
            # For each key in the "student" (row) list
            for key in student:
                # Append the type of the value of the student at the key
                data_types_s.append(type(student[key]))
            # For the length of the keys in dic_a, compare types by calling check_equal
            for i in range(len(data_types_s)):
                # checks if the elements of data_types match the values you hard coded in types_schoolkey_expected below
                if check_equal(f'{f"School dictionary: Test {str(i + 1)} {str(data_types_s[i])}:":<66}', data_types_s[i], types_schoolkey_expected[i]) == True:
                    pass_count_school += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types_s[i]) + "=="
                          + str(types_schoolkey_expected[i]) + "  ERROR school")  # Print what line the error was at for debugging purposes
                    error_count_school += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student

    if pass_count_school == 8:  # If the test passed for the whole length of keys, set the whole test equal to True
        bool_school = True
    else:  # Else, set the test equal to False
        bool_school = False

    return bool_failures, bool_age, bool_health, bool_school



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

    if check_equal(f'{"Number of students remains the same in either dictionary:":<66}', counter_original, counter_modified):
        same_number = True
    if check_equal(f'{"G_Avg key was successfully added to the new dictionary:":<66}', counter_original, counter_G_Avg):
        added_successfully = True
    if check_equal(f'{"Correct Average Calculated for random sample:":<66}', sample_avg, actual_avg):
        random_avg = True

    if same_number and added_successfully and random_avg:  # All three cases must be correct to return True
        return True
    else:  # Failure in any one of the checks
        return False
