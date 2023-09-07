def numero_a_letras(numero ):

    #parte_entera, parte_decimal = numero.split(".")
    #parte_entera = int(parte_entera) 
    #parte_decimal = int(parte_decimal) 

    if isinstance(numero, int):  # Número entero
        parte_entera = numero
        parte_decimal = 0
    elif isinstance(numero, float):  # Número decimal
        parte_entera, parte_decimal = str(numero).split(".")
        if(len(parte_decimal)>6):
            return "Decimales fuera de rango"
        parte_decimal = int(parte_decimal)       
    else:
        return "Entrada inválida"

    if(numero > 999999999999999999999999):
        return 'Numero fuera de rango'
    
    unidades = ['', 'un', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    veinte = ['veinte', 'veintiuno', 'veintidos', 'veintitres', 'veinticuatro', 'veintecinco', 'veinteseis', 'veintesiete', 'veinteocho', 'veintenueve']
    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
    escalas = ['', 'mil', 'millones', 'mil', 'billones', 'mil', 'trillones', 'mil']
    escalas_decimales = ['decimos', 'centesimos', 'milesimos', 'diezmilesimos', 'cienmilesimos', 'millonesimos']

    def convertir_a_palabras(num):
        """" Recibe Numeros de 3 Digitos """
        if num == 0:    
            return 'cero'
        elif num < 10:
            return unidades[num]
        elif num < 20:
            return especiales[num - 10]
        elif num < 30:
            return veinte[num - 20]
        elif num < 100:
            return decenas[num // 10] + ('' if num % 10 == 0 else ' y ' + convertir_a_palabras(num % 10))
        elif num < 1000:
            return centenas[num // 100] + ('' if num % 100 == 0 else ' ' + convertir_a_palabras(num % 100))

    grupos = []
    num_str = str(parte_entera)
    while len(num_str) > 0:
        grupos.insert(0, num_str[-3:])
        num_str = num_str[:-3]

    palabras = []
    for i, grupo in enumerate(grupos):
        grupo_int = int(grupo)
        if grupo_int != 0:
            palabras.append(convertir_a_palabras(grupo_int) + ' ' + escalas[len(grupos) - i - 1])
  
    if parte_decimal:
        return ' '.join(palabras) + 'con ' + numero_a_letras(parte_decimal) + escalas_decimales[len(str(numero).split(".")[1])-1]
    else:    
        return ' '.join(palabras)



    