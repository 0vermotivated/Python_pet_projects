import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd
import requests

import mail
from mail import*

def get_json():
    response = requests.get('https://app-396711.1cmycloud.com/applications/Demo-dev/api/deals')
    m = response.json()
    m.sort(key=lambda x: x['ДатаСоздания'])
    return m


def get_info():
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    query = "SELECT COUNT(*), SUM(Сумма) FROM test;"
    cursor.execute(query)
    result = cursor.fetchone()
    msg = "Количество сделок: " + str(result[0]) + "\nСумма за весь период: " + str(result[1])
    #label.config(text=msg)
    conn.close()
    return msg
    # label.config(text="Сообщение отправлено")


def on_button1_click():
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    df = pd.DataFrame(get_json())
    q = '''
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        date TEXT,
        client TEXT,
        name TEXT,
        stage TEXT,
        sum INTEGER,
        eq TEXT
    );
    '''
    cursor.execute(q)
    df.to_sql('test', conn, if_exists='replace', index=False)
    conn.close()
    label.config(text="Данные загружены в базу данных")


def on_button2_click():
    rt = tk.Tk()
    rt.title("Данные из БД")

    tree = ttk.Treeview(rt)
    tree['columns'] = ('Код', 'ДатаСоздания', 'Клиент', 'Наименование', 'Стадия', 'Сумма', 'Валюта')

    tree.heading('Код', text='Код')
    tree.heading('ДатаСоздания', text='ДатаСоздания')
    tree.heading('Клиент', text='Клиент')
    tree.heading('Наименование', text='Наименование')
    tree.heading('Стадия', text='Стадия')
    tree.heading('Сумма', text='Сумма')
    tree.heading('Валюта', text='Валюта')

    tree.pack(expand=True, fill='both')

    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    conn.close()
    rt.mainloop()


def on_button3_click():
    msg = get_info()
    mail.send_msg(msg)
    label.config(text="Сообщение успешно отправлено")


def on_button4_click():
    root.quit()


root = tk.Tk()
root.title("Пример интерфейса с кнопками")

label = tk.Label(root, text="")
label.pack(pady=20)
button1 = tk.Button(root, text="Взять данные из облачного сервиса", command=on_button1_click)
button1.pack(pady=10)
button2 = tk.Button(root, text="Показать данные из БД", command=on_button2_click)
button2.pack(pady=10)
button3 = tk.Button(root, text="Отправить сообщение на почту", command=on_button3_click)
button3.pack(pady=10)
button4 = tk.Button(root, text="Завершить программу", command=on_button4_click)
button4.pack(pady=10)

root.mainloop()