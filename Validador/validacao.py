def formula_magica(resultado):
    digito_obtido = (resultado * 10) % 11
    digito_obtido = digito_obtido if digito_obtido <= 9 else 0
    return str(digito_obtido)

def verifica_digito(cpf):
    primeiros_nove = cpf[:9]
    contador = 10
    resultado = 0
    for digito in primeiros_nove:
        resultado += int(digito) * contador
        contador -= 1
    decimo_digito = formula_magica(resultado)

    contador += 10
    resultado *= 0
    primeiros_dez = primeiros_nove + decimo_digito

    for digito in primeiros_dez:
        resultado += int(digito) * contador
        contador -= 1
    decimopri_digito = formula_magica(resultado)

    return decimo_digito + decimopri_digito

def validador_cpf(data = None):
    if int(data):
        cpf = str(data)
    else:
        cpf = data
    if "." in cpf:
        caracteres = ['.', '-']
        for i in caracteres:
            cpf = cpf.replace(i, '')
    validacao = str(verifica_digito(cpf))

    if validacao in cpf[9:]:
        print(f'O CPF: {cpf} é Validado')
    else:
        print('CPF Invalido')