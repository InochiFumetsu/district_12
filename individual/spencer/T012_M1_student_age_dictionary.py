# STUDENT AGE DICTIONARY FILE

# AUTHOR: SPENCER HISCOX
# STUDENT NO.: 101230073

"""
  c. You have included type annotations and docstring. Do not forget to include the preconditions, if any.
"""


def student_age_dictionary(file_name: str) -> dict:
    """
    """
    with open(file_name, 'r') as data_file:
        raw_import = []
        for line in data_file:
            raw_import.append(line)

    keys = []
    raw_import[0] = raw_import[0].strip("\n").split(sep=",")
    for element in raw_import[0]:
        keys.append(element)

    del raw_import[0]

    for i in range(len(raw_import)):
        raw_import[i] = raw_import[i].strip("\n").split(sep=",")

    i = 0
    entries = []
    for i in range(len(raw_import)):
        amalgam = dict()
        for j in range(len(keys)):
            amalgam[keys[j]] = raw_import[i][j]
        entries.append(amalgam)

    age_dictionary = dict()
    for i in range(len(entries)):
        if entries[i]['Age'] in age_dictionary:
            age_dictionary[entries[i]['Age']].append(entries[i])
            del age_dictionary[entries[i]['Age']][len(age_dictionary[entries[i]['Age']]) - 1]['Age']
        else:
            age_dictionary[entries[i]['Age']] = [entries[i]]
            del age_dictionary[entries[i]['Age']][0]['Age']

    return age_dictionary


# MAIN SCRIPT (CALLING FUNCTION)
student_age_dictionary = student_age_dictionary('student-mat.csv')
