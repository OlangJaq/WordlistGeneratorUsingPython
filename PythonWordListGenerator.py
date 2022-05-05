if __name__ == "__main__":
    s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()"   #All the characters that will make the word
    with open("wordlist8chars.txt","a+") as file:   #Name of the file that will be generated and will add new words at the end. 
        for a in s:
            for b in s:
                for c in s:
                    for d in s:
                        for e in s:
                            for f in s:
                                for g in s:
                                    for h in s:
                                        file.write(a+b+c+d+e+f+g+h+'\n')
