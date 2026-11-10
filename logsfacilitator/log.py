from functools import wraps
from time import perf_counter
from datetime import datetime
from os import getcwd,chdir ,path
from tracemalloc import start,get_traced_memory,stop
from inspect import signature

def log_message(message:str,folder:str,writer_log:bool=True):
    """
    Logs a message to a file or prints it to the console.

    Args:
        message (str): The message to be logged.
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True."""
    separa = "=+="*20
    if writer_log:
        diretorio_log = check_existence_of_folder(folder=folder)
        with open(path.join(diretorio_log,"log.txt"),"a",encoding="utf-8") as arquivo:
            arquivo.write(f"{message}\n{separa}\n")
    elif not writer_log:
        print(f"{message}\n{separa}\n")

def check_existence_of_folder(current_directory:str=getcwd(),folder:str=None,old_directory:str=None)->str:
    """
    Checks for the existence of a folder in a directory and returns the full path of the folder if it exists. 
Otherwise, it goes up one level in the directory and checks again until it finds the folder or reaches the root directory

    Args:
        current_directory (str): Current directory. Default is the current working directory.
        folder (str): Name of the folder to be checked.
        old_directory (str, optional): Previous directory. Defaults to None.

    Returns:
        str: Full path of the folder if it exists.
    
    Example:
        >>> check_existence_of_folder(current_directory="/home/user/documents", folder="my_folder")
        '/home/user/documents/my_folder'
        
    Raises:
        FileNotFoundError: If the folder is not found in any directory.
    """
    diretorio = path.join(current_directory, folder)

    if path.isdir(diretorio):
        return diretorio
    else: 
        chdir("..")
        current_directory = getcwd()
        if current_directory == old_directory:
            raise FileNotFoundError(f"A folder '{folder}' was not found in any directory")
        return check_existence_of_folder(current_directory,folder,old_directory=current_directory)

def measure_time(folder:str,writer_log:bool=True):
    """
    Measures the time taken by a function and logs the result.

    Args:
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True.

    Example:
        >>> @measure_time(folder="logs", writer_log=True)
        >>> def my_function():
        >>>     # Function code here
    """
    def decorador(funcao):
        @wraps(funcao)
        def interna(*args, **kwargs):

            inicio = perf_counter()
            resultado = funcao(*args, **kwargs)
            fim = perf_counter()

            tempo = fim - inicio
            minuto = tempo // 60
            segundo = tempo % 60
            variaveis = signature(funcao).bind(*args, **kwargs).arguments
            registro =f"Log:{datetime.now()}\nFunction: {funcao.__name__}, Args: {variaveis}\n Time: {minuto }:{segundo:.4f} seconds"
            log_message(message=registro, folder=folder, writer_log=writer_log)

            return resultado
        return interna
    return decorador

def measure_memory(folder:str,writer_log:bool=True):
    """
    Measures the memory used by a function and logs the result.

    Args:
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True.
    
    Example:
        >>> @measure_memory(folder="logs", writer_log=True)
        >>> def my_function():
        >>>     # Function code here
    """
    def decorador(funcao):
        @wraps(funcao)
        def interna(*args, **kwargs):
            start()
            resultado = funcao(*args, **kwargs)
            memoria_atual, memoria_maxima = get_traced_memory()
            stop()

            
            assinatura = signature(funcao)
            variaveis = assinatura.bind(*args, **kwargs).arguments
            registro = f"Log:{datetime.now()}\nFunction: {funcao.__name__}, Args: {variaveis}\n Memory current: {memoria_atual / 1024 / 1024:.2f} MB, Memory maximum: {memoria_maxima / 1024 / 1024:.2f} MB"
            log_message(message=registro, folder=folder, writer_log=writer_log)
            return resultado
        return interna
    return decorador

def measure_time_and_memory(folder:str,writer_log:bool=True):
    """
    Measures the time and memory used by a function and records the result.

    Args:
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True.

    Example:
        >>> @measure_time_and_memory(folder="logs", writer_log=True)
        >>> def my_function():
        >>>     # Function code here    
    """
    def decorador(funcao):
        @wraps(funcao)
        def interna(*args, **kwargs):
            start()
            inicio = perf_counter()
            resultado = funcao(*args, **kwargs)
            memoria_atual, memoria_maxima = get_traced_memory()
            stop()
            fim = perf_counter()
            tempo = fim - inicio
            minuto = tempo // 60
            segundo = tempo % 60
            variaveis = signature(funcao).bind(*args, **kwargs).arguments
            registro = f"Logs:{datetime.now()}\nFunction: {funcao.__name__}, Args: {variaveis}\nTime: {minuto }:{segundo:.4f} seconds\nMemory current: {memoria_atual / 1024 / 1024:.2f} MB, Memory maximum: {memoria_maxima / 1024 / 1024:.2f} MB"
            log_message(message=registro, folder=folder, writer_log=writer_log)
            return resultado
        return interna
    return decorador

