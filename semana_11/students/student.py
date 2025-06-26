class Student:
    """
    Class that represents a student with his or her information and grades.
    """
    def __init__(self, nombre="", seccion="", español=0.0, ingles=0.0, sociales=0.0, ciencias=0.0):
        """
        Initializes a new student with his or her data and grades.

        Args:
            nombre (str): Student's full name
            seccion (str): Section to which the student belongs
            español (float): Spanish rating (0-100)
            ingles (float): English rating (0-100)
            sociales (float): Social Rating (0-100)
            ciencias (float): Science rating (0-100)
        """
        self.nombre = nombre
        self.seccion = seccion
        self.español = float(español)
        self.ingles = float(ingles)
        self.sociales = float(sociales)
        self.ciencias = float(ciencias)
    
    def calcular_promedio(self):
        """
        Calculates the average of the student's grades.

        Returns:
            float: Grade point average
        """
        return (self.español + self.ingles + self.sociales + self.ciencias) / 4
    
    def to_dict(self):
        """
        Converts Student object to a dictionary for CSV export.

        Returns:
            dict: Dictionary with student data
        """
        return {
            "nombre": self.nombre,
            "seccion": self.seccion,
            "español": self.español,
            "ingles": self.ingles,
            "sociales": self.sociales,
            "ciencias": self.ciencias
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Creates a Student object from a dictionary.

        Args:
            data (dict): Dictionary with student data

        Returns:
            Student: Student object created from the dictionary
        """
        return cls(
            nombre=data.get("nombre", ""),
            seccion=data.get("seccion", ""),
            español=data.get("español", 0.0),
            ingles=data.get("ingles", 0.0),
            sociales=data.get("sociales", 0.0),
            ciencias=data.get("ciencias", 0.0)
        )