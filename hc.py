msg_ = [[]] * 15
msg_[0] = "Enter an equation"
msg_[1] = "Do you even know what numbers are? Stay focused!"
msg_[2] = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_[3] = "Yeah... division by zero. Smart move..."
msg_[4] = "Do you want to store the result? (y / n):" 
msg_[5] = "Do you want to continue calculations? (y / n):"
msg_[6] = " ... lazy"
msg_[7] = " ... very lazy"
msg_[8] = " ... very, very lazy"
msg_[9] = "You are"
msg_[10] = "Are you sure? It is only one digit! (y / n)"
msg_[11] = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_[12] = "Last chance! Do you really want to embarrass yourself? (y / n)"

mask_1 = ["+", "-", "*", "/"]
mask_2 = ["y", "n", "Y", "N"]

def is_one_digit(v):
    return v > -10 and v < 10 and v.is_integer()

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_[7]
    if (v1 == 0 or v2 == 0) and v3 in mask_1[:-1]:
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)

calc = ""
result = 0.0
memory = 0.0
repeat = True

while repeat:  # calc != "exit":
    print(msg_[0])
    x = oper = y = ""
    calc = input()
    if not calc:
        continue
    t = calc.split()
    if len(t) == 3:
        x, oper, y = t
    if x == "M":
        x = str(memory)
    if y == "M":
        y = str(memory)
    
    isnum = True
    for a in (x, y):
        if len(a):
            if a[0] == "-":
                a = a[1:]
            a = a.split(".", 1)
            if not "".join(a).isdigit():
                isnum = False
        else:
            isnum = False
    
    if not isnum:
        print(msg_[1])
        continue
    elif not oper in mask_1:
        print(msg_[2])
        continue

    x = float(x)
    y = float(y)
    result = 0.0
    check(x, y, oper)
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0.0:
        result = x / y
    else:
        print(msg_[3])
        continue
    print(result)
    
    answer = ""
    while not answer in mask_2:  # answer != "y" or answer != "n":  # True:  # 
        print(msg_[4])
        #answer = "y"
        answer = input().lower()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:
                    print(msg_[msg_index])
                    #answer = "y"
                    answer = input().lower()
                    if answer == "y":
                        msg_index += 1
                    if answer == "n":
                        break
                if answer == "y":
                    memory = result
            else:
                memory = result
    
    answer = ""
    while not answer in mask_2:  # answer != "y" or answer != "n":  # True:  # 
        print(msg_[5])
        #answer = "y"
        answer = input().lower()
        if answer == "y":
            repeat = True
        elif answer == "n":
            repeat = False
