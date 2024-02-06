# Software QA Test Engineer Assignment

## Context:

This assignment was completed to demonstrate coding and testing skills in the context of a software engineer

This document is structured in the following 3 parts
- Installation and setup
- Application
- Testing 

## Installation and setup
- Ensure you have Python (3.8 or later) installed on your system. 
- Download or clone the repository to your local machine. 
- Navigate to the directory containing the Python script (application.py).
- Install the application and its dependencies:
  - open a terminal in this directory
  - all the dependencies are saved in `requirements.txt` file
  - use the following bash command to install all the dependencies
  - ```pip install -r requirements.txt ```
  - once the dependencies have been installed the application and the test files are ready to run.
  



## Application

The application is stored in the `application.py` file, it takes as an input two YAML files, `current_version`
and `new_version`, and updates `current_version` as follows:

**Base case:**
- If a field of `new_version` is not present in `current_version`, it should be
  added to `current_version` with its value set to the value from `new_version`.
- If a field of `new_version` is present in `current_version`, it should keep the
  value from `current_version`.
- If a field of `current_version` is not present in `new_version`, it should be
  removed from `current_version`.

**Note:** In terms of logic this also translates to making a copy of the `new_version`, and then for all fields that are same in both files the values from `current_version` are kept

**Force Values:**
- Force the update of `current_version` by only replacing the values of the
  currently existing fields with the values from `new_version`

**Note:** In terms of logic this also translated to making a copy of the `current_version` and for fields that exist in both files, force the values from `new_version`

**Force Values:**
- Force the update of `current_version` by replacing the values of the currently
  existing fields with the values from `new_version` and adding or removing the
  fields according  to the requirement mentioned above.

**Note:** In terms of logic this also translated to simply making a copy of the `new_version`

>**Important Note:** The application should be compatible with the configuration file provided for this assignment, which 
is a nested dictionary, there are many ways to deal with this but for the purpose of this assignment Flatten and 
Flatten functions are used from the `flatten-dict` library this helps convert a nested dictionary to a simple one and back. 
Read more here (https://pypi.org/project/flatten-dict/)

**Run application.py**

To run the application open the terminal and use the following bash command:

```./application.py current_version.yaml new_version.yaml [--force-values] [--force-fields] [--log-level]```

`application.py` is the actual name of the Python script. Replace `current_version.yaml` and `new_version.yaml` with the paths to your YAML files. 
Optional arguments `--force-values` and `--force-fields` can be used to force specific update behaviors (see above). In 
addition `--log-level` can be used to det the loggig to different levels including INFO, DEBUG and ERRORS. By default it 
is set to INFO which gives the INFO messages and ERROR messages. To change the --logging-level see the example below  
Exapmle usage:
- Run the base case:

```./application.py current_version.yaml new_version.yaml```

- To force update of values only:

```./application.py current_version.yaml new_version.yaml --force-values```

- To force update of values and fields:

```./application.py current_version.yaml new_version.yaml --force-fields```
- To change Logging level to DEBUG:

```./application.py current_version.yaml new_version.yaml --logging-level DEBUG```


## Testing


Inorder to  assess the correct behaviour of the application several tests are implemented.
There are numerous ways to structure the tests depending on the application being tested. In 
since I know how my application is structured, I test each function used in the application 
individually and then test the entire application to ensure it is working correctly as a whole.
Since the application  has 3 main steps read yaml, update yaml and write yaml. with update yaml having
3 subdivisions i.e. base case, force new values only, force new fields and values. So each of these 5 
functionalities are tested individually. This is useable since i know how my application is structured.
> Alternatively a different approach could be used, two different test files could be build, the main one testing the application as a whole 
> and incase this test fails run a second file that tests the functionality of each function individually.
> Ofcourse if a programmer is unaware of how an application is structured a different test approach is needed.


**Run Tests**

5 different tests are included in the `test_application.py` file. Using the following bash command will run all the test 
files within the present directory, in this case only `test_application.py`. Open the terminal in the same directory and type:

```pytest ``` to run the test, add an optional argument ```--verbose``` to see the detailed view.




