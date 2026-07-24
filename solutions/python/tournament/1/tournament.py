def tally(rows):
    teams = {}
    for row in rows:
        team1, team2, result = row.split(";")
        if team1 not in teams:
            teams[team1] = {"W": 0, "D": 0, "L": 0, "P": 0, "MP": 0}
        if team2 not in teams:
            teams[team2] = {"W": 0, "D": 0, "L": 0, "P": 0, "MP": 0}
        if result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1
            teams[team2]["MP"] += 1
            teams[team1]["MP"] += 1
            
        elif result == "loss":
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
            teams[team1]["L"] += 1
            teams[team2]["MP"] += 1
            teams[team1]["MP"] += 1
        elif result == "draw":
            teams[team2]["D"] += 1
            teams[team1]["D"] += 1
            teams[team2]["MP"] += 1
            teams[team1]["MP"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1
    sortedteams = sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0]))
    header = "Team                           | MP |  W |  D |  L |  P"
    result = [header]
    for name, s in sortedteams:
        result.append(f"{name:<31s}|{s['MP']:3d} |{s['W']:3d} |{s['D']:3d} |{s['L']:3d} |{s['P']:3d}")
    return result