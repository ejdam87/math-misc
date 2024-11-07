import constraint as csp

people = [ "a", "e", "d", "s", "b" ]

preferences = {
    "a": ["t", "d1", "d2", "h1", "h2"],
    "e": ["t", "d1", "d2", "h1", "h2"],
    "d": ["t", "d1", "d2", "h1", "h2"],
    "s": ["t", "d1", "d2", "h1", "h2"],
    "b": ["t", "d1", "d2", "h1", "h2"]
}

p = csp.Problem()
for person, prefs in preferences.items():
    p.addVariable( person, prefs )

p.addConstraint(csp.AllDifferentConstraint())

def get_probs(assignments: dict[ str, str ], person: str) -> dict[ str, float ]:

    healer_count = 0
    dps_count = 0
    tank_count = 0

    total = len(assignments)

    for assignment in assignments:
        if assignment[person] in ["h1", "h2"]:
            healer_count += 1
        elif assignment[person] in ["d1", "d2"]:
            dps_count += 1
        else:
            tank_count += 1

    return {
        "healer": healer_count / total,
        "dps"   : dps_count    / total,
        "tank"  : tank_count   / total
    }

print( get_probs( p.getSolutions(), "a" ) )
