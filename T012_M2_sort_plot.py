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

if __name__ = "__main__":
    age_result = student_list(T012_M1_load_data.student_age_dictionary('student-mat.csv'))
    school_result = student_list(T012_M1_load_data.student_school_dictionary('student-mat.csv'))
    failures_result = student_list(T012_M1_load_data.student_failures_dictionary('student-mat.csv'))
    health_result = student_list(T012_M1_load_data.student_health_dictionary('student-mat.csv'))
    
