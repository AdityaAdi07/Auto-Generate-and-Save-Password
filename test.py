robo_x=0
robo_y=0
turns=0
coord_fin=[]
def robo_walk(a):
    global robo_x, robo_y, turns, coord_fin
    if turns==0:
        for ech in range (1,a+1):
            robo_y+=1
            print(robo_x, robo_y)
            coord= str(robo_x)+str(robo_y)
            coord_fin.append(coord)


    elif turns%2==0:
        if turns%4==0:
            for ech in range(1, a+1):
                robo_y += 1
                print(robo_x, robo_y)
                coord = str(robo_x) + str(robo_y)
                coord_fin.append(coord)
        elif turns%4!=0:
            for ech in range(1, a+1):
                robo_y -= 1
                print(robo_x, robo_y)
                coord = str(robo_x) + str(robo_y)
                coord_fin.append(coord)

    elif turns%2!=0:
        if turns==1:
            for ech in range(1, a+1):
                robo_x += 1
                print(robo_x, robo_y)
                coord = str(robo_x) + str(robo_y)
                coord_fin.append(coord)
        elif turns==3:
            for ech in range(1, a+1):
                robo_x -= 1
                print(robo_x, robo_y)
                coord = str(robo_x) + str(robo_y)
                coord_fin.append(coord)
        elif turns%4==1:
            for ech in range(1, a+1):
                robo_x += 1
                print(robo_x, robo_y)
                coord = str(robo_x) + str(robo_y)
                coord_fin.append(coord)
        elif turns%4==3:
            for ech in range(1, a+1):
                robo_x -= 1
                print(robo_x, robo_y)
                coord = str(robo_x) + str(robo_y)
                coord_fin.append(coord)


    turns+=1



a=[4, 4, 3, 2, 2, 3]
for val in a:
    robo_walk(val)
print(coord_fin)
def finale(lst):
    for i in range (len(lst)):
        for j in range(i+1, len(lst)):
            if int(lst[i])==int(lst[j]):
                return True

    return False

print(finale(coord_fin))


