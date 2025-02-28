from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3", lang='en', slow=False):
    try:
        # Create gTTS object
        speech = gTTS(text=text, lang=lang, slow=slow)
        
        # Save the audio file
        speech.save(filename)
        
        print(f"Audio saved as {filename}")
        return filename
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
        return None



##Test
text = "vanakkam"

output_file = text_to_speech(text, filename="example.mp3")

if output_file:
    # os.system("start example.mp3")  # For Windows
    # os.system("afplay example.mp3")  # For macOS
    os.system("mpg321 example.mp3")  # For Linux
