class BanckAccount:
    def __init__(self, balance = 0):
        """
        Inicializa una cuenta bancaria con un balance inicial.

        Args:
            balance(float): Balance inicial de la cuenta (por defecto es 0).
        """
        self.balance = balance

    def deposit(self, amount):
        """
        metodo para ingresar dinero a la cuenta.

        Args:
            amount(float): cantidad de dinero a depositar.
        """
        if amount > 0:
            self.balance += amount
            print(f"El deposito fue exitoso. Nuevo balance: ${self.balance}")
        else:
            print("el monto a depositar debe de ser positivo")

    def withdraw(self, amount):
        """
        Metodo para retirar dinero de la cuenta.

        Args:
            amount (float): cantidad de dinero que se va a retirar
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Retiro de dinero exitoso, Nuevo balance: ${self.balance}")
            else:
                print("El monto a retirar debe de ser positivo")

    def get_balance(self):
        """
        Metodo para consultar el balance actual.

        Returns:
            float: Balance acutal de la cuenta.
        """
        return self.balance

class SavingAccount(BanckAccount):
    def __init__(self, balance=0, min_balance=0):
        """
        Inicializa una cuenta de ahorros con el balance inicial y balance minimo.

        Args:
            balance(float): balance inicial de la cuenta
            min_balance(float): balance minimo que debe de tener la cuenta.
        """
        super().__init__(balance) #Llama al constructor de la clase padre y le pasa el balance inicial
        self.min_balance = min_balance


    def withdraw(self, amount):
        """
        Metodo para retirar dinero de la cuenta de ahorros
        Sobrescribe el metodo de la clase padre para incluir la validacion del balance minimo

        Args:
            amount(float): cantidad de dinero a retirar

        Raises:
            ValueError: si el retiro haria que el balance quede debajo del minimo
        """
        if amount > 0:
            #verifica si despues del retiro el balance quedaria por encima del minimo
            if (self.balance - amount) >= self.min_balance:
                self.balance -= amount
                print(f"El retiro fue exitoso. El nuevo balance : ${self.balance}")
            else: #lanza un error si el retiro violaria el balance minimo
                raise ValueError(f"Error: El retiro haria que el balance sea de (${self.balance - amount}) " f"lo dejaria por debajo del minimo permitido (${self.min_balance})")
        else:
            print("El monto a retitrar debe de ser positivo.")

#usage
if __name__ == "__main__":
    print(f"===Ejemplo de Cuenta bancaria===")
    #crea uan cuenta bancaria normal
    cuenta_normal = BanckAccount(100)
    print(f"Balance incial: ${cuenta_normal.get_balance()}")

    #deposita dinero en la cuenta
    cuenta_normal.deposit(3)

    #retido de dinero
    cuenta_normal.withdraw(30)

    print("\n===Ejemplo de Ahorros de la cuenta===")
    #crea una cuenta de ahorros con un balance inicial de 100 y un balance minimo de 20
    cuenta_ahorros = SavingAccount(balance=99, min_balance=20)
    print(f"Balance inicial: ${cuenta_ahorros.get_balance()}")
    print(f"Balance minimo: ${cuenta_ahorros.min_balance}")

    #deposita dinero en la cuenta de ahorros
    cuenta_ahorros.deposit(25)

    #retiro de dindero(balance inicial quedaria en %75, por encima del minimo)
    cuenta_ahorros.withdraw(50)

    try:
        cuenta_ahorros.withdraw(60)
    except ValueError as e:
        print(f"Error capturado: {e}")
    print(f"El Balance final es de: ${cuenta_ahorros.get_balance()}")





