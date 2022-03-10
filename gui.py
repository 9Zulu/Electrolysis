from ast import Break
import RPi.GPIO as GPIO
import time

#Mocht je trouwens willen dat dit ook door andere mensen gebruikt kan worden zet ik de Engelse vertaling erbij.

# Dit zijn de pins (fysieke board pins)/These are the physical board pins
ledin = 18
ledout = 31

# Stroomsterkte/Current
I = 1.5
# Tijd/Time
T = float()
# Volume
V = float()
# Constante van Faraday/Constant of Faraday
F = pow(9.64853365, 4)

# Geeft variabele die de user zijn keuze bepaald/Gives the variable that determines the user's choice
vort = ""

# Voor het aanzetten van de tijd op de raspberry pi/For turning on the time on the raspberry pi
formula_v = None
T = None


def ToF():
    if vort == "Tijd":
        T = int(input("Hoe lang wil je dat de machine runt? (In seconden)\n"))
        formula_v = I*T/F*24.5
        print("je krijgt dan "+ str(round(formula_v, 2)) +" in kubieke decimeter\n")
        yn = input("typ 'Y' als je wilt beginnen, typ 'N' als je wilt afbreken")

        if yn == "Y" or "y":
            circuit_T()
        else:
            print("Programma afbreken..\n")
            ToF()

    if vort == "Volume":
        V = input("Hoeveel gas wil je dat de machine maakt (in kubieke decimeter))\n")
        v = float(V)
        formula_t = v/24.5*F/I #De v/24.5 moet echt tussen haakjes anders werkt het niet meer. Je zou eventueel ook eerst v/24.5 uitrekenen en dat antwoord vervolgens toepassen in de formule.
        print("Dit duurt dan "+ str(round(formula_t, 2)) +" seconden\n")
        yn = input("typ 'Y' als je wilt beginnen, typ 'N' als je wilt afbreken")

        if yn == "Y" or "y":
            circuit_V()
        else:
            print("Programma afbreken..\n")
            ToF()

print("Welkom bij het electrolyseprogramma!")
start = input("Druk op enter om te beginnen\n")

while vort != "Tijd" or "Volume":
    vort = input("Wil je een meting doen aan de hand van volume of tijd?\n Opties: 'Tijd','Volume'\n")
    if vort == "Tijd" or "Volume":
        print("Je hebt "+ vort+ " gekozen")
        ToF()
    else:
        print("Er is iets fout gegaan, kies je meting opnieuw")
            
def circuit_V():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledout, GPIO.OUT)
    GPIO.setup(ledin, GPIO.IN)
    
    for i in range(formula_v):
        GPIO.output(ledin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(ledin, GPIO.LOW)
        time.sleep(0.2)
        print('Switch status = ', GPIO.input(ledout))
    GPIO.cleanup()

def circuit_T():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledout, GPIO.OUT)
    GPIO.setup(ledin, GPIO.IN)

    for i in range(T):
        GPIO.output(ledin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(ledin, GPIO.LOW)
        time.sleep(0.2)
        print('Switch status = ', GPIO.input(ledout))
    GPIO.cleanup()
