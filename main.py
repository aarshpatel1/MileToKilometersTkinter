import tkinter

# Tk class
window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label class
label = tkinter.Label(text="Hello World", font=("Courier", 24, "bold"))
label.pack()
label["text"] = "It is new label."
label.config(font=("Arial", 24, "bold"))


# Button class
def button_clicked():
    # print("I got clicked")
    # label["text"] = "Button got clicked."
    # label.config(font=("Arial", 24, "bold"))
    label["text"] = entry.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry class
entry = tkinter.Entry(width=15)
entry.pack()

window.mainloop()
