players = {}

while True:
    line = input().strip()
    if line == "EOF":
        break

    winner, loser, scores = line.split(":")
    set_list = scores.split(",")

    if winner not in players:
        players[winner] = [0, 0, 0, 0, 0, 0]
    if loser not in players:
        players[loser] = [0, 0, 0, 0, 0, 0]

    winner_sets = 0
    loser_sets = 0

    for s in set_list:
        w, l = map(int, s.split("-"))

        players[winner][3] += w
        players[winner][5] += l
        players[loser][3] += l
        players[loser][5] += w

        if w > l:
            winner_sets += 1
        else:
            loser_sets += 1

    players[winner][2] += winner_sets
    players[winner][4] += loser_sets
    players[loser][2] += loser_sets
    players[loser][4] += winner_sets

    if len(set_list) >= 4:
        players[winner][0] += 1   
    else:
        players[winner][1] += 1   

result = sorted(players.items(), key=lambda x: (
    -x[1][0],   
    -x[1][1],   
    -x[1][2],   
    -x[1][3],   
     x[1][4],   
     x[1][5]    
))

for name, stats in result:
    print(name, *stats)