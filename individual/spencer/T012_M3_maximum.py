# AUTHOR:
#    Spencer Hiscox    101230073

import T012_M1_load_data as ld, T012_M2_sort_plot as sp, scipy.optimize as scop



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



def maximum(attribute: str)->tuple:
    """Return (a, b) where a = the value of 'attribute' within the data 
    contained in student-mat.csv file which pertains to the highest average
    grade obtained within that attribute, b = the highest average grade 
    (the grade obtained by a).
    
    Preconditions: attribute must exactly equal one of the column headers in 
        the student-mat.csv file
    
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
    dictionary = ld.add_average(ld.student_age_dictionary("student-mat.csv"))
    dictionary2 = ld.add_average(ld.student_age_dictionary("student-mat.csv"))
    
    raw_data = sp.student_list(dictionary)
    values = set()
    for entry in raw_data:
        values.add(entry[attribute])
        
    minimum, maximum = min(values), max(values)
    
    coefficients = tuple(sp.curve_fit(dictionary2, attribute, 2))
    
    regression_max = scop.fminbound(
        evaluate_negate_quadratic, minimum, maximum, args=coefficients)
    
    return (round(regression_max, 2), round(-evaluate_negate_quadratic(regression_max, coefficients[0], coefficients[1], coefficients[2]), 2))



#MAIN SCRIPT
if __name__ == "__main__":
    attributes = ['Health', 'Age', 'StudyTime', 'Failures', 'Absences']
    results = []
    for attribute in attributes:
        results.append(maximum(attribute))
        
