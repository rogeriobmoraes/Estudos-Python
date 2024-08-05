#Adicionar frutas a um lista de frutas

def listafrutas():
    frutas = ['maçã', 'banana', 'cereja']
    print(frutas)  # Mostra a lista de frutas

def nomefruta(frutas):
    nova_fruta = input("Digite o nome da fruta a ser adicionada na lista: ")
    frutas.append(nova_fruta)  # Adiciona o nome da fruta à lista

# Exemplo de uso
lista = ['maçã', 'banana', 'cereja']
listafrutas()  # Exibe a lista inicial
nomefruta(lista)  # Adiciona uma nova fruta à lista
print(lista)  # Mostra a lista atualizada