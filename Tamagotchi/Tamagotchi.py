import time
import random

def hehe():
    
    i = True
    list_of_phrases = ["Tamagatchi is sleeping....","Tamagatchi is eating....","Tamagatchi is playing video games....","Tamagatchi is bathing...."]
    while i == True:
        for i in range(100):
            print(list_of_phrases[random.randint(0,3)])
            time.sleep(random.randint(1,30))
    
    hehe()

hehe()