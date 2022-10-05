def divisors(num):
    try:
        if num <= 0:
           raise ValueError("Debe de ser un numero positivo mayor a 0") 
        divisors = [i for i in range(1, num+1) if num%i==0]
        return divisors
    except ValueError as ve:
        return ve

def run():
    try:
        num = int(input("Ingrese un numero:"))
        print(divisors(num))
    except ValueError as ve:
        print("Debe de ingresar un numero")
    
    print("Termino el programa")

if __name__ == "__main__":
    run()