# NPC Randomiser

This is a randomiser for Dungeon Masters to create quick NPCs on the fly. It can be easily tweaked to change the rate of appearance for certain attributes, as well as add new attributes into the mix. 

Randomised NPCs will be generated on run. Here's some examples:
```
Gender: Male
Class: Warlock
Race: Gnome
Name: Kellen
Attitude: Excitable
```

```
Gender: Female
Class: Druid
Race: Half-elf
Name: Nichele
Attitude: Anxious
```

```
Gender: Agender
Class: Ranger
Race: Human
Name: Letti
Attitude: Shy
```

```
Gender: Genderfluid
Class: Wizard
Race: Dwarf
Name: Ulfgar
Attitude: Stoic
```

As a Dungeon Master, I regularly have trouble thinking up character names and traits on the fly, and it's *always* coming up. I hope this tool helps to prevent creating stereotypical/flat characters and makes running games a whole lot easier.

# Installation
Ensure you have [Python 3](https://www.python.org/downloads/) installed on your computer.

This program can be run via Python or any Terminal interfacing software.

# Changing Values
You can easily [modify the .py](#modify-the-python-file) to add, change or remove:
- Genders
- Classes
- Races

Or [modify the .txt](#modify-the-text-files) files to add, change or remove:
- Names
- Attributes (i.e. personality)

## Modify the Python file
1. Open [npcRandomiser.py](https://github.com/buhains/NPC-Randomiser/blob/main/npcRandomiser.py) in your code/text editing software.
2. Scroll down to the `def` function that covers the trait you want to modify, e.g. `def races():`.
3. Underneath, you should see a dictionary starting with `trait = {` e.g. `races = {`

**Adding a new trait**
1. To add a new type for this trait, copy one of the lines e.g. `"None":4`. 
2. Press enter to add a new line underneath.
3. Ensure there is a comma (`,`) at the end of the line.

**Modifying a trait**
- Change type: Replace the value within the quotation marks (`"`) to the new type you want to add e.g. `"Warforged"`.
- Change probability: Replace the number with the proportion you want this type to appear. Ensure there is still a comma (`,`) at the end of the number.
    - `1`: I want this type to appear at a normal amount.
    - `2`: I want this type to appear twice as much as other types.
    - `0.5`: I want this type to appear half as much as other types.
    - So on and so forth.

**Removing a trait**

Delete the entire line, including the comma. 

## Modify the Text files
Open the folder of the trait you want to change the randomisation pool for. Within, there are .txt files pertaining to the different pools the program can pull from.
- If adding a new .txt file, make sure it is named with the following convention: **race**_**gender**.txt
- If modifying a .txt file, make sure to leave no empty lines at the end or in the middle of the list.
- If deleting a .txt file, please make sure that it is not possible to get this gender and race combination as a result.
If the Gender and Race still exist in the .py dictionaries, this may result in an error.