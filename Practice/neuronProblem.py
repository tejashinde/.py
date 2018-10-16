N = int(input("Please enter number of Neurons : "))
min = int(input("Please enter minimum value : "))
max = int(input("Please enter maximum value : "))
neuronList = []
wList = []
bList = []

for i in range(1,N+1):
    w = int(input("Please enter w for neuron number",i," : " ))
    b = int(input("Please enter b for neuron number",i," : " ))
    wList.append(w)
    bList.append(b)
    neuronList.append(i)

def calculateNeuron(neuronList,wList,bList,min,max):
    output = neuronList[0]
    flag = 0
    for j in range (len(neuronList)+1):
        output = (output * wList[j]) + bList[j]
    if (output%2 == 0):
