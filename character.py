class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_questComplete(self, quest_complete):
        self.questComplete = quest_complete
    
    def complete(self):
        if self.questComplete is not None:
            print(f'{self.questComplete}')
        

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def set_weakness(self, weakness_to_set):
        self.weakness = weakness_to_set

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f'You fend off {self.name} with the {self.weakness}')
            return True
       # elif self.weakness == None:
            print(f'{self.name} does not want to fight')  
            return False
        else:
            print("That isn't working, try something else")
            return False



if __name__ == "__main__":
    tenna = Enemy('Tenna', "a really sexy TV")
    tenna.set_conversation('IIIIIITS T V TIME!!!!')
    tenna.set_weakness('Glooby People')
    tenna.describe()
    tenna.talk()
    print('What will you fight Tenna with?')
    wpn = input(">>")
    tenna.fight(wpn)