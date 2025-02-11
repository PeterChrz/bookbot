def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        #words = file_contents.split()
        #print(len(words))
        return file_contents
        
def count(file_contents):
    #Dictionary of all letters
    #alpha = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, ' ':0, '':0, '.':0, ',':0, '!':0, '?':0, '@':0}    
    #Whole book coming in.
    alpha = {}  
    #print(file_contents)
    for c in file_contents:
        alpha[c.lower()] = alpha.get(c.lower(), 0) + 1
   #     if c.lower() in alpha:
   #         #value = alpha[c.lower()]
   #         #value += 1
   #         alpha[c.lower()] += 1
   #     else:
   #         alpha[c.lower()] = 1

    return alpha


print(count(main()))