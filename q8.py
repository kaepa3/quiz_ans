
def move (move_list):
    if len(move_list) == 12 + 1:
        return 1

    direction =  [[1,0],[-1,0],[0,1],[0,-1]]
    count = 0
    for v in direction:
        next = [move_list[-1][0] + v[0], move_list[-1][-1] + v[1]]
        if  next not in move_list:
            count += move(move_list +[next]) 
          
    return count
    


print(move([[0,0]]))