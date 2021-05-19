import idc


file = open("D:\\_virus\\IceID\\api.txt", 'r')
lines = file.readlines()

newlist = [[x for x in line.rstrip().split("  ")] for line in lines]

file.close()

for list in newlist:
    if (Qword(int(list[0],16)) == int(list[1],16)) and (int(list[1],16) != 0):
        name = list[2].split(".")
        MakeName(int(list[0],16), name[1])

#count=0
#for line in lines:
#    count += 1
#    print("Line{}: {}".format(count, line.strip()))