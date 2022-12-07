# AUTHOR:
#    Spencer Hiscox    101230073

import T012_M1_load_data as ld, T012_M2_sort_plot as sp, scipy.optimize as scop
from numpy import float64
from typing import Dict, List



def evaluate_negate_quadratic(x: float, a: float, b: float, c: float)->float:
    """Return the negated value of a quadratic equation, evaluated at x, with
    coefficients a, b and c when written in standard form: ax² + bx + c = 0
    
    Preconditions: a ≠ 0
    
    >>> evaluate_negate_quadratic(2, 1, 2, 1)
    -9.0
    
    >>> evaluate_negate_quadratic(3, 1, -6, 9)
    0.0
    
    >>> evaluate_negate_quadratic(2, -1, -2, -1)
    9.0
    """
    if type(x) != float64 and type(x) != float and type(x) != int:
        raise TypeError("Invalid argument. First position argument (x) must be "
                        "of type <numpy.float64>.")
    if type(a) != float64 and type(a) != float and type(a) != int:
        raise TypeError("Invalid argument. Second position argument (a) must be"
                        " of type <numpy.float64>.")
    if type(b) != float64 and type(b) != float and type(b) != int:
        raise TypeError("Invalid argument. Third position argument (b) must be "
                        "of type <numpy.float64>.")
    if type(c) != float64 and type(c) != float and type(c) != int:
        raise TypeError("Invalid argument. Fourth position argument (c) must be"
                        " of type <numpy.float64>.")
    if a == 0 or abs(a) < 0.0000000001:
        raise ValueError("Invalid argument. Second position argument must not "
                         "be zero (a ≠ 0).")

    return float(-(a * x ** 2 + b * x + c))



def maximum(attribute: str, i_dict: Dict[int or str, List[dict]])->tuple:
    """Return (a, b) where a = the value of 'attribute' within the data 
    contained in student-mat.csv file which pertains to the highest average
    grade obtained within that attribute, b = the highest average grade 
    (the grade obtained by a).
    
    Preconditions: 
        1) attribute must exactly equal one of the keys in the 
        dictionary passed as the second position argument (i_dict).
        
        2) attribute must refer to a numeric value within nested dictionaries 
        contained in second position argument (i_dict).
        
        3) i_dict must be a dictionary which uses the same data structure as a
        dictionary created using one of the functions defined in 
        T012_M1_load_data.py
    
    >>> maximum('Health', ld.student_age_dictionary("student-mat.csv"))
    (1.0, 11.85)
    
    >>> maximum('Age', ld.student_age_dictionary("student-mat.csv"))
    (16.89, 11.15)
    
    >>> maximum('StudyTime', ld.student_school_dictionary("student-mat.csv"))
    (4.0, 11.84)
    
    >>> maximum('Failures', ld.student_health_dictionary("student-mat.csv"))
    (0.0, 11.36)
    
    >>> maximum('Absences', ld.student_failures_dictionary("student-mat.csv"))
    (0.0, 11.5)

    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument. Second position argument (i_dict) "
                        "must be of type <dict>.")
    if type(attribute) != str \
       and type(attribute) != int \
       and type(attribute) != float:
        raise TypeError("Invalid argument. First position argument (attribute) "
                        "must be of type <str> or type <int> or type <float>.")
    
    for key in i_dict:
        if type(i_dict[key]) != list:
            raise TypeError("Invalid argument. Second position argument "
                            "(i_dict) must be a <dict> with values of type "
                            "<list>.")
        for entry in i_dict[key]:
            if type(entry) != dict:
                raise TypeError("Invalid argument. Second position argument "
                                "(i_dict) must be a <dict> with <list> values "
                                "containing entries of type <dict>.")
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
    
    for entry in raw_data:
        if not attribute in entry:
            raise ValueError("Invalid argument. First position argument "
                             "(attribute) must be a key in nested dictionaries "
                             "of second position argument (i_dict).")        
        if type(entry[attribute]) != int and type(entry[attribute]) != float:
            raise ValueError("Invalid Argument. First position argument "
                             "(attribute) must refer to a value within nested "
                             "dictionaries contained in second position "
                             "argument (i_dict) of type <int> or type <float>.")
        break
    
    values = set()
    for entry in raw_data:
        values.add(entry[attribute])
        
    minimum, maximum = min(values), max(values)
    
    coefficients = tuple(sp.curve_fit(i_dict_copy, attribute, 2))
    
    regression_max = scop.fminbound(
        evaluate_negate_quadratic, minimum, maximum, args=coefficients)
    
    return (round(regression_max, 2), round(-evaluate_negate_quadratic(
        regression_max, coefficients[0], coefficients[1], coefficients[2]), 2))



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
