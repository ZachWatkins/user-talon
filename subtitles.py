from talon import speech_system, actions

def on_pre_phrase(phrase):
    words = phrase.get("phrase")

    if words and actions.speech.enabled():
        text = " ".join(words)
        show_subtitle(text)

speech_system.register("pre:phrase", on_pre_phrase)
