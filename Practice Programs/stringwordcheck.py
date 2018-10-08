string = "Tejas is a boy"
dict = {}
def countWords(stringInput):
    try :
        for word in stringInput.split():
            dict[word] += 1
    except AttributeError:
        print("Please enter a string only")
        count = "No words"
    return dict
print('Number of words in the string are : ' , countWords(string))
