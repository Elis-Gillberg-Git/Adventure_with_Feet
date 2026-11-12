def lampoil(name):
    if gold >= 5:
        lampoil = True,
        rich = True,
        poor = False,   
    elif gold < 5:
        poor = True,  
        rich = False,

def rope():
    if gold >= 10:
        lampoil = True,
        rich = True, 
        poor = False,   
    elif gold < 10:
        poor = True,  
        rich = False,

def bomb():
    if gold >= 20:
        lampoil = True,
        rich = True,
        poor = False,   
    elif gold < 20:
        poor = True,  
        rich = False,

def poor_hero():
    return "Tyvärr, "f"{name}",", jag kan inte ge dig kredit! Kom tillbaka när du är lite mmmm rikare.",

def hero_buy():
    return "Tack för köpet, kom gärna tillbacka"