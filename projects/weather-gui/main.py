import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight=.08, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=.65, relheight=1)

btn = tk.Button(frame, text='test button', font=40)
btn.place(relx=0.7, relwidth=.3, relheight=1)



lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=.25, relwidth=.75, relheight=.6,anchor='n')

label = tk.Label(lower_frame, bg='yellow')
label.place(relwidth=1, relheight=1)

# btn.pack(side='left', fill='both', expand=True)
# btn.grid(row=0, column=0)



# label.pack(side='left')
# label.grid(row=0, column=1)



root.mainloop()

