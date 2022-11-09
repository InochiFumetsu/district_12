#THIS IS THE MAIN PROJECT FILE WHICH WILL IMPORT THE OTHER TWO MODULES
#version: 0.0

import importlib as imp               # Spencer: I am not sure of the syntax they will teach us for this in class (don't know if this is how they'll want us to do it)
imp.import_module(load_data_12.py)    #          I'm just including it to kind of show what I *THINK* they're going to have us do for the 2 "modules" we have to write.
imp.import_module(sort_plot_12.py)

# Ok so it SEEMS as though you only have to remove the ">>>>>>>master" and "<<<<<<<slave" lines of "code" in the file it shows you highlighting the conflicts in
# order to have the option to mark the file as "conflicts resolved" (top right button) -- actually, on further testing, you only need to remove the "<<<<<<<"
# and ">>>>>>>" -- apart from that you just rewrite whatever's in the file to be the way you want it and mark it as "resolved" --> then you can merge!