import os
import random
import time

# caratteri_matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\"
caratteri_matrix = "01" # Modifica i caratteri
larghezza_terminale, altezza_terminale = os.get_terminal_size()

gocce = [{'x': random.randint(0, larghezza_terminale - 1), 'y': random.randint(0, altezza_terminale - 1),
          'carattere': random.choice(caratteri_matrix)} for _ in range(100)]

while True:
    schermo = [[' ' for _ in range(larghezza_terminale)] for _ in range(altezza_terminale)]
    for goccia in gocce:
        x, y, char = goccia['x'], goccia['y'], goccia['carattere']
        schermo[y][x] = char
        goccia['y'] += 1
        if goccia['y'] >= altezza_terminale:
            goccia['y'] = 0
            goccia['x'] = random.randint(0, larghezza_terminale - 1)
            goccia['carattere'] = random.choice(caratteri_matrix)

    os.system('cls' if os.name == 'nt' else 'clear')
    for riga in schermo:
        print(''.join(riga))
    time.sleep(0.01) # Modifica il tempo
