from Validador import validacao
if __name__ == "__main__" :
    print("Digite seu CPF: \n")
    cpf = input()
    print(validacao.validador_cpf(cpf))
