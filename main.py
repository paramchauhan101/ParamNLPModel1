import spacy
import nltk
from fuzzywuzzy import process
from nltk.sentiment import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]

predefined_qas = {
    "what is your name?": "My name is ParamNLPModel1",
    "how’s it going": "It's going well, thanks for asking!",
    "what’s up": "Not much, just here to chat with you.",
    "how have you been": "I've been great! How about you?",
    "how’s life treating you": "Life's good, can't complain.",
    "what’s new": "Not much, what about you?",
    "how’s everything": "Everything's fine, thanks for asking.",
    "how’s your day going": "My day is going well, how about yours?",
    "how’s your week been": "My week has been good, how has yours been?",
    "how’s work/school": "It's going well. How about yours?",
    "what’s happening": "Not much, what's happening with you?",
    "what’s the good word": "The good word is 'Chatbot'!",
    "how’s it hanging": "It's hanging just fine, thank you.",
    "how’s your day so far": "My day has been good so far, how about yours?",
    "anything exciting happening": "Nothing too exciting, what about you?",
    "how’s your morning/afternoon/evening": "It's been good, how about yours?",
    "what’s the latest": "Not much, just keeping up with things.",
    "how’s your family": "My family is great, how's yours?",
    "how’s your health": "My health is good, thank you for asking.",
    "how are things": "Things are going well, how about with you?",
    "how’s your mood today": "I'm feeling good, how about you?",
    "what’s been keeping you busy": "Just chatting with people like you!",
    "how’s the weather treating you": "Weather's fine, how is it there?",
    "how’s your weekend going": "My weekend is going well, how about yours?",
    "how did you spend your weekend": "I spent my weekend relaxing, how about you?",
    "how’s your schedule looking today": "Pretty open, how about yours?",
    "how’s your energy level": "I’m feeling energized, how about you?",
    "how’s your mental health": "My mental health is good, thank you for asking.",
    "how’s your sleep lately": "I’ve been sleeping well, how about you?",
    "what’s been on your mind": "Just thinking about conversations!",
    "how’s your coffee/tea today": "My coffee/tea is great, thank you!"
}

def correct_spelling(text, choices):
    corrected_text = []
    for word in text.split():
        best_match = process.extractOne(word, choices)
        if best_match and best_match[1] > 80:
            corrected_text.append(best_match[0])
        else:
            corrected_text.append(word)
    return ' '.join(corrected_text)

def get_greeting_response(text):
    for word in text.split():
        if word.lower() in greetings:
            return "Hello! How can I help you today?"
    return None

def get_predefined_response(text):
    text = text.lower()
    for question in predefined_qas:
        if question in text:
            return predefined_qas[question]
    return None

def analyze_emotion(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return "You seem happy!"
    elif sentiment['compound'] <= -0.05:
        return "You seem sad."
    else:
        return "You seem neutral."

def chatbot_response(user_input):
    corrected_input = correct_spelling(user_input, greetings + list(predefined_qas.keys()))
    response = get_greeting_response(corrected_input)
    if response:
        return response
    response = get_predefined_response(corrected_input)
    if response:
        return response
    emotion_response = analyze_emotion(corrected_input)
    return emotion_response

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot_response(user_input)
    print(f"ParamNLPModel1: {response}")
