def removeShutdownOptions():
    filepath = "/home/joep/.config/ksmserverrc"
    indexString = "[General]"
    insertText = "confirmLogout=false"

    __insertStringUnderSubstring(filepath, indexString, insertText)

def __getIndexOfSubstring(filepath, substring):
    with open(filepath, "r") as f:
        contents = f.read()
        return contents.index(substring)
    
def __insertStringUnderIndex(filepath, index, insertText):
    with open(filepath, "r") as f:
        contents = f.readlines()

    contents.insert(index + 1, insertText + "\n")

    with open(filepath, "w") as f:
        contents = "".join(contents)
        f.write(contents)    

def __insertStringAtIndex(filepath, index, insertText):
    with open(filepath, "r") as f:
        contents = f.readlines()

    contents.insert(index, insertText + "\n")

    with open(filepath, "w") as f:
        contents = "".join(contents)
        f.write(contents)    

def __getAnchorIndex(filepath, indexString):
    with open(filepath) as file:
        if indexString in file:
            return __getIndexOfSubstring(filepath, indexString)
        else:
            index = 0
            __insertStringAtIndex(filepath, index, indexString)
            return index
        
def __insertStringUnderSubstring(filepath, indexString, insertText):
    index = __getAnchorIndex(filepath, indexString)                 
    __insertStringUnderIndex(filepath, index, insertText)