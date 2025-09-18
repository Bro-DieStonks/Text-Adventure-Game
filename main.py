from room import Room
from character import Enemy
from item import Item
from RPG_Info import RPGinfo

alive = False
boss = False
stage = 1
escape_rooms = None
Escape_sequence = None

Evil_Mining_Corp = RPGinfo('Evil Mining Corp')
Evil_Mining_Corp.welcome()
RPGinfo.info()
RPGinfo.credits()

player_name = input('What is your name? ')
alive = True

entrance_chamber = Room("Entrance Chamber") # this is an instance of a room called "Entrance Chamber"
escape_hatch = Room('Escape Hatch')
vents = Room("Vents")
hallway = Room("Hallway")
meeting_room = Room('Meeting Room')
storage_compartment = Room('Storage Compartment')
prison = Room('Prison')
security_room = Room('Security Room')
boss_chamber = Room('Boss Chamber')


escape_hatch.set_description(None)
entrance_chamber.set_description('A vast open room with a giant sign that reads "Evil Mining Corp"')
vents.set_description('Tight dark vents. The air is thin, and it smells of dust')
hallway.set_description('A long dark ominous hallway. You sense you are being watched.')
meeting_room.set_description('A large table stands in the center of the room. Multiple chairs are toppled over, signifying some form of struggle.')
storage_compartment.set_description('Piles of crates fill the room. Cobweds are strung from the dark corners. It seems like this place isnt well taken care of.')
prison.set_description('Rows of cells line the room, water leaking from the roof above you. You spot a shadow in the back corner. Do you investigate?')
security_room.set_description('A large computer stands on a desk in the center of the room. You approch the computer with caution as the computer flashes on, displaying a screen that says "Enter PASSWORD to begin"')
boss_chamber.set_description("A large figure stands in the center, guarding Danile. You're almost there")


escape_hatch.link_room(entrance_chamber, 'east')
entrance_chamber.link_room(hallway, 'east')
entrance_chamber.link_room(escape_hatch, 'west')
hallway.link_room(entrance_chamber, 'west')
hallway.link_room(storage_compartment, 'east')
hallway.link_room(vents, 'north')
storage_compartment.link_room(hallway, 'west')
storage_compartment.link_room(meeting_room, 'north')
storage_compartment.link_room(prison, 'south')
prison.link_room(storage_compartment, 'north')
vents.link_room(hallway, 'south')
vents.link_room(meeting_room, 'east')
meeting_room.link_room(vents, 'west')
meeting_room.link_room(storage_compartment, 'south')
meeting_room.link_room(security_room, 'north')
meeting_room.link_room(boss_chamber, 'east')
security_room.link_room(meeting_room, 'south')
boss_chamber.link_room(meeting_room, 'west')

sawblade = Item()
sawblade.set_name('Rusted Sawblade')
sawblade.set_description('A rusty sawblade. It seems old and broken but maybe could be put to use one more time')


screwdriver = Item()
screwdriver.set_name("George's Screwdriver")
screwdriver.set_description("An old screwdriver given to you by George. Could be useful for opening something.")

key = Item()
key.set_name('Meeting Room Key')
key.set_description('The key to the meeting room. You can open a shortcut back to the storage compartment with this.')
meeting_room.set_item(key)

sword = Item()
sword.set_name('Sword of 1000 Elements')
sword.set_description('An ancient sword spoken only through legend. How did the Evil Mining Corp get their hands on it?')



george = Enemy('George', 'A lonely prisoner')
george.set_conversation(f'Hello there {player_name}. Will you please help me out of this cell? I have an item you might find of use... You will? Alright, head back to the storage room and search for something that can break these cell bars.')
george.set_questComplete('Ahh there we go, free at last! Here, as promised, this screwdriver.')
george.set_weakness(None)
prison.set_character(george)

boss = Enemy('Garonell', 'The Boss of Evil Mining Corp')
boss.set_weakness('Water')
boss_chamber.set_character(boss)

meeting_room.lock()
vents.lock()
boss_chamber.lock()
escape_hatch.lock()

current_room = security_room
inventory = []

