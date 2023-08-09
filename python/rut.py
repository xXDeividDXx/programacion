def digito_verificador(rut):
    rut = str(rut)
    suma = 0
    multiplicador = 2
    for i in range(len(rut)-1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    dv = 11 - resto
    if dv == 10:
        return 'K'
    elif dv == 11:
        return '0'
    else:
        return str(dv)
    
rut = input("Hola, digite su rut sin el digito verificador: ")
dv = digito_verificador(rut)
dv_comparativo = input("Digite su digito verificador:")
if (dv == dv_comparativo):
    print("Su RUT es valido.")
else:
    print("Su RUT es falsificao ermanito.")    