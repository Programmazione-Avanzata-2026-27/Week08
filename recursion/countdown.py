from time import sleep

# Contare da 10 a 1 in maniera ricorsiva
def countdown(n):
    if n==0:
        return # Esco dalla ricorsione
    else:
        print(n)
        sleep(1)
        print(f"Chiamo la funzione con {n-1}")
        countdown(n-1)
        print(f"Esco dalla funzione")


countdown(10)
print("Finito il programma")