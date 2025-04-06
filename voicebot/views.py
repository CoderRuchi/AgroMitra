from django.shortcuts import render, redirect
from .voice_assistant import listen, speak, translate_text, generate_agriculture_response, is_conversation_end
from django.http import JsonResponse

def talk(request):
    # Initialize conversation history if it doesn't exist in session
    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []

    # Initialize variables
    user_input = ""
    translated = ""
    bot_response = ""
    continuous_mode = False
    conversation_ended = False
    selected_lang = "en"  # Default to English

    if request.method == "POST":
        # Check if clear history button was clicked
        if request.POST.get("clear_history") == "true":
            # Clear the conversation history
            request.session['conversation_history'] = []
            request.session.modified = True
            return redirect('talk')

        # Check if it's a continuous mode request
        continuous_mode = request.POST.get("continuous_mode") == "true"

        # Get language selection
        lang_code = request.POST.get("lang")
        print(f"Selected language from form: {lang_code}")

        # Map language names to language codes
        lang_map = {
            'english': 'en',
            'hindi': 'hi',
            'marathi': 'mr',
            'gujarati': 'gu',
            'tamil': 'ta',
            'telugu': 'te'
        }

        # Get the language code, default to English
        selected_lang = lang_map.get(lang_code, 'en')
        print(f"Mapped to language code: {selected_lang}")

        # If starting continuous mode, add a welcome message
        if continuous_mode and not request.session['conversation_history']:
            welcome_msg = "Welcome to continuous conversation mode. I'll listen to your questions until you say 'bye'. What would you like to know about agriculture?"
            welcome_translated = translate_text(welcome_msg, dest_lang=selected_lang)
            speak(welcome_translated, language=selected_lang)

            # Add to conversation history
            request.session['conversation_history'].append({
                'user_input': '',
                'bot_response': welcome_msg,
                'translated': welcome_translated
            })
            request.session.modified = True

        # Get user input via speech recognition
        user_input = listen(language_code=f"{selected_lang}-IN")

        # Generate a meaningful response using the agriculture response generator
        # Pass the conversation history for context-aware responses
        bot_response = generate_agriculture_response(user_input, request.session.get('conversation_history', []))

        # Check if conversation should end
        conversation_ended = is_conversation_end(user_input)

        # Translate the response to the selected language
        translated = translate_text(bot_response, dest_lang=selected_lang)

        # Speak the translated response and get the audio file path
        print(f"Calling speak() with language: {selected_lang}")
        audio_path = speak(translated, language=selected_lang)
        print(f"Received audio_path: {audio_path}")

        # Add to conversation history
        request.session['conversation_history'].append({
            'user_input': user_input,
            'bot_response': bot_response,
            'translated': translated,
            'audio_path': audio_path
        })
        request.session.modified = True

        # If conversation ended, clear the history
        if conversation_ended:
            request.session['conversation_history'] = []
            request.session.modified = True

    # For AJAX requests, return JSON response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'user_input': user_input,
            'bot_response': bot_response,
            'translated': translated,
            'conversation_ended': conversation_ended,
            'conversation_history': request.session.get('conversation_history', [])
        })

    # For regular requests, render the template
    return render(request, "voicebot/talk.html", {
        "user_input": user_input,
        "translated": translated,
        "bot_response": bot_response,
        "conversation_history": request.session.get('conversation_history', []),
        "selected_lang": selected_lang
    })
