orçamento_total = float(input("digite o orçamento total em reais(BRL): "))
destino = input( "digite o nome da cidade/paísde destino:  ")
custo_passagem = float( input ("digite o custo da passagem em reais (BRL)"))
custo_diario_euro = float(input("digite o custo diario da hospedagem em euro(EUR): "))
quantidade_de_dias = int(input("digite a quantidade de dias da viagem: "))
hospedagem_total_BRL = (custo_diario_euro*6.10)
custo_total = custo_passagem + hospedagem_total_BRL
print("-------------------------")
print("custo total da hospedagem em BRL: R$", custo_total)
if orçamento_total >= custo_total:
    print("Sucesso! Seu orçamento é suficiente.")
else:
    faltante = custo_total - orçamento_total
    print("orçamento insuficiente.")
    print("faltam para completar a viagem : R$", faltante)
          