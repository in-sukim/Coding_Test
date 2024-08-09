def solution(book_time):
    book_list = []
    for book in book_time:
        start, end = book
        
        start_h, start_m = start.split(':')
        end_h, end_m = end.split(':')
        
        start_time = int(start_h) * 60 + int(start_m)
        end_time = int(end_h) * 60 + int(end_m) + 10
        
        book_list.append([start_time, end_time])
    book_list.sort(key = lambda x:(x[0],x[1]))
    
    rooms = []
    for book in book_list:
        start, end = book
        if not rooms:
            rooms.append([start, end])
            continue
        else:
            for idx, room in enumerate(rooms):
                if room[-1] <= start:
                    rooms[idx] = room + [start, end]
                    break
            else:
                    rooms.append([start, end])
    return len(rooms)
            
            