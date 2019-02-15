class Calculadora:
    primer_numero = None
    segundo_numero = None
    comdando = None
    
    def __init__(self, primer_numero=None, segundo_numero=None, comando=None):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero    
        self.comando = comando
    
    def __str__(self):
        message = "Calculadora\n"
        message += "\tprimer numero: {}\n".format(self.primer_numero)
        message += "\tsegundo numero: {}\n".format(self.segundo_numero)
        return message        

    def calcular(self):
        resultado = None
        if self.comando == "-":
            resultado = self.primer_numero - self.segundo_numero
        elif self.comando == "+":
            resultado = self.primer_numero + self.segundo_numero
        elif self.comando == "/":
            resultado = self.primer_numero / self.segundo_numero
        elif self.comando == "x":
            resultado = self.primer_numero * self.segundo_numero
        return resultado







#manejo de error
def checkear_numero(num):
    try:
        return float(num)
    except:
        print("Por favor ingrese un numero, no se haga el pelotudo")
        quit()




# control de comado
def control_de_comando(comando):
    # control de errors
    comandos = ["+", "-", "x", "/"]
    comando_correcto = False
    for i in comandos:
        if i == comando:
            comando_correcto = True
    if comando_correcto == False:
        print("Ingrese un comando correcto pelotudo")
        quit()
    return comando




#funcion principal
def main():
    print("operaciones")
    print("===========")
    print("+(suma), -(resta), /(division), x(multiplicacion)")

    primer_numero = checkear_numero(raw_input('Ingresa un numero: '))
    segundo_numero = checkear_numero(raw_input('Ingresa otro numero: '))
    comando = control_de_comando(raw_input("que operacion te gustaria "))
    
    #instanciar la calculadora
    calc = Calculadora(primer_numero, segundo_numero, comando)
    resultado = calc.calcular()
    print("El resultado es igual a (a pedido de Miguelon) {}".format(resultado))

    











def test_calculadora():
    primer_numero = 7
    segundo_numero = 8
    comando = "+"
    calc  = Calculadora(primer_numero, segundo_numero, comando)
    assert calc.calcular() == 15













if __name__ == "__main__":
    test_calculadora()
    main()


