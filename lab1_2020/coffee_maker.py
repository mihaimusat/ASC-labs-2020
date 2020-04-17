import sys
import load_recipes

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
COMMANDS = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"
ALL = "all"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

# Coffee types
COFFEE_TYPES = {AMERICANO:{WATER:10, COFFEE:10, MILK:0},
                CAPPUCCINO:{WATER:5, COFFEE:10, MILK:10},
                ESPRESSO:{WATER:5, COFFEE:10, MILK:0}}

def check_res(coffee_type):
    for res in RESOURCES:
        if RESOURCES[res] < COFFEE_TYPES[coffee_type][res]:
            return False
    return True

def make(coffee_type):
    if coffee_type not in COFFEE_TYPES.keys():
        print("Error: Unknown coffee type")
        return
    else:
        if check_res(coffee_type):
            for res in RESOURCES:
                RESOURCES[res] -= COFFEE_TYPES[coffee_type][res]
        print("Here is your %s!" % (coffee_type))

def refill(resource_type):
    if resource_type not in RESOURCES.keys() and resource_type != ALL:
        print("Error: Unknown resource")
    else:
        if resource_type == ALL:
            for res in RESOURCES:
                RESOURCES[res] = 100
        else:
            RESOURCES[resource_type] = 100

def main():
    print("I'm a smart coffee maker")
    while(True):
        print("Enter command:")
        cmd = sys.stdin.readline().strip()
        if cmd not in COMMANDS:
            print("Error: Unknown command")
            return
        else:
            if cmd == LIST_COFFEES:
                result = tuple(COFFEE_TYPES.keys())
                print(result)
            elif cmd == RESOURCE_STATUS:
                for resource in RESOURCES:
                    print("{}: {}%".format(resource, RESOURCES[resource]))
            elif cmd == MAKE_COFFEE:
                print("Which coffee?")
                coffee_type = sys.stdin.readline().strip().lower()
                make(coffee_type)
            elif cmd == REFILL:
                print("Which resource? Type 'all' for refilling everything")
                resource_type = sys.stdin.readline().strip().lower()
                refill(resource_type)
            elif cmd == HELP:
                print("You can use one of the following commands:")
                print(COMMANDS)
            elif cmd == EXIT or cmd == "":
                break

if __name__ == "__main__":
    main()
