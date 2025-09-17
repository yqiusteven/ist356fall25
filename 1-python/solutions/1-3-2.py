'''
Write a function called `cleanup` which takes a string as input and returns a "cleaned string" meaning:
 - remove any ? , . or !
 - strip off the whitespace from the ends
 - return text in lower case
 
 write code to call your function and test it

'''

'''
def cleanup(dirtystr:str) -> str:
    noPunct =dirtystr.strip('?,.!') # remove punctuation
    return noPunct.strip().lower()
    # removes punctuation



# main code 



'''
def cleanup(dirtystr: str) -> str:
    for ch in "?,.!":
        if ch in dirtystr:
            return dirtystr.replace(ch, "").strip().lower()


#main code 

dirtystr = "  Hello, World!  "
cleanedstr = cleanup(dirtystr)
print(cleanedstr)