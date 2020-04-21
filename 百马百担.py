for x in range(1,34):
    for y in range(0,51):
        for z in range(0,100):
            if 3 * x + 2 * y + z / 2 == 100:
                if x + y + z == 100:
                    print("大马有：",x,"匹，中马有：",y,"匹，小马有：",(100 - x - y),"匹")              
