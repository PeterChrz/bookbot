def main(location):
    with open(location) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    print(f"--- Begin report of {location} ---")
    print(f"{len(words)} words found in the document")
    print(" ")
    return file_contents
 
def sort_on(dict):
    return  list(dict.keys())[0]  
       
def count(file_contents):
    alpha = {} 
    final_numbers = []
    
    #print(file_contents)
    for c in file_contents:
        alpha[c.lower()] = alpha.get(c.lower(), 0) + 1

    #Create list of dictionaries.
    #final_numbers = [{k: alpha[k]} for k in alpha]
    for k in alpha:
        final_numbers.append({k:alpha[k]})
        
    #Sort dictionary
    final_numbers.sort(reverse=True, key=sort_on)
    
    #print only letters 
    for i in final_numbers:
       print(f"The '{list(i.keys())[0]}' character was found {list(i.values())[0]} times")
       if 'a' in list(i.keys()):
            return True


count(main("books/frankenstein.txt"))