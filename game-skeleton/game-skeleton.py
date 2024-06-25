class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def move(self, direction):
        # Code to move the player to a new room based on direction
        pass
    
    def take_item(self, item):
        # Code to add item to player's inventory
        pass
    
    def use_item(self, item):
        # Code to use item (if applicable)
        pass
    
    def __str__(self):
        return f"Player {self.name} is in {self.current_room}"

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room
    
    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Create rooms
kitchen = Room("Kitchen", "A bright and airy kitchen.")
bedroom = Room("Bedroom", "A cozy bedroom with a large bed.")
garden = Room("Garden", "A lush garden with blooming flowers.")

# Define room exits
kitchen.add_exit("north", garden)
garden.add_exit("south", kitchen)
bedroom.add_exit("east", kitchen)
kitchen.add_exit("west", bedroom)

# Create items
knife = Item("Knife", "A sharp kitchen knife.")
key = Item("Key", "An old rusty key.")

# Add items to rooms
kitchen.add_item(knife)
bedroom.add_item(key)

# Initialize player
player_name = input("Enter your name: ")
player = Player(player_name, kitchen)

# Main game loop
while True:
    print(player.current_room.name)
    print(player.current_room.description)
    print("Exits:", list(player.current_room.exits.keys()))
    
    command = input("Enter command (e.g., 'go north', 'take item'): ").strip().lower().split()
    
    if command[0] == "go":
        direction = command[1]
        if direction in player.current_room.exits:
            player.move(direction)
        else:
            print("You cannot go that way.")
    
    elif command[0] == "take":
        item_name = " ".join(command[1:])
        # Check if item exists in current room
        # Add item to player's inventory
        # Remove item from room
    
    # Implement other commands as needed (e.g., use, inspect, quit)
