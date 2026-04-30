nomes = []
notas = []
cursos = []

n = int(input("Quantos alunos deseja cadastrar? "))

for i in range(n):
    print("\nAluno", i + 1)
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    curso = input("Curso (ccp/tads): ").lower()
    
    nomes.append(nome)
    notas.append(nota)
    cursos.append(curso)

qtd_tads = 0
for curso in cursos:
    if curso == "tads":
        qtd_tads += 1

soma = 0
for nota in notas:
    soma += nota

media = soma / n if n > 0 else 0

acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1

print("\n RESULTADOS")
print("Quantidade de alunos de TADS:", qtd_tads)
print("Média das notas:", media)
print("Quantidade de alunos com nota acima da média:", acima_media)