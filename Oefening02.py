# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit
# Test hier bovenstaande functies uit (zie opgave voor meer detail)

def filter_misses_postcode(dict_missen, pc1, pc2):
    list_misses = []
    for naam, postcode in dict_missen.items():
     if pc1 <= postcode <= pc2:
         list_misses.append(naam)
    return list_misses

misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}

postcode1 = int(input("geef de kleinste postcode op: "))
postcode2 = int(input("geef de grootste postcode op: "))

antwoord = filter_misses_postcode(misses_2018, postcode1, postcode2)
print(f"Dit zijn de gevonden missen uit 2018: {antwoord}")

antwoord = filter_misses_postcode(misses_2019, postcode1, postcode2)
print(f"Dit zijn de gevonden missen uit 2019: {antwoord}")