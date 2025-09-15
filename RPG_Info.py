class RPGinfo():
    author = "Brodie Stokes"

    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print(f'Welcome to {self.title}. Use "help" for commands')
    
    @staticmethod
    def info():
        print('Made useimg the OOP RPG Game Creator')

    @classmethod
    def credits(cls):
        print('Thanks you for playing')
        print(f'Created by {cls.author}. ')