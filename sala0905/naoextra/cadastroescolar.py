print ("---qual seu setor?-----------")
print ("--- 1 setor dos alunos-------")
print ("--- 2 setor dos professores--")
print ("--- 3 setor financeiro-------")
resp = int(input("insira o numero de seu setor"))
match resp:
    case 1:
        nome = str(input("insira seu nome"))
        nota1 = int(input("insira primeira nota"))
        nota2 = int(input("insira sua segunda nota"))
        notatotal = (nota1 + nota2)/2
        if notatotal >= 70:
            print ("aprovado")
        elif notatotal < 70 and notatotal >= 40:
            print("recuperação")
        else:
            print("reprovado")
    case 2:
        nome = str(input("insira seu nome professor"))
        titulacao = str(input("diga sua titulação professor"))
        if titulacao == "mestrado" or titulacao == "doutorado":
            print (f"vc esta apto a orientar projetos {nome}")
        elif titulacao == "graduado":
            print (f"vc esta apenas apto a dar aulas {nome}")
        else:
            print("titulacao invalida")
    case 3:
        categoria = int(input("selecione sua categoria 1- aluno 2- professor"))
        match categoria:
            case 1:
                pagar = int(input("pague sua mensalidade R$1000"))
                if pagar < 1000:
                    print("pagamento insuficiente")
            case 2:
                valorhora = int(input("insira o valor de suas horas trabalhadas"))
                valorhoratotal = valorhora * 160
                horaextra = int(input("quantas horas extras voce trabalhou?"))
                salarioextra = horaextra * (valorhora/2)
                salariototal = valorhoratotal + salarioextra
                print(f"seu salario é {salariototal}")
