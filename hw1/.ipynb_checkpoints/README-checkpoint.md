# Homework 1
UIC CS 418, Spring 2024

## Files/Folders:

* README.md (this file): This file providing information about environment setup for getting started with homework.
* warmup.ipynb: Jupyter notebook file for a warmup assignment which is not graded. 
* hw1.ipynb: Jupyter notebook file containing instruction for the assignment.
* hw1part1.py: Python file containing skeleton functions of part1 to be completed and submitted for grading.
* hw1part2.py: Python file containing skeleton functions of part2 to be completed and submitted for grading.
* airports.dat, flights.dat, parse_page_test1.html, parse_page_test2.html: Sample data files
* run_tests_sample.py, tests_sample_part1, tests_sample_part2: Tools for testing correctness of the functions in hw1part1.py and hw1part2.py
* correct.png: sample gradescope submission results


## Setup and Prerequisites
The main programming language for this course is Python. We will create an environment that uses version 3.11.5. 
We will use the same programming environment for all the assignments which ensures that everyone has the same python library versions. 
Homework assignments will be graded using only this environment and no others, so make sure that you set it up correctly.

Install anaconda 2023.09-0 for python 3.11: https://www.anaconda.com/download

elena-macbook$ conda install anaconda=2023.09-0

If you already have anaconda, make sure it's updated to this version:

elena-macbook$ conda update conda

In your terminal, check whether you have the right anaconda version:

elena-macbook$ conda --version
conda 23.9.0

If the command cannot be found, then make sure you have closed and re-opened the terminal window after installing it.

Create a directory for CS 418 homework (e.g., cs418-hw)

Move hw1.zip to that directory and unzip it.

Create a python 3.11.5 environment (this allows you to use a python version that may be different from your machine's default version):

elena-macbook:cs418-hw$ conda create -n cs418env python=3.11.5 anaconda

Activate the environment:

elena-macbook:cs418-hw$ conda activate cs418env   #omit the conda part on windows

Change to homework directory:

(cs418env) elena-macbook:cs418-hw elena$ cd hw1

Start the Jupyter notebook:

(cs418env) elena-macbook:hw1 elena$ jupyter notebook &

This should open a Jupyter notebook in your web browser and display the contents of the current directory. 

======== COMPLETE THIS PART TO GET FAMILIAR WITH PYTHON BASICS =========

From the directory displayed in the browser, select warmup.ipynb, and follow the instructions in the notebook. The warmup will not be graded but it is highly recommended that everyone completes it, especially if you have little to no prior Python or Jupyter notebook knowledge.  Even if you are familiar with Python, you may learn something new that will help you with the homework assignments.

=================== HOMEWORK INSTRUCTIONS ==========================

Select hw1.ipynb, and follow the instructions in the notebook. This part will be graded.

