from functools import wraps
from time import perf_counter
from datetime import datetime
from os import getcwd,chdir 
from tracemalloc import start,get_traced_memory,stop


def check_existence_of_folder(current_directory:str=getcwd(),folder:str=None,diretorio_ant:str=None)->str:
    """
    Verifica a existência de uma pasta em um diretório e retorna o caminho completo da pasta se ela existir. 
    Caso contrário, sobe um nível no diretório e verifica novamente até encontrar a pasta ou chegar ao diretório raiz.

    Args:
        current_directory (str): Diretório atual. Padrão é o diretório de trabalho atual.
        folder (str): Nome da pasta a ser verificada.
        diretorio_ant (str, optional): Diretório anterior. Padrão é None.

    Returns:
        str: Caminho completo da pasta se ela existir.

    Raises:
        FileNotFoundError: Se a pasta não for encontrada em nenhum diretório.
    """
    diretorio = folder.join(current_directory, folder)
    if folder.isdir(diretorio):
        return diretorio
    else: 
        chdir("..")
        current_directory = getcwd()
        if current_directory == diretorio_ant:
            raise FileNotFoundError(f"A folder '{folder}' não foi encontrada em nenhum diretório")
        return check_existence_of_folder(current_directory,folder,diretorio_ant=current_directory)

def measure_time(folder:str,writer_log:bool=True):
    """
    Args:
        folder (str): Nome da pasta onde o log será salvo.
        writer_log (bool, optional): Se True, escreve o log em um arquivo. Se False, imprime o log no console. Padrão é True.

    Mede o tempo utilizado por uma função e registra o resultado.
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
    Args:
        folder (str): Nome da pasta onde o log será salvo.
        writer_log (bool, optional): Se True, escreve o log em um arquivo. Se False, imprime o log no console. Padrão é True.

    Mede a memória utilizada por uma função e registra o resultado.
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
    args:
        folder (str): Nome da pasta onde o log será salvo.
        writer_log (bool, optional): Se True, escreve o log em um arquivo. Se False, imprime o log no console. Padrão é True.

    Mede o tempo e a memória utilizada por uma função e registra o resultado.
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

