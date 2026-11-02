import pandas as pd
from sympy import sympify, symbols, diff

def regresao(x:list,y:list, return_values:bool=False)-> str|list[float]:
    """
    Vai receber duas listas de valores, X e Y, e calcular os valores de A e B da regressão linear.
    A equação da regressão linear é dada por: Y = A*X + B, onde A é o coeficiente angular e B é o coeficiente linear.
    
    Args:
        x (list): Lista de valores de X.
        y (list): Lista de valores de Y.
        return_values (bool, optional): Se True, retorna os valores de A e B. Se False, retorna a tabela e as fórmulas em uma string. Padrão é False.
        
    Returns:
        list[float]: Lista contendo os valores de A e B, se return_values for True.
        str: String contendo a tabela e as fórmulas, se return_values for False.
    """
    
    #criação da Tabela
    df = pd.DataFrame({"X":x,"Y":y})
    df["XY"] = df["X"]*df["Y"]
    df["X²"]=df["X"]**2

    #Definição de variaveis 
    n = df["X"].count() # numero de valores de X 
    ex = df["X"].sum() # soma de X
    ey = df["Y"].sum() # soma de Y
    exy = df["XY"].sum()# Soma de XY
    ex2 = df["X²"].sum()# Soma de X²

    #Definir A e B 
    divisor = (n*(ex2)-(ex)**2)
    a = (n*(exy)-(ex)*(ey))/divisor
    b = (ex2*ey-(exy)*(ex))/divisor
    if return_values:
        return [a,b]
    else:
        #Exibir a Tabela 
        separa= "=+="*20
        tabela= separa+"\nTabela de valores\n"+df.to_string(index=False)+"\n"
    
        #Exibir as variavei
        def_var= separa+f"""\nDefinição de variaveis:
N = {n}, N é o numero de valores de X
EX  = {ex}, EX é a Soma dos valores de X
EY  = {ey}, EY é a Soma dos valores de Y
EXY = {exy}, EXY é a Soma dos valores de XY
EX² = {ex2}, EX² é a Soma dos valores de X²
{separa}"""
        #Exibir as formulas de A e B
        form_a= f"""Formula A:
A = (n*(exy)-(ex)*(ey))/(n*(ex2)-(ex)²)
A = ({n}*({exy})-({ex})*({ey}))/({n}*({ex2})-({ex})²)
A = ({n*(exy)}-{round((ex)*(ey),3)})/({n*(ex2)}-{(ex)**2})
A = {round(n*(exy)-(ex)*(ey),3)}/{(n*(ex2)-(ex)**2)}
A = {round(a,3)}
{separa}"""

        form_b= f"""Formula B:
B = (ex2*ey-(exy)*(ex))/(n*(ex2)-(ex)²)
B = ({ex2}*{ey}-({exy})*({ex}))/({n}*({ex2})-({ex})²)
B = ({ex2*ey}-{(exy)*(ex)})/({n*(ex2)}-{(ex)**2})
B = {round(ex2*ey-(exy)*(ex),3)}/{(n*(ex2)-(ex)**2)}
B = {round(b,3)}
{separa}"""
        return tabela+"\n"+def_var+"\n"+form_a+"\n"+form_b


def formula():
    print("Digite a função:")
    f = input()
    f = f.replace("^", "**")
    espressao = sympify(f)
    return espressao

def funca(e,x):
    s = symbols('x')
    resultado = round(e.subs(s, x), 5)
    return  resultado

def derivada(e,x):
    s = symbols('x')
    derivada = diff(e, s)
    resulrdiv = round(derivada.subs(s, x), 5)
    return resulrdiv
