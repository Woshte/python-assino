# Define the Supe class
class Supe:
    def __init__(self, name, city):
        self.name = name   # Instance variable
        self.city = city   # Instance variable
    
    def display_info(self):
        return f"{self.name} from {self.city}"

# Subclass inheriting from Supe
class Others(Supe):
    def display_info(self):  # Method overriding for polymorphism
        return f"{self.name} is an antagonist from {self.city}"

# Creating objects with unique attributes
Hero1 = Supe("Batman", "Gotham")
Hero2 = Supe("Superman", "Metropolis")
Villain = Others("Joker", "Gotham")

# Print attributes
print(Hero1.name)  # Output: Batman
print(Hero2.city)  # Output: Metropolis
print(Villain.name)  # Output: Joker

# Demonstrate polymorphism with method overriding
for DC in [Hero1, Hero2, Villain]:
    print(DC.display_info())
