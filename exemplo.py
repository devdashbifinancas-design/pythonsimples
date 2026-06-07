# Meu primeiro programa em Python

nome = input("Digite seu nome: ")

print("Olá,", nome + "! Seja bem-vindo ao Python.")
# Sistema simples de avaliação de filmes

filme = input("Digite o nome do filme: ")
nota = float(input("Digite a nota do filme (0 a 10): "))

print("\nFilme:", filme)
print("Nota:", nota)

if nota >= 8:
    print("Excelente filme!")
elif nota >= 6:
    print("Bom filme!")
else:
    print("Filme regular ou ruim.")
    print("curso")