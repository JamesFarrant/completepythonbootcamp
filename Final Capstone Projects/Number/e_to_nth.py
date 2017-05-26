from math import e

def e_to_nth(places):
    if places <= 20:
        print round(e, places)
    else:
        return None

e_to_nth(9)
