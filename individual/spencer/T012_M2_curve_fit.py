#CURVE_FIT FUNCTION
#AUTHOR:
#   Spencer Hiscox    101230073



import T012_M1_load_data
import T012_M2_student_list
from numpy import polyfit


def curve_fit(i_dict: dict, metric: str, degree: int) -> list:
    """Return a list of the coefficients of the variables for the degree 
    polynomial specified as 'degree' argument, defined by performing polynomial
    regression of average 'G_Avg' for each student associated with a particular
    metric specified as 'metric' argument. If specified 'degree' is higher than
    number of data points available from which to perform a regression, the 
    regression will be performed with the degree of the resultant polynomial 
    equal to the number of data points available in the data set.
    
    Preconditions: 1) Dictionary passed into function as 'i_dict' must be a 
        dictionary generated using one of the four functions defined in 
        T012_M1_load_data.py
        2) The 'metric' selected for the second position argument must be one 
        of the keys contained within the returned list from student_list(i_dict)
    
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Health', 3)
    [-0.0278538498754179, 0.46987985738198207, -2.2742147821236243, 
    13.7162164641214]
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Failures', 2)
    [0.35420696644042277, -2.729867788461538, 11.356343090120658]
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Failures', 4)
    x-wingide-python-shell://129836008/6:1: RankWarning: Polyfit may be poorly 
    conditioned
    [-0.0129539441809042, 0.0769655894192614, 0.21512492094821192, 
    -2.6557070790070747, 11.356570512820507]
    >>>curve_fit(T012_M1_load_data.student_age_dictionary('student-mat.csv'), 
    'Failures', 32)
    x-wingide-python-shell://129836008/6:1: RankWarning: Polyfit may be poorly 
    conditioned
    [-0.0129539441809042, 0.0769655894192614, 0.21512492094821192, 
    -2.6557070790070747, 11.356570512820507]
    """
    if type(i_dict) != dict:
        raise TypeError("Invalid argument: parameter <i_dict> (argument in "
                         "position 1) must be of type <dict>")    
    
    for key in i_dict:
        if type(i_dict[key]) != list:
            raise ValueError("Invalid argument: parameter <i_dict> (argument in"
                    " position 1) must be a dictionary whose values are lists.")
        for i in range(len(i_dict[key])):
            if type(i_dict[key][i]) != dict:
                raise ValueError("Invalid argument: parameter <i_dict> "
                                 "(argument in position 1) must be a dictionary"
                                 " whose values are lists of dictionaries.")                
            if not 'G_Avg' in i_dict[key][i]:
                i_dict = T012_M1_load_data.add_average(i_dict)
            break
        break
    
    i_dict = T012_M2_student_list.student_list(i_dict)
    
    if not metric in i_dict[0]:
        raise ValueError("Invalid argument: parameter <metric> (argument in "
                         "position 2) not contained in i_dict.")
    if type(i_dict[0][metric]) != int and type(i_dict[0][metric]) != float:
        raise ValueError("Invalid argument: parameter <metric> (argument in "
                         "position 2) must be a key whose values are numeric")
    if type(metric) != str:
        raise TypeError("Invalid argument: parameter <metric> (argument in "
                         "position 2) must be of type <string>")
    if type(degree) != int:
        raise TypeError("Invalid argument: parameter <degree> (argument in "
                         "position 3) must be of type <int>")
    
    
    dataset = {}
    for entry in i_dict:
        if entry[metric] in dataset:
            dataset[entry[metric]][0] += entry['G_Avg']
            dataset[entry[metric]][1] += 1
            continue
        dataset[entry[metric]] = [entry['G_Avg'], 1 ]
            
    for key in dataset:
        dataset[key] = dataset[key][0] / dataset[key][1]
        
    num_data_points = len(dataset)
    if num_data_points <= degree:
        degree = num_data_points - 1
        
    return list(polyfit(list(dataset.keys()), list(dataset.values()), degree))



if __name__ == "__main__":
    
    metrics = ['StudyTime', 'Health', 'Absences', 'Failures', 'Age']
    
    curve_fit_results = []
    
    for metric in metrics:
        for degree in range(1, 6):
            curve_fit_results.append(curve_fit(
                T012_M1_load_data.student_age_dictionary(
                    'student-mat.csv'), metric, degree))
            curve_fit_results.append(curve_fit(
                T012_M1_load_data.student_school_dictionary(
                    'student-mat.csv'), metric, degree))
            curve_fit_results.append(curve_fit(
                T012_M1_load_data.student_failures_dictionary(
                    'student-mat.csv'), metric, degree))
            curve_fit_results.append(curve_fit(
                T012_M1_load_data.student_health_dictionary(
                    'student-mat.csv'), metric, degree))