#STUDENT_LIST FUNCTION
#AUTHOR:
#   Spencer Hiscox    101230073



import T012_M1_load_data


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



if __name__ == "__main__":
    
    student_list_results = []
    
    student_list_results.append(student_list(T012_M1_load_data.student_age_dictionary('student-mat.csv')))
    student_list_results.append(student_list(T012_M1_load_data.student_school_dictionary('student-mat.csv')))
    student_list_results.append(student_list(T012_M1_load_data.student_failures_dictionary('student-mat.csv')))
    student_list_results.append(student_list(T012_M1_load_data.student_health_dictionary('student-mat.csv')))
