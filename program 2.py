# this uses truel_functions to graph results
from PIL import Image
from truel_functions import d, simple_truel, rank, convert, passing_truel, random_truel

values = [[0 for i in range(100)] for i in range(100)]
img = Image.new('RGB', (100, 100), 'white')
pixels = img.load()

##filename = "data2.txt"
##with open(filename, 'r') as file:
##    for line in file:
##        data = list(map(lambda x: float(x), line.split()))
##        values[int(data[0]*100-1)][int(data[1]*100-1)] = int(data[3]*255)
##file.close()

##filename = "player1.txt"
##with open(filename, 'r') as file:
##    for line in file:
##        data = list(map(lambda x: float(x), line.split()))
##        values[int(data[0]*100-1)][int(data[1]*100-1)] = int(data[2]*255)
##file.close()

##for j in range(1, 101):
##    for k in range(1, 101):
##        i_acc = 0
##        i_max = 0
##        for i in range(1, 101):
##            t = simple_truel(i/100, j/100, k/100)
##            if t[0] > i_max:
##                i_acc = i/100
##                i_max = t[0]
##        #print(j/100, k/100, i_acc, i_max)
##        pixels[j-1, 100-k] = (int(i_max*255),int(i_max*255),int(i_max*255))

##for i in range(1, 101):
##    for k in range(1, 101):
##        j_acc = 0
##        j_max = 0
##        for j in range(1, 101):
##            t = simple_truel(i/100, j/100, k/100)
##            if t[1] > j_max:
##                j_acc = j/100
##                j_max = t[1]
##        #print(j/100, k/100, i_acc, i_max)
##        pixels[i-1, 100-k] = (int(j_max*255),int(j_max*255),int(j_max*255))

##for i in range(1, 101):
##    for j in range(1, 101):
##        k_acc = 0
##        k_max = 0
##        for k in range(1, 101):
##            t = simple_truel(i/100, j/100, k/100)
##            if t[2] > k_max:
##                k_acc = k/100
##                k_max = t[2]
##        #print(j/100, k/100, i_acc, i_max)
##        pixels[i-1, 100-j] = (int(k_max*255),int(k_max*255),int(k_max*255))

##for i in range(1, 101):
##    for j in range(1, 101):
##        values[i-1][j-1] = int((d(i/100, j/100)*255))
##
##
##for i in range(1, 101):
##    for j in range(1, 101):
##        if d(i/100, j/100) > 0.5:
##            values[i-1][j-1] = 255
##        elif d(i/100, j/100) < 0.5:
##            values[i-1][j-1] = 0
##        else:
##            values[i-1][j-1] = 100
##
##for i in range(100):
##    for j in range(100):
##        pixels[i,99-j] = (values[i][j], values[i][j], values[i][j])

##k = 1
##for i in range(1, 101):
##    for j in range(1, 101):
##        t = passing_truel(i/100, j/100, k, '1')
##        if rank(t)[2] == 1:
##            pixels[i-1, 100-j] = (255,0,0)
##        elif rank(t)[2] == 2:
##            pixels[i-1, 100-j] = (0,255,0)
##        elif rank(t)[2] == 3:
##            pixels[i-1, 100-j] = (0,0,255)
##        elif rank(t)[2] == 12:
##            pixels[i-1, 100-j] = (255,255,0)
##        elif rank(t)[2] == 13:
##            pixels[i-1, 100-j] = (255,0,255)
##        elif rank(t)[2] == 23:
##            pixels[i-1, 100-j] = (0,255,255)
##        elif rank(t)[2] == 0:
##            pixels[i-1, 100-j] = (255,255,255)
##
###img.save("best_1_R.png", "PNG")
##img.show()


for k in range(1, 11):
    x = 0
    y = 0
    z = 0
    xy = 0
    xz = 0
    yz = 0
    xyz = 0
    
    for i in range(1, 101):
        for j in range(1, 101):
            t1 = simple_truel(i/100, j/100, k/10)
            t2 = passing_truel(i/100, j/100, k/10, '2')
            if t1[0] >= t2[0]:
                t = t1
            else:
                t = t2 
            if rank(t)[2] == 1:
                pixels[i-1, 100-j] = (255,0,0)
                x += 1
            elif rank(t)[2] == 2:
                pixels[i-1, 100-j] = (0,255,0)
                y += 1
            elif rank(t)[2] == 3:
                pixels[i-1, 100-j] = (0,0,255)
                z += 1
            elif rank(t)[2] == 12:
                pixels[i-1, 100-j] = (255,255,0)
                xy += 1
            elif rank(t)[2] == 13:
                pixels[i-1, 100-j] = (255,0,255)
                xz += 1
            elif rank(t)[2] == 23:
                pixels[i-1, 100-j] = (0,255,255)
                yz += 1
            elif rank(t)[2] == 0:
                pixels[i-1, 100-j] = (0,0,0)
                xyz += 1
    ##print(y)
    ##print(z)
    ##print(xy)
    ##print(xz)
    ##print(yz)
    ##print(xyz)

    img.save("p2_optimal_k"+str(k/10)+".png", "PNG")
    img.show()
    input(x)

##for k in range(1,11):
##    x = 0
##    y = 0
##    tied = 0
##    for i in range(1, 101):
##        for j in range(1, 101):
##            t1 = simple_truel(i/100, j/100, k/10)
##            t2 = random_truel(i/100, j/100, k/10)
##            if t1[2] > t2[2]:
##                pixels[i-1, 100-j] = (0,0,255)
##                x += 1
##            elif t1[2] < t2[2]:
##                pixels[i-1, 100-j] = (255,255,0)
##                y += 1
##            elif t1[2] == t2[2]:
##                pixels[i-1, 100-j] = (255,255,255)
##                tied += 1
##    img.save("R_best_var_"+str(k/10)+"_3.png", "PNG")
##    img.show()
##    input(str(x)+' '+str(y)+' '+str(tied))


