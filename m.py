from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
global score

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.minsize(height=650, width=850)


def random_word():
    data_file = pd.read_csv("data/french_words.csv")
    df = data_file.to_dict(orient="records")
    ran = random.randint(1, len(df) - 1)
    return ran


def new_word():
    random_number = random_word()
    word_label["text"] = df[random_number]["French"]


card_back = PhotoImage(file="images/card_back.png")


def show_eng():
    canvas.create_image(405, 270, image=card_back)
    random_number = random_word()
    word_label.config(fill="white")
    word_label["text"] = df[random_number]["English"]
    print("Fliped")


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

data_file = pd.read_csv("data/french_words.csv")
df = data_file.to_dict(orient="records")
random_num = random_word()

language_label = Label(text="French")
language_label.config(font=("Arial", 40, "italic"), background="white")
language_label.grid(column=0, row=0)
language_label.place(x=300, y=80)

word_label = Label(text=df[random_num]["French"])
word_label.config(font=("Arial", 60, "bold"), background="white")
word_label.grid(column=0, row=0)
word_label.place(x=270, y=210)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=new_word)
right_button.config(highlightthickness=0, relief='ridge')
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, relief='ridge', command=new_word)
wrong_button.config(highlightthickness=0, pady=50)
wrong_button.grid(column=0, row=1)

window.after(3000, show_eng)
window.mainloop()
