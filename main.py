from import_stats import *


def change_back(kan_word):
    canvas.itemconfig(canvas_image_main, image=back_img)
    canvas.itemconfig(title, text="ಕನ್ನಡ", fill="white")
    canvas.itemconfig(word, text=kan_word, fill="white")


def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0, 1002)
    kan_word = data_dict['Kannada'][index]
    eng_word = data_dict['English'][index]
    canvas.itemconfig(canvas_image_main, image=canvas_img)
    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(word, text=eng_word, fill="black")
    flip_timer = window.after(3000, change_back, kan_word)


BACKGROUND_COLOR = "#B1DDC6"
data_dict = pd.DataFrame(pd.read_csv("data/english_to_kan.csv")).to_dict()
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(width=800, height=526)
canvas_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image_main = canvas.create_image(400, 263, image=canvas_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(0)
canvas.grid(row=0, column=0, columnspan=2)
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
flip_timer = window.after(0,next_card )


window.mainloop()
