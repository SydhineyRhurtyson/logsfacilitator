# **logsfacilitator**
Esta biblioteca tem como objetivo facilitar o registro de consumo de memória e tempo de execução de funções. Além disso, ela centraliza funções utilitárias compartilhadas entre múltiplos projetos, facilitando o acesso e a reutilização desse código.
****
[English](https://github.com/SydhineyRhurtyson/logsfacilitator/blob/main/.gitignore/README.md) | [Português (Brasil)]
****
### Como instalar
Instalar via pip 

```
pip install logsfacilitator
```
****
### Como usar 

```
import logsfaciliti 

```
****
### Decoratores
 
*Os decoradores incluídos servem para registrar o consumo de recursos e o tempo de execução das funções.* 

#### **measure_time**
Os decoradores incluídos servem para registrar o consumo de recursos e o tempo de execução das funções.
  
    Args:
        folder (str): Nome da pasta onde o log será salvo. A função verifica automaticamente se esta pasta existe.
        writer_log (bool, optional): Se True, registra o log no arquivo. Se False, imprime o log no console. O padrão é True.

#### **measure_memory**
Mede o consumo de memoria RAM usado para roda a função podendo impimir no terminal ou registrar em um arquivo de logs
  
    Args:
        folder (str): Nome da pasta onde o log será salvo. A função verifica automaticamente se esta pasta existe.
        writer_log (bool, optional): Se True, registra o log no arquivo. Se False, imprime o log no console. O padrão é True.

#### **measure_time_and_memory**
Mede simultaneamente o tempo de execução e o consumo de memória RAM da função. O resultado pode ser impresso no terminal ou registrado em um arquivo de log.
 
    Args:
        folder (str): Nome da pasta onde o log será salvo. A função verifica automaticamente se esta pasta existe.
        writer_log (bool, optional): Se True, registra o log no arquivo. Se False, imprime o log no console. O padrão é True.

****
### **Funções**

#### **check_existence_of_folder**
Verifica a existência de uma pasta em um diretório e retorna o caminho completo se ela existir. Caso contrário, sobe um nível no diretório e verifica novamente de forma recursiva até encontrar a pasta ou chegar ao diretório raiz.

    Args:
        current_directory (str): Diretório inicial da busca. O padrão é o diretório de trabalho atual.
        folder (str): Nome da pasta a ser verificada
        old_directory (str, optional): Diretório anterior. O padrão é None..
    
    Retorna :
        str: Caminho completo da pasta..
    
    Raises: 
        FileNotFoundError: Se a pasta não for encontrada em nenhum nível até o diretório raiz.

#### **set_list_float**
Recebe uma string e a transforma em uma lista de números decimais (float).

    Args:
        varia (str): Nome da variável para exibir na mensagem do console (se console=True), ou a própria string com os valores separados por vírgula que será convertida na lista (se console=False).
        console (bool, opcional): Se True, solicitará uma entrada (input) do usuário no terminal. Se False, utilizará a string fornecida no argumento varia.
    
    Retorno:
        (list[float]): Uma lista contendo os valores numéricos.

#### **set_list_int**
Recebe uma string e a transforma em uma lista de números inteiros (ints).

    Args:
        varia (str): Nome da variável para exibir na mensagem do console (se console=True), ou a própria string com os valores separados por vírgula que será convertida na lista (se console=False).
        console (bool, opcional): Se True, solicitará uma entrada (input) do usuário no terminal. Se False, utilizará a string fornecida no argumento varia.
    
    Retorno:
        (list[int]): Uma lista contendo os valores numéricos inteiros.

    
