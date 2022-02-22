import math

def primer (k:float,x:float,a:float)-> float:
    return (1/(k*math.sqrt(2*math.pi)))*math.exp((-1)*math.pow((x-a),2)/(2*k*k))

def get_input()->float:
    while True:
        try:
            return float(input())
        except ValueError as exc:
            print(f"Введено неправильное значение {exc}")

def print_output (y:float):
    print(f"Результат={y}")

def main():
    print("Ввод переменной k:")
    input_k=get_input()
    print("Ввод переменной x:")
    input_x=get_input()
    print("Ввод переменной a:")
    input_a = get_input()
    output_y=primer(input_k,input_x,input_a)
    print_output(output_y)

if __name__=="__main__":
    main()