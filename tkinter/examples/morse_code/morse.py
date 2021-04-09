# Morse Code Translator
from threading import Thread
from time import sleep
from tkinter import Tk, Toplevel, Text, END, DISABLED, NORMAL, \
    BOTH, X, Y, LEFT, RIGHT, BOTTOM
from tkinter.ttk import Label, Button, Frame

from PIL import ImageTk
from playsound import playsound

# morse code dictionaries
english_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' ', '|': '|', '': '',
}

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])


class Guide(Toplevel):
    def __init__(self, app, **kwargs):
        super().__init__(app.root, **kwargs)
        self.title("Morse Guide")
        self.geometry(f'350x350+{self.master.winfo_x() + 400}+{self.master.winfo_y()}')
        self.protocol("WM_DELETE_WINDOW", app.hide_guide)
        self.bind('<Escape>', app.hide_guide)

        # Create the Image, Label, and pack
        self.morse = ImageTk.PhotoImage(file='morse_chart.png')  # to keep in memory
        Label(self, image=self.morse).pack(padx=10, pady=10, ipadx=5, ipady=5)

        Button(self, text="Close", command=app.hide_guide).pack(padx=10, ipadx=50)


class ButtonFrame(Frame):
    def __init__(self, app, **kwargs):
        super().__init__(app.root, **kwargs)
        self.guide_button = Button(self, text="Guide", command=app.show_guide)
        self.guide_button.pack(fill=X, ipadx=20, ipady=2, padx=(10, 5), pady=5)

        Button(self, text="Clear", command=app.clear) \
            .pack(fill=X, ipadx=20, ipady=2, padx=(10, 5), pady=5)

        Button(self, text="🔊 Play Morse", command=app.play) \
            .pack(side=BOTTOM, fill=X, ipadx=20, ipady=2, padx=(10, 5), pady=5)


class RightFrame(Frame):
    def __init__(self, app, **kwargs):
        super().__init__(app.root, **kwargs)
        self.eng_text = Text(self, height=8, width=40)
        self.eng_text.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.eng_text.focus()

        child_frame = Frame(self)
        Button(child_frame, text="⇩ To Morse", command=app.to_morse) \
            .pack(side=LEFT, fill=X, expand=True, padx=5)
        Label(child_frame, text="↓↑").pack(side=LEFT)
        Button(child_frame, text="⇧ To English", command=app.to_english) \
            .pack(side=RIGHT, fill=X, expand=True, padx=5)
        child_frame.pack(fill=X)

        self.morse_text = Text(self, height=8, width=40)
        self.morse_text.pack(fill=BOTH, expand=True, padx=5, pady=5)


class App:
    """Controller"""

    def __init__(self):
        self.root = Tk()
        self.root.title('Morse Code Translator')
        self.root.minsize(400, 280)
        # self.root.resizable(False, False)

        self.guide = None  # Guide window (lazy instantiation)

        self.button_frame = ButtonFrame(self)
        self.button_frame.pack(side=LEFT, fill=Y)

        self.right_frame = RightFrame(self)
        self.right_frame.pack(fill=BOTH, expand=True)

        self.root.bind('<F1>', self.show_guide)

    def run(self):
        self.root.mainloop()

    def to_morse(self):
        """Convert an English message to morse code"""

        # Get the input text and standardize it to lower case
        text = self.right_frame.eng_text.get("1.0", END)
        text = text.lower()

        # Remove any letters or symbols not in our dict keys
        for letter in text:
            if letter not in english_to_morse.keys():
                text = text.replace(letter, "")

        # String to hold morse code message
        morse_code = ""

        # Break up into individual words based on space " " and put into a list
        word_list = text.split(" ")

        # Turn each individual word in word_list into a list of letters
        for word in word_list:
            letters = list(word)
            # For each letter, get the morse code representation and append it to the string morse code
            for letter in letters:
                morse_char = english_to_morse[letter]
                morse_code += morse_char
                # Separate individual letters with a space
                morse_code += " "
            # Separate individual words with a |
            morse_code += "|"

        self.right_frame.morse_text.insert("1.0", morse_code)

    def to_english(self):
        """Convert a morse code message to english"""

        # Get the input text
        text = self.right_frame.morse_text.get("1.0", END)

        # Remove any letters or symbols not in our dict keys
        for letter in text:
            if letter not in morse_to_english.keys():
                text = text.replace(letter, "")

        # String to hold English message
        english = ""

        # Break up each word based on | and put into a list
        word_list = text.split("|")

        # Turn each word into a list of letters
        for word in word_list:
            letters = word.split(" ")
            # For each letter, get the English representation and add it to the string English
            for letter in letters:
                english_char = morse_to_english[letter]
                english += english_char
            # separate individual words with a space
            english += " "

        self.right_frame.eng_text.insert("1.0", english)

    def clear(self):
        """Clear both text fields"""
        self.right_frame.eng_text.delete("1.0", END)
        self.right_frame.morse_text.delete("1.0", END)

    def play(self):
        """Play tones for corresponding dots and dashes"""

        def task():
            # Play the tones (., -, " " , |)
            text = self.right_frame.morse_text.get("1.0", END)
            for value in text:
                if value == ".":
                    playsound('dot.mp3')
                    sleep(0.1)
                elif value == "-":
                    playsound('dash.mp3')
                    sleep(0.2)
                elif value == " ":
                    sleep(0.3)
                elif value == "|":
                    sleep(0.5)

        Thread(target=task).start()

    def show_guide(self, *args):
        """Show a morse code guide in a second window"""
        # Guide window
        if self.guide:
            self.guide.state('normal')
        else:
            self.guide = Guide(self)
        self.guide.focus()

        # Disable the guide button
        self.button_frame.guide_button.config(state=DISABLED)

    def hide_guide(self, *args):
        """Hide the guide"""
        self.guide.state('withdrawn')
        self.button_frame.guide_button.config(state=NORMAL)


if __name__ == '__main__':
    App().run()
