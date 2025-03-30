area:float = float(input("Insira a área em m²: \n *"))
quantidadeLitrosNecessarios:float = area / 3 
numeroDeLatas:float = quantidadeLitrosNecessarios / 18
numeroDeLatasInt:int = quantidadeLitrosNecessarios // 18
print(f"O número de latas necessárias sera de:{ 1 + numeroDeLatasInt}\n preço a pagar pelas latas:R${(1 + numeroDeLatasInt) * 80:.2f}") if(numeroDeLatas > numeroDeLatasInt) else print(f"O número de latas necessárias será de:{numeroDeLatasInt} \n O preço total a pagar pelas latas será de: R${numeroDeLatasInt * 80:.2f}")
