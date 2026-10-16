


class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, expression: str) -> str:

        try:
            res = eval(expression)

            stroka = f"{expression} = {res}"
            self.history.append(stroka)
            return str(res)

        except (NameError, ZeroDivisionError, SyntaxError):
            return "Ошибка"

    def show_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()
        return "История удалена"


"""print("----Для выхода напишите exit----")
print("----Для очистки напишите clear----")
print("----Для показа истории напишите history----")
pr1 = Calculator()

while True:
    user_mes = input("Введите пример:")
    user_mes = user_mes.lower()

    if user_mes == "exit":
        break
    elif user_mes == "clear":
        print(pr1.clear_history())
    elif user_mes == "history":
        print(pr1.show_history())
    else:
        print(pr1.calculate(user_mes)) """
