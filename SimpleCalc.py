from tkinter import*
import tkinter.font as font
import math

root = Tk()
root.title("Calculator Sederhana")
root["bg"] = "#cbab7f"
root.geometry("310x410")

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["bg"] = "#cbab7f"
e.grid(row=0, columnspan=4, pady=25, padx=20)


def cetak(nilai):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(nilai))


def tambah():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "jumlah"
    b_awl = float(blgnawal)
    e.delete(0, END)


def kurang():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "kurang"
    b_awl = float(blgnawal)
    e.delete(0, END)


def kali():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "kali"
    b_awl = float(blgnawal)
    e.delete(0, END)


def bagi():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "bagi"
    b_awl = float(blgnawal)
    e.delete(0, END)


def hapus():
    e.delete(0, END)


def samadengan():
    b_akhr = e.get()
    e.delete(0, END)
    if mat == "jumlah":
        e.insert(0, b_awl + float(b_akhr))
    elif mat == "kurang":
        e.insert(0, b_awl - float(b_akhr))
    elif mat == "bagi":
        try:
            hitung = b_awl / float(b_akhr)
            e.insert(0, hitung)
        except ZeroDivisionError:
            e.insert(0, "Tidak Bisa Dibagi 0")

    elif mat == "kali":
        e.insert(0, b_awl * float(b_akhr))


btn = Button(root, text="1", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(1))
btn2 = Button(root, text="2", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(2))
btn3 = Button(root, text="3", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(3))
btn4 = Button(root, text="4", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(4))
btn5 = Button(root, text="5", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(5))
btn6 = Button(root, text="6", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(6))
btn7 = Button(root, text="7", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(7))
btn8 = Button(root, text="8", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(8))
btn9 = Button(root, text="9", padx=30, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(9))
btn0 = Button(root, text="0", padx=70, bg="#5d432c",
                fg="white", pady=20, command=lambda: cetak(0))
btndot = Button(root, text=".", padx=30, bg="#967c61",
                fg="white", pady=20, command=lambda: cetak("."))
tam = Button(root, text="+", padx=30, bg="#967c61",
                fg="white", pady=20, command=tambah)
kur = Button(root, text="-", padx=30, bg="#967c61",
                fg="white", pady=20, command=kurang)
bag = Button(root, text="÷", padx=30, bg="#967c61",
                fg="white", pady=20, command=bagi)
kal = Button(root, text="x", padx=30, bg="#967c61",
                fg="white", pady=20, command=kali)
hap = Button(root, text="C", padx=70, bg="#dcd2c9", pady=20, command=hapus)
equal = Button(root, text="=", padx=70, bg="#dcd2c9",
                pady=20, command=samadengan)


btn.grid(row=3, column=0, pady=2)
btn2.grid(row=3, column=1, pady=2)
btn3.grid(row=3, column=2, pady=2)
btn4.grid(row=2, column=0, pady=2)
btn5.grid(row=2, column=1, pady=2)
btn6.grid(row=2, column=2, pady=2)
btn7.grid(row=1, column=0, pady=2)
btn8.grid(row=1, column=1, pady=2)
btn9.grid(row=1, column=2, pady=2)
btn0.grid(row=4, column=1, columnspan=2)
btndot.grid(row=4, column=0, pady=2)

tam.grid(row=1, column=3, pady=2)
kur.grid(row=2, column=3, pady=2)
bag.grid(row=3, column=3, pady=2)
kal.grid(row=4, column=3, pady=2)
hap.grid(row=5, column=0, columnspan=2)
equal.grid(row=5, column=2, columnspan=2)


root.mainloop()