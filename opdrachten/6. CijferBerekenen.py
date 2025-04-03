##Opracht
# Schrijf een programma dat op basis van een "percentage goede antwoorden" aangeeft welk cijfer iemand heeft.
# Het aantal goede antwoorden wordt per "run" van het programma random gekozen en weergegeven. (regel 14 tm 16)
# Bedenk zelf een cijfer systeem. 100 = 10 , 95 = 9.5 etc.

##TIPS:
#   1.  Gebruik 'print(<string>)' om de uitkomst van de opdracht te laten weten aan de gebruiker.
#       <string> = een door jou gekozen string.
#   2.  Verschillende strings ("text" of een variabele van type string) kunnen samengevoegd worden met de + operator.
#       Let op: de strings worden direct aan elkaar geplakt.
#   3.  Gebruik str(<variabele>) om een variabele om te zetten naar een string zodat deze geprint kan worden.

##Programma
import random
goedeAntwoorden = random.randint(1,100)
print("Het aantal goede antwoorden is " + str(goedeAntwoorden))