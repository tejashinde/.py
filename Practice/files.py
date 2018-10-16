f = open("D:/College/MSc (CA)/Programming/Python/a.txt","r")
print(f.readlines(2));
f.flush();
#opening the filw in write mode
f = open("D:/College/MSc (CA)/Programming/Python/a.txt","w")
f.write("!@#$%^&*()_+");
#opening in read and append mode
f = open("D:/College/MSc (CA)/Programming/Python/a.txt","a+")
f.write("Tejas" + "\n");
print("New line appended")
f.flush()
f.close()
#Clear all the data in the file
f = open("D:/College/MSc (CA)/Programming/Python/a.txt","r")
for lines in f.readlines():
    print("" + lines)
f.flush()
f.close()
