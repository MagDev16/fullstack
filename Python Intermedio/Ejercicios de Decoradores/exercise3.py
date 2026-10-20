from datetime import date
from functools import wraps
from typing import Any, Callable



class User:
# Entity constructor: encapsulates the birth date as a 'date' type
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self._date_of_birth = date_of_birth
        
# Reading interface for the date of birth
    @property
    def date_of_birth(self) -> date:
        return self._date_of_birth
    
# Dynamically computed property to derive the 'age' state
    @property
    def age(self) -> int:
        today = date.today()
        # Calculation of year difference
        years = today.year - self._date_of_birth.year
        
        # Boolean evaluation of the adjustment by day/month (returns True if they haven't had their birthday)
        not_yet_had_birthday = (today.month, today.day) < (
            self._date_of_birth.month,
            self._date_of_birth.day,
        )
        return years - int(not_yet_had_birthday)


# ==============================================================================
# MIDDLEWARE / ASPECTO: DECORADOR DE AUTORIZACIÓN POR EDAD
# ==============================================================================
def require_adult(func: Callable) -> Callable:
    """Higher-order decorator that acts as an authorization guard to check if the received 'User' entity meets the age majority rule (>= 18)."""
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Signature inspection and identification of the 'User' type parameter
        user: User | None = None
        
        # Sequential traversal of positional and named arguments
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, User):
                user = arg
                break
            
        # Invariant Control: Ensure the presence of the User object in the call
        if user is None:
            raise ValueError(
                f"La función '{func.__name__}' requiere un parámetro de tipo 'User'."
            )
            
        # 3. Evaluation of the Business Rule (Policy Enforcement)
        if user.age < 18:
            raise PermissionError(
                f"Acceso denegado: El usuario '{user.name}' es menor de edad."
            )

        return func(*args, **kwargs)

    return wrapper


# =============================================================
# Caso de Uso
# =============================================================
if __name__ == "__main__":
    adult_user = User("Manuel", date(1987, 9, 16))
    minor_user = User("Manuel", date(2015, 9, 16))

    @require_adult
    def solicitar_prestamo(user: User, monto: float) -> str:
        return f"Transaccion aprobada: Prestamo de ${monto} asignado a {user.name}"

    # Execution with a valid user (Returns the expected result)
    print(solicitar_prestamo(adult_user, 100000.0))
    
    #solicitar_prestamo(minor_user, 5000.0)