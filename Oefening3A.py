# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit
# Test hier bovenstaande functies uit (zie opgave voor meer detail)

def geef_provincie(postcode):
    
    provincie = ""

    if 8000 <= postcode <= 8999:
        provincie = "West-Vlaanderen"
        return "wvl"
    elif postcode in range(9000,10000):
        return "ovl"
    elif postcode in range (2000,3000):
        return "Antwerpen"
    elif postcode in range (3500,4000):
        return "limburg"
    elif postcode in range (1500,2000) or postcode in range (3000,3500):
        return "vlaams brabant"
    else: 
        return "onbekend"

def geef_aantal(dict_missen):
    dict_aantal = {}
    for postcode in dict_missen.values():
        provincie = geef_provincie(postcode)
        #indien de pronvincie nog niet bestaat, aanmaken
        if not provincie in dict_aantal:
            dict_aantal[provincie] = 1
        #indien de provincie al bestaat +1
        else: 
            dict_aantal[provincie] += 1
    return dict_aantal


misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}

print(f"de missen met hun provincie uit 2018 zijn: {geef_aantal(misses_2018)}")
print(f"de missen met hun provincie uit 2019 zijn: {geef_aantal(misses_2019)}")