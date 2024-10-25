##by this we can able to save english text to audio,we can use male or female voice.

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





# import pyttsx3
# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Function to convert text to speech and save as audio file
# def save_audio():
#     text = text_entry.get("1.0", tk.END).strip()
    
#     if not text:
#         messagebox.showerror("Error", "Please enter some text!")
#         return

#     # Get the selected voice option
#     voice_option = voice_var.get()
#     voices = engine.getProperty('voices')
#     if voice_option == "Male":
#         engine.setProperty('voice', voices[0].id)  # Male voice
#     else:
#         engine.setProperty('voice', voices[1].id)  # Female voice

#     # Set speech rate and volume
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 1.0)

#     # Ask the user to select a file path to save the audio
#     save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
#                                              filetypes=[("MP3 files", "*.mp3")])

#     if save_path:
#         engine.save_to_file(text, save_path)
#         engine.runAndWait()
#         messagebox.showinfo("Success", f"Audio file saved as '{save_path}'.")

# # Create the tkinter window
# root = tk.Tk()
# root.title("Text-to-Speech Converter")

# # Create text input field
# text_label = tk.Label(root, text="Enter the text to convert:")
# text_label.pack(pady=10)

# text_entry = tk.Text(root, height=25, width=120)
# text_entry.pack(padx=10, pady=5)

# # Create a dropdown for voice selection (Male/Female)
# voice_var = tk.StringVar(value="Male")  # Default to male voice
# voice_label = tk.Label(root, text="Choose Voice:")
# voice_label.pack(pady=5)

# voice_options = tk.OptionMenu(root, voice_var, "Male", "Female")
# voice_options.pack(pady=5)

# # Create a button to save the audio file
# save_button = tk.Button(root, text="Convert and Save Audio", command=save_audio)
# save_button.pack(pady=20)

# # Run the tkinter event loop
# root.mainloop()








#---------------------

#by this we can able to convert tamil text to tamil audio.



# from gtts import gTTS
# import os

