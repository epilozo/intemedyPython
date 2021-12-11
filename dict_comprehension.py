from math import sqrt

def run():
        
     """   list_dictionary = {}
     for i in range(1,101):
        if i % 3 != 0: 
             list_dictionary[i] = i ** 3
    
     print(list_dictionary) """
     ## lo mismo que el anterior pero en comprehension
     """ list_dictionary = { i : i ** 3 for i in range(1,101) if i % 3 != 0  } 
     print(list_dictionary) """
     
     # dictionary primeros 100 numeros naturales con su respectifa raiz cuadradas
     list_dictionary = { i : round(sqrt(i),2) for i in range(1,101)} 
     print(list_dictionary)


if __name__ == "__main__":
    run()