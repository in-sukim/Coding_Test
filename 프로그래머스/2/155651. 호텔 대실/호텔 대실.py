def solution(book_time):
    def convert_min(str_time:str) -> int:
        h,m = map(int, str_time.split(':'))
        return (h * 60) + m
        
    book_list = []
    for book in book_time:
        start, end = map(convert_min, book)
        print(start, end)
        book_list.append([start, end+10])
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
            
            