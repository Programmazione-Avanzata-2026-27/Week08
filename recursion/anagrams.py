
class Anagrams:
    def __init__(self):
        pass

    def recursion(self, anagramma_parziale, lettere_rimanenti):
        if len(lettere_rimanenti)==0: # Finito le lettere
            print(anagramma_parziale)
        else:
            for i in range(len(lettere_rimanenti)):
                anagramma_parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.recursion(anagramma_parziale, nuove_lettere_rimanenti)
                anagramma_parziale = anagramma_parziale[:-1]

anagram = Anagrams()
anagram.recursion("", "dog")


