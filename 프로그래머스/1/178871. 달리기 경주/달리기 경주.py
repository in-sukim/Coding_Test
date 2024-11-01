def solution(players, callings):
    player_order = dict()
    player_order = {key: idx for idx, key in enumerate(players)}
        
    for call in callings:
        call_idx = player_order[call]
        ahead_idx = call_idx - 1
        player_order[call], player_order[players[ahead_idx]] = ahead_idx, call_idx
        players[ahead_idx], players[call_idx] = players[call_idx], players[ahead_idx]
    return players
    