# AUTHOR:
#    Spencer Hiscox    101230073

import T012_M1_load_data as ld, T012_M2_sort_plot as sp, scipy.optimize as scop
from typing import Dict, List



def evaluate_negate_quadratic(x: float, a: float, b: float, c: float)->float:
    """Return the negated value of a quadratic equation, evaluated at x, with
    coefficients a, b and c when written in standard form: ax² + bx + c = 0
    
    Preconditions: 1) a ≠ 0
                   2) b² - 4ac > 0
    
    >>> evaluate_negate_quadratic(2, 1, 2, 1)
    -9
    
    >>> evaluate_negate_quadratic(3, 1, -6, 9)
    0
    
    >>> evaluate_negate_quadratic(2, -1, -2, -1)
    9
    """
    return -(a * x ** 2 + b * x + c)



def maximum(attribute: str, i_dict: Dict[int or str, List[dict]])->tuple:
    """Return (a, b) where a = the value of 'attribute' within the data 
    contained in student-mat.csv file which pertains to the highest average
    grade obtained within that attribute, b = the highest average grade 
    (the grade obtained by a).
    
    Preconditions: 1) attribute must exactly equal one of the column headers in 
        the student-mat.csv file
        2) i_dict must be a dictionary created using one of the functions 
        defined in T012_M1_load_data.py
    
    >>> maximum('Health')
    (1.0, 11.85)
    
    >>> maximum('Age')
    (16.89, 11.15)
    
    >>> maximum('StudyTime')
    (4.0, 11.84)
    
    >>> maximum('Failures')
    (0.0, 11.36)
    
    >>> maximum('Absences')
    (0.0, 11.5)

    """
    for key in i_dict:
        for entry in i_dict[key]:
            if not 'G_Avg' in entry:
                i_dict = ld.add_average(i_dict)
            break
        break
    
    i_dict_copy = {}
    for key in i_dict:
        for entry in i_dict[key]:
            if key in i_dict_copy:
                i_dict_copy[key].append(entry.copy())
                continue
            i_dict_copy[key] = [entry.copy()] 
    
    raw_data = sp.student_list(i_dict)
    values = set()
    for entry in raw_data:
        values.add(entry[attribute])
        
    minimum, maximum = min(values), max(values)
    
    coefficients = tuple(sp.curve_fit(i_dict_copy, attribute, 2))
    
    regression_max = scop.fminbound(
        evaluate_negate_quadratic, minimum, maximum, args=coefficients)
    
    return (round(regression_max, 2), round(-evaluate_negate_quadratic(regression_max, coefficients[0], coefficients[1], coefficients[2]), 2))



#MAIN SCRIPT
if __name__ == "__main__":
    attributes = ['Health', 'Age', 'StudyTime', 'Failures', 'Absences']
    results = {}
    first_run = True
    for attribute in attributes:
        if first_run:
            first_run = False
            results['Age'] = [maximum(attribute, 
                           ld.student_age_dictionary("student-mat.csv"))]
            results['School'] = [maximum(attribute, 
                           ld.student_school_dictionary("student-mat.csv"))]
            results['Failures'] = [maximum(attribute, 
                           ld.student_failures_dictionary("student-mat.csv"))]
            results['Health'] = [maximum(attribute, 
                           ld.student_health_dictionary("student-mat.csv"))]
            continue
        results['Age'].append(maximum(attribute, 
                       ld.student_age_dictionary("student-mat.csv")))
        results['School'].append(maximum(attribute, 
                       ld.student_school_dictionary("student-mat.csv")))
        results['Failures'].append(maximum(attribute, 
                       ld.student_failures_dictionary("student-mat.csv")))
        results['Health'].append(maximum(attribute, 
                       ld.student_health_dictionary("student-mat.csv")))
