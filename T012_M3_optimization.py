# AUTHORS:
#    Spencer Hiscox    101230073
#    Milan Djordjevic  101262178
#    Jack Roberts      101261505
#    Esteban Heidrich  101267959


import T012_M1_load_data as ld, T012_M2_sort_plot as sp, scipy.optimize as scop
from numpy import float64
from typing import Dict, List



def quadratic(x: float, a: float, b: float, c: float) -> float:
    """
    Return the value of a quadratic a*x^2 + b*x + c with coefficients a, b, and c, evaluated at x.

    >>> quadratic(0, 2, -4, 5)
    5
    >>> quadratic(1, 1, -2, 3)
    2
    >>> quadratic(-2, 2, 4, -1)
    -1
    """
    return a * pow(x, 2) + b * x + c



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
    
    
    
def minimum(my_dict: dict, attribute: str) -> tuple:
    """
    Return a tuple containing the minimum attribute and the value of G_Avg of
    that minimum based off a quadratic regression determined through curve_fit()
    Precondition: attribute is a propery defined key in any one of the loaded dictionaries
    and my_dict follows correct format and is generated from load_data module.
    >>> minimum(ld.student_age_dictionary('student-mat.csv'), "Health")
    (3.69, 10.27)
    >>> minimum(ld.student_age_dictionary('student-mat.csv'), "Age")
    (22.0, 8.02)
    >>> minimum(ld.student_age_dictionary('student-mat.csv'), "Failures")
    (3.0, 6.35)
    """
    # sorts the input list (to easily obtain the domain)
    sorted_list = sp.sort_students_bubble(
        my_dict, attribute)
    # gets coefficients of quadratic
    coefs = sp.curve_fit(
        my_dict, attribute, 2)
    # converts to tuple for fminbound argument
    coefs_tup = tuple(coefs)

    a, b, c = coefs_tup
    # finds endpoints of domain
    lower = sorted_list[0][attribute]
    upper = sorted_list[len(sorted_list) - 1][attribute]

    min_x = round(scop.fminbound(quadratic, lower, upper, args=coefs_tup), 2)
    min_x_and_min_y = (min_x, round(quadratic(min_x, a, b, c), 2))

    return min_x_and_min_y



def maximum(i_dict: Dict[int or str, List[dict]], attribute: str)->tuple:
    """Return (a, b) where a = the value of 'attribute' within the data 
    contained in student-mat.csv file which pertains to the highest average
    grade obtained within that attribute, b = the highest average grade 
    (the grade obtained by a).
    
    Preconditions: 
        1) attribute must exactly equal one of the keys in the 
        dictionary passed as the first position argument (i_dict).
        
        2) attribute must refer to a numeric value within nested dictionaries 
        contained in first position argument (i_dict).
        
        3) i_dict must be a dictionary which uses the same data structure as a
        dictionary created using one of the functions defined in 
        T012_M1_load_data.py
    
    >>> maximum(ld.student_age_dictionary("student-mat.csv"), 'Health')
    (1.0, 11.85)
    
    >>> maximum(ld.student_age_dictionary("student-mat.csv"), 'Age')
    (16.89, 11.15)
    
    >>> maximum(ld.student_school_dictionary("student-mat.csv"), 'StudyTime')
    (4.0, 11.84)
    
    >>> maximum(ld.student_health_dictionary("student-mat.csv"), 'Failures')
    (0.0, 11.36)
    
    >>> maximum(ld.student_failures_dictionary("student-mat.csv"), 'Absences')
    (0.0, 11.5)

    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument. First position argument (i_dict) "
                        "must be of type <dict>.")
    if type(attribute) != str \
       and type(attribute) != int \
       and type(attribute) != float:
        raise TypeError("Invalid argument. Second position argument (attribute) "
                        "must be of type <str> or type <int> or type <float>.")
    
    for key in i_dict:
        if type(i_dict[key]) != list:
            raise TypeError("Invalid argument. First position argument "
                            "(i_dict) must be a <dict> with values of type "
                            "<list>.")
        for entry in i_dict[key]:
            if type(entry) != dict:
                raise TypeError("Invalid argument. First position argument "
                                "(i_dict) must be a <dict> with <list> values "
                                "containing entries of type <dict>.")
            if not 'G_Avg' in entry:
                i_dict = ld.add_average(i_dict)
            break
        break
    
    raw_data = sp.student_list(i_dict)
    
    for entry in raw_data:
        if not attribute in entry:
            raise ValueError("Invalid argument. Second position argument "
                             "(attribute) must be a key in nested dictionaries "
                             "of second position argument (i_dict).")        
        if type(entry[attribute]) != int and type(entry[attribute]) != float:
            raise ValueError("Invalid Argument. Second position argument "
                             "(attribute) must refer to a value within nested "
                             "dictionaries contained in first position "
                             "argument (i_dict) of type <int> or type <float>.")
        break
    
    values = set()
    for entry in raw_data:
        values.add(entry[attribute])
        
    minimum, maximum = min(values), max(values)
    
    coefficients = tuple(sp.curve_fit(i_dict, attribute, 2))
    
    regression_max = scop.fminbound(
        evaluate_negate_quadratic, minimum, maximum, args=coefficients)
    
    return (round(regression_max, 2), round(-evaluate_negate_quadratic(
        regression_max, coefficients[0], coefficients[1], coefficients[2]), 2))



# MAIN SCRIPT
if __name__ == "__main__":
    attributes = ['Health', 'Age', 'StudyTime', 'Failures', 'Absences']
    results_max = {}
    results_min = {}
    first_run = True
    for attribute in attributes:
        if first_run:
            first_run = False
            results_max['Age'] = [maximum(
                ld.student_age_dictionary("student-mat.csv"), attribute)]
            results_max['School'] = [maximum(
                ld.student_school_dictionary("student-mat.csv"), attribute)]
            results_max['Failures'] = [maximum(
                ld.student_failures_dictionary("student-mat.csv"), attribute)]
            results_max['Health'] = [maximum(
                ld.student_health_dictionary("student-mat.csv"), attribute)]
            results_min['Age'] = [minimum(
                ld.student_age_dictionary("student-mat.csv"), attribute)]
            results_min['School'] = [minimum(
                ld.student_school_dictionary("student-mat.csv"), attribute)]
            results_min['Failures'] = [minimum(
                ld.student_failures_dictionary("student-mat.csv"), attribute)]
            results_min['Health'] = [minimum(
                ld.student_health_dictionary("student-mat.csv"), attribute)]            
            continue
        results_max['Age'].append(maximum(
            ld.student_age_dictionary("student-mat.csv"), attribute))
        results_max['School'].append(maximum(
            ld.student_school_dictionary("student-mat.csv"), attribute))
        results_max['Failures'].append(maximum(
            ld.student_failures_dictionary("student-mat.csv"), attribute))
        results_max['Health'].append(maximum(
            ld.student_health_dictionary("student-mat.csv"), attribute))
        results_min['Age'].append(minimum(
            ld.student_age_dictionary("student-mat.csv"), attribute))
        results_min['School'].append(minimum(
            ld.student_school_dictionary("student-mat.csv"), attribute))
        results_min['Failures'].append(minimum(
            ld.student_failures_dictionary("student-mat.csv"), attribute))
        results_min['Health'].append(minimum(
            ld.student_health_dictionary("student-mat.csv"), attribute))        
