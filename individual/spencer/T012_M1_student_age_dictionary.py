# STUDENT AGE DICTIONARY FILE

# AUTHOR: SPENCER HISCOX

"""
The keys of the dictionary are the students' ages.
A student's age range is from 15 to 22.
See below for the sample output of the function:
{ 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3,
'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10},
{another element},
… ],
16 : [ {'School': 'MS', 'StudyTime': 1, 'Failures': 1.2,
'Health': 4, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7},
{another element},
… ],
… }

1. Follow the FDR to implement the function you have been assigned. (Note that FDR was covered in ECOR1041).
  a. You can use “import string” and “from typing import List” only. If you think other libraries are needed, you must ask the TAs for approval. Note: You can treat a
     CSV file as a text file; just open it with Notepad instead of Excel to check how the data is organized.
  b. Assume that your data does not contain duplicated entries.
  c. Required Filename: Txxx_M1_yyy.py where xxx is your team identifier (e.g., 035) and yyy = {student_age_dictionary, student_health_dictionary,
     student_school_dictionary, or student_failures_dictionary} based on the function that you are implementing.
2. Test your function. For this lab, you can just call your function to ensure that the data is loaded correctly. For testing purposes, use student-mat.csv.
3. Submit your function (Txxx_M1_yyy.py) on Brightspace (individual submission of your assigned function). Before you submit, ensure:
  a. Your name and student number are written at the top of the file as a Python comment.
  b. The function has the proper name.
  c. You have included type annotations and docstring. Do not forget to include the preconditions, if any.
  d. At the end of the file, you have included the main script which calls the function.
  e. The file name is correct.
  f. Run Txxx_M1_yyy.py one more time to ensure that there are no errors!
"""


def student_age_dictionary(file_name: str) -> dict:
    """
    """
    data_file = open(file_name, 'r')
    raw_import = []
    for line in data_file:
        raw_import.append(line)

    keys = []
    raw_import[0] = raw_import[0].strip("\n").split(sep=",")
    for element in raw_import[0]:
        keys.append(element)

    values = []
    for entry in raw_import[1:]:
        values.append(entry)

    for i in range(len(values)):
        values[i] = values[i].strip("\n").split(sep=",")

    i = 0
    entries = []
    for i in range(len(values)):
        amalgam = dict()
        for j in range(len(keys)):
            amalgam[keys[j]] = values[i][j]
        entries.append(amalgam)

    age_dictionary = dict()
    for i in range(len(entries)):
        if entries[i]['Age'] in age_dictionary:
            
        else:
            age_dictionary[entries[i]['Age']] = [entries[i]]
            del age_dictionary[entries[i]['Age']][len(age_dictionary[entries[i]['Age']]) - 1]['Age']
    print(age_dictionary)


student_age_dictionary('student-mat.csv')

