import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight=.1, anchor='n')

btn = tk.Button(frame, text='test button', bg='gray', fg='red')
btn.place(relx=0, rely=0, relwidth=.25, relheight=.25)
# btn.pack(side='left', fill='both', expand=True)
# btn.grid(row=0, column=0)

label = tk.Label(frame, text='This is a label', bg='yellow')
label.place(relx=.3, rely=0, relwidth=0.45, relheight=.25)
# label.pack(side='left')
# label.grid(row=0, column=1)

entry = tk.Entry(frame, bg='green')
entry.place(relx=.8, rely=0, relwidth=.2, relheight=.25)
# entry.grid(row=0, column=2)

root.mainloop()

