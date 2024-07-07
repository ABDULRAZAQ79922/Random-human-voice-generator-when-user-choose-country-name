import tkinter as tk
from tkinter import ttk
import pyttsx3
import random


phrases = {
    'USA': ["Hello, how are you?", "Have a great day!", "What's up?", "Nice to meet you."],
    'UK': ["Good morning!", "How do you do?", "Cheers!", "Lovely weather, isn't it?"],
    'India': ["Namaste!", "How are you?", "Have a nice day!", "What's new with you?"],
    'Australia': ["G'day mate!", "How's it going?", "Cheers!", "See you later!"],
    'France': ["Bonjour!", "Comment ça va?", "Bonne journée!", "Enchanté!"],
    'Germany': ["Guten Tag!", "Wie geht's?", "Schönen Tag!", "Bis bald!"],
    'Spain': ["¡Hola!", "¿Cómo estás?", "¡Que tengas un buen día!", "Nos vemos!"],
    'Italy': ["Ciao!", "Come stai?", "Buona giornata!", "A presto!"]
    
}


engine = pyttsx3.init()


def set_voice_properties():
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
   


def generate_voice():
    country = country_var.get()
    if country:
        phrase = random.choice(phrases[country])
        voice_info.set(f'Generating voice for {country}: "{phrase}"')
        engine.say(phrase)
        engine.runAndWait()
    else:
        voice_info.set('Please select a country.')


root = tk.Tk()
root.title("Random Human Voice Generator")
root.geometry("500x300")
root.configure(bg='#f5f5f5')


style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12), background='#f5f5f5')
style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='#000000', background='#4CAF50')  # Green color
style.configure('TCombobox', font=('Helvetica', 12))
style.map('TButton', background=[('active', '#388E3C')]) 

country_var = tk.StringVar()
country_label = ttk.Label(root, text="Select Country:")
country_label.pack(pady=10)
country_menu = ttk.Combobox(root, textvariable=country_var)
country_menu['values'] = list(phrases.keys())
country_menu.pack(pady=5)


generate_button = ttk.Button(root, text="Generate Voice", command=generate_voice, style='TButton')
generate_button.pack(pady=20)


voice_info = tk.StringVar()
voice_label = ttk.Label(root, textvariable=voice_info, wraplength=400)
voice_label.pack(pady=10)


footer = ttk.Label(root, text="Random Human Voice Generator © 2024", font=('Helvetica', 10, 'italic'))
footer.pack(side='bottom', pady=10)


set_voice_properties()
root.mainloop()
