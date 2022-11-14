# district_12
ECOR1042_Lab1B_Course_Project

# CODE CONVENTION:
    <do we want to institute any coding conventions we all have to adhere to before we begin coding?>
    for example: 80 character line limits or writing docstrings for all functions / commenting all code?

# REPO PROCEDURE:
## To begin working on a new section:
    1) Create a new branch
        ***suggest title format: "LabX_<purpose_of_branch>"***
        example: "Lab3_[function]:Import_from_csv"
    2) Inside your new branch, open the file you intend to work on in the editor on the website.
    3) Select all (CTRL-A), copy (CTRL-C)
    4) Open the corresponding file on your computer in Wing101
    5) Select all (CTRL-A), paste (CTRL-V)
    6) Save the file (CTRL-S)
    7) Begin your edit.
    
## When you are finished writing your section:
    1) Save your file (CTRL-S)
    2) Select all (CTRL-A), copy (CTRL-C)
    3) Go back to the branch version of the file (should still be open in the editor on the website)
    4) Select all (CTRL-A), paste (CTRL-V)
    5) Update commit title / description
    6) Click *COMMIT*
    7) Create a *Pull Request*

## Creating a "pull request" (PR)
    1) Click on "pull requests" tab (top menu)
    2) Click "new pull request" (green button, top-right)
    3) ***ENSURE BASE=master and COMPARE=<your_branch_to_merge_in>***
        note the arrow between these two drop-down menus if you forget which way the merge is going.
    4) Update merge title / description: 
        the title is really what matters here, want to write something to-the-point, but descriptive.
        The aim is to make it easy for anyone to know what they're looking at if they're going back 
        over PRs / merges / branches weeks from now.
    5) Click Create Pull Request.
    6) ***RESOLVE ANY CONFLICTS YOUR FILE HAS WITH THE MASTER VERSION***



# Lab 3 “LOAD DATA MODULE” <Text Processing / Dicts / Lists>
    •	Read .csv file into data structure
    •	“Text Processing”? -> create a dictionary and fill it with student data
    •	Keys (not sure if we’re supposed to do one (dict) for each or just pick one):
       o	School
       o	Age
       o	Health
       o	Failures
    •	Calculate each student’s average grade
       o	Append it into the dict
   
# Lab 4 <Unit testing / sets>
    •	Unit testing:
       o	Perform a bunch of tests to ensure previously build (load data) module works “perfectly”

# Lab 5 “SORT/PLOT MODULE” <Lists/Sorting/CurveFitting/Plotting>
    •	Create a function which converts the dictionaries (created by previously written functions) into 
            LISTS of students
    •	Create functionS (multiple) *using sorting algorithms (I assume taught in lecture)* which sort
            the (above) lists according to the different data (age / grades / health etc.) AND RETURN THE 
            SORTED DATA
    •	“Do regression and/or interpolation to return the polynomial that best fits your data” – that’s 
            all it says, I don’t know which data set we’re supposed to use for that (or if it matters – 
            it shouldn’t) – also don’t know if it’s supposed to be a single function that performs 
            multiple types of regression or what…
    •	Create A function which plots histograms of the students’ data (based I guess on which sorted list
            you pass as an argument to the function?)

# Lab 6
    •	“find minimum and maximum of given data using different libraries” – whatever that means
       o	Supposed to use OPTIMIZATION AND EQUATION OF LINE OF BEST FIT --  though that might be for the 
            whole lab not just the above task
    •	Create TWO user interfaces which allow the user to “call and execute the functions created in the 
            past labs”:
       1.	Take inputs directly from the terminal to execute commands
       2.	Second will read a string of commands from a text file (“batch interface”)
    •	Create “ReadMe” file & “wrap up” whatever that means.
