from tkinter import *

FONT = ("Arial", 12, "normal")


def miles_to_kms():
    miles = float(mile_entry.get())
    kilometers = round(miles * 1.609344, 3)
    kilometers_answer["text"] = kilometers


window = Tk()
window.title("Mile to Kilometers converter")
window.config(padx=20, pady=50)
# window.minsize(width=200,height=100)

mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

kilometers_answer = Label(text="0", font=FONT)
kilometers_answer.grid(column=1, row=1)
kilometers_answer.config(padx=10, pady=10)

kilometers_label = Label(text="Kilometers", font=FONT)
kilometers_label.grid(column=2, row=1)
kilometers_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", font=FONT, command=miles_to_kms)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=5, pady=5)

window.mainloop()
