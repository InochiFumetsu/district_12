#STUDENT HEALTH DICTIONARY FILE

#AUTHOR: <Esteban>

import string
from typing import List

def student_health_dictionary(file_name: str) -> dict:
    """This function takes student information and sorts them by their health 
    condition. 
    
    precondtions: file_name must be an existing file in the same folder as 
    python
    
    >>>student_health_dictionary(student_info)
    {'3': [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Failures': '0',
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another element},
    ...], 
    {'5': [{'School': 'GP', 'Age': '15', 'StudyTime': '3', 'Failures': '0',
    'Absences': '2', 'G1': '15', 'G2': '14', 'G3': '15'}, {another element},
    ...], 
    ...}
    """
    health_dictionary = {}
    first_run = True
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    raw_data = []
    file_content = open(file_name, "r")
    for line in file_content:
        counter_1 += 1
    raw_data = [0] * counter_1
    file_content = open(file_name, "r")
    for line in file_content:
        if first_run:
            line = line.strip()
            student_dict_keys = line.split(",")
            first_run = False
        raw_data[counter_2] = line.strip()
        counter_2 += 1
    for j in raw_data:
        student_stat_1 = j.split(",")
        health = student_stat_1[4]
        if not health in health_dictionary:
            health_dictionary[health] = []
            health_dictionary[health].append({
                student_dict_keys[0]: student_stat_1[0],
                student_dict_keys[1]: student_stat_1[1],
                student_dict_keys[2]: student_stat_1[2],
                student_dict_keys[3]: student_stat_1[3],
                student_dict_keys[5]: student_stat_1[5],
                student_dict_keys[6]: student_stat_1[6],
                student_dict_keys[7]: student_stat_1[7],
                student_dict_keys[8]: student_stat_1[8]
            })
        else:
            health_dictionary[health].append({
                student_dict_keys[0]: student_stat_1[0],
                student_dict_keys[1]: student_stat_1[1],
                student_dict_keys[2]: student_stat_1[2],
                student_dict_keys[3]: student_stat_1[3],
                student_dict_keys[5]: student_stat_1[5],
                student_dict_keys[6]: student_stat_1[6],
                student_dict_keys[7]: student_stat_1[7],
                student_dict_keys[8]: student_stat_1[8]
            })
        counter_3 += 1
    del health_dictionary["Health"]
    return health_dictionary