while alive == True:
   

    if current_room == vents or 'Meeting Room Key' in inventory:
        meeting_room.unlock()
    else:
        meeting_room.lock()

    print('\n')
    current_room.get_details()
    if boss_chamber.character == None:
        print(f'You have {escape_rooms} moves to escape')
    
    inhabitant = current_room.get_character()
    if inhabitant:
        inhabitant.describe()
    room_item = current_room.get_item()
    if room_item:
        room_item.describe()

    
    if current_room == boss_chamber:
        boss = True
    
        if boss == True:
            inhabitant = current_room.get_character
            print('The boss turn a blazing red colour. What element will you set the sword to?')
            fight_with = input('>> ')
            if fight_with in ['water', 'Water']:
                stage += 1
                print('The boss falls to the ground but quickly gets back up. The boss turns a bright green colour')
            else:
                    print('The boss laughs at your feeble attempt to damage him, striking back with blazinng speed catching you off guard. Your conciousness slowly fades away as two guards appear and take you away.')
                    current_room.set_character(None)
                    alive = False
            if stage == 2:
                print('What element will you set the sword to?')
                fight_with = input('>>')
                if fight_with in ['fire', 'Fire']:
                    stage += 1
                    print('The boss screams in pain at the flames. Hes getting weaker. The boss turns a dark blue colour')
                else:
                    print('The boss laughs at your feeble attempt to damage him, striking back with blazinng speed catching you off guard. Your conciousness slowly fades away as two guards appear and take you away.')
                    current_room.set_character(None)
                    alive = False
            if stage == 3:
                print('What element will you set the sword to?')
                fight_with = input('>>')
                if fight_with in ['earth', 'Earth']:
                    print('Giant rocks come up from the earth, impaling the boss from below.')
                    print('You quickly rush to save Danile as the building begins to shake. You need to get out')
                    current_room.set_character(None)
                    print('\n')
                    current_room.get_details()
                    escape_rooms = 5
                    print(f'You have {escape_rooms} moves to escape')
                    Escape_sequence = True
                    escape_hatch.unlock()
                else:
                    print('The boss laughs at your feeble attempt to damage him, striking back with blazinng speed catching you off guard. Your conciousness slowly fades away as two guards appear and take you away.')
                    current_room.set_character(None)
                    alive = False
    

    command = input('>>')

    if command in ['north', 'south', 'east', 'west']:
        current_room = current_room.move(command)
        if Escape_sequence == True:
            escape_rooms -= 1
    elif command == 'talk':
        if inhabitant:
            inhabitant.talk()
            if current_room.character == george:
                storage_compartment.set_item(sawblade)
        

        else:
            print("There's nobody around")
    elif command == 'fight':
        if inhabitant:
            print('What will you fight with')
            fight_with = input('>> ')
        if inhabitant.fight(fight_with):
             current_room.set_character(None)
        elif fight_with != inhabitant.weakness:
            alive = False
        else:
            print('There is noone here to fight')
    elif command == 'grab':
        if room_item:
            print(f'You pick up {current_room.item.name}')
            inventory.append(current_room.item.name)
            current_room.set_item(None)
    elif command == 'inventory':
        print (f'{inventory}')       
    elif command == 'use':
        if "George's Screwdriver" in inventory and current_room == hallway:
            vents.unlock()
            print('You unlock the vents')
        elif "Rusted Sawblade" in inventory and current_room == prison:
            if inhabitant:
                inhabitant.complete()
                current_room.set_item(screwdriver)
        elif "Meeting Room Key" in inventory and current_room == meeting_room:
            meeting_room.unlock()
            storage_compartment.unlock()
            print('You unlock the door. Now you can make it to your hiding spot in case of emergancy')
        else:
            print('But there was nothing to use')
    elif command in ['password' , 'PASSWORD' , 'Password'] and current_room == security_room:
        print('The screen changes to display 3 questions')
        print('1. "How many rooms are there in this facility?"')
        print('2. How many letters does our only prisoners name have?')
        print('3. How many items have you currently collected')
        password = input('>>')
        if password == '863':
            print('The screens lights up green displaying text that reads "Access Granted". A large pedestal emerges from the left of the room.')
            current_room.set_item(sword)
            boss_chamber.unlock()
        elif password != '863':
            print('The screen flashes red, diplaying text that reads "Access Denied"')
    elif command == 'help':
        print('Commands: north, south, east, west, talk, grab, use, fight, (only in security room - password), (only in boss - fire, water, earth)')
    else:
        print('Look at this idiot, they cant spell')

    if current_room == escape_hatch:
        print('You and Danile jump out of the escape hatch just as the building self destructs, You Won!')
        alive = False

    if escape_rooms == 0:
     alive = False

RPGinfo.author = 'Brodie' 
RPGinfo.credits()





#Best route through the game
#east, east, south, talk, north, grab, south, use, grab, north, west, use, north, east, grab, north, password, 863, grab, south, east, water, fire, earth, west, west, south, west, west