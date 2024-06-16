class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return  f'({self.x},{self.y})'
    

def orientation(p1 : Point, p2 : Point, p3 : Point):
    val = (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)

    if val > 0:
        return 0
    elif val < 0:
        return 1
    else:
        return 2 
    
def is_between(p : Point, q : Point, r : Point):
    if ((r.x <= q.x <= p.x) or (p.x <= q.x <= r.x)) and ((r.y <= q.y <= p.y) or (p.y <= q.y <= r.y)):
        return True

    return False 
   
    
def jarvis_algorithm(data, second_veriosn=False):
    init_id = 0

    for i in range(len(data)):
        if data[init_id].x > data[i].x:
            init_id = i
        elif data[init_id].x == data[i].x:
            if data[init_id].y > data[i].y:
                init_id = i

    
    p = init_id
    result = []

    while True:
        result.append(data[p])

        q = p + 1
        if q == len(data):
            q = 0

        for r in range(len(data)):
            if orientation(data[p], data[q], data[r]) == 0:
                q = r
        
        if second_veriosn:
            if orientation(data[p],data[r],data[q]) == 2 and is_between(data[p], data[q], data[r]):
                    q = r
        
        p = q

        if p == init_id:
            break

    return result



if __name__ == '__main__':
    data = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    points = [Point(el[0], el[1]) for el in data] 

    ans_1 = jarvis_algorithm(points)
    ans_2 = jarvis_algorithm(points, True)

    print(ans_1)
    print(ans_2)


