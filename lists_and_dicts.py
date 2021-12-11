
def run():
    my_list = [1,"Hello",True,4.5]
    my_dict ={"first_name":"Emma", "lastname":"Pilozo"}
    
    my_lista_by2 = [i * 2 for i in range(1,10)]
    
    super_list = [
              {"first_name":"Emma", "lastname":"Pilozo","edad":51},
              {"first_name":"Maite", "lastname":"Baquerizo","edad":18},
              {"first_name":"Nicolas", "lastname":"Baquerizo","edad":20},   
              {"first_name":"Lucia", "lastname":"Baquerizo","edad":23},
              {"first_name":"Keiko", "lastname":"Perruno","edad":9},
              {"first_name":"Hans", "lastname":"Gatuno","edad":5},   
                  ]
    
    super_dict = {
                "natural_nums":[1,2,3,4,5],
                "integer_nums":[-1,0,-2,5,8],
                "floating_nums":[3.4,0,6.7,9,12.3]
    }
    
    print("="*50)
    print("Listado de Diccionario")
    print("="*50)
    for keys,values in super_dict.items():
        print(" {} - {} ".format(keys,values))

    print (" ")    
    print("="*50)
    print("Listado de Listas")
    print("="*50)
    for i,t in enumerate(super_list):
         print("\n")
         print("Lista # ",i)
         for key, values in t.items():
             print("Diccionario {} - {} ".format(key,values))
            
        
        
       # print(" {} ".format(i))


if __name__ == "__main__":
    run()
    
    




