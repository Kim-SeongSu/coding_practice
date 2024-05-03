'''
# 시간초과
def solution(players, callings):
    for call in callings:
        x = players.index(call)
        players[x], players[x-1] = players[x-1], players[x]
    return players

# 시간초과
def solution(players, callings):
    rank, k = {}, 1
    for player in players:
        rank[k] = player
        k += 1

    for call in callings:
        x = [i for i in rank.keys() if rank[i] == call]
        rank[x[0]], rank[x[0]-1] = rank[x[0]-1], rank[x[0]]
    return list(rank.values())
'''

def solution(players, callings):
    rank = {player:i for i,player in enumerate(players)}

    for call in callings:
        idx = rank[call]
        rank[call] -= 1
        rank[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players