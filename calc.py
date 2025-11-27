def suma(a,b):
    try:

        return float(a) + float(b)
    except Exception as e:
        raise ValueError("Entradas no numéricas") from e


def resta(a,b):
    try:
        return float(a) - float(b)
    except Exception as e:
        raise ValueError("Entradas numéricas") from e
    

def multiplicacion(a,b):
    try:
        return float(a) * float(b)
    except Exception as e:  
        raise ValueError("Entradas no numéricas") from e 

def division(a,b):
    try:
        b_float = float(b)
        if b_float == 0:
            raise ValueError("No se puede dividir entre 0")
        return float(a) / b_float
    except Exception as e:  
        raise ValueError("Entradas no numéricas") from e 