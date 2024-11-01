def solution(players, callings):
    player_order = dict()
    for idx, player in enumerate(players):
        player_order[player] = idx
        
    for call in callings:
        call_idx = player_order[call]
        ahead_idx = call_idx - 1
        player_order[call], player_order[players[ahead_idx]] = ahead_idx, call_idx
        players[ahead_idx], players[call_idx] = players[call_idx], players[ahead_idx]
    player_order = [i[0] for i in sorted(player_order.items(), key = lambda x: x[1])]
    return player_order
        
    
        