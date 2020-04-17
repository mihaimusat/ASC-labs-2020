import os, os.path

"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""

RECIPES_FOLDER = "recipes"

def parse_recipes():
    if not os.path.exists(RECIPES_FOLDER):
        print("Error: Recipes folder does not exist")
    elif not os.path.isdir(RECIPES_FOLDER):
        print("Error: Given path is not a folder")
    else:
        recipes = {}
        for file in os.listdir(RECIPES_FOLDER):
            (name, resources) = parse_input(RECIPES_FOLDER + "/" + file)
            recipes[name] = resources
        return recipes

def parse_input(filename):
    coffee_recipe = {}
    with open(filename, 'r') as f:
        coffee_type = f.readline().strip()
        for line in f.readlines():
            tokens = line.split("=")
            coffee_recipe[tokens[0]] = int(tokens[1].strip())
    return coffee_type, coffee_recipe