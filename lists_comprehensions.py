def run():
    # Crear con un list comprehensions,
    # una lista de todos los multiplos de 4
    # que a la vez tambien son multiplos de 6 y 9
    # has 5 digitos


    my_list =[i for i in range(10000) if i%4== 0 and i%6==0 and i%9 == 0 and i!=0]
    print(my_list)
    


if __name__ == "__main__":
    run()
    