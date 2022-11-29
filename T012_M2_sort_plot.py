#LOAD DATA MODULE
#AUTHORS:
#   Spencer Hiscox    101230073
#   Jack Roberts      101261505
#   Esteban Heidrich  101267959
#   Milan Djordjevic  101262178



import T012_M1_load_data
from numpy import polyfit


def student_list(i_dict: dict) -> list:
    """Return list compilation of all student data entries contained in the 
    dictionary passed to the function in the first position argument ('i_dict')
    which contain the appropriate entries for the key from which the dictionary
    passed in was created.
    
    Preconditions: 1) Dictionary passed into function as 'i_dict' must be a 
        dictionary generated using one of the four functions defined in 
        T012_M1_load_data.py
    
    >>>student_list(T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 
    6, 'G1': 5.0, 'G2': 6.0, 'G3': 6.0, 'Age': 18}, {'School': 'MB', 
    'StudyTime': 1.0, 'Failures': 2, 'Health': 4, 'Absences': 0, 'G1': 7.0, 
    'G2': 4.0, 'G3': 0.0, 'Age': 18}, ... ,
    {'School': 'MS', 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 
    3, 'G1': 10.0, 'G2': 8.0, 'G3': 7.0, 'Age': 21}]
    >>>student_list(T012_M1_load_data.student_school_dictionary(
    'student-mat.csv'))
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 
    'G1': 5.0, 'G2': 6.0, 'G3': 6.0, 'School': 'GP'}, {'Age': 17, 'StudyTime': 
    2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5.0, 'G2': 5.0, 'G3': 
    6.0, 'School': 'GP}, ... ,
    {'Age': 19, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 5, 
    'G1': 8.0, 'G2': 9.0, 'G3': 9.0, 'School': 'MS'}]

    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument: parameter <i_dict> (argument in "
                         "position 1) must be of type <dict>")        
    
    expected = {}
    metric = ''
    actual = {}
    key_fail = False
    with open('student-mat.csv', 'r') as file:
        keys = file.readline().strip("\n ").split(sep=",")
        
        for dict_key in iter(i_dict):
            if type(i_dict[dict_key]) != list:
                raise ValueError("Invalid argument: parameter <i_dict> (argument in"
                        " position 1) must be a dictionary whose values are lists.")
            if type(i_dict[dict_key][0]) != dict:
                raise ValueError("Invalid argument: parameter <i_dict> "
                                 "(argument in position 1) must be a dictionary"
                                 " whose values are lists of dictionaries.")
            
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
        raise ValueError("Invalid argument: parameter <i_dict> (argument in "
                         "position 1) must be a dictionary whose keys match the"
                         " column headers in 'student-mat.csv' file.")
    
    output_list = []
    for key in i_dict:            
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
    arr = student_list(my_dict)

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



def curve_fit(i_dict: dict, metric: str, degree: int) -> list:
    """Return a list of the coefficients of the variables for the degree 
    polynomial specified as 'degree' argument, defined by performing polynomial
    regression of average 'G_Avg' for each student associated with a particular
    metric specified as 'metric' argument. If specified 'degree' is higher than
    number of data points available from which to perform a regression, the 
    regression will be performed with the degree of the resultant polynomial 
    equal to the number of data points available in the data set.
    
    Preconditions: 1) Dictionary passed into function as 'i_dict' must be a 
        dictionary generated using one of the four functions defined in 
        T012_M1_load_data.py
        2) The 'metric' selected for the second position argument must be one 
        of the keys contained within the returned list from student_list(i_dict)
    
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Health', 3)
    [-0.0278538498754179, 0.46987985738198207, -2.2742147821236243, 
    13.7162164641214]
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Failures', 2)
    [0.35420696644042277, -2.729867788461538, 11.356343090120658]
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Failures', 4)
    x-wingide-python-shell://129836008/6:1: RankWarning: Polyfit may be poorly 
    conditioned
    [-0.0129539441809042, 0.0769655894192614, 0.21512492094821192, 
    -2.6557070790070747, 11.356570512820507]
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Failures', 32)
    x-wingide-python-shell://129836008/6:1: RankWarning: Polyfit may be poorly 
    conditioned
    [-0.0129539441809042, 0.0769655894192614, 0.21512492094821192, 
    -2.6557070790070747, 11.356570512820507]
    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument: parameter <i_dict> (argument in "
                         "position 1) must be of type <dict>")    
    
    for key in i_dict:
        if type(i_dict[key]) != list:
            raise ValueError("Invalid argument: parameter <i_dict> (argument in"
                    " position 1) must be a dictionary whose values are lists.")
        for i in range(len(i_dict[key])):
            if type(i_dict[key][i]) != dict:
                raise ValueError("Invalid argument: parameter <i_dict> "
                                 "(argument in position 1) must be a dictionary"
                                 " whose values are lists of dictionaries.")                
            if not 'G_Avg' in i_dict[key][i]:
                i_dict = T012_M1_load_data.add_average(i_dict)
            break
        break
    
    i_dict = student_list(i_dict)
    
    if not metric in i_dict[0]:
        raise ValueError("Invalid argument: parameter <metric> (argument in "
                         "position 2) not contained in i_dict.")
    if type(i_dict[0][metric]) != int and type(i_dict[0][metric]) != float:
        raise ValueError("Invalid argument: parameter <metric> (argument in "
                         "position 2) must be a key whose values are numeric")
    if type(metric) != str:
        raise TypeError("Invalid argument: parameter <metric> (argument in "
                         "position 2) must be of type <string>")
    if type(degree) != int:
        raise TypeError("Invalid argument: parameter <degree> (argument in "
                         "position 3) must be of type <int>")
    
    
    dataset = {}
    for entry in i_dict:
        if entry[metric] in dataset:
            dataset[entry[metric]][0] += entry['G_Avg']
            dataset[entry[metric]][1] += 1
            continue
        dataset[entry[metric]] = [entry['G_Avg'], 1 ]
            
    for key in dataset:
        dataset[key] = dataset[key][0] / dataset[key][1]
        
    num_data_points = len(dataset)
    if num_data_points < degree:
        degree = num_data_points
        
    return list(polyfit(list(dataset.keys()), list(dataset.values()), degree))



