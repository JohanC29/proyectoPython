from ast import comprehension
from codecs import raw_unicode_escape_decode


def run():
    # Crear, con un dictionaty comprehension
    # un diccionario cyas llaves sean los 1000
    # primeros numeros naturales con sus raices 
    # cuadradas como valores

    my_dir = {i:i**(1/2) for i in range(1,1001)}
        
    print(my_dir)
    


if __name__ == "__main__":
    run()
    