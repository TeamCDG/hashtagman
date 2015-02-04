from random import *

true = True
false = False

None if False else None

greetings = [
    "Urusai",
    "Zatknis",
    "Hallo!",
    "Merde",
    "Theophilus stultus est",
    "Greetings summoner"
    ]

li = ['KATZENKLO', 'MEDIZINBALL', 'SCHNEEMANN',
         'AUTOBAHN', 'SCHULBUS', 'RHABARBERSAFT', 'HIPPOGREIF']

version = "#HashtagMan v0.1.0a2"

def partSol(tip, sol):
    """
    Beispiel:
    >>> partSol('AEDKLM', 'KATZENKLO')
    'KA__E_KL_'
    """

    x = "".ljust(len(sol),  "_")
    for i in range(len(sol)):
        if sol[i] in tip:
           x =  x[:i] + sol[i] + x[i+1:]
    return x

def hits(tip, sol):
    """
    Beispiel:
    >>> hits('AEDKLM', 'KATZENKLO')
    5
    """
    h = 0
    for i in range(len(sol)):
        if sol[i] in tip:
            h += 1
    return h

def falseChars(tip, sol):
    """
    Beispiel:
    >>> falseChars('AEDKLM', 'KATZENKLO')
    'DM'
    """
    f = ""
    for c in tip:
        if not c in sol:
            f += c
    return f

def rightChoice(tip, sol):
    """
    >>> rightChoice('AEDKLM', 'KATZENKLO')
    False
    >>> rightChoice('AEDKLMNTZO', 'KATZENKLO')
    True
    """

    r = true
    for c in sol:
        if not c in tip:
            r  = false
            break
    return r

def greeting():
    """
    Gibt zufällig eine passende Begrüßung zurück.
    """
    return greetings[randint(0, len(greetings)-1)]

def guess():
    tip = ""
    print(version, ": ", greeting())
    sol = li[randint(0, len(li)-1)]
    maxf = 10
    curf = 0

    while not rightChoice(tip, sol) and curf < maxf:
        print(partSol(tip, sol))
        print("faults "+str(curf)+" / "+str(maxf)+": "+falseChars(tip, sol))
        c = input("tip: ").upper()[0]
        if(len(falseChars(c, sol)) > 0):
            curf +=1
        tip += c

    if(rightChoice(tip, sol)):
        print("sieg")
    else:
        print("niederlage")

#guess()

from doctest import testmod
#testmod(verbose=True)
