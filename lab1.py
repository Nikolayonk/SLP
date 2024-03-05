import tkinter as tk
from collections import Counter
import re

def remove_vowels(word):
    vowels = "ауоыиэяюёе" # гласные буквы
    return re.sub(f"[{vowels}]+$", '', word)

def process_text():
    input_text = text_input.get("1.0", tk.END)
    words = re.findall(r'\b\w+\b', input_text.lower())  # игнорирование регистра и извлечение слов
    words = [remove_vowels(word) for word in words]  # Удаление гласных в словах повторяющихся

    word_counts = Counter(words) # Подсчет частоты встречаемости слов
    most_common_word, most_common_count = word_counts.most_common(1)[0] # Получение наиболее и наименее часто встречающихся слов
    least_common_word, least_common_count = word_counts.most_common()[-1]
    # Формирование строки с результатами
    result_text = f"{most_common_word} - {most_common_count} большее количество повторяющихся слов\n\n{least_common_word} - {least_common_count} редко встречающееся слово"
     # Включение редактирования текстового поля с результатами
    text_result.config(state=tk.NORMAL)
    # Очистка и заполнение текстового поля с результатами
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, result_text)
    # Отключение редактирования текстового поля с результатами
    text_result.config(state=tk.DISABLED)

def paste_text():
    text_input.delete("1.0", tk.END) # очистка поля
    text_input.insert(tk.END, root.clipboard_get())

# Создание основного окна
root = tk.Tk()
root.title("Лабораторная 1")

# Создание текстовых полей
text_input = tk.Text(root, height=10, width=50, wrap=tk.WORD)
text_result = tk.Text(root, height=10, width=50, wrap=tk.WORD)
text_result.config(state=tk.DISABLED)

# Создание кнопок
btn_paste = tk.Button(root, text="Вставить текст из буфера", command=paste_text)
btn_process = tk.Button(root, text="Посчитать", command=process_text)

# Размещение элементов на окне
text_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
btn_process.grid(row=1, column=0, padx=10, pady=10)
btn_paste.grid(row=1, column=1, padx=10, pady=10)
text_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Запуск главного цикла приложения
root.mainloop()