# # The text you want to convert to speech
# tamil_text = """செயற்கை நுண்ணறிவு (AI) என்பது மனிதர்களைப் போல சிந்திக்கவும் கற்றுக்கொள்ளவும் திட்டமிடப்பட்ட இயந்திரங்களில் மனித நுண்ணறிவின் உருவகப்படுத்துதலைக் குறிக்கிறது.கற்றல் மற்றும் சிக்கலைத் தீர்ப்பது போன்ற மனித மனதுடன் தொடர்புடைய பண்புகளை வெளிப்படுத்தும் எந்தவொரு இயந்திரத்திற்கும் இந்த சொல் பயன்படுத்தப்படலாம்.
# AI தொழில்நுட்பம் இரண்டு முக்கிய வகைகளாக பிரிக்கப்பட்டுள்ளது:
# குறுகிய AI (அல்லது பலவீனமான AI): முக அங்கீகாரம், மொழி மொழிபெயர்ப்பு அல்லது சதுரங்கம் விளையாடுவது போன்ற ஒரு குறிப்பிட்ட பணிக்காக வடிவமைக்கப்பட்டு பயிற்சி பெற்றது.
# பொது AI (அல்லது வலுவான AI): பகுத்தறிவு, சிக்கலைத் தீர்ப்பது அல்லது கற்றல் போன்ற ஒரு மனிதனால் செய்யக்கூடிய எந்தவொரு அறிவுசார் பணியையும் செய்வதை நோக்கமாகக் கொண்டுள்ளது.
# AI ஆராய்ச்சி மற்றும் பயன்பாட்டின் முக்கிய பகுதிகள் பின்வருமாறு:
# இயந்திர கற்றல் (எம்.எல்): வெளிப்படையாக திட்டமிடப்படாமல் இயந்திரங்களை தரவிலிருந்து கற்றுக்கொள்ளவும் அவற்றின் செயல்திறனை மேம்படுத்தவும் இயந்திரங்களை இயக்குகிறது.
# இயற்கை மொழி செயலாக்கம் (என்.எல்.பி): மனித மொழியைப் புரிந்துகொள்ளவும், விளக்கவும், உருவாக்கவும் இயந்திரங்களை அனுமதிக்கிறது.
# ரோபாட்டிக்ஸ்: சுற்றுச்சூழலுடன் தொடர்பு கொள்ள AI ஐ இயற்பியல் அமைப்புகளுடன் ஒருங்கிணைக்கிறது.
# கணினி பார்வை: படங்கள் மற்றும் வீடியோக்களிலிருந்து காட்சி தரவை விளக்கவும் புரிந்துகொள்ளவும் இயந்திரங்களை இயக்குகிறது.
# நிபுணர் அமைப்புகள்: கட்டமைக்கப்பட்ட வடிவத்தில் குறிப்பிடப்பட்டுள்ள அறிவை மேம்படுத்துவதன் மூலம் மனித முடிவெடுப்பதைப் பிரதிபலிக்கவும்.
# நரம்பியல் நெட்வொர்க்குகள்: மனித மூளை கட்டமைப்பால் ஈர்க்கப்பட்டு, இந்த நெட்வொர்க்குகள் செயலாக்குகின்றன மற்றும் தகவல்களை அனுப்புகின்றன.
# தொழில்கள் முழுவதும் AI ஏராளமான பயன்பாடுகளைக் கொண்டுள்ளது:
# உடல்நலம்: நோயறிதல், தனிப்பயனாக்கப்பட்ட மருத்துவம் மற்றும் மருத்துவ ஆராய்ச்சி.
# நிதி: இடர் மதிப்பீடு, மோசடி கண்டறிதல் மற்றும் போர்ட்ஃபோலியோ மேலாண்மை.
# போக்குவரத்து: தன்னாட்சி வாகனங்கள் மற்றும் பாதை தேர்வுமுறை.
# கல்வி: தனிப்பயனாக்கப்பட்ட கற்றல், புத்திசாலித்தனமான பயிற்சி மற்றும் தானியங்கி தரப்படுத்தல்.
# வாடிக்கையாளர் சேவை: சாட்போட்கள், மெய்நிகர் உதவியாளர்கள் மற்றும் உணர்வு பகுப்பாய்வு.
# தொழில்களை மாற்றுவதற்கும், நாம் வாழும் மற்றும் வேலை செய்யும் விதத்தில் புரட்சியை ஏற்படுத்துவதற்கும் AIS சாத்தியம் மிகப் பெரியது, மேலும் அதன் தொடர்ச்சியான வளர்ச்சி மற்றும் ஒருங்கிணைப்பு எதிர்காலத்திற்கான அதிக வாக்குறுதியைக் கொண்டுள்ளன."""

# # Specify the language code for Tamil
# language = 'ta'

# # Initialize gTTS object
# tts = gTTS(text=tamil_text, lang=language, slow=False)

# # Specify the path where the audio file will be saved
# save_path = r"C:\Text-to-Speech(Male and Female Voice)\output_tamil_voice.mp3"

# # Ensure the directory exists
# os.makedirs(os.path.dirname(save_path), exist_ok=True)

# # Save the audio file
# tts.save(save_path)

# # Notify that the audio file has been saved
# print(f"The Tamil audio file has been saved as '{save_path}'.")











