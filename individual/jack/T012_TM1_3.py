# Test 3: Dictionary Values: Individual Student Entries
# Jack Roberts 101261505
# Lab 4 ECOR1042
# T012_TM1_3
import check_equal
import T012_M1_load_data


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
            for key in student:  # For each key in the "student" (row) list
                # Append the type of the value of the student at the key
                data_types.append(type(student[key]))
            # For the length of the keys in dic, compare types by calling check_equal
            for i in range(len(data_types)):
                # checks if the elements of data_types match the values you hard coded in types_failureskey_expected below
                if check_equal.check_equal("Failures dictionary: Test " + str(i + 1) + " " + str(data_types[i]), data_types[i], types_failureskey_expected[i]) == True:
                    pass_count_failures += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types[i]) + "==" +
                          str(types_failureskey_expected[i]) + "  ERROR failures")  # Print what line the error was at for debugging purposes
                    error_count_failures += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student
    print("")  # Print a blank line for clarity

    if pass_count_failures == 8:  # If the test passed for the whole length of keys, set the whole test equal to True
        bool_failures = True
    else:  # Else, set the test equal to False
        bool_failures = False

    # Create the failure dictionary expected key
    types_agekey_expected = [str, float, int, int, int, float, float, float]
    # Make dic the variable assigned to the student_failures_dictionary
    dic_a = (T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    pass_count_age = 0  # Create test pass counter
    error_count_age = 0  # Create test error counter
    for key in dic_a:  # Create loop for the keys in the dic variable
        # For every "student" (row) in the dictionary at the key
        for student in dic_a[key]:
            data_types_a = []  # Create list for types at each key
            for key in student:  # For each key in the "student" (row) list
                # Append the type of the value of the student at the key
                data_types_a.append(type(student[key]))
            # For the length of the keys in dic_a, compare types by calling check_equal
            for i in range(len(data_types_a)):
                # checks if the elements of data_types match the values you hard coded in types_agekey_expected below
                if check_equal.check_equal("Age dictionary: Test " + str(i + 1) + " " + str(data_types_a[i]), data_types_a[i], types_agekey_expected[i]) == True:
                    pass_count_age += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types_a[i]) + "==" +
                          str(types_agekey_expected[i]) + "  ERROR age")  # Print what line the error was at for debugging purposes
                    error_count_age += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student
    print("")  # Print a blank line for clarity

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
            for key in student:  # For each key in the "student" (row) list
                # Append the type of the value of the student at the key
                data_types_h.append(type(student[key]))
            # For the length of the keys in dic_a, compare types by calling check_equal
            for i in range(len(data_types_h)):
                # checks if the elements of data_types match the values you hard coded in types_healthkey_expected below
                if check_equal.check_equal("Health dictionary: Test " + str(i + 1) + " " + str(data_types_h[i]), data_types_h[i], types_healthkey_expected[i]) == True:
                    pass_count_health += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types_h[i]) + "==" +
                          str(types_healthkey_expected[i]) + "  ERROR health")  # Print what line the error was at for debugging purposes
                    error_count_health += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student
    print("")  # Print a blank line for clarity

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
            for key in student:  # For each key in the "student" (row) list
                # Append the type of the value of the student at the key
                data_types_s.append(type(student[key]))
            # For the length of the keys in dic_a, compare types by calling check_equal
            for i in range(len(data_types_s)):
                # checks if the elements of data_types match the values you hard coded in types_schoolkey_expected below
                if check_equal.check_equal("School dictionary: Test " + str(i + 1) + " " + str(data_types_s[i]), data_types_s[i], types_schoolkey_expected[i]) == True:
                    pass_count_school += 1  # If the test passes, add one to the pass count
                else:
                    print(str(data_types_s[i]) + "==" +
                          str(types_schoolkey_expected[i]) + "  ERROR school")  # Print what line the error was at for debugging purposes
                    error_count_school += 1  # If the test fails, add one to the error count
            break  # Break out of the for loop as we only need the data from one student
        break  # Break out of the for loop as we only need the data from one student

    if pass_count_school == 8:  # If the test passed for the whole length of keys, set the whole test equal to True
        bool_school = True
    else:  # Else, set the test equal to False
        bool_school = False

    # Print Pass and Failures count and return booleans
    print("\n" + "Failures Pass count: " + str(pass_count_failures))
    print("Failures Error count: " + str(error_count_failures))
    print("Age Pass count: " + str(pass_count_age))
    print("Age Error count: " + str(error_count_age))
    print("Health Pass count: " + str(pass_count_health))
    print("Health Error count: " + str(error_count_health))
    print("School Pass count: " + str(pass_count_school))
    print("School Error count: " + str(error_count_school) + "\n")
    return bool_failures, bool_age, bool_health, bool_school
