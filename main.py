import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib.pyplot as plt

from con_rates_get import get_rates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import numpy as np
from synth_data import synth_imaginary
root = tk.Tk()
root.title("Currency conversion APP")

#Cоздание вкладок
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Первая вкладка")

#Функция построения графика:
def build_graph():
    x = range(0, 1000)
    y = synth_imaginary(1000)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=tab2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0, padx=50, pady=50)

rates = get_rates()

currency = ["USD", "EUR", "RUB"]

currency_rates = {c : rates['rates'][c] for c in currency}
currency_rates['IMG'] = (synth_imaginary(1000))[-1]


def convert_currency():
    try:
        amount = float(amount_entry.get())
    except:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число!")
        return

    fromc = from_currency.get()
    toc = to_currency.get()

    result = amount * currency_rates[toc] / currency_rates[fromc]
    result_label.config(text =f"Результат: {result}")



tk.Label(tab1, text="Количество: ").grid(row = 0, column = 0, padx = 10, pady = 10)
amount_entry = tk.Entry(tab1)
amount_entry.grid(row = 0, column = 1, padx = 20, pady = 5, sticky="ew")

tk.Label(tab1, text = "Из:").grid(row=1, column = 0, padx = 10, pady = 10, sticky="ew")
from_currency = tk.StringVar(value= "USD")
from_currency_menu = ttk.Combobox(tab1, textvariable=from_currency, values=list(currency_rates.keys()))
from_currency_menu.grid(row=1, column = 1, padx = 15, pady = 10, sticky="ew")

tk.Label(tab1, text = "В:").grid(row = 2, column = 0, padx=10, pady = 10, sticky="ew")
to_currency = tk.StringVar(value = "EUR")
to_currency_menu = ttk.Combobox(tab1, textvariable=to_currency, values=list(currency_rates.keys()))
to_currency_menu.grid(row = 2, column = 1, padx = 15, pady = 10, sticky="ew")

convert_button = tk.Button(tab1, text = "Конвертировать", command = convert_currency)
convert_button.grid(row = 3, column = 1, padx = 15, pady = 8, sticky="ew")

result_label = tk.Label(tab1, text = "Результат:")
result_label.grid(row = 4, column = 0, columnspan = 10, padx = 10, pady = 10, sticky="ew")

tab1.columnconfigure(0, weight=1)
tab1.columnconfigure(1, weight=1)
tab1.columnconfigure(3, weight=1)
tab1.rowconfigure(4, weight=1)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Вторая вкладка")

tk.Label(tab2, text="График валюты IMG").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
tab2.columnconfigure(0, weight=1)

build_graph_button = tk.Button(tab2, text = "Построить график", command = build_graph)
build_graph_button.grid(row = 1, column = 0, padx=10, pady=10, sticky = "ew")
root.mainloop()