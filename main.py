#-----------------------
# БИБЛИОТЕКА TKINTER
#-----------------------
from tkinter import*
import tkinter.ttk as ttk


#-------------------------------------------------------------------
# ФУНКЦИЯ ПРОВЕРКИ СОДЕРЖИМОГО COMBOBOX1 И ИЗМЕНЕНИЯ ТЕКСТА LABEL
#-------------------------------------------------------------------
def comb1(event):
    print('[DEBUG] event:', event)
    print('[DEBUG] event.widget:', event.widget)
    print('[DEBUG] event.widget.get():', event.widget.get())
    if combobox.get() == 'Black':
         label['text'] = "0"
    if combobox.get() == 'Brown':
         label['text'] = "1"
    if combobox.get() == 'Red':
         label['text'] = "2"
    if combobox.get() == 'Orange':
         label['text'] = "3"
    if combobox.get() == 'Yellow':
         label['text'] = "4"
    if combobox.get() == 'Green':
         label['text'] = "5"
    if combobox.get() == 'Blue':
        label['text'] = "6"
    if combobox.get() == 'Purple':
        label['text'] = "7"
    if combobox.get() == 'Gray':
        label['text'] = "8"
    if combobox.get() == 'White':
        label['text'] = "9"

#--------------------------------------------------------------------
# ФУНКЦИЯ ПРОВЕРКИ СОДЕРЖИМОГО COMBOBOX2 И ИЗМЕНЕНИЯ ТЕКСТА LABEL
#--------------------------------------------------------------------
def comb2(event):
    print('[DEBUG] event:', event)
    print('[DEBUG] event.widget:', event.widget)
    print('[DEBUG] event.widget.get():', event.widget.get())
    if combobox1.get() == 'Black':
        label1['text'] = "0"
    if combobox1.get() == 'Brown':
        label1['text'] = "1"
    if combobox1.get() == 'Red':
        label1['text'] = "2"
    if combobox1.get() == 'Orange':
        label1['text'] = "3"
    if combobox1.get() == 'Yellow':
        label1['text'] = "4"
    if combobox1.get() == 'Green':
        label1['text'] = "5"
    if combobox1.get() == 'Blue':
        label1['text'] = "6"
    if combobox1.get() == 'Purple':
        label1['text'] = "7"
    if combobox1.get() == 'Gray':
        label1['text'] = "8"
    if combobox1.get() == 'White':
        label1['text'] = "9"

#-----------------------------------
# ФУНКЦИЯ ВЫХОДНОГО РЕЗУЛЬТАТА
#-----------------------------------
def out_num():
    label2['text'] = label['text'] + label1['text']


#-----------------------------------
# СОЗДАНИЕ ОКНА
#-----------------------------------
root = Tk()
root.geometry('600x600')
root.title("Подсчёт сопротивления резистра")

# первый combobox
combobox = ttk.Combobox(root, values=['Black', 'Brown', 'Red',
                                      'Orange', 'Yellow', 'Green',
                                      'Blue', 'Purple', 'Gray', 'White'])
# расположение первого combobox
combobox.place(x=85, y=200)

# второй combobox
combobox1 = ttk.Combobox(root, values=['Black', 'Brown', 'Red',
                                      'Orange', 'Yellow', 'Green',
                                      'Blue', 'Purple', 'Gray', 'White'])
# расположение второго combobox
combobox1.place(x=350, y=200)

# привязка функций к combobox
combobox.bind('<<ComboboxSelected>>', comb1)
# привязка функций к combobox1
combobox1.bind('<<ComboboxSelected>>', comb2)


# первый label
label = Label(root, text='0')
# расположение первого label
label.place(x=150, y=230)

# второй label
label1 = Label(root, text='0')
# расположение второго label
label1.place(x=415, y=230)

# кнопка обработки выходного числа
btn = ttk.Button(text="output", command=out_num)
# расположение кнопки
btn.place(x=250, y=300)

# третий label
label2 = Label(root, text='0')
# расположение третьего label
label2.place(x=280, y=330)


# цикл главного окна
root.mainloop()
