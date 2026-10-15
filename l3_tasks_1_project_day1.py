
class CalculatorEngine:

    def __init__(self):
        self.history = []






    def Calc (self, num1: float, num2: float, operator: str):

        if operator == "+":
            res = num1 + num2
            self.history.append(res)
            return res
        elif operator == "-":
            res = num1 - num2
            self.history.append(res)
            return res
        elif operator == "*":
            res = num1 * num2
            self.history.append(res)
            return res
        elif operator == "/":
            if num2 == 0:
                return "Делить на ноль нельзя"
            else:
                res = num1 / num2
                self.history.append(res)
                return res
        else:

            return "Неизвестная операция"

    def clear_history(self):
            self.history.clear()
            print( "История была очищена")

    def show_history(self):
            return self.history

if __name__ == '__main__':
    my_calc = CalculatorEngine()
    i = 0
    while i < 5:
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        op = input("Введите знак: ")


        print("Результат:", my_calc.Calc(x, y, op))


        print("История калькулятора:", my_calc.show_history())
        i += 1
        if i == 3:
            my_calc.clear_history()