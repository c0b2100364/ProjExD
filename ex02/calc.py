import tkinter as tk
import tkinter.messagebox as tkm

def click_alclear(event):
    entry.delete(0, tk.END)

def click_clear(event):
    clea = entry.get()
    cl = clea[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, cl)

def click_number(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)


def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

root =tk.Tk()
root.geometry("400x570")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=4)


r, c = 1, 0

acle = tk.Button(root, text="AC", font=("Times New Roman", 30), width=4, height=1)
acle.bind("<1>", click_alclear)
acle.grid(row=r, column=c)

cle = tk.Button(root, text="C", font=("Times New Roman", 30), width=4, height=1)
cle.bind("<1>", click_clear)
cle.grid(row=r, column=c+1)


numbers = list(range(9, -1, -1))
#operators = ["+"]
for i, num in enumerate(numbers, 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=4, height=1)
    btn.bind("<1>", click_number)
    btn.grid(row=r+1, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

warubtn = tk.Button(root, text=f"/", font=("Times New Roman", 30), width=4, height=1)
warubtn.bind("<1>", click_number)
warubtn.grid(row=r-3, column=c+2)

kakebtn = tk.Button(root, text=f"*", font=("Times New Roman", 30), width=4, height=1)
kakebtn.bind("<1>", click_number)
kakebtn.grid(row=r-2, column=c+2)

maibtn = tk.Button(root, text=f"-", font=("Times New Roman", 30), width=4, height=1)
maibtn.bind("<1>", click_number)
maibtn.grid(row=r-1, column=c+2)

plubtn = tk.Button(root, text=f"+", font=("Times New Roman", 30), width=4, height=1)
plubtn.bind("<1>", click_number)
plubtn.grid(row=r, column=c+2)

btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), width=4, height=1)
btn.bind("<1>", click_equal)
btn.grid(row=r+1, column=c+2)

tenbtn = tk.Button(root, text=f".", font=("Times New Roman", 30), width=4, height=1)
tenbtn.bind("<1>", click_number)
tenbtn.grid(row=r+1, column=c+1)

root.mainloop()