import pyttsx3

# Initialize the text-to-speech engine
text_to_speech_engine = pyttsx3.init()

# Text to be converted to speech
intro_text = '''
    Hello! I'm Fathima Sheerin, and I specialize in Data Science and Machine Learning. 
    I enjoy working on projects that combine my love for technology and solving real-world problems.
'''

# Convert text to speech
text_to_speech_engine.say(intro_text)

# Run the speech engine
text_to_speech_engine.runAndWait()
