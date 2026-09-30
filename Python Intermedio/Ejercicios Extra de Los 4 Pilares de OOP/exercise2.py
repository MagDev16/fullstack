from abc import ABC, abstractmethod

class User(ABC):
    
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def get_role(self) -> str:
        pass
    
    @abstractmethod
    def has_permission(self, permission: str) -> bool:
        pass
    
class AdminUser(User):
    def get_role(self):
        return "Admin"
    
    def has_permission(self, permission):
        return True
    
class RegularUser(User):
    def get_role(self):
        return "Regular"
    
    def has_permission(self, permission):
        return False

# --- Caso de Uso --- #
if __name__ == "__main__":
    user1 = AdminUser("Manuel")
    user2 = RegularUser("Agustin")

print(user1.has_permission("delete")) 
print(user2.has_permission("delete"))