from tkinter import *
import pandas
import json
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = dict()
to_learn = dict()

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_clock
    window.after_cancel(flip_clock)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_clock = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text= "English", fill="white")
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")
    canvas.itemconfig(card_background, image= card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Language Learning")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_clock = window.after(3000, func=flip_card)

card_back_img = PhotoImage(file= "images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")


#french_words_list = data.French.to_list()
#print(french_words_list)
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 250, text="", fill="black", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()


window.mainloop()

