import threading
def print_cube(number):
    # print("Cube : {}".format(number * number * number))
    for iterator in range (0,number):
        print('Less than 10: ' + str(iterator))
        iterator += 1

def print_square(number):
    # print("Square : {}".format(number * number))
    for iterator in range (number,21):
        print('More than equal to 10 : ' + str(iterator))
        iterator += 1

if __name__ == '__main__':
    squareThread = threading.Thread(target=print_square,args=(10,))
    cubeThread = threading.Thread(target=print_cube,args=(10,))

    squareThread.start()
    cubeThread.start()
    
    squareThread.join()
    cubeThread.join()

    print("Success")
