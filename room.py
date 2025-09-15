class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}  # this is a dictionary to hold the rooms that are next to this room
        self.character = None
        self.item = None
        self.locked = False
    
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def set_character(self, room_character):
        self.character = room_character
    
    def set_item(self, room_item):
        self.item = room_item

    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.item
    
    def lock(self):
        self.locked = True
    
    def unlock(self):
        self.locked = False

    def describe(self):
        print(self.description)
        for direction in self.linked_rooms:
            print(f'{self.linked_rooms[direction].name} is to the {direction}')

    def get_details(self):
        print(self.name)
        print("="*len(self.name))
        self.describe()

    def link_room(self, room_to_link, direction):
        "add the room_to_link into the dictionary under the key direction"
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        "search through the direction in linked_rooms and return the room room in that direction"
        if direction in self.linked_rooms:
            if self.linked_rooms[direction].locked:
                print('You cant go that way, its locked')
                return self
            else:
                return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    

if __name__ == "__main__":
    # this conditional will only allow the code written here to be run if we run room.py
    # this is great for testing files
    kitchen = Room("Kitchen") # this is an instance of a room called "Kitchen"
    dining_room = Room('Dining Room')

    kitchen.set_description("A dark, dank room, that has lots of flies!!!") # This sets the description from None to the string provided.

    print(kitchen.name) # this line calls the name attribute
    print("-----------------------")
    # print(kitchen.get_description()) # this line calls the get_description method

    kitchen.link_room(dining_room, 'south') # this is add "south": dining_hall to the dictionary linked_rooms
    kitchen.describe()