from Calculator import Calculator

a,f,b, *x = input().split()

x.reverse()
while 1:
    Calc = Calculator(int(a),int(b))
    if f == '+': a = Calc.add() # 덧셈
    elif f == '-': a = Calc.sub() # 뺄셈
    elif f == '*': a = Calc.mul() # 곱셈
    elif f == '/': a = Calc.div() # 나눗셈
    elif f == '**': a = Calc.pow() # 제곱

    try:
        f = x.pop()
        print(f)
        b = x.pop()
        print(b)
    except:
        break
    print(a)
print(a)
