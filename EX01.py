import tkinter as tk
from googletrans import Translator

def translate_text():
    # Get the text to translate from the entry widget
    text_to_translate = entry.get()

    # Translate the text from English to Sinhala
    translator = Translator()
    translated_text = translator.translate(text_to_translate, src='en', dest='si')

    # Update the label with the translated text
    translated_label.config(text=translated_text.text)

# Create the main application window
app = tk.Tk()
app.title("English to Sinhala Translator")

# Create an entry widget for input
entry = tk.Entry(app, width=40)
entry.pack(pady=10)

# Create a button to trigger translation
translate_button = tk.Button(app, text="Translate", command=translate_text)
translate_button.pack()

# Create a label to display the translated text
translated_label = tk.Label(app, text="", wraplength=300)
translated_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
