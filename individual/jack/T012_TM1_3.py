#Jack... copy/paste your function here and merge it...
# Test 3: Dictionary Values: Individual Student Entries
# Jack Roberts 101261505
# Lab 4 ECOR1042
# T012_TM1_3
import check_equal
import T012_M1_load_data


def type_test() -> bool:
    print("")

    types_failureskey_expected = [
        str, int, float, int, int, float, float, float]
    dic = (T012_M1_load_data.student_failures_dictionary(
        'student-mat.csv'))
    pass_count_failures = 0
    error_count_failures = 0
    for key in dic:
        for student in dic[key]:
            data_types = []
            for key in student:
                data_types.append(type(student[key]))
            for i in range(len(data_types)):
                # checks if the elements of data_types match the values you hard coded in types_failureskey_expected below
                if check_equal.check_equal("Failures dictionary: Test " + str(i + 1) + " " + str(data_types[i]), data_types[i], types_failureskey_expected[i]) == True:
                    pass_count_failures += 1
                else:
                    print(str(data_types[i]) + "==" +
                          str(types_failureskey_expected[i]) + "  ERROR failures")
                    error_count_failures += 1
            break
        break
    print("")

    #print("Failures Pass count: " + str(pass_count_failures))
    #print("Failures Error count: " + str(error_count_failures) + "\n")
    if pass_count_failures == 8:
        bool_failures = True
    else:
        bool_failures = False

    types_agekey_expected = [str, float, int, int, int, float, float, float]
    dic_a = (T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    pass_count_age = 0
    error_count_age = 0
    for key in dic_a:
        for student in dic_a[key]:
            data_types_a = []
            for key in student:
                data_types_a.append(type(student[key]))
            for i in range(len(data_types_a)):
                # checks if the elements of data_types match the values you hard coded in types_agekey_expected below
                if check_equal.check_equal("Age dictionary: Test " + str(i + 1) + " " + str(data_types_a[i]), data_types_a[i], types_agekey_expected[i]) == True:
                    pass_count_age += 1
                else:
                    print(str(data_types_a[i]) + "==" +
                          str(types_agekey_expected[i]) + "  ERROR age")
                    error_count_age += 1
            break
        break
    print("")

    #print("Age Pass count: " + str(pass_count_age))
    #print("Age Error count: " + str(error_count_age) + "\n")
    if pass_count_age == 8:
        bool_age = True
    else:
        bool_age = False

    types_healthkey_expected = [
        str, int, float, int, int, float, float, float]
    dic_h = (T012_M1_load_data.student_health_dictionary('student-mat.csv'))
    pass_count_health = 0
    error_count_health = 0
    for key in dic_h:
        for student in dic_h[key]:
            data_types_h = []
            for key in student:
                data_types_h.append(type(student[key]))
            for i in range(len(data_types_h)):
                # checks if the elements of data_types match the values you hard coded in types_healthkey_expected below
                if check_equal.check_equal("Health dictionary: Test " + str(i + 1) + " " + str(data_types_h[i]), data_types_h[i], types_healthkey_expected[i]) == True:
                    pass_count_health += 1
                else:
                    print(str(data_types_h[i]) + "==" +
                          str(types_healthkey_expected[i]) + "  ERROR health")
                    error_count_health += 1
            break
        break
    print("")

    #print("Health Pass count: " + str(pass_count_health))
    #print("Health Error count: " + str(error_count_health) + "\n")
    if pass_count_health == 8:
        bool_health = True
    else:
        bool_health = False

    types_schoolkey_expected = [
        int, float, int, int, int, float, float, float]
    dic_s = (T012_M1_load_data.student_school_dictionary('student-mat.csv'))
    pass_count_school = 0
    error_count_school = 0
    for key in dic_s:
        for student in dic_s[key]:
            data_types_s = []
            for key in student:
                data_types_s.append(type(student[key]))
            for i in range(len(data_types_s)):
                # checks if the elements of data_types match the values you hard coded in types_schoolkey_expected below
                if check_equal.check_equal("School dictionary: Test " + str(i + 1) + " " + str(data_types_s[i]), data_types_s[i], types_schoolkey_expected[i]) == True:
                    pass_count_school += 1
                else:
                    print(str(data_types_s[i]) + "==" +
                          str(types_schoolkey_expected[i]) + "  ERROR school")
                    error_count_school += 1
            break
        break

    #print("School Pass count: " + str(pass_count_school))
    #print("School Error count: " + str(error_count_school) + "\n")
    if pass_count_school == 8:
        bool_school = True
    else:
        bool_school = False

    print("\n" + "Failures Pass count: " + str(pass_count_failures))
    print("Failures Error count: " + str(error_count_failures))
    print("Age Pass count: " + str(pass_count_age))
    print("Age Error count: " + str(error_count_age))
    print("Health Pass count: " + str(pass_count_health))
    print("Health Error count: " + str(error_count_health))
    print("School Pass count: " + str(pass_count_school))
    print("School Error count: " + str(error_count_school) + "\n")
    return bool_failures, bool_age, bool_health, bool_school
