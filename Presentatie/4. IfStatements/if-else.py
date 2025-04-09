##############################IF & ELSE###############################
#code
#if(<Conditie>):
#   <Code blok als de uitkomst van de conditie true is>
#Rest van de code

x=5

if(x == 5):
    print("x is gelijk aan 5")
    print("rest van het code blok")
print("Code buiten het if-else statement")

#code
#if(<Conditie>):
#   <Code blok als de uitkomst van de conditie true is>
#else:
#   <Code blok als de uitkomst van de conditie false is>
#Rest van de code

x=4

if(x == 5):
    print("x is gelijk aan 5")
else:
    print("x is niet gelijk aan 5...")
print("Code buiten het if-else statement")

#code
#if(<Conditie1>):
#   <Code blok als de uitkomst van de conditie1 true is>
#else:
#   <Code blok als de uitkomst van de conditie1 false is>
#   if(<conditie2>):
#       <Code blok als de uitkomst van de conditie1 false is en coditie2 true is>
#   else:
#       <Code blok als de uitkomst van de conditie1 false is en coditie2 false is>
#Rest van de code

x=4

if(x == 5):
    print("x is gelijk aan 5")
else:
    if(x<5):
        print("x is kleiner dan 5!")
    else:
        print("x is groter dan 5!")
print("Code buiten het if-else statement")
