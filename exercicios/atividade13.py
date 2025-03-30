def calcularPeso(altura,genero):
    if(genero > 2 or genero < 1) : return print("Digite um gênero válido!")
    print(f"seu peso ideal como homem é:{72.7 * altura - 58:.2f}KG") if(genero == 1) else print(f"Seu peso ideal como mulher é:{62.1 * altura - 44.7:.2f}KG")

altura:float = float(input("Digite sua altura em metros:"))
genero:int = int(input("Digite 1 para homem e 2 para mulher:"))
calcularPeso(altura,genero)