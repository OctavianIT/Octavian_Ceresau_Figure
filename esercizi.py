a = "Perimetro Quadrato"
b = "Circoferenza Cerchio"
c = "Perimetro Rettangolo"

while True:
    print(f"\nScegli cosa vuoi calcolare: \na){a} \nb){b} \nc){c}")
    risposta = input(f"Riposta: ")

    if risposta == a:
        cmQuad = float (input("\nDimensione lato Quadrato (in cm): "))
        print (f"{cmQuad*4} cm")
        again = input("\nVuoi calcolare un'altra figura?(si/no) \n")
        if again == "si":
            continue
        elif again:
            break

    elif risposta == b:
        cmCerchio = float (input("\nDimensione raggio Cerchio (in cm): "))
        print ((cmCerchio*2)*3.14)
        again = input("\nVuoi calcolare un'altra figura?(si/no) \n")
        if again == "si":
            continue
        elif again:
            break
        

    elif risposta == c:
        cmRettangolo_base = float(input("\nDimensione base Rettangolo (in cm): "))
        cmRettangolo_h = float(input("\nDimensione altezza Rettangolo (in cm): "))
        print (f"{(cmRettangolo_base*2)+(cmRettangolo_h*2)}cm")
        again = input("\nVuoi calcolare un'altra figura?(si/no) \n")
        if again == "si":
            continue
        elif again:
            break

        

    elif risposta:
        print("\n")
        print("\n-- Riscrivi la figura come da elenco --\n")
        continue














