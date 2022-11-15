"""Hey guys, so I had actually written another little script to help check 
the output of the code we wrote for our individual functions, in addition 
to the one I shared in teams earlier today. I thought I'd share it too, 
so I'm going to share it in this file and I'll include the script I shared
earlier so they're all be in one place
"""



#SCRIPT 1:
for i in iter("""<return_val>"""):
    print(i, ":", " " * (4 - len(str(len("""<return_val>"""[i])))),
          len("""<return_val>"""[i]), "x", sep="")


"""Here, replace <return_val> (and associated quotes) with whatever value
your function returns.

for example, if your return statement looks like this:
return school_dictionary

then you would replace every instance of <return_val> (and associated quotes)
in the above script, with "school_dictionary", so you'd get:

for i in iter(school_dictionary):
    print(i, ":", len(school_dictionary[i]))
    
YOU INSERT THIS CODE RIGHT BEFORE THE RETURN STATEMENT IN YOUR FUNCTION
****DO NOT LEAVE THIS CODE IN YOUR FINAL SUBMISSION TO BRIGHTSPACE****
  be sure to remove it again once you've finished checking your output.
  
This code will display the key values in your dictionary and the number of 
entries (students) contained inside the list (the value) associated with
each of those keys in your dictionary. To use this as a check you would 
check those numbers against the number of entries for each of the different
keys in the 'student-mat.csv' file.
"""



#SCRIPT 2:
with open('output_check.txt', 'a') as check_out:
    for i in iter("""<return_val>"""):
        check_out.write(i + ":\n")
        for j in range(len("""<return_val>"""[i])):
            check_out.write('\t' + str("""<return_val>"""[i][j]) + '\n')
        check_out.write("\n\n\n")

"""
As with the previous code, replace each instance of <return_val> (and 
associated quotations) with the name of the object you are returning 
from your function. (see above if you need an example of what I mean
by that).

As before, insert the code before the return statement in your function.
Save and run your program.

This script will write the contents of your dictionary to a '.txt' file
in the same directory as your saved function file. The difference is, 
I this script changes the formatting of the output to something that's 
extremely easily readable. Just run the function -- then go open the 
"output_check.txt" file and you should have a very easy time seeing 
and understanding exactly what your function has done and if it has 
created the dictionary properly.

****AGAIN, PLEASE REMEMBER TO *REMOVE* THIS CODE FROM YOUR FUNCTION 
***BEFORE*** SUBMITTING YOUR FILE****
"""



#SCRIPT 3:
for i in iter("""<return_val>"""):
    print(i, ":", sep="")
    for j in range(len("""<return_val>"""[i])):
        print("\t", """<return_val>"""[i][j], sep="")
        
"""
This is just a "print-to-console" version of SCRIPT 2
"""
