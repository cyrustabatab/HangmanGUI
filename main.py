import tkinter,random
from tkinter import messagebox

words = ['hello','basketball','tennis','school','college']



images= ['hangman0.png','hangman1.png','hangman2.png','hangman3.png','hangman4.png','hangman5.png','hangman6.png']


def get_random_word_and_underlines():
    '''return random word along with list of same length of underlines representing current state of guesses of user'''

    word = random.choice(words)

    underlines = ['_'] * len(word)

    return word,underlines

def reset_info_label():

    info_label['text'] = ''
    check_button['state'] = 'active'


def check_guess():
    global lives,reset_number,image,image_index
    guess = guess_entry.get()
    if not guess:
        messagebox.showerror(title='ERROR',message='Please enter a character')
        guess_entry.delete(0,tkinter.END)
    elif not guess[0].isalpha():
        guess = guess[0]
        messagebox.showerror(title='ERROR',message='Please enter a VALID character(no numbers or special characters)')
    else:
        if guess in guesses_made:
                info_label['text'] = 'Already guessed'
                info_label['fg'] = 'yellow'
                check_button['state'] = 'disabled'
                reset_number = window.after(1000,reset_info_label)

        else:
            found = False
            for i,character in enumerate(word):
                if character == guess:
                    underlines[i] = guess
                    found = True
            
            if not found:
                lives -= 1
                image_index += 1
                image = tkinter.PhotoImage(file=images[image_index])
                canvas.itemconfig(hangman_image,image=image)
                info_label['text'] = 'Incorrect'
                info_label['fg'] = 'red'
                check_button['state'] = 'disabled'
                reset_number = window.after(1000,reset_info_label)
            else:
                word_state_text['text'] = ' '.join(underlines)
                info_label['text'] = 'Correct'
                info_label['fg'] = 'green'
                check_button['state'] = 'disabled'
                reset_number = window.after(1000,reset_info_label)

            guesses_made.add(guess)



    guess_entry.delete(0,tkinter.END)

def check_length(*args):

    entry = guess_entry.get()

    if len(entry) > 1:
        guess_entry.delete(1,tkinter.END)



font = ('Arial',40,'bold')
BGCOLOR = 'white'


window = tkinter.Tk()
window.title('Hangman')
window.configure(padx=50,pady=50,bg=BGCOLOR)



title_label = tkinter.Label(text='HANGMAN',font=font,bg=BGCOLOR)
title_label.grid(row=0,column=0)


frame = tkinter.Frame(bg=BGCOLOR)
image_index = 0
canvas = tkinter.Canvas(frame,width=300,height=300,bg=BGCOLOR,highlightthickness=0)
image = tkinter.PhotoImage(file=images[image_index])
hangman_image = canvas.create_image(150,150,image=image)
canvas.grid(row=0,column=0,rowspan=2)



lives = 6
guesses_made = set()
reset_number = None
word,underlines = get_random_word_and_underlines()

word_state_text = tkinter.Label(frame,text=' '.join(underlines),bg=BGCOLOR,font=font)

word_state_text.grid(row=0,column=1)



frame_2 = tkinter.Frame(frame,bg=BGCOLOR)
guess_label = tkinter.Label(frame_2,text='Guess:',font=font,bg=BGCOLOR)
guess_label.grid(row=0,column=0)


str_var = tkinter.StringVar()

guess_entry = tkinter.Entry(frame_2,font=font,width=5,textvariable=str_var)
guess_entry.focus_set()
guess_entry.grid(row=0,column=1,padx=20)
str_var.trace('w',check_length)
frame_2.grid(row=1,column=1)


frame.grid(row=1,column=0)





info_label = tkinter.Label(text='',font=font,bg=BGCOLOR)
info_label.grid(row=2,column=0,sticky=tkinter.W)
check_button = tkinter.Button(text='Check',font=font,command=check_guess)
check_button.grid(row=2,column=0,sticky=tkinter.E)





window.mainloop()



