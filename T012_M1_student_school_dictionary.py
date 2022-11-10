#STUDENT SCHOOL DICTIONARY FILE

"""
The keys of the dictionary are the initials of the schools the students attended.
The function assumes that only the schools listed in the data set provided (student-mat.csv) exist for the keys.
See below for the sample output of the function:
{ 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
{another element},
… ],
'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12 },
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
