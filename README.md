### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

In addition to the standard Anaconda distribution of Python, you will need to install the following libraries.
1. plotly 
2. chart-studio

This Jupyter notebook should run without errors using Python 3.x

## Project Motivation<a name="motivation"></a>

Traditional Master's degrees come with increasingly exorbitant costs. Even after the current Covid-19 pandemic abates and traditional in-person, in-classroom instruction resumes, many college-age individuals will have to confront the question whether taking on potentially six-figure debt provides the appropriate long-term payoff. 

For this project I will perform the following analysis steps
1. From Stack Overflow survey data, determine data scientist starting salary for cohorts with some college education or a bachelor's degree PLUS an online data science-specific training
2. From Stack Overflow survey data, determine data scientist starting salary for cohorts with a Master's Degree 
3. Compare these salary points with other public, credible sources
4. Use a consolidated view of starting salaries as a starting point for an NPV calculation
5. Determine which cohort would attain a higher NPV based on this simplified model after 10 years


## File Descriptions <a name="files"></a>

There is 1 main notebook, 1 Python file containing utility functions, and 1 data file. Pertinent environment variables such as the Chart Studio API key reside in the .env file which was marked as .gitignore to avoid unwanted propagation of the proprietary API key and is not included. Markdown cells are used extensively to facilitate walk throughs of the approach.

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@josh_2774/how-do-you-become-a-developer-5ef1c1c68711).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

- Stack Overflow for the invaluabule source data
- Udacity Data Science Nanodegree for some of the routine pre-processing steps 
- 

