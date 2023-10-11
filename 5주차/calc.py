def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

while True:
    print("사칙연산을 선택하세요:")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")
    
    choice = input("선택 (1/2/3/4/5): ")
    
    if choice == '5':
        print("프로그램을 종료합니다.")
        break
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: ")
        
        if choice == '1':
            print("결과: ", add(num1, num2))
        elif choice == '2':
            print("결과: ", subtract(num1, num2))
        elif choice == '3':
            print("결과: ", multiply(num1, num2))
        elif choice == '4':
            print("결과: ", divide(num1, num2))
    else:
        print("잘못된 옵션입니다. 다시선택하세요")