#FUNCTION CALLS HERE
if __name__ == "__main__":
    
    metrics = ['StudyTime', 'Health', 'Absences', 'Failures', 'Age', 'School', 'G1', 'G2', 'G3']
    not_numeric = ['School', 'G1', 'G2', 'G3']
    
    curve_fit_results = []
    selection_sort_results = []
    bubble_sort_results = []
    student_list_results = []
    
    student_list_results.append(student_list(T012_M1_load_data.student_age_dictionary('student-mat.csv')))
    student_list_results.append(student_list(T012_M1_load_data.student_school_dictionary('student-mat.csv')))
    student_list_results.append(student_list(T012_M1_load_data.student_failures_dictionary('student-mat.csv')))
    student_list_results.append(student_list(T012_M1_load_data.student_health_dictionary('student-mat.csv')))
    for metric in metrics:
        selection_sort_results.append(sort_students_selection(T012_M1_load_data.student_age_dictionary('student-mat.csv'), metric))
        selection_sort_results.append(sort_students_selection(T012_M1_load_data.student_school_dictionary('student-mat.csv'), metric))
        selection_sort_results.append(sort_students_selection(T012_M1_load_data.student_failures_dictionary('student-mat.csv'), metric))
        selection_sort_results.append(sort_students_selection(T012_M1_load_data.student_health_dictionary('student-mat.csv'), metric))
        bubble_sort_results.append(sort_students_bubble(T012_M1_load_data.student_age_dictionary('student-mat.csv'), metric))
        bubble_sort_results.append(sort_students_bubble(T012_M1_load_data.student_school_dictionary('student-mat.csv'), metric))
        bubble_sort_results.append(sort_students_bubble(T012_M1_load_data.student_failures_dictionary('student-mat.csv'), metric))
        bubble_sort_results.append(sort_students_bubble(T012_M1_load_data.student_health_dictionary('student-mat.csv'), metric))
        for degree in range(1, 6):
            if not metric in not_numeric:
                curve_fit_results.append(curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), metric, degree))
                curve_fit_results.append(curve_fit(T012_M1_load_data.student_school_dictionary('student-mat.csv'), metric, degree))
                curve_fit_results.append(curve_fit(T012_M1_load_data.student_failures_dictionary('student-mat.csv'), metric, degree))
                curve_fit_results.append(curve_fit(T012_M1_load_data.student_health_dictionary('student-mat.csv'), metric, degree))
