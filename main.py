import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="Inglés")
    canvas.itemconfig(word_text, text=current_card["English"])


def flip_card():
    canvas.itemconfig(lang_text, text="Español", fill="white")
    canvas.itemconfig(word_text, text=current_card["Spanish"], fill="white")
    canvas.itemconfig(background_card, image=back_img)


def is_known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file="./images/card_front.png")
back_img = tk.PhotoImage(file="./images/card_back.png")
background_card = canvas.create_image(400, 263, image=front_img)
lang_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

cross_image = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=cross_image,
                         highlightbackground=BACKGROUND_COLOR,
                         highlightthickness=0,
                         command=next_card)
wrong_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=check_image,
                         highlightbackground=BACKGROUND_COLOR,
                         highlightthickness=0,
                         command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
