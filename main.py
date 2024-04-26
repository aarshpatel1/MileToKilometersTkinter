import tkinter

# Tk class
window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label class
label = tkinter.Label(text="Hello World", font=("Courier", 24, "bold"))
label["text"] = "It is new label."
label.config(font=("Arial", 24, "bold"))
label.grid(column=0, row=0)


# Button class
def button_clicked():
    # print("I got clicked")
    # label["text"] = "Button got clicked."
    # label.config(font=("Arial", 24, "bold"))
    label["text"] = entry.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Click Here")
new_button.grid(column=2, row=0)

# Entry class
entry = tkinter.Entry(width=15)
entry.grid(column=3, row=4)

window.mainloop()
