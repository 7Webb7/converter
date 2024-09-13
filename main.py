import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from con_rates_get import get_rates
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

root = tk.Tk()
root.title("Currency conversion APP")

rates = get_rates()

currency = ["USD", "EUR", "RUB"]

currency_rates = {c : rates['rates'][c] for c in currency}



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



tk.Label(root, text="Количество: ").grid(row = 0, column = 0, padx = 10, pady = 10)
amount_entry = tk.Entry(root)
amount_entry.grid(row = 0, column = 1, padx = 20, pady = 5, sticky="ew")

tk.Label(root, text = "Из:").grid(row=1, column = 0, padx = 10, pady = 10, sticky="ew")
from_currency = tk.StringVar(value= "USD")
from_currency_menu = ttk.Combobox(root, textvariable=from_currency, values=list(currency_rates.keys()))
from_currency_menu.grid(row=1, column = 1, padx = 15, pady = 10, sticky="ew")

tk.Label(root, text = "В:").grid(row = 2, column = 0, padx=10, pady = 10, sticky="ew")
to_currency = tk.StringVar(value = "EUR")
to_currency_menu = ttk.Combobox(root, textvariable=to_currency, values=list(currency_rates.keys()))
to_currency_menu.grid(row = 2, column = 1, padx = 15, pady = 10, sticky="ew")

convert_button = tk.Button(root, text = "Конвертировать", command = convert_currency)
convert_button.grid(row = 3, column = 1, padx = 15, pady = 8, sticky="ew")

result_label = tk.Label(root, text = "Результат:")
result_label.grid(row = 4, column = 0, columnspan = 10, padx = 10, pady = 10, sticky="ew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(4, weight=1)




root.mainloop()