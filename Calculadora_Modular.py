def sumaModular():
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            sumaModular()
        if a < mod:
            a = a % mod
        else:
            if b < mod:
                b = b % mod
        suma = a + b
        suma = suma % mod
        return suma
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        sumaModular()


def multiplicacionModular():
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            multiplicacionModular()
        if a < mod:
            a = a % mod
        else:
            if b < mod:
                b = b % mod
        multiplicacion = a * b
        multiplicacion = multiplicacion % mod
        return multiplicacion
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        multiplicacionModular()


def divisionModular():
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            divisionModular()
        if a < mod:
            a = a % mod
        else:
            if b < mod:
                b = b % mod
        inverso = modInverse(b, mod)
        inverso = str(inverso)
        if not inverso.isdigit():
            return f"Su segundo valor no tiene inverso, vuelva a intentarlo"
        else:
            inverso = int(inverso)
            division = (a * inverso) % mod
            return division
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        divisionModular()


def potenciaModular():
    try:
        a = int(input("Ingrese el numero base: "))
        b = int(input("Ingrese la potencia de su numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            potenciaModular()
        potencia = (a ** b) % mod
        return potencia
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        potenciaModular()


def raizCuadradaModular():
    try:
        valor = int(input("Ingrese el numero de la raiz: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while valor <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            raizCuadradaModular()
        valor = valor % mod
        raices = []
        for x in range(0, mod):
            a = x * x
            if a % mod == valor:
                raices.append(x)

        if len(raices) > 0:
            lst_raices = str(raices)[1:-1]
            print("Las raices cuadradas son:", lst_raices)

        if len(raices) == 0:
            print("La raiz cuadrada modular no existe, vuelve a intentarlo")
        return
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        raizCuadradaModular()


def modInverse(A, M):
    try:
        for X in range(1, M):
            if ((A % M) * (X % M)) % M == 1:
                return X
        return f"No tiene inverso modular"
    except:
        print("No tiene inverso")

    try:
        resultado = int(input("Ingrese un numero: "))
        mod = int(input("Ingrese el mod (Zn): "))
        print("El inverso del nùmero es:", modInverse(resultado, mod))
    except ValueError:
        print("Debes ingresar un valor numerico")
    except NameError:
        print("Debes ingresar un valor numerico")


def listaInversos():
    try:
        M = int(input("Ingrese el mod (Zn): "))
        if M <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            listaInversos()

        inversos = {}
        for A in range(0, M):
            for X in range(1, M):
                operacion = (A % M) * (X % M)
                if operacion % M == 1:
                    inversos[A] = X

        if len(inversos) > 0:
            for x, y in inversos.items():
                print(f"El inverso de {x} en mod {M} es {y}")
        if len(inversos) == 0:
            print("Su numero no tiene inversos, vuelva a intentarlo")
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        listaInversos()


def cuadradosPerfectos():
    try:
        mod = int(input("Ingrese el modulo (Zn): "))
        lst_cuadrados = []
        for x in range(0, mod):
            a = (x * x) % mod
            lst_cuadrados.append(a)
        lst_cuadrados = set(lst_cuadrados)
        lst_cuadrados = str(lst_cuadrados)[1:-1]
        print(f"Los cuadrados perfectos de {mod} son {lst_cuadrados}")
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        cuadradosPerfectos()


def ValidarNumeroModulo():
    try:
        a = int(input("Ingrese el primer numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        modulovalido = a % mod
        return modulovalido
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        ValidarNumeroModulo()


# MENU DE LA CALCULADORA:
print(
    "-------------------------------------------------------------------------------------------------------------------")

print("♠️----BIENVENIDO A LA CALCULADORA MODULAR----♠️")
print("❤️ ----Por favor tome su tiempo y revise todas las opciones a usar:")

print(
    "-------------------------------------------------------------------------------------------------------------------")


def menuCalculadora():
    try:
        print("1. Suma modular")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("2. Multiplicacion Modular")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("3. Division Modular")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("4. Potencia Modular")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("5. Raiz cuadrada modular")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("6. Lista de inversos modulares para Zn")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("7. Cuadrados perfectos modulares (lista y cantidad de raices)")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("8. Hallar el inverso de un numero en Zn")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("9. Hallar el modulo de un numero negativo")
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        opcion = int(input("Ingresa la operacion que deseas realizar: "))
        print(
            "-------------------------------------------------------------------------------------------------------------------")

        print("==" * 22)
        if opcion == 1:
            print("El resultado de su suma es:", sumaModular())
        elif opcion == 2:
            print("El resultado de su multiplicacion es:", multiplicacionModular())
        elif opcion == 3:
            print("El resultado de su division es:", divisionModular())
        elif opcion == 4:
            print("El resultado de su potencia modular es:", potenciaModular())
        elif opcion == 5:
            raizCuadradaModular()
        elif opcion == 6:
            listaInversos()
        elif opcion == 7:
            cuadradosPerfectos()
        elif opcion == 8:
            resultado = int(input("Ingrese un numero: "))
            mod = int(input("Ingrese el mod (Zn): "))
            print("El inverso del numero es:", modInverse(resultado, mod))
        elif opcion == 9:
            print("El resultado de su modulo es:", ValidarNumeroModulo())
        else:
            print("Ingrese un valor valido")
            menuCalculadora()

        while True:
            newTry = input("Desea volver a intentarlo? (s/n): ")
            if newTry == "n" or newTry == "N":
                exit()
            elif newTry == "s" or newTry == "S":
                menuCalculadora()
            else:
                print("Ingrese un valor valido")
                input("Desea volver a intentarlo? (s/n): ")
    except ValueError:
        print("Debes ingresar un valor numerico, vuelve a intentarlo")
        menuCalculadora()


menuCalculadora()
