reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético', 
'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético', 'Etanol', 'Acetona', 
'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona', 'Metanol', 'Ácido Sulfúrico', 
'Acetona', 'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
'2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01',
'2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02',
'2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01',
'2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
'2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01', '2024-ETA-01']

pureza = [99.5, 98.2, 99.5, 95.0, 99.8, 97.5, 98.0, 96.2, 99.1, 94.5, 
          99.5, 98.2, 96.0, 98.0, 99.8, 95.0, 99.1, 98.5, 99.5, 98.2, 
          94.5, 99.0, 99.8, 99.5, 98.2, 99.1, 95.0, 99.0, 98.5, 99.8]

reagentes_unicos = set(reagentes)
print(f"Reagentes únicos disponíveis: {reagentes_unicos}\n")

inventario_completo = list(zip(reagentes, lotes, pureza))

print("Frascos com pureza superior a 95%:")
frascos_alta_pureza = [
    (nome, lote, p) 
    for nome, lote, p in inventario_completo 
    if p > 95.0
]

for nome, lote, p in frascos_alta_pureza:
    print(f"- Reagente: {nome} | Lote: {lote} | Pureza: {p}%")
