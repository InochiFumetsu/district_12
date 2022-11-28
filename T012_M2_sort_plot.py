import T012_M1_load_data

def student_list(i_dict: dict) -> list:
    """
    """
    expected = {}
    metric = ''
    actual = {}
    key_fail = False
    with open('student-mat.csv', 'r') as file:
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
        print("\n\n\nInvalid dictionary: Primary key mismatch. Empty list returned.\n")
        input("Press <ENTER> to continue.\n\n")
        return []
    
    output_list = []
    for key in i_dict.keys():
        for entry in i_dict[key]:
            entry[metric] = key
            output_list.append(entry)
            
    return output_list
    
def sort_students_bubble(my_dict: dict, attribute: str) -> list:
    """
    Return a sorted dictoinary in ascending order or alphabetical order by using bubble sort, based off the passed attribute.
    Precondition: attribute is a valid/ accepted key in my_dict and the passed dictionary follows specific format (dictionary with lists as keys, each containing dictionaries)

    >>>sort_students_bubble(T012_M1_load_data.student_failures_dictionary('student-mat.csv'), "Age")
    [{'School': 'GP', 'Age': 15, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 15.0, 'G2': 14.0, 'G3': 15.0, 'Failures': 0}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 1, 'Absences': 0, 'G1': 16.0, 'G2': 18.0, 'G3': 19.0, 'Failures': 0},
    ...
    ...
    ]
    >>>sort_students_bubble(T012_M1_load_data.student_age_dictionary('student-mat.csv'), "Health")
    [{'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 13, 'G1': 17.0, 'G2': 17.0, 'G3': 17.0, 'Age': 18}, 
    {'School': 'BD', 'StudyTime': 1.0, 'Failures': 0, 'Health': 1, 'Absences': 8, 'G1': 10.0, 'G2': 11.0, 'G3': 10.0, 'Age': 18}, 
    ...
    ...
    ]
    >>>sort_students_bubble(T012_M1_load_data.add_average(T012_M1_load_data.student_age_dictionary('student-mat.csv')), "Health")
    [{'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 13, 'G1': 17.0, 'G2': 17.0, 'G3': 17.0, 'G_Avg': 17.0, 'Age': 18}, 
    {'School': 'BD', 'StudyTime': 1.0, 'Failures': 0, 'Health': 1, 'Absences': 8, 'G1': 10.0, 'G2': 11.0, 'G3': 10.0, 'G_Avg': 10.33, 'Age': 18}, 
    {'School': 'BD', 'StudyTime': 1.0, 'Failures': 0, 'Health': 1, 'Absences': 5, 'G1': 16.0, 'G2': 15.0, 'G3': 16.0, 'G_Avg': 15.67, 'Age': 18}, 
    ...
    ...
    ]

    """

    # converts dictionary of list of dictionaries to a list of dictionaries
    arr = T012_M2_sort_plot.student_list(my_dict)

    swap = True
    while swap:
        swap = False  # assumes algorithm is done
        for i in range(len(arr) - 1):
            if arr[i][attribute] > arr[i + 1][attribute]:  # compares side by side items in list
                # swaps them if necessary
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True  # swapping is not done yet
    return arr

if __name__ == "__main__":
    age_result = student_list(T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    school_result = student_list(T012_M1_load_data.student_school_dictionary('student-mat.csv'))
    failures_result = student_list(T012_M1_load_data.student_failures_dictionary('student-mat.csv'))
    health_result = student_list(T012_M1_load_data.student_health_dictionary('student-mat.csv'))
    
