
print('*****Bienvenidos al corrector de texto*******')
print()
while True:
    print("-------MENU INTERACTIVO----------")
    print()
    print("1. Formalizar texto. ")
    print("2. Convertir texto a mayuscula. ")
    print("3. Convertir texto a minuscula. ")
    print("4. Salir")
    print()
    elegir = input('Elija su accion: ')

    if elegir == "1":
        texto = input("Ingrese su texto a formalizar: ")
        print()
        texto1 = input(f'Asi que este es su texto a formalizar:\n{texto} - Desea formalizarlo? ')
        if texto1.lower() == 'si':
            texto_formalizado = texto.strip().capitalize()
            print()
            print(f'Su texto formalizado es:\n{texto_formalizado}')
            print()
            print()
        else:
            print()
            print("Regresando al programa....")
            print()

    elif elegir == "2":
        texto = input("Ingrese su texto a convertir a mayusculas: ")
        print()
        texto1 = input(f"Asi que el texto que desea convertir a mayusculas es:\n{texto} - Desea convertirlo? ")
        if texto1.lower() == 'si':
            texto_formalizado = texto.strip().upper()
            print()
            print(f"Su texto en mayusculas es:\n{texto_formalizado}")
            print()
            print()
        else:
            print()
            print("Regresando al programa....")
            print()


    elif elegir == "3":
        texto = input("Ingrese su texto a convertir a minusculas: ")
        print()
        texto1 = input(f"Asi que el texto que desea convertir a minusculas es:\n{texto} - Desea convertirlo? ")
        if texto1.lower() == 'si':
            texto_formalizado = texto.strip().lower()
            print()
            print(f"Su texto en minusculas es:\n{texto_formalizado}")
            print()
            print()
        else:
            print()
            print("Regresando al programa....")
            print()

 
    elif elegir == "4":
        print()
        print("Muchas gracias por probar nuestro programa!\n\nEsperamos le haya gustado.             Desarrollado por \'Yensi\' ")
        break
                       



    
