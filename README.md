# **logsfacilitator**
This library aims to facilitate logging memory consumption and execution time for functions. Additionally, it centralizes utility functions shared across multiple projects, making it easier to access and reuse this code.
****
**English** | [Português (Brasil)](https://github.com/SydhineyRhurtyson/logsfacilitator/blob/main/README.pt-BR.md) 
****
### How to Install
Install via pip: 

```
pip install logsfacilitator
```
****
### How to Use 

```
import logsfaciliti 

```
****
### Decorators
 
*The included decorators are used to record resource consumption and function execution time.* 

#### **measure_time**
Measures the time taken to run the function. The result can be printed in the terminal or logged in a file.
    
    Args:
        folder (str): Name of the folder where the log will be saved. The function automatically checks if this folder exists.
        writer_log (bool, optional): If True, records the log in the file. If False, prints the log to the console. Default is True.

#### **measure_memory**
Measures the RAM memory consumption used to run the function. The result can be printed in the terminal or logged in a file.
    
    Args:
        folder (str): Name of the folder where the log will be saved. The function automatically checks if this folder exists.
        writer_log (bool, optional): If True, records the log in the file. If False, prints the log to the console. Default is True. 

#### **measure_time**
Simultaneously measures the execution time and RAM memory consumption of the function. The result can be printed in the terminal or logged in a file.
    
    Args:
        folder (str): Name of the folder where the log will be saved. The function automatically checks if this folder exists.
        writer_log (bool, optional): If True, records the log in the file. If False, prints the log to the console. Default is True.

****
### **Functions**

#### **check_existence_of_folder**
Checks for the existence of a folder in a directory and returns the full path if it exists. Otherwise, it moves up one directory level and checks again recursively until it finds the folder or reaches the root directory.

    Args:
        current_directory (str): Starting directory for the search. Default is the current working directory.
        folder (str): Name of the folder to be checked.
        old_directory (str, optional):Previous directory. Default is None.
    
    Retorna :
        str: Full path to the folder.
    
    Raises: 
        FileNotFoundError: If the folder is not found at any level up to the root directory..

#### **set_list_float**
Receives a string and transforms it into a list of decimal numbers (float).

    Args:
        varia (str): Name of the variable to display in the console prompt (if console=True), or the actual string with comma-separated values to be converted into the list (if console=False).
        console(bool,optional): If True, prompts the user for an input in the terminal. If False, uses the string provided in the varia argument.
    
    Retorno:
        (list[float]): A list containing the numeric values.

#### **set_list_int**
Receives a string and transforms it into a list of int

    Args:
        varia (str): Name of the variable to display in the console prompt (if console=True), or the actual string with comma-separated values to be converted into the list (if console=False).
        console(bool,optional): If True, prompts the user for an input in the terminal. If False, uses the string provided in the varia argument.
    
    Retorno:
       (list[int]): A list containing the numeric values.
    
    
