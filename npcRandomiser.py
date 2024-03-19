import random
import codecs

# Traits:
## Add more types of a trait by copying one line and replacing the values.
## The numerical value = the likelihood of this trait appearing (in proportion to others listed). See readme.md for more details.

genders = {  
    "Female": 1,
    "Male": 1,
    "Genderfluid": 1,
    "Agender": 1
}

classes = {
    "None": 4,
    "Fighter (Sword User)": 2,
    "Barbarian": 1,
    "Bard": 1,
    "Cleric": 1,
    "Druid": 1,
    "Fighter (Archer)": 1,
    "Monk": 1,
    "Paladin": 1,
    "Ranger": 1,
    "Rogue": 1,
    "Sorcerer": 1,
    "Warlock": 1,
    "Wizard": 1,
    "Artificer": 1,
    "Blood Hunter": 1
}

races = {
    "Human": 3,
    "Elf": 1,
    "Dwarf": 1,
    "Halfling": 1,
    "Gnome": 1,
    "Tiefling": 1,
    "Half-elf": 1,
    "Drow": 0.5,
    "Half-orc": 0.5,
    "Dragonborn": 0.5,
    "Aasimar": 0.1,
    "Changeling": 0.1,
    "Yuan-ti": 0.1,
    "Merfolk": 0.1,
    "Genasi": 0.1
}

def main():
    gender = random_weights(genders)
    race = random_weights(races)
    print("Name:", names(gender,race))
    print("Gender:", gender)
    print("Class:", random_weights(classes))
    print("Race:", race)
    print("Attitude:", attitudes())

def names(gender,race):
    # Checks if character is non-binary to use All Genders list
    if gender == "Genderfluid" or gender == "Agender":
        gender = "All"

    # Checks if character is Drow to use the Elf list
    if race == "Drow":
        race = "Elf"

    # Checks if character is Half-elf or Aasimar to use the Human list
    elif race == "Half-elf" or race == "Aasimar":
        race = "Human"

    # Checks if character is part of gender-neutral race names list:
    if race == "Changeling" or race == "Genasi" or race == "Yuan-ti":
        file_name = str(f"names/{race}.txt").lower()
        
    else:
        file_name = str(f"names/{race}_{gender}.txt").lower()

    f = codecs.open(file_name,"r",encoding="utf=8")
    name_list = f.readlines()
    name = random.choice(name_list).replace("\n","")
    return name

def attitudes():
    f = codecs.open("attitudes/attitudes.txt","r",encoding="utf=8")
    attitudes = f.readlines()
    attitude = random.choice(attitudes)
    return attitude

def random_weights(property_to_weight: dict[str, float]) -> str:
    properties = list(property_to_weight.keys())
    weights = list(property_to_weight.values())
    return random.choices(properties, weights)[0]

if __name__ == "__main__":
    main()
