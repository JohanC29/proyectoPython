def divisors(num):
    assert num > 0 , "Debe de ser un numero positivo mayor a 0"
    
    divisors = [i for i in range(1, num+1) if num%i==0]
    return divisors


def run():

    num = input("Ingrese un numero:")
    
    assert num.isnumeric(), "Debe de ingresar un numero"
    print(divisors(int(num)))
    
    print("Termino el programa")

if __name__ == "__main__":
    run()