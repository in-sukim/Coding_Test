def solution(bandage, health, attacks):   
    time = 0
    sucess_time = 0
    max_health = health
    current_health = health
    max_time = max([i[0] for i in attacks])
    
    while time < max_time+1:
        if attacks[0][0] == time:
            current_health -= attacks[0][-1] 
            sucess_time = 0
            attacks = attacks[1:]
        else:
            if time != 0:
                sucess_time += 1
                if sucess_time == bandage[0]:
                    current_health += bandage[2]
                    sucess_time = 0
                current_health += bandage[1]
                
                if current_health > max_health:
                    current_health = max_health
                    
        if current_health <= 0:
            return -1
        time += 1
    
    return current_health