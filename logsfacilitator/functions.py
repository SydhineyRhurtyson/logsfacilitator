def set_list_float(varia:str, console:bool=True)-> list[float]:
    """
    Get a str in transform in float list.

    Args:
        varia (str): Variable name to display in the console message, or a string containing comma-separated values ​​that will be converted into a list.
        console (bool): If True, it will prompt for input in the console. If False, it will receive a string with the values ​​separated by commas.
    Returns:
        list[float]: Float list.
    """
    if console:
        x= input(f"""Enter the variables for {varia}
        "Note: separate with commas; use a decimal point for float numbers
        """).split(",")
    if not console:
        x= varia.split(",")
    x= [float(val) for val in x]
    return x

def set_list_int(varia:str, console:bool=True)-> list[int]:
    """
    Get a str in transform in int list.

    Args:
        varia (str): Variable name to display in the console message, or a string containing comma-separated values ​​that will be converted into a list.
        console (bool): If True, it will prompt for input in the console. If False, it will receive a string with the values ​​separated by commas.
    Returns:
        list[int]: int list.
    """
    if console:
        x= input(f"""Enter the variables for {varia}
        "Note: separate with commas, don`t permit float numbers
        """).split(",")
    if not console:
        x= varia.split(",")
    x= [int(val) for val in x]
    return x
