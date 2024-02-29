import random

def main():
    gender = genders()
    race = races()
    print("Gender:", gender)
    print("Class:", classes())
    print("Race:", race)
    print("Name:", names(gender,race))
    print("Attitude:", attitudes())

def genders():
    genders = [  # Add more potential randomised values by copying one line and replacing the values in "quotes".
        # lower_limit and upper_limit control percentage chance to appear. In the below example, each gender has a 25% chance to appear.
        {"gender": "Female", "lower_limit":"0", "upper_limit":"0.25"},  
        {"gender": "Genderfluid", "lower_limit":"0.25", "upper_limit":"0.5"},
        {"gender": "Agender", "lower_limit":"0.5", "upper_limit":"0.75"},
        {"gender": "Male", "lower_limit":"0.75", "upper_limit":"1"}
    ]
    
    genderRandom = random.random()
    for gender in genders:
        lower_limit = float(gender["lower_limit"])
        upper_limit = float(gender["upper_limit"])
        if lower_limit < genderRandom <= upper_limit:
            return(gender["gender"])
        else:
            continue

def classes():
    classes = [
        {"class": None, "lower_limit":"0", "upper_limit":"0.2"},
        {"class": "Barbarian", "lower_limit":"0.2", "upper_limit":"0.25"},
        {"class": "Bard", "lower_limit":"0.25", "upper_limit":"0.3"},
        {"class": "Cleric", "lower_limit":"0.3", "upper_limit":"0.35"},
        {"class": "Druid", "lower_limit":"0.35", "upper_limit":"0.4"},
        {"class": "Fighter (Archer)", "lower_limit":"0.4", "upper_limit":"0.45"},
        {"class": "Monk", "lower_limit":"0.45", "upper_limit":"0.5"},
        {"class": "Paladin", "lower_limit":"0.5", "upper_limit":"0.55"},
        {"class": "Ranger", "lower_limit":"0.55", "upper_limit":"0.6"},
        {"class": "Rogue", "lower_limit":"0.6", "upper_limit":"0.65"},
        {"class": "Sorcerer", "lower_limit":"0.65", "upper_limit":"0.7"},
        {"class": "Warlock", "lower_limit":"0.7", "upper_limit":"0.75"},
        {"class": "Wizard", "lower_limit":"0.75", "upper_limit":"0.8"},
        {"class": "Artificer", "lower_limit":"0.8", "upper_limit":"0.85"},
        {"class": "Blood Hunter", "lower_limit":"0.85", "upper_limit":"0.9"},
        {"class": "Fighter (Sword User)", "lower_limit":"0.9", "upper_limit":"1"}
    ]
    
    classRandom = random.random()
    for job in classes:
        lower_limit = float(job["lower_limit"])
        upper_limit = float(job["upper_limit"])
        if lower_limit < classRandom <= upper_limit:
            return job["class"]
        else:
            continue

def races():
    
    races = [
        {"race": "Human", "lower_limit": "0", "upper_limit":"0.3"},
        {"race": "Elf", "lower_limit":"0.3", "upper_limit":"0.4"},
        {"race": "Dwarf", "lower_limit":"0.3", "upper_limit":"0.4"},
        {"race": "Halfling", "lower_limit":"0.4", "upper_limit":"0.5"},
        {"race": "Gnome", "lower_limit":"0.5", "upper_limit":"0.6"},
        {"race": "Tiefling", "lower_limit":"0.6", "upper_limit":"0.7"},
        {"race": "Half-elf", "lower_limit":"0.7", "upper_limit":"0.8"},
        {"race": "Drow", "lower_limit":"0.8", "upper_limit":"0.85"},
        {"race": "Half-orc", "lower_limit":"0.85", "upper_limit":"0.9"},
        {"race": "Dragonborn", "lower_limit":"0.9", "upper_limit":"0.95"},
        {"race": "Aasimar", "lower_limit":"0.95", "upper_limit":"0.96"},
        {"race": "Changeling", "lower_limit":"0.96", "upper_limit":"0.97"},
        {"race": "Yuan-ti", "lower_limit":"0.97", "upper_limit":"0.98"},
        {"race": "Merfolk", "lower_limit":"0.98", "upper_limit":"0.99"},
        {"race": "Genasi", "lower_limit":"0.99", "upper_limit":"1"}
    ]
    
    raceRandom = random.random()

    for race in races:
        lower_limit = float(race["lower_limit"])
        upper_limit = float(race["upper_limit"])
        if lower_limit < raceRandom <= upper_limit:
            return race["race"]
        else:
            continue

