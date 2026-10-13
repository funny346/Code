import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Крестики-нолики")
root.iconbitmap("icon1.ico")

# ===== Глобальные переменные =====
current_player = "X"  # Начинают крестики
buttons = []  # Список для хранения всех кнопок


# ===== Функция проверки победы =====
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
        [0, 4, 8], [2, 4, 6]  # Диагональные линии
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return True
    return False


# ===== Функция обработки клика =====
def on_click(index):
    global current_player
    if buttons[index]["text"] == "":  # Проверяем, что клетка пустая
        buttons[index]["text"] = current_player  # Записываем символ игрока (X или O)

        if check_winner():  # Проверяем победу
            messagebox.showinfo("Победа!", f"Победил {current_player}!")  # Всплывающее окно с победителем
        elif all(button["text"] != "" for button in buttons):  # Проверяем ничью
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")  # Всплывающее окно с ничьей
        else:
            # Меняем игрока
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


# ===== Функция сброса игры =====
def reset_game():
    global current_player
    current_player = "X"  # Первый ход всегда за "X"

    # Очищаем все кнопки, возвращая им стандартный цвет и убирая текст
    for button in buttons:
        button.config(text="", bg=default_button_color)


# ===== Создание кнопок =====
for i in range(9):
    button = tk.Button(
        root,
        text="",  # Изначально пустая
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx)  # Привязываем функцию к кнопке
    )
    button.grid(row=i // 3, column=i % 3)  # Размещаем в сетке 3x3
    buttons.append(button)  # Добавляем кнопку в список

# Запоминаем стандартный цвет кнопок
default_button_color = buttons[0].cget("bg")

# ===== Создание кнопки сброса =====
reset_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()