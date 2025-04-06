import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
from chatbot.utils import AgricultureResponseGenerator

def listen(language_code='en-IN'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=language_code)
        return text
    except:
        return "Sorry, I could not understand."

def speak(text, language='en'):
    # For debugging
    print(f"speak() called with language: {language}, text: {text[:50]}...")

    # If language is English, we'll still generate audio for consistency
    # This ensures audio works for all languages including English

    # Limit text length to reduce file size and generation time
    max_chars = 300
    if len(text) > max_chars:
        text = text[:max_chars] + "..."

    try:
        # Create a unique filename based on timestamp to avoid conflicts
        import time
        import random

        # Simple timestamp-based filename to avoid any hashing issues
        timestamp = int(time.time())
        random_num = random.randint(1000, 9999)
        filename = f"audio_{timestamp}_{random_num}.mp3"

        # Create media directory if it doesn't exist
        media_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media', 'audio')
        os.makedirs(media_dir, exist_ok=True)

        # Full path to the audio file
        filepath = os.path.join(media_dir, filename)
        print(f"Will save audio to: {filepath}")

        # Generate and save the audio file with optimized settings
        # Force lang parameter to a supported language code
        lang_code = language
        if language == 'en':
            lang_code = 'en'
        elif language not in ['hi', 'mr', 'gu', 'ta', 'te']:
            # Default to Hindi if language not supported
            lang_code = 'hi'

        print(f"Using language code: {lang_code} for gTTS")

        # Create the gTTS object and save the file
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(filepath)

        # Verify the file was created
        if os.path.exists(filepath):
            print(f"Audio file successfully created at: {filepath}")
            file_size = os.path.getsize(filepath)
            print(f"File size: {file_size} bytes")
        else:
            print(f"Failed to create audio file at: {filepath}")
            return None

        # Return the path to the audio file for the frontend to use
        relative_path = f"/media/audio/{filename}"
        print(f"Returning relative path: {relative_path}")
        return relative_path

    except Exception as e:
        print(f"Error generating audio: {str(e)}")
        import traceback
        traceback.print_exc()
        # Return None to indicate that audio generation failed
        return None

def translate_text(text, dest_lang):
    # If destination language is English, no need to translate
    if dest_lang == 'en':
        return text

    translator = Translator()
    result = translator.translate(text, dest=dest_lang)
    return result.text

def generate_agriculture_response(user_input, conversation_history=None):
    """
    Generate a response to the user's agriculture-related query

    Args:
        user_input (str): The user's question or message
        conversation_history (list, optional): List of previous messages for context
    """
    if not user_input or user_input == "Sorry, I could not understand.":
        return "I'm here to help with your agricultural questions. Please ask about crops, soil, weather, or farming practices."

    # Check if user wants to end the conversation
    if is_conversation_end(user_input):
        return "Thank you for using the agricultural voice assistant. Goodbye!"

    # Use the AgricultureResponseGenerator to get a response with conversation history for context
    return AgricultureResponseGenerator.generate_response(user_input, conversation_history)

def is_conversation_end(user_input):
    """
    Check if the user wants to end the conversation
    """
    if not user_input:
        return False

    # Convert to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # List of phrases that indicate the user wants to end the conversation
    end_phrases = [
        'bye', 'goodbye', 'exit', 'quit', 'stop', 'end',
        'thank you bye', 'thanks bye', 'bye bye', 'see you', 'see you later'
    ]

    # Check if any of the end phrases are in the user input
    for phrase in end_phrases:
        if phrase in user_input:
            return True

    return False