def names(gender,race):
    match race:
        
        case "Elf" | "Drow":
            if gender == "Female":
                name_list = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]
            elif gender == "Male":
                name_list = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
            else:
                name_list = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia", "Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
            
        case "Dwarf":
            if gender == "Female":
                name_list = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
            elif gender == "Male":
                name_list = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
            else:
                name_list = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra", "Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
            
        case "Halfling":
            if gender == "Female":
                name_list = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
            elif gender == "Male":
                name_list = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
            else:
                name_list = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby", "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
            
        case "Gnome":
            if gender == "Female":
                name_list = ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna"]
            elif gender == "Male":
                name_list = ["Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook"]
            else:
                name_list = ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna", "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook", "Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Ku", "Nim", "Oneshoe", "Pock", "Sparklegem", "Stumbleduck"]
        
        case "Tiefling":
            if gender == "Female":
                name_list = ["Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia", "Orianna", "Phelaia", "Rieta", "Art", "Carrion", "Chant", "Creed", "Despair", "Excellence", "Fear", "Glory", "Hope", "Ideal", "Music", "Nowhere", "Open", "Poetry", "Quest", "Random", "Reverence", "Sorrow", "Temerity", "Torment", "Weary"]
            elif gender == "Male":
                name_list = ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai", "Morthos", "Pelaios", "Skamos", "Therai", "Art", "Carrion", "Chant", "Creed", "Despair", "Excellence", "Fear", "Glory", "Hope", "Ideal", "Music", "Nowhere", "Open", "Poetry", "Quest", "Random", "Reverence", "Sorrow", "Temerity", "Torment", "Weary"]
            else:
                name_list = ["Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia", "Orianna", "Phelaia", "Rieta", "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai", "Morthos", "Pelaios", "Skamos", "Therai", "Art", "Carrion", "Chant", "Creed", "Despair", "Excellence", "Fear", "Glory", "Hope", "Ideal", "Music", "Nowhere", "Open", "Poetry", "Quest", "Random", "Reverence", "Sorrow", "Temerity", "Torment", "Weary"]
        
        case "Half-orc":
            if gender == "Female":
                name_list = ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"]
            elif gender == "Male":
                name_list = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk"]
            else:
                name_list = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk", "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"]
        
        case "Dragonborn":
            name_list = ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn", "Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"]
        
        case "Changeling":
            name_list = ["Aunn", "Bin", "Cas", "Dox", "Hars", "Mas", "Nix", "Ot", "Paik", "Sim", "Vil", "Yug"]
        
        case "Yuan-ti":
            name_list = ["Asutali", "Eztli", "Hessatal", "Hitotee", "Issahu", "Itstli", "Izsashi", "Manuya", "Meztli", "Nesalli", "Otleh", "Shalkashlah", "Sisava", "Sitlali", "Soakosh", "Shossuzill", "Orshuss", "Ssimalli", "Suisatal", "Talash", "Ushrashi", "Teoshi", "Yaotal", "Yasstuss", "Zihu", "Zhehshu"]
        
        case "Merfolk":
            name_list = ["Tertis", "Anchor", "Reif", "Aquarius", "Trenton", "Peleck", "Agual", "Naga", "Barracudon", "Caspian", "Pacifica", "Marinna", "Adreanna", "Raina", "Noelani", "Sarmisira", "Miste", "Lausanne", "Hali"]
        
        case "Genasi":
            name_list = ["Soot", "Phoenix", "Flow", "Mason", "Whistle", "Basin", "Granite", "Amethyst", "Cyclone", "Dantean", "Storm", "Azure", "Kindle", "Wither", "Onyx", "Garnet", "River", "Aeolus", "Gale"]
        
        case _:
            if gender == "Female":
                name_list = ["Ruthiva", "Yara", "Karlote", "Yenta", "Diantha", "Bella", "Aria", "Enz", "Cereden", "Vorrmor", "Isphek", "Tori", "Kelvixa", "Malela", "Amrath", "Oldarane", "Maxil", "Nichele", "Sevandor", "Naois", "Cavosse", "Elyn", "Kyara", "Ravathene", "Nienra", "Asicia", "Rhylash", "Harobel", "Megwen", "Hauke", "Lys", "Letti", "Fernya", "Emyar"]
            elif gender == "Male":
                name_list = ["Jacksyn", "Ubbe", "Tyr", "Looth", "Dostaan", "Orissanat", "Oth", "Jalnio", "Stamos", "Shua", "Arne", "Rek", "Jarrow", "Macra", "Corem", "Myrrhne", "Rion", "Lucien", "Morvaen", "Olyver", "Jyden", "Kerce"]
            else:
                name_list = ["Jacksyn", "Ubbe", "Tyr", "Looth", "Dostaan", "Orissanat", "Oth", "Jalnio", "Stamos", "Shua", "Arne", "Rek", "Jarrow", "Macra", "Corem", "Myrrhne", "Rion", "Lucien", "Morvaen", "Olyver", "Jyden", "Kerce", "Ruthiva", "Yara", "Karlote", "Yenta", "Diantha", "Bella", "Aria", "Enz", "Cereden", "Vorrmor", "Isphek", "Tori", "Kelvixa", "Malela", "Amrath", "Oldarane", "Maxil", "Nichele", "Sevandor", "Naois", "Cavosse", "Elyn", "Kyara", "Ravathene", "Nienra", "Asicia", "Rhylash", "Harobel", "Megwen", "Hauke", "Lys", "Letti", "Fernya", "Emyar", "Kai", "Cleo", "Sage", "Casey"]
    return(random.choice(name_list))

def attitudes():
    attitudes = ["Mischievous", "Gentle", "Excitable", "Flirty", "Mysterious", "Dramatic", "Stoic", "Noble", "Rough", "Rude", "Terse", "Awkward", "Shy", "Naive", "Nerdy", "Anxious", "Type-A", "Chill", "Sinister"]
    attitude = random.choice(attitudes)
    return attitude

if __name__ == "__main__":
    main()