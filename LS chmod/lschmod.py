from os import chmod,path
chmod = 0
chmods =''
for modes in open("ls.txt","r").readlines():
    print(chmod(path(modes.split(' ')[-1])))
    # chmod = 0
    # print(modes.split(' ')[0][1:])
    # for char in :
        # if(char == 'r'):
        #     chmod += 4
        # elif(char == 'w'):
        #     chmod += 2
        # elif(char == 'x'):
        #     chmod += 1
    # print(chmod)
