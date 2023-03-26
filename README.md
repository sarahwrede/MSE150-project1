# MSE150-project1
This repository contains the starting point for Project 1 for MSE 150 Spring 2023 at Boise State University.
This project required me to have NoMachine which contains bash, python, and nano text editor. I also had to have a Git account.
The code for this project can be found in the plot.py file.
You can run it by using $ python plot.py 'filepath/filename' at the command line.
For example, if I ran '$ python plot.py raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw' at the command line I can expect it to populate a graph of stress vs. strain data and a linear regression line of the linear portion of the graph. It will also save the figure under the filename as a .png, and bash will also print the slope of the linear regression line.
The GNU license can be found in the LICENSE.txt file. 

I learned a lot about python through trial and error.
I attempted each part of the project and confirmed whether it would work as intended or not.
I ran into a lot of issues trying to create a linear regression of the linear portion, and trying to use a code other than np.concatenate.
Each time I attempted to run python plot.py at the command line I was getting errors of different sorts.
I would decipher the error and edit my code accordingly, and eventually I got the desired results.
