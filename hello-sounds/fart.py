from playsound import playsound
import random

farts = (
    'fart-1.wav',
    'fart-2.wav',
    'fart-3.wav',
    'fart-4.wav'
)

for i in range(0, 2):
    fart_index = random.randint(0, len(farts) - 1)
    playsound(farts[fart_index])
