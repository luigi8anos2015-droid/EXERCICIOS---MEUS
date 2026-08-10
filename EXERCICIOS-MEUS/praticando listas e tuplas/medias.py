notas = input("Digite as notas dos alunos separadas por vírgula: ").split(",")
nota=[float(nota) for nota in notas]
media = sum(nota) / len(notas)
print(f"Média final da turma: {media:.2f}")