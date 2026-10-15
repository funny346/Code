import customtkinter as ctk
# Импортируем ваш готовый движок калькулятора
from l3_tasks_1_project_day1 import CalculatorEngine

# Настраиваем внешний вид (темная тема и синие элементы)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class CalculatorGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Создаем объект вашего движка калькулятора внутри интерфейса
        self.engine = CalculatorEngine()

        # Настройки окна
        self.title("Modern Calculator")
        self.geometry("400x500")

        # --- СЮДА МЫ БУДЕМ ДОБАВЛЯТЬ КНОПКИ И ДИСПЛЕЙ ---
        # Пример создания дисплея (поля вывода):
        self.display = ctk.CTkEntry(self, width=380, height=50, font=("Arial", 24), justify="right")
        self.display.grid(row=0, column=0, padx=10, pady=20, columnspan=4)

        # Пример создания одной кнопки:
        self.btn_1 = ctk.CTkButton(self, text="1", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("1"))
        self.btn_1.grid(row=1, column=0, padx=5, pady=5)
        self.btn_2 = ctk.CTkButton(self, text="2", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("2"))
        self.btn_2.grid(row=1, column=1, padx=5, pady=5)
        self.btn_3 = ctk.CTkButton(self, text="3", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("3"))
        self.btn_3.grid(row=1, column=2, padx=5, pady=5)
        self.btn_4 = ctk.CTkButton(self, text="4", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("4"))
        self.btn_4.grid(row=2, column=0, padx=5, pady=5)
        self.btn_5 = ctk.CTkButton(self, text="5", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("5"))
        self.btn_5.grid(row=2, column=1, padx=5, pady=5)
        self.btn_6 = ctk.CTkButton(self, text="6", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("6"))
        self.btn_6.grid(row=2, column=2, padx=5, pady=5)
        self.btn_7 = ctk.CTkButton(self, text="7", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("7"))
        self.btn_7.grid(row=3, column=0, padx=5, pady=5)
        self.btn_8 = ctk.CTkButton(self, text="8", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("8"))
        self.btn_8.grid(row=3, column=1, padx=5, pady=5)

        self.btn_9 = ctk.CTkButton(self, text="9", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("9"))
        self.btn_9.grid(row=3, column=2, padx=5, pady=5)
        self.btn_0 = ctk.CTkButton(self, text="0", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("0"))
        self.btn_0.grid(row=4, column=1, padx=5, pady=5)

        # + - * /
        self.btn_p = ctk.CTkButton(self, text="+", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_operator("+"))
        self.btn_p.grid(row=1, column=3, padx=5, pady=5)
        self.btn_m = ctk.CTkButton(self, text="-", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_operator("-"))
        self.btn_m.grid(row=2, column=3, padx=5, pady=5)

        self.btn_u = ctk.CTkButton(self, text="*", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_operator("*"))
        self.btn_u.grid(row=3, column=3, padx=5, pady=5)
        self.btn_d = ctk.CTkButton(self, text="/", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_operator("/"))
        self.btn_d.grid(row=4, column=3, padx=5, pady=5)

        self.btn_point = ctk.CTkButton(self, text=".", width=80, height=60, font=("Arial", 20),
                                   command=lambda: self.press_number("."))
        self.btn_point.grid(row=4, column=2, padx=5, pady=5)
        #clear
        self.btn_pm = ctk.CTkButton(self, text="C", width=80, height=60, font=("Arial", 20),
                                    command=lambda: self.clear_all())
        self.btn_pm.grid(row=4, column=0, padx=5, pady=5)
        # =
        self.btn_equal = ctk.CTkButton(self, text="=", width=380, height=50, font=("Arial", 20), fg_color="green",
                                       command=lambda: self.calculate_result())
        self.btn_equal.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        self.history_box = ctk.CTkTextbox(self, width=380, height=120, font=("Arial", 14))
        self.history_box.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
        self.history_box.insert("0.0", "История вычислений:\n")



    def press_number(self, number):
        # Логика нажатия на цифру (добавление в дисплей)
        self.display.insert("end", number)

    def press_operator(self, op):
        """Запоминает первое число и знак, а дисплей очищает для ввода второго числа"""
        try:
            self.first_num = float(self.display.get())
            self.operator = op
            self.display.delete(0, "end")
        except ValueError:
            pass

    def calculate_result(self):
        """Берет данные и отправляет их в ваш CalculatorEngine"""
        if self.first_num is not None and self.operator is not None:
            try:
                second_num = float(self.display.get())

                # ВЫЗОВ ВАШЕГО ДВИЖКА КЛАССА!
                result = self.engine.Calc(self.first_num, second_num, self.operator)

                # Выводим результат на дисплей
                self.display.delete(0, "end")
                self.display.insert("end", str(result))

                # Обновляем окно истории на экране
                self.update_history_ui()

                # Сбрасываем переменные для следующего круга
                self.first_num = None
                self.operator = None

            except ValueError:
                self.display.delete(0, "end")
                self.display.insert("end", "Ошибка")


    def clear_all(self):
        """Полный сброс"""
        self.display.delete(0, "end")
        self.first_num = None
        self.operator = None
    def update_history_ui(self):

        self.history_box.delete("1.0", "end")
        self.history_box.insert("0.0", "История вычислений:\n")
        for item in self.engine.show_history():
            self.history_box.insert("end", f"{item}\n")
if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
