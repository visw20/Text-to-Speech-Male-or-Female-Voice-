
# import pyttsx3
# import os

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Get the available voices
# voices = engine.getProperty('voices')

# # Set the voice to male (usually the first voice is male, but you can loop through to find others)
# engine.setProperty('voice', voices[0].id)  # Use voices[1] for female voice 0 for male voice

# # Set the speech rate (optional, default is 200 words per minute)
# engine.setProperty('rate', 150)  # Adjust the rate as needed

# # Set the volume (optional, default is 1.0, max is 1.0)
# engine.setProperty('volume', 1.0)  # Adjust the volume as needed

# # The text you want to convert to speech
# text = """The Human mind is a vast stretch of the Universe he delves in.
# Unlike the Universe a Human Mind can be expanded and stretched beyond Unlimited boundaries.

# Now, Imagine the existence of this mysterious and Beautiful Mind inside each of us.

# So Why are we discussing about man and mind ?

# That's because we are going to deep dive into the mindsets of Billionaires and what sets them apart from a common man.

# What do you think made him or her think differently ?

# We are bringing to you a new web series that explores that minding and journeys of the most successful women enterpreneurs and billionaires.


# what does it truly mean to possess the mindset of a billionaire?This questions is at the core of our endeavour.
# we belive that the billionaire mindset encompasses a journey of self-improvement,the audacious setting of colossal goals,the willingness to embrace and manage risks,an unwavering commitment to action even when plans for awry,
# a dedication to continuous self improvement and an unquenchable and an unquenchable thirst for excellence.


# Our mission is to engage in candid conversations with some of the world’s most influential  and successful individuals, digging into their life experiences, influences, pivotal moments  and personal growth trajectories.
 
# Through in-depth interviews, psychological analysis, and comprehensive storytelling, we aim  to shed light on the cognitive patterns, behavioural traits and life philosophies that underpin  the Billionaire mindset. 
# We believe their experiences and wisdom will leave a lasting legacy by inspiring and  educating future generations of leaders and entrepreneurs.
 

# Join us in this extraordinary journey as we unveil the billionaire mindset and inspire a world  of dreamers, doers, and future leaders. Together, we can empower individuals to transcend their limits and achieve greatness.

  
# “If you want to succeed, you should strike out on new paths, rather than  travel the worn paths of accepted success.” 
# -John Rockefeller"""

# # Specify the path where the audio file will be saved
# save_path = r"C:\Text-to-Speech(Male and Female Voice)\output_male_voice.mp3"

# # Ensure the directory exists
# os.makedirs(os.path.dirname(save_path), exist_ok=True)

# # Convert the text to speech and save it as an audio file
# engine.save_to_file(text, save_path)

# # Run the engine to process the speech conversion
# engine.runAndWait()

# # Notify that the audio file has been saved
# print(f"The audio file has been saved as '{save_path}'.")




# engine.setProperty('voice', voices[1].id)  # Switch to female voice
# engine.setProperty('rate', 200)  # Faster speech
# engine.setProperty('volume', 0.8)  # Slightly lower volume





import pyttsx3
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech and save as audio file
def save_audio():
    text = text_entry.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Get the selected voice option
    voice_option = voice_var.get()
    voices = engine.getProperty('voices')
    if voice_option == "Male":
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice

    # Set speech rate and volume
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    # Ask the user to select a file path to save the audio
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes=[("MP3 files", "*.mp3")])

    if save_path:
        engine.save_to_file(text, save_path)
        engine.runAndWait()
        messagebox.showinfo("Success", f"Audio file saved as '{save_path}'.")

# Create the tkinter window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create text input field
text_label = tk.Label(root, text="Enter the text to convert:")
text_label.pack(pady=10)

text_entry = tk.Text(root, height=25, width=120)
text_entry.pack(padx=10, pady=5)

# Create a dropdown for voice selection (Male/Female)
voice_var = tk.StringVar(value="Male")  # Default to male voice
voice_label = tk.Label(root, text="Choose Voice:")
voice_label.pack(pady=5)

voice_options = tk.OptionMenu(root, voice_var, "Male", "Female")
voice_options.pack(pady=5)

# Create a button to save the audio file
save_button = tk.Button(root, text="Convert and Save Audio", command=save_audio)
save_button.pack(pady=20)

# Run the tkinter event loop
root.mainloop()




