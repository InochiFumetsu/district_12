from typing import Tuple

def check_no_entries_by_key(i_dict: Dict[str, List[dict]], file_name: str)->Tuple[list]:
    """
    """
    ##### raise Error checks
    expected = {}
    with open(file_name, 'r') as file:
        metric = ''
        keys = file.readline().strip("\n ").split(sep=",")
        for dict_key in iter(i_dict):
            for key in keys:
                if key in i_dict[dict_key][0]:
                    continue
                else:
                    metric = key
                    break
            break
        index = keys.index(metric)
        key = 0
        for line in file:
            line = line.strip("\n ").split(sep=",")
            if line[index].isdigit():
                if (len(line[index].rsplit(sep=".")) - 1):                    
                    key = float(line[index])
                else:
                    key = int(line[index])
            else:
                key = line[index]
            if key in expected:
                expected[key] += 1
            else:
                expected[key] = 1

    actual = {}
    for key in iter(i_dict):
        actual[key] = len(i_dict[key])

    amalgam = {}
    for key in actual:
        amalgam[key] = (actual[key], expected[key])
    
    actual, expected = [], []
    for key in amalgam:
        actual.append(amalgam[key][0])
        expected.append(amalgam[key][1])
    
    return (actual, expected)
