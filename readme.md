# Introduction

This is a mini program can be used for trimming extra data set in csv. Put your csv files under "input" folder and run the program using python. The trimmed data will be outputed under "output" folder. 

## Usage

1. Create a "input" folder and a "output" folder under the directory
2. Put your csv under "input" folder created
3. Run the code "main.py"
4. Find the outputed csv under "output" folder

## Explanation
The program will check the minimum number count of rows in each column. For example there are some columns with 14 rows, some columns with 13 rows. Then the minimum number of rows will be 13. Those columns with 14 rows will be trimmed to have 13 rows, ie the 14th rows of these coloumns will be trimmed.