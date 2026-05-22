def atacar(nome_atacante,ataque,nome_do_defensor,hp_defensor):
    novo_hp= hp_defensor - ataque
    print(f"{nome_atacante} causou {ataque} de dano em {nome_do_defensor}!" )
    return novo_hp
def exebir_placar(nome1, hp1, nome2, hp2):
    print(f"status: {nome1}({hp1}HP) vs {nome2} ({hp2} HP)")
    print("-"*30)
nome1 = input("nome do monstro 1 ")
hp1 = int(input("HP do monstro 1 "))
ataque1 = int(input("ataque do mostro 1 "))

nome2 =input("nome do monstro 2 ")
hp2 = int(input("HP do monstor2 "))
ataque2 = int(input("ataque do monstro 2 "))

print("\n---QUE COMECE O DUELO! ----\n")

while hp1>0 and hp2>0:
    hp2 = atacar(nome1, ataque1, nome2, hp2)
    if hp2 >0 :
        hp1 = atacar(nome1, hp1, nome2, hp2)

print("===FIM DA BATALHA===")
if hp1>0:
    print(f"{nome1} VENCEU O DUELO!")
else:
    print(f"{nome1} VENCEU O DUELO!")    
