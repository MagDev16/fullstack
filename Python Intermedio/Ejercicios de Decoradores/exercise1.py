from functools import wraps
from typing import Any, Callable

def log_execution (func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[LOG] Ejecutando la funcion '{func.__name__}')")
        print(f"      - Parametros posicionales(*args: {args})")
        print(f"      - Parametros nombrados (**kwargs): {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"      - Valor retornado: {result}\n")
        return result
    
    return wrapper

# ======================================================================
# CASO DE USO
# ======================================================================

if __name__ == "__main__":
    @log_execution
    def calcular_total(precio: float, cantidad: int, descuento: float = 0.0 ) -> float:
        total = (precio * cantidad) * (1 - descuento)
        return total
    
    resultado = calcular_total(150.0, 4, descuento=0.1)