from functools import wraps
from typing import Any, Callable

def validate_numbers(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        
        all_arguments = list(args) + list(kwargs.values())
        
        for arg in all_arguments:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise  TypeError(
                    f"Validacion no completada en '{func.__name__}': "
                    f"El parametro '{arg}' de tipo '{type(arg).__name__}' no es un numero valido."
                )
        return func(*args, **kwargs)
    return wrapper

# ==============================================================================
# CASO DE USO
# ==============================================================================

if __name__ == "__main__":
    
    @validate_numbers
    def calcular_promedio(a: float, b: float, c: float) -> float:
        return (a + b + c) / 3
    
    resultado = calcular_promedio(10, 9, 10)
    print(f"Promedio calculado: {resultado}")
    
    