import random 
import os

def run():
    find_word   = read()
    find_letters= []
    final_word  = []
    guion = '_'
    for i,l in enumerate(find_word):
        find_letters.append(guion)
        final_word.append(l)
            
    game_over = False
    while not game_over:
        os.system("cls")
        print("!Adivina la palabra! \n")
        print([fl for fl in find_letters])
                
        try:
            letter = input ("Ingrese una letra : ")
        except TypeError:
            print ("Must to enter only letter")
            
        ## look if letter exists in the word and show it   
       
        for i,l in enumerate(find_word):
            if letter in l:
                find_letters[i] = letter
            elif find_letters[i] != "_" :
                  find_letters[i] = l
           
    
        if find_letters == final_word:
            print("\n !Felicidades.. Acertastes la palabra es : " + find_word)
            game_over = True
             
             
        
def read():
    ## read the file
    list_words = []
    with open("./files/data.txt","r",encoding="utf-8") as f:
           for w in f:
                w=w.rstrip('\n')
                list_words.append(w)
                
    # choice words list in random way
    
    find_word = random.randrange(1,len(list_words))
    return list_words[find_word]


if __name__ == "__main__":
    run()
    
    