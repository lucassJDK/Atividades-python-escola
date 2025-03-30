def calcularImpostosESalarioLiquido(ganhoPorHora,diasTrabalhados):
    salarioTotal:float = ganhoPorHora * diasTrabalhados
    impostos:float = [salarioTotal * 0.11,salarioTotal * 0.08,salarioTotal * 0.05] #Desconto de 11% do Imposto de Renda,desconto de 8% do INSS e desconto de 5% do sindicato
    impostosSomados:float = 0
    for n in impostos:
        impostosSomados += n
    return print(f"Salário bruto:R${salarioTotal:.2f} \n valor pago ao IR:R${impostos[0]:.2f} \n valor pago ao INSS:R${impostos[1]:.2f} \n valor pago ao sindicato:R${impostos[2]:.2f} \n Salário líquido:R${salarioTotal - impostosSomados:.2f}")
ganhoPorHora:float = float(input("Digite quantos você ganha por hora: \n *"))
diasTrabalhados:int = int(input("Digite a quantidade de dias trabalhados: \n *"))
calcularImpostosESalarioLiquido(ganhoPorHora,diasTrabalhados)
