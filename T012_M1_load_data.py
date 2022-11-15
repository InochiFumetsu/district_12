#LOAD DATA MODULE
#AUTHORS:
#   Spencer Hiscox
#   Jack Roberts
#   Esteban Heidrich 101267959
#   Milan Djordjevic

"""
● Copy the four functions developed in Task 1 into this file. Ensure that the functions are one after the other and the main script 
  (i.e., all function calls, a combination of the main scripts of the four individual files) are at the end of the file.
● Run Txxx_M1_load_data.py and ensure that there are no errors.

1. Follow the FDR to implement a function called load_data. This function must be placed below the four individual functions in the file Txxx_M1_load_data.py
Function Description:
  ● The function lets the user choose how the data will be loaded (i.e., which of the four functions you developed should be used).
  ● It takes two input parameters: (1) the file name where the data is stored, and (2) a string describing the key of the dictionary to be returned 
    ('School', 'Age', 'Health', 'Failures').
  ● It returns a dictionary with the data loaded using the key based on the input parameter. If the key provided is not valid, the function will print the error 
    message “Invalid Key” and return an empty dictionary.
2. Test your function. For this lab, you can just call your function to ensure that the data is loaded correctly. For testing purposes, use student-mat.csv. 
Ensure that the function calls are added to the end of the main script.

1. Follow the FDR to implement a function called add_average. This function must be placed inside the file Txxx_M1_load_data.py below load_data.
Function Description:
● The function will add the average of the student’s grades (G1, G2 and G3) as an additional attribute to the dictionary.
● It takes one input parameter (regardless of the key): (1) a dictionary
● It returns the dictionary updated with the average grade. Sample output (assuming school as key):
{ 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 },
{another element},
… ],
'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33 },
{another element},
… ],
… }
2. Test your function. For this lab, you can just call your function to ensure that the data is loaded correctly. For testing purposes, use student-mat.csv. 
Ensure that the function calls are added to the end of the main script.

1. Submit your module (Txxx_M1_load_data.py) on Brightspace (One submission per team). Before you submit, ensure:
  a. All the active team members’ names are at the top of the file as a Python comment. If a name is missing, that person will receive zero. We will assume that 
     the person did not participate in the task.
  b. The functions have the proper names.
  c. You have included type annotations and docstrings. Do not forget to include the preconditions, if any.
  d. At the end of the file, you have the main script in which the functions are called, and all testing scenarios are covered. For this lab, function calls are 
     enough to ensure that the data is properly loaded.
  e. The file name is correct.
  f. Run Txxx_M1_load_data.py one more time to ensure that there are no errors!
"""

#!! BELOW ALL OTHER FUNCTIONS!!
#def add_average():
#student_health_dictionary by Esteban Heidrich 101267959
def student_health_dictionary(file_name: str) -> dict:
    """This function takes student information and sorts them by their health 
    condition. 
    
    precondtions: file_name must be an existing file in the same folder as 
    this function
    
    >>>student_health_dictionary("student_info.txt")
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
    counter = 0
    raw_data = []
    file_content = open(file_name, "r")
    for line in file_content:
        if first_run:           
            student_dict_keys = line.strip().split(",")
            first_run = False
        raw_data += [0]
        raw_data[counter] = line.strip()
        counter += 1
    del raw_data[0]
    for j in raw_data:
        student_stat_1 = j.split(",")
        health = int(student_stat_1[4])
        if not health in health_dictionary:
            health_dictionary[health] = []
        health_dictionary[health].append({
            student_dict_keys[0]: student_stat_1[0],
            student_dict_keys[1]: int(student_stat_1[1]),
            student_dict_keys[2]: int(student_stat_1[2]),
            student_dict_keys[3]: int(student_stat_1[3]),
            student_dict_keys[5]: int(student_stat_1[5]),
            student_dict_keys[6]: int(student_stat_1[6]),
            student_dict_keys[7]: int(student_stat_1[7]),
            student_dict_keys[8]: int(student_stat_1[8]),
        })
    return health_dictionary
health_dictionary = student_health_dictionary("student_info.txt")
