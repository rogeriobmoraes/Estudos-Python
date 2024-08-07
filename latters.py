def main(): #Inicio da funcao main
    name = ["Mario", "Luigi", "Daise", "Yoshi"] #Declaracao da minha lista 
    for i in range(len(name)): #Estrutura for para percorrer minha lista, a cada interacao for recebe o valor do ince atual
        print(write_latter(name[i], "Princess Peach")) #Denro do print esta a chamada para a funcao write_latter
       


def write_latter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """



main() #Chamada a funcao main -> inicio do pprgrama