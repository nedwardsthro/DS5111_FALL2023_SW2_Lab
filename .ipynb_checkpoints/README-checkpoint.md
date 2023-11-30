# DS5111_FALL2023_SW2_Lab
Homework for Data Engineering Fall 2023

1. To get the make to work, I had to take away the spaces and replace them with tabs. I also had to find the appropriate lines of code for the make env command. I also had to define that test was a .PHONY command in the makefile.

2. To make the python3 -m venv env work, I had to sudo apt install venv. Essentially, I had to install the venv package to set up the environment.

3. Because the two commands both create the virtual environment but the virtual environment can only be created once, these two lines should be run on the same command.

4. It is possible that both the file and the makefile command could both be executed. We could fix this by changing the makefile command or the file name.

5. It appends the current directory to the sys.path so that we import the proper function when we run import bin.clockdeco_param as cp. 
