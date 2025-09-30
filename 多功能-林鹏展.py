import tkinter as A
from tkinter import ttk as B, messagebox as C, filedialog as D
import time as E
import random as F

def G(event=None):
    try:
        H = eval(I.get())
        I.delete(0, A.END)
        I.insert(A.END, str(H))
    except Exception as J:
        C.showerror("Error", f"Invalid expression\n{J}")

def K():
    L = E.strftime('%H:%M:%S')
    M.config(text=L)
    N.after(1000, K)

def O():
    I.delete(0, A.END)

def P():
    Q = I.get()
    if Q:
        I.delete(len(Q)-1, A.END)

def R():
    S = D.asksaveasfilename(defaultextension=".txt",
                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if S:
        with open(S, 'w') as T:
            T.write(U.get(1.0, A.END))

def V(W):
    X1, Y1 = (W.x - 1), (W.y - 1)
    X2, Y2 = (W.x + 1), (W.y + 1)
    Z.create_oval(X1, Y1, X2, Y2, fill="black", width=2)

def a():
    Z.delete("all")

def b():
    for c in d:
        e = f.coords(c["id"])
        if e[2] >= f.winfo_width() or e[0] <= 0:
            c["dx"] = -c["dx"]
        if e[3] >= f.winfo_height() or e[1] <= 0:
            c["dy"] = -c["dy"]
        f.move(c["id"], c["dx"], c["dy"])
    N.after(50, b)

N = A.Tk()
N.title("多功能窗口")
N.geometry("1300x700")

g = A.PhotoImage(file="15.png")
f = A.Canvas(N, width=1600, height=750)
f.place(x=100, y=100, relwidth=1, relheight=1)
f.create_image(0, 0, image=g, anchor='nw')

I = A.Entry(N, width=40, font=('Arial', 14))
I.bind("<Return>", G)
I.grid(row=0, column=0, columnspan=4, pady=10)

h = ["red", "green", "blue", "yellow", "purple", "orange"]
d = []

for i in range(20):
    j, k = F.randint(0, 1580), F.randint(0, 730)
    l, m = F.choice([-3, -2, -1, 1, 2, 3]), F.choice([-3, -2, -1, 1, 2, 3])
    n = F.choice(h)
    o = f.create_oval(j, k, j+20, k+20, fill=n)
    d.append({"id": o, "dx": l, "dy": m})

b()

I = A.Entry(N, width=40, font=('Arial', 14))
I.bind("<Return>", G)
I.grid(row=1, column=0, columnspan=4, pady=10)

p = [
    ('7', 'light blue'), ('8', 'light green'), ('9', 'light pink'), ('/', 'light yellow'),
    ('4', 'light blue'), ('5', 'light green'), ('6', 'light pink'), ('*', 'light yellow'),
    ('1', 'light blue'), ('2', 'light green'), ('3', 'light pink'), ('-', 'light yellow'),
    ('0', 'light blue'), ('.', 'light green'), ('=', 'light pink'), ('+', 'light yellow'),
    ('(', 'light blue'), (')', 'light green'), ('C', 'light pink'), ('DEL', 'light yellow')
]

q, r = 2, 0
for s, t in p:
    if s == '=':
        A.Button(N, text=s, font=('Arial', 14), bg=t, command=G).grid(row=q, column=r, columnspan=2, sticky="nsew", padx=5, pady=5)
        r += 1
    elif s == 'C':
        A.Button(N, text=s, font=('Arial', 14), bg=t, command=O).grid(row=q, column=r, sticky="nsew", padx=5, pady=5)
    elif s == 'DEL':
        A.Button(N, text=s, font=('Arial', 14), bg=t, command=P).grid(row=q, column=r, sticky="nsew", padx=5, pady=5)
    else:
        A.Button(N, text=s, font=('Arial', 14), bg=t, command=lambda u=s: I.insert(A.END, u)).grid(row=q, column=r, sticky="nsew", padx=5, pady=5)

    r += 1
    if r > 3:
        r = 0
        q += 1

M = A.Label(N, font=('calibri', 20, 'bold'), background='purple', foreground='white')
M.grid(row=q, column=0, columnspan=4, pady=10)
K()

q += 1
U = A.Text(N, height=10, font=('Arial', 14))
U.grid(row=q, column=0, columnspan=4, padx=10, pady=10)
v = A.Button(N, text="保存记事本", font=('Arial', 14), bg='light cyan', command=R)
v.grid(row=q+1, column=0, columnspan=4, pady=10)

Z = A.Canvas(N, bg="white", width=200, height=200)
Z.grid(row=0, column=4, rowspan=6, padx=10, pady=10)
Z.bind("<B1-Motion>", V)

w = A.Button(N, text="清空画板", font=('Arial', 14), bg='light salmon', command=a)
w.grid(row=6, column=4, pady=10)

N.mainloop()
