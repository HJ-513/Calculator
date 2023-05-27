class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        try:
            return self.first / self.second
        except ZeroDivisionError:
            return "ZeroDivisionError"
    def pow(self):
        return self.first**self.second

if __name__ == "__main__":
    a = Calculator(5,2)
    x = a.add()
    print(x)
    a = Calculator(x,2)
    x = a.pow()
    print(x)