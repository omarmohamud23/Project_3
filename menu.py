
class Menu:

     #initialize options and functions 
    def __init__(self):
        self.menu_options = {}
        self.functions = {}
  
    #Adding the option 
    def add_option(self, key, description, function):
        self.menu_options[key] = description
        self.functions[key] = function

    #Checking where the option is valid 
    def is_valid(self, choice):
        return choice in self.menu_options

    #Getting action from the function 
    def get_action(self, choice):
        return self.functions.get(choice)

    #Displays the options 
    def __str__(self):
        texts = [f'{key}: {self.menu_options[key]}' for key in self.menu_options.keys()]
        return '\n'.join(texts)