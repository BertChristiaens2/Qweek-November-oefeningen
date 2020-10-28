# Er geldt dat:
# •West-Vlaanderen: postcodes tussen 8000-8999
# •Oost-Vlaanderen: postcodes tussen 9000-9999
# •Antwerpen: postcodes tussen 2000-2999
# •Limburg: postcodes tussen 3500-3999
# •Vlaams-Brabant: postcodes tussen 1500-1999 en 3000-3499

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
    
pc = int(input("geef een postcode op: "))
print(f"De postcode {pc} ligt in de provincie {geef_provincie(pc)}")
