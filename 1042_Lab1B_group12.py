#THIS IS THE MAIN PROJECT FILE WHICH WILL IMPORT THE OTHER TWO MODULES
#version: 0.0

import importlib as imp               # Spencer: I am not sure of the syntax they will teach us for this in class (don't know if this is how they'll want us to do it)
imp.import_module(load_data_12.py)    #          I'm just including it to kind of show what I *THINK* they're going to have us do for the 2 "modules" we have to write.
imp.import_module(sort_plot_12.py)

# STEP 2: Here I am editing master branch to make sure the version of the file in the slave branch (with its changes) is out of date compared to this.
