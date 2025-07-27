# Create a class 'Programmer' for storing information of few programmers working at Microsoft.

class Programmer:
    def __init__(self, name, language, role):
        self.name = name
        self.language = language
        self.role = role

harry = Programmer('Harry', 'JS', 'Frontend Dev') # Programmer Harry
fahad = Programmer('Fahad', 'C++', 'OS Dev') # Programmer Fahad
zohaib = Programmer('Zohaib', 'Python', 'Data Scientist') # Programmer Zohaib

print(f'Name = {harry.name}\n\tLanguage = {harry.language}\n\tRole = {harry.role}')
print('')
print(f'Name = {fahad.name}\n\tLanguage = {fahad.language}\n\tRole = {fahad.role}')
print('')
print(f'Name = {zohaib.name}\n\tLanguage = {zohaib.language}\n\tRole = {zohaib.role}')
