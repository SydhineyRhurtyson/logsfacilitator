def receber_lista_float(varia:str, prompt:bool=True)-> list[float]:
    """
    Recebe uma lista de números float do usuário.

    Args:
        varia (str): Nome da variável para exibir na mensagem de prompt | Vai recerber um string com os valores separados por vírgula.
        prompt (bool): Indica se deve exibir a mensagem de prompt.

    Returns:
        list[float]: Lista de números float.
    """
    if prompt:
        x= input(f"""Digite as variaveis de {varia}
        "OBS: separado por Virgula, ponto flutuante com ponto
        """).split(",")
    if not prompt:
        x= varia.split(",")
    x= [float(val) for val in x]
    return x

def receber_lista_int(varia:str, prompt:bool=True)-> list[int]:
    """
    Recebe uma lista de números int do usuário.

    Args:
        varia (str): Nome da variável para exibir na mensagem de prompt | Vai recerber um string com os valores separados por vírgula.
        prompt (bool): Indica se deve exibir a mensagem de prompt.

    Returns:
        list[int]: Lista de números int.
    """
    if prompt:
        x= input(f"""Digite as variaveis de {varia}
        "OBS: separado por Virgula, ponto flutuante com ponto
        """).split(",")
    if not prompt:
        x= varia.split(",")
    x= [int(val) for val in x]
    return x
