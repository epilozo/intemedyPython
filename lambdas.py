def run():
    ## funciones anonimas
    fibo = lambda cadena : cadena == cadena[::-1]
    print(fibo('emma'))
    
    my_list = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x : x % 2 != 0, my_list))  
    print (odd) 
    
    my_list = [1,2,3,4,5]
    squares = [i ** 2 for i in my_list]
    print (squares)
    
    
    
    
    
    
## funcion orden superior.. recibe como parametro otra funcion y hace algo con ella
## en todos los leguajes, 3 funciones de orden superior son:
## filter map and reduce
def saludo(funcion):
    funcion()
    
    
def hola():
    print("hola como estas")
    
    
def bye():
    print("adios, te veo luego")  
    
    
 ## uso filter
     


if __name__ == "__main__":
    saludo(hola)
    saludo(bye)
    run()
    