"""
Dolar a euro: 1
Yen a euro: 0.0072
Libra a euro: 1.18
"""

text = "Coversor de divisas"

print(text + "\n" + ("-" * len(text)) + "\n")

dolar_euro = 1.00
yen_euro = 0.0072
libra_euro = 1.18

cantidad_euros = float(input("Introduce cuantos euros quieres convertir: "))

divisa_a_converir = input("A que divisa quieres convertilos:\n"
                          "D/d para convertir a dolares\n"
                          "Y/y para converit a yenes japoneses\n"
                          "L/l para converit a libras\n")
if divisa_a_converir == "D" or divisa_a_converir == "d":
    dolares = cantidad_euros / dolar_euro
    print("{} euros son {} dolares".format(cantidad_euros, dolares))
elif divisa_a_converir == "Y" or divisa_a_converir == "y":
    yenes = cantidad_euros / yen_euro
    print("{} euros son {} yenes".format(cantidad_euros, yenes))
elif divisa_a_converir == "L" or divisa_a_converir == "l":
    libras = cantidad_euros / libra_euro
    print("{} euros son {} libras".format(cantidad_euros, libras))
