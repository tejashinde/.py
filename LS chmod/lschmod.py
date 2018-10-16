import re
for modes in open("ls.txt","r").readlines():
    chmods = ""
    for mode in re.findall('...',modes.split()[0][1:10]):
        chmod = 0
        if mode[0] != "-":
            chmod += 4
        if mode[1] != "-":
            chmod += 2
        if mode[2] != "-":
            chmod += 1
        chmods += str(chmod)
    print(chmods)
