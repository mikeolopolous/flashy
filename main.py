import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_img)
lang_text = canvas.create_text(400, 150, text="language", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

cross_image = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=cross_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=check_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
