pessoa = { 
    "infop": {
        "nome": "Rogerio",
        "idade": 28,
        "peso": 78.5,
        "altura": "1.71",
        "sexo": "M",
    },
    "infocont": {
        "email": "exemplo@exemplo.com",
        "celular": 93984252064,
        "endereco": "Rua 13, Buenos Aires, Argentina",
        "datas": {
            "datanasc": "13/10/1994",
            "dianiver": "13/10",
            "datacasam": "11/01",
        }
    }
}

for chave, valor in pessoa.items():
    print(f"{chave}:")
    for subchave, subvalor in valor.items():
        if subchave == "datas" and isinstance(subvalor, dict):  # Verifica se a chave é 'datas' e o valor é um dicionário
            print(f"  {subchave}:")
            for subsubchave, subsubvalor in subvalor.items():
                print(f"    {subsubchave}: {subsubvalor}")
        else:
            print(f"  {subchave}: {subvalor}")
