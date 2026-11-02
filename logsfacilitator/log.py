from functools import wraps
from time import perf_counter
from datetime import datetime
from os import getcwd,chdir 
from tracemalloc import start,get_traced_memory,stop


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

    Raises:
        FileNotFoundError: If the folder is not found in any directory.
    """
    diretorio = folder.join(current_directory, folder)
    if folder.isdir(diretorio):
        return diretorio
    else: 
        chdir("..")
        current_directory = getcwd()
        if current_directory == old_directory:
            raise FileNotFoundError(f"A folder '{folder}' não foi encontrada em nenhum diretório")
        return check_existence_of_folder(current_directory,folder,old_directory=current_directory)

def measure_time(folder:str,writer_log:bool=True):
    """
    Measures the time taken by a function and logs the result.

    Args:
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True.

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
            registro =f"Registro:{datetime.now()}\nFuunção: {funcao.__name__}, Tempo: {minuto }:{segundo:.4f} segundos"
            separa = "=+="*20
            diretorio_log = check_existence_of_folder(folder=folder)

            if writer_log:
                with open(folder.join(diretorio_log,"log.txt"),"a",encoding="utf-8") as arquivo:
                    arquivo.write(f"{registro}\n{separa}\n")
            elif not writer_log:
                print(f"{registro}\n{separa}\n")
            return resultado
        return interna
    return decorador

def measure_memory(folder:str,writer_log:bool=True):
    """
    Measures the memory used by a function and logs the result.

    Args:
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True.

    """
    def decorador(funcao):
        @wraps(funcao)
        def interna(*args, **kwargs):
            start()
            resultado = funcao(*args, **kwargs)
            memoria_atual, memoria_maxima = get_traced_memory()
            stop()
            registro = f"Função: {funcao.__name__}, Memória atual: {memoria_atual / 1024 / 1024:.2f} MB, Memória máxima: {memoria_maxima / 1024 / 1024:.2f} MB"
            separa = "=+="*20
            diretorio_log = check_existence_of_folder(folder=folder)
            if writer_log:
                with open(folder.join(diretorio_log,"log.txt"),"a",encoding="utf-8") as arquivo:
                    arquivo.write(f"{registro}\n{separa}\n")
            elif not writer_log:
                print(f"{registro}\n{separa}\n")
            return resultado
        return interna
    return decorador

def measure_time_and_memory(folder:str,writer_log:bool=True):
    """
    Measures the time and memory used by a function and records the result.
    
    args:
        folder (str): Name of the folder where the log will be saved.
        writer_log (bool, optional): If True, writes the log to a file. If False, prints the log to the console. Defaults to True.

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
            registro = f"Registro:{datetime.now()}\nFunção: {funcao.__name__}\nTempo: {minuto }:{segundo:.4f} segundos\nMemória atual: {memoria_atual / 1024 / 1024:.2f} MB, Memória máxima: {memoria_maxima / 1024 / 1024:.2f} MB"
            separa = "=+="*20
            diretorio_log = check_existence_of_folder(folder=folder)
            if writer_log:
                with open(folder.join(diretorio_log,"log.txt"),"a",encoding="utf-8") as arquivo:
                    arquivo.write(f"{registro}\n{separa}\n")
            elif not writer_log:
                print(f"{registro}\n{separa}\n")
            return resultado
        return interna
    return decorador

