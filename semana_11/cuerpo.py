class Head:
    def __init__(self):
        self.has_brain = True
        self.eyes = 2
        self.ears = 2
        self.nose = 1
        self.mouth = 1

class Hand:
    def __init__(self, is_right=True):
        self.fingers = 5
        self.is_right = is_right  # Para distinguir entre mano derecha e izquierda

class Arm:
    def __init__(self, hand):
        self.hand = hand
        self.length = "medium"  # Ejemplo de atributo adicional

class Leg:
    def __init__(self, foot, is_right=True):
        self.foot = foot
        self.is_right = is_right  # Para distinguir entre pierna derecha e izquierda
        self.length = "long"  # Ejemplo de atributo adicional

class Foot:
    def __init__(self, toes=5):
        self.toes = toes
        self.has_nails = True

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.organs = ["heart", "lungs", "stomach"]  # Ejemplo de atributo adicional

class Human:
    def __init__(self, name):
        self.name = name
        
        # Crear las partes del cuerpo
        self.head = Head()
        
        # Manos y brazos
        self.left_hand = Hand(is_right=False)
        self.right_hand = Hand(is_right=True)
        self.left_arm = Arm(self.left_hand)
        self.right_arm = Arm(self.right_hand)
        
        # Pies y piernas
        self.left_foot = Foot()
        self.right_foot = Foot()
        self.left_leg = Leg(self.left_foot, is_right=False)
        self.right_leg = Leg(self.right_foot, is_right=True)
        
        # Torso que conecta todo
        self.torso = Torso(
            head=self.head,
            left_arm=self.left_arm,
            right_arm=self.right_arm,
            left_leg=self.left_leg,
            right_leg=self.right_leg
        )
    
    def describe(self):
        print(f"\nDescripción de {self.name}:")
        print(f"- Tiene {self.head.eyes} ojos y {self.head.ears} orejas.")
        print(f"- Cada mano tiene {self.left_hand.fingers} dedos.")
        print("- Mano derecha" if self.right_hand.is_right else "- Mano izquierda")
        print("- Mano izquierda" if not self.left_hand.is_right else "- Mano derecha")
        print(f"- Cada pie tiene {self.left_foot.toes} dedos.")
        print(f"- Órganos en el torso: {', '.join(self.torso.organs)}")

# Ejemplo de uso
if __name__ == "__main__":
    john = Human("John Doe")
    john.describe()