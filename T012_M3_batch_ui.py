#by Esteban Heidrich SID: 101267959

import T012_M1_load_data
import T012_M2_sort_plot
import T012_M3_optimization
def batch_ui():
    command_list = []
    print("Please input the name of file where the commands are sotred")
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
                print(sorted_data)
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
                command_list[1], loaded_data)
            print("Highest grade average for",
                  command_list[1], "is", max_result)
