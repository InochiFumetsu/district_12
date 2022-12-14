"""
Copyright © 2022, Esteban Heidrich, Jack Roberts, Milan Djordjevic, Spencer Hiscox. All rights reserved. Study-PY™ is a trademark of district_12™ developers.

Copyright © 2005-2022, NumPy Developers. All rights reserved.

Copyright © 2001-2002 Enthought, Inc. 2003-2022, SciPy Developers. All rights reserved.

Copyright © 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012–2022 The Matplotlib development team.

For full licensing information, see the README.md file in the root folder of the master branch of this repository:
https://github.com/InochiFumetsu/district_12/blob/master/README.md
"""


import T012_M1_load_data
import T012_M2_sort_plot
import T012_M3_optimization
def batch_ui():
    command_list = []
    print("Please input the name of file where the commands are stored")
    cmd_file = input()
    file_contents = open(cmd_file, 'r')
    for line in file_contents:
        line = line.split(';')
        command_list = line
        command_list[-1] = command_list[-1].strip('\n')
        if command_list[0].lower() == "l":
            try:
                loaded_data = T012_M1_load_data.add_average(T012_M1_load_data.load_data(
                    command_list[1], command_list[2]))
                if loaded_data == {}:
                    print("There is a command error in the file")
                    break
                else:
                    print("Data Loaded")
            except:
                print("There is a command error in the file")
                break
        elif command_list[0].lower() == "s":
            sorted_data = T012_M2_sort_plot.sort_students_bubble(
                loaded_data, command_list[1])
            if command_list[2] == 'Y':
                print("Here is your sorted data")
                for i in iter(sorted_data):
                    print(i, ":", sep="")
                    for j in range(len(sorted_data[i])):
                        print("\t", sorted_data[i][j], sep="")
            elif command_list[2] == 'N':
                print("Data sorted but not shown")
            else:
                print("There is a command error in the file")
                break
            #print("There is a command error in the file")
            # break
        elif command_list[0].lower() == "h":
            try:
                T012_M2_sort_plot.histogram(loaded_data, command_list[1])
                print("histograms with", command_list[1], "will be shown")
            except:
                print("There is a command error in the file")
                break
        elif command_list[0].lower() == "w":
            min_result = T012_M3_optimization.minimum(
                loaded_data, command_list[1])
            print("Lowest grade average for",
                  command_list[1], "is", min_result)
        elif command_list[0].lower() == "b":
            max_result = T012_M3_optimization.maximum(
                loaded_data, command_list[1])
            print("Highest grade average for",
                  command_list[1], "is", max_result)
          file_contents.close()
          
if name == "__main__":
    batch_ui()
