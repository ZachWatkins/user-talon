from talon import noise, speech_system

def on_pop(active):
    speech_system.engine_mimic("wake up"),
noise.register("pop", on_pop)

def on_hiss(active):
    speech_system.engine_mimic("go to sleep"),
noise.register("hiss", on_hiss)
