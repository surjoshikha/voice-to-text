import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

# Function to capture voice and convert to text
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label["text"] = "Listening..."
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="en-US")
            text_output.insert(tk.END, text + "\n")
            status_label["text"] = "Voice captured successfully!"
        except sr.UnknownValueError:
            status_label["text"] = "Sorry, could not understand the audio."
        except sr.RequestError as e:
            status_label["text"] = f"API Error: {e}"
        except Exception as e:
            status_label["text"] = f"Error: {e}"

# GUI Setup
root = tk.Tk()
root.title("Voice-to-Text Interface")
root.geometry("500x300")

# Header
header_label = tk.Label(root, text="Voice-to-Text", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# Output Text Box
text_output = tk.Text(root, height=10, width=50, font=("Arial", 12))
text_output.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

# Button to Start Voice Recognition
voice_button = ttk.Button(root, text="Speak", command=voice_to_text)
voice_button.pack(pady=10)

# Run the GUI
root.mainloop()