# Supported Languages in gTTS:
# Afrikaans (af)
# Arabic (ar)
# Bengali (bn)
# Bosnian (bs)
# Catalan (ca)
# Czech (cs)
# Danish (da)
# Dutch (nl)
# English (en)
# Various accents: US, UK, Australia, etc.
# Filipino (fil)
# Finnish (fi)
# French (fr)
# German (de)
# Greek (el)
# Gujarati (gu)
# Hindi (hi)
# Hungarian (hu)
# Indonesian (id)
# Italian (it)
# Japanese (ja)
# Javanese (jw)
# Kannada (kn)
# Khmer (km)
# Korean (ko)
# Latin (la)
# Latvian (lv)
# Malayalam (ml)
# Mandarin Chinese (zh-CN)
# Marathi (mr)
# Nepali (ne)
# Norwegian (no)
# Polish (pl)
# Portuguese (pt)
# Brazil: pt-BR, Portugal: pt-PT
# Punjabi (pa)
# Romanian (ro)
# Russian (ru)
# Serbian (sr)
# Sinhala (si)
# Slovak (sk)
# Spanish (es)
# Variants: Spain: es-ES, Latin America: es-419
# Sundanese (su)
# Swahili (sw)
# Swedish (sv)
# Tamil (ta)
# Telugu (te)
# Thai (th)
# Turkish (tr)
# Ukrainian (uk)
# Urdu (ur)
# Vietnamese (vi)
# Welsh (cy)







#######################

# # by this we can able to transulate english text to other language audio

# from gtts import gTTS
# from googletrans import Translator
# import os


# # # The text you want to convert to speech
# english_text = """The Human mind is a vast stretch of the Universe he delves in.
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

  
# “If you want to succeed, you should strike out on new paths, rather than  travel the worn paths of accepted success."""


# # Translate English text to Tamil
# translator = Translator()
# translated_text = translator.translate(english_text, dest='ta').text

# # Initialize gTTS object with the translated Tamil text
# tts = gTTS(text=translated_text, lang='ta', slow=False)

# # Specify the path to save the audio file
# save_path = r"C:\Text-to-Speech(Male and Female Voice)\output_tamil2_voice.mp3"
# os.makedirs(os.path.dirname(save_path), exist_ok=True)

# # Save the audio file
# tts.save(save_path)

# print(f"The Tamil audio file has been saved as '{save_path}'.")







import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from gtts import gTTS
from googletrans import Translator, LANGUAGES
import os

# Initialize translator
translator = Translator()

def translate_and_save():
    # Get text from Text widget
    text_to_translate = text_input.get("1.0", tk.END).strip()
    if not text_to_translate:
        messagebox.showerror("Error", "Please enter text to translate.")
        return

    # Get the selected target language code
    target_lang_code = lang_var.get()
    
    # Translate text to the selected language
    translated_text = translator.translate(text_to_translate, dest=target_lang_code).text
    
    # Get save path from user
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                              filetypes=[("MP3 files", "*.mp3")],
                                              title="Save Translated Audio File")
    if not save_path:
        return
    
    # Initialize gTTS object with translated text
    tts = gTTS(text=translated_text, lang=target_lang_code, slow=False)
    
    # Save the audio file
    tts.save(save_path)
    messagebox.showinfo("Success", f"Audio saved successfully as {save_path}")

# Create main Tkinter window
root = tk.Tk()
root.title("Text-to-Speech Translator")
root.geometry("600x600")

# Add a label and text box for text input
label = tk.Label(root, text="Enter Your Text:", font=("Arial", 14))
label.pack(pady=10)
text_input = tk.Text(root, wrap=tk.WORD, font=("Arial", 12),  width=70, height=15)
text_input.pack(padx=20, pady=10)

# Add a dropdown menu for language selection
lang_var = tk.StringVar(root)
lang_var.set("ta")  # Set default to Tamil
lang_label = tk.Label(root, text="Select Target Language:", font=("Arial", 12))
lang_label.pack(pady=5)
lang_menu = ttk.Combobox(root, textvariable=lang_var, values=list(LANGUAGES.keys()), state="readonly", font=("Arial", 12))
lang_menu.pack()

# Add a button to translate and generate audio
translate_button = tk.Button(root, text="Translate and Save as Audio",
                              font=("Arial", 12), command=translate_and_save)
translate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
























