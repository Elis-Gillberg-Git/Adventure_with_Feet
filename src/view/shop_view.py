from component.shop import gold

rich = False
Poor = True

def intro_shop():
    return "Lampolja, rep, bomber? Vill du ha det? Då är det ditt, min vän. Så länge du har tillräckligt med guld."

def cahs_counter(gold):
    return "du har "f"{gold}"

def shoping_response(name):
    if rich == True:
        return "Tack för köpet, kom gärna tillbacka",
    elif Poor == True:
        return "Tyvärr, "f"{name}",", jag kan inte ge dig kredit! Kom tillbaka när du är lite mmmm rikare.",
    elif Poor == False and rich == False:
        return"",
