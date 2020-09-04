def no_dups(s):
    # Your code here
    words = {}
    count = ""
    phrase = s.split()
    for i in phrase:
        if i not in words and i != "":
            words[i] = 1
        elif i  != "":
            words[i] +=1
            
    for i in words:
        count += f"{i } "
    return count.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))