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
    
def sort_students_selection(dic: dict, key: str) -> dict:
    """
    Example:
    sort_students_selection(T012_M1_load_data.add_average(T012_M1_load_data.student_failures_dictionary('student-mat.csv')), "G_Avg")

    [{'School': 'MB', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 4.0, 'G2': 0.0, 'G3': 0.0, 'G_Avg': 1.33, 'Failures': 2}, {'School': 'MB', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 5.0, 'G2': 0.0, 'G3': 0.0, 'G_Avg': 1.67, 'Failures': 3}, {'School': 'MB', 'Age': 19, 'StudyTime': 1.0, 'Health': 4, 'Absences': 0, 'G1': 5.0, 'G2': 0.0, 'G3': 0.0, 'G_Avg': 1.67, 'Failures': 3}, ...

    sort_students_selection(T012_M1_load_data.student_age_dictionary('student-mat.csv'), "School")

    [{'School': 'BD', 'StudyTime': 2.0, 'Failures': 1, 'Health': 2, 'Absences': 0, 'G1': 7.0, 'G2': 7.0, 'G3': 0.0, 'Age': 18}, {'School': 'BD', 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 7.0, 'G2': 0.0, 'G3': 0.0, 'Age': 18}, {'School': 'BD', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 8, 'G1': 3.0, 'G2': 5.0, 'G3': 5.0, 'Age': 18}, {'School': 'BD', 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'G1': 6.0, 'G2': 8.0, 'G3': 8.0, 'Age': 18}, ...

    sort_students_selection(T012_M1_load_data.student_health_dictionary('student-mat.csv'), "Health")

    [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6.0, 'G2': 5.0, 'G3': 6.0, 'Health': 1}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16.0, 'G2': 18.0, 'G3': 19.0, 'Health': 1}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 13.0, 'G2': 14.0, 'G3': 15.0, 'Health': 1}, {'School': 'GP', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 15.0, 'G2': 16.0, 'G3': 15.0, 'Health': 1}, ...

    The function sort_students_selection takes an input dictionary thats imported from T012_M1_load_data and the key of to choice to sort that dictionary by, and sorts a new list called dictionary thats data is converted to a list using T012_M2_student_list.student_list from a dictionary, using a selection sort algorithm.

    The input parameter dic is expected to be one of the four dictionaries from T012_M1_load_data (student_failures_dictionary, student_age_dictionary, student_health_dictionary, student_school_dictionary)

    The input parameter key is expected to be a string indicating the key you wish to sort the list by ("School", "Age", "StudyTime", "Health", "Absences", "Failures", "G1", "G2", "G3", "G_Avg")

    Preconditions: The dic and key input parmeters MUST follow the instructions listed in their respective parameter descriptions. In order to sort by G_Avg, the function must be called in the same format as called in the example above (meaning the dictionary can change, and so can the key). Must have the most recent version of T012_M1_load_data.py in the same folder as this python file.
    """
    dictionary = student_list(
        dic)  # Create dictionary after using student_list function on the input dictionary.
    for i in range(len(dictionary)):  # Start for loop for the length of the list
        minimum_index = i  # Set a minimum index equal to index
        # Start for loop for range of index to the length of the dictionary
        for j in range(i + 1, len(dictionary)):
            # Compare the dictionary at the highest sorted index (minimum index), to the dictionary at j, both with respect to the key parameter
            if (dictionary[minimum_index][key] > dictionary[j][key]):
                # If the dictionary at j is lower than previous minimum_index, make j the new minimum index
                minimum_index = j
        temp = dictionary[i]  # put array at index i into temporary (Swap)
        # Make list at i the value of dictionary at minimum index (Swap)
        dictionary[i] = dictionary[minimum_index]
        # Now set the list at minimum index equal to the temp, completing the swap.
        dictionary[minimum_index] = temp

    return dictionary  # Return sorted dictionary

if __name__ == "__main__":
    age_result = student_list(T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    school_result = student_list(T012_M1_load_data.student_school_dictionary('student-mat.csv'))
    failures_result = student_list(T012_M1_load_data.student_failures_dictionary('student-mat.csv'))
    health_result = student_list(T012_M1_load_data.student_health_dictionary('student-mat.csv'))
    
