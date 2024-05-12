def verificador_CPF (cpf_input):
    
    digito1 = cpf_input[9]
    digito2 = cpf_input[10]
    num_cpf = 0
    soma_cpf = 0
    resto_cpf = 0
    contador = 1

    if len(cpf_input) == 11:

        while contador <= 9:
            num_cpf = int(cpf_input[contador-1])*contador
            soma_cpf = soma_cpf+num_cpf
            contador += 1

        if (soma_cpf%11 != 10):
            resto_cpf = str(soma_cpf%11)

        elif (soma_cpf%11 == 10):
            resto_cpf = "0"

        contador = 0
        soma_cpf = 0
        num_cpf = 0

        while contador <= 9:
            num_cpf = int(cpf_input[contador])*contador
            soma_cpf = soma_cpf+num_cpf
            contador += 1

        if (soma_cpf%11 == 10):
            resto_cpf = resto_cpf+"0"
            
        else:
            resto_cpf = resto_cpf+str(soma_cpf%11)
              
        
    if(resto_cpf[0] == digito1 and resto_cpf[1] == digito2):
        return 1

    else:
        return 0    
    
cpf_input = input("Insira o CPF:\n")
resposta = verificador_CPF(cpf_input)

print(f"Resposta: {resposta}")