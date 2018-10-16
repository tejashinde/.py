def printA():
    print("Function : printA | Call : AMain Original")

if __name__ == '__main__':
    def printA():
        print("Function : printA | Call : AMain Overriden")

    printA()
