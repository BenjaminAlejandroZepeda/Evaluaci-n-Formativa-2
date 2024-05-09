"""formativa"""

pikachu = 0
Otaku = 0
pulpoVen = 0
anguila = 0
MENU2 = False
opc = 0
MENU1 = True
Dest = False
code = "soyotaku"
descuento = 0
SUBSUBTOTAL = 0
codes = False
while MENU1 is True:
    print(f"""
        Delivery de Sushi
            MENU
    =======================
    1. Pikachu Roll $4500 pedidos:{pikachu}
    2. Otaku Roll $5000  Pedidos:{Otaku}
    3. Pulpo Venenoso Roll $5200 Pedidos :{pulpoVen}
    4. Anguila Eléctrica Roll $4800 Pedidos:{anguila}
    5. Terminar pedido
    6. Cerrar
    """)
    try:
        opc = int(input("Elija una opción: "))
    except:
        print("Elija una Opción valida por favor....")
        opc = 0

    if opc == 1:
        print("agregado!!")
        pikachu = pikachu+1
    elif opc == 2:
        print("agregado!!")
        Otaku = Otaku+1
    elif opc == 3:
        print("agregado!!")
        pulpoVen = pulpoVen+1
    elif opc == 4:
        print("agregado!!")
        anguila = anguila+1
    elif opc == 5:
        productos = pikachu+Otaku+pulpoVen+anguila
        print(f"""
        el total de productos es: {productos}
        Código de descuento: soyotaku
            """)
        codes = True

        while codes is True:
            codigoIn = (input("Escriba el Código de descuento: "))

            if codigoIn == code:
                print("Código valido")
                Dest = True
                codes = False
            elif codigoIn == "X":
                print("**********")
                break
            else:
                print("""
                    Código invalido o expirado
                    Intente nuevamente o escriba : X , para salir""")

        pikachu = pikachu*4500
        Otaku = Otaku*5000
        pulpoVen = pulpoVen*5200
        anguila = anguila*4800
        SUBTOTAL = pikachu+Otaku+pulpoVen+anguila

        if Dest is True:
            descuento = SUBTOTAL*0.1
            SUBSUBTOTAL = SUBTOTAL*0.9
            TOTAL = SUBSUBTOTAL
        else:
            TOTAL = SUBTOTAL

        print(f"""""Calculando total....
    1. Pikachu Roll: {pikachu}
    2. Otaku Roll: {Otaku}
    3. Pulpo Venenoso Roll: {pulpoVen}
    4. Anguila Eléctrica Roll: {anguila}
    ================================
    Subtotal: $ {SUBTOTAL}
    Descuento: $ {descuento}
    Total: $ {TOTAL}
        """)
        MENU2 = True

        while MENU2 is True:
            print("""
                1. Terminar pedido y salir
                2. Terminar pedido y volver al menu
                """)
            try:
                opc = int(input("Elija una opción: "))
            except ValueError:
                print("Elija una Opción valida por favor....")

            if opc == 1:
                print(""" 
                    PAGO REALIZADO.....
                    Que tenga un buen dia....
                    """)
                MENU1 = False
                break
            elif opc == 2:
                print("""     
                    PAGO REALIZADO......
                    Volviendo al menu.....""")
                pikachu = 0
                Otaku = 0
                pulpoVen = 0
                anguila = 0
                MENU2 = False
                opc = 0
                MENU1 = True
                Dest = False
                code = "soyotaku"
                descuento = 0
                SUBSUBTOTAL = 0
                codes = False
                break

    elif opc == 6:
        print("cerrando....")
        break
    else:
        print("Ingrese una Opción valida")
        opc = 0
