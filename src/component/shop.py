def gold():
    gold = 20,

def lampoil():
    if gold >= 5:
        lampoil = True,
        gold -= 5
        rich = True,
        poor = False,   
    elif gold < 5:
        poor = True,  
        rich = False,

def rope():
    if gold >= 10:
        lampoil = True,
        gold -= 10
        rich = True, 
        poor = False,   
    elif gold < 10:
        poor = True,  
        rich = False,

def bomb():
    if gold >= 20:
        lampoil = True,
        gold -= 20
        rich = True,
        poor = False,   
    elif gold < 20:
        poor = True,  
        rich = False,

