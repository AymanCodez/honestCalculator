def check_number(num1, num2):
    if num1 in digits:
        num1 = int(num1)
    else:
        if num1 == 'M':
            num1 = memory
        else:
            try:
                num1 = float(num1)
            except ValueError:
                return False
    if num2 in digits:
        num2 = int(num2)
    else:
        if num2 == 'M':
            num2 = memory
        else:
            try:
                num2 = float(num2)
            except ValueError:
                return False

    return num1, num2


def check_operation(operation):
    if operation in operations:
        return operation
    else:
        return False


def is_one_digit_float(num):
    return type(num) == float and -100.0 < num < 100.0


def is_one_digit(num):
    if type(num) == int:
        return -100 < num < 100
    elif num.is_integer():
        return -10.0 < num < 10.0
    else:
        return False


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"
    if v1 == 1 or v2 == 1 and v3 == '*':
        msg += " ... very lazy"
    if v1 == 0 or v2 == 0 and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += " ... very, very lazy"

    if msg != "":
        msg = "You are" + msg
        print(msg)


def calculate(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/" and num2 != 0:
        return num1 / num2
    else:
        return False


def store1():
    while True:
        print("Are you sure? It is only one digit! (y / n)")
        answer = input()
        if answer == 'y':
            return answer
        elif answer == 'n':
            return answer
        else:
            continue


def store2():
    while True:
        print("Don't be silly! It's just one number! Add to the memory? (y / n)")
        answer = input()
        if answer == 'y':
            return answer
        elif answer == 'n':
            return answer
        else:
            continue


def store3():
    while True:
        print("Last chance! Do you really want to embarrass yourself? (y / n)")
        answer = input()
        if answer == 'y':
            return answer
        elif answer == 'n':
            return answer
        else:
            continue


def store_or_not(rslt):
    while True:
        print("Do you want to store the result? (y / n):")
        answer = input()
        if answer == 'y':

            if type(rslt) == float and not rslt.is_integer():
                return answer
            elif -10.0 < rslt < 10.0:
                a = store1()
                if a == 'y':

                    b = store2()
                    if b == 'y':

                        c = store3()
                        if c == 'y':
                            return c
                        elif c == 'n':
                            return c
                        else:
                            continue

                    elif b == 'n':
                        return b
                    else:
                        continue

                elif a == 'n':
                    return a
                else:
                    continue
            else:
                return answer

        elif answer == 'n':
            return answer
        else:
            continue


def continue_or_not():
    while True:
        print("Do you want to continue calculations? (y / n):")
        answer = input()
        if answer == 'y' or answer == 'n':
            break

    return answer


operations = ["+", "-", "*", "/"]
digits = "0123456789"
memory = 0

while True:
    print("Enter an equation")
    calc = input().split()

    if not check_number(calc[0], calc[2]):
        print("Do you even know what numbers are? Stay focused!")
    else:
        x, y = check_number(calc[0], calc[2])
        if not check_operation(calc[1]):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        else:
            operation = check_operation(calc[1])

            check(x, y, operation)

            if calculate(x, y, operation) is False:
                print("Yeah... division by zero. Smart move...")
            else:
                result = float(calculate(x, y, operation))
                print(result)

                if is_one_digit(result) or is_one_digit_float(result):
                    ans = store_or_not(result)
                    if ans == 'y':
                        memory = result
                else:
                    memory = result

                ans2 = continue_or_not()
                if ans2 == 'y':
                    continue
                else:
                    break
