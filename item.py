class Item():
    def __init__(self):
        self.name = None
        self.description = None
        self.visible = False
    
    def describe(self):
        print( "There is " + self.name + " in the room")
        print( self.description )

    def set_name(self, name_to_set):
        self.name = name_to_set

    def set_description(self, description_to_set):
        self.description = description_to_set

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def hide(self):
        self.visible = False
    
    def show(self):
        self.visible = True
    
    def get_details(self):
        print(f"""{self.name}
{"-"*len(self.name)}
{self.description if self.description else ''}
""")

if __name__ == "__main__":
    sword = Item()
    sword.set_name("Green Sword of Agnor")
    sword.set_description("A glistening green blade with one sharp edge and a gentle curve")

    sword.get_details()