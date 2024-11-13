dia=(input("Escolhe um dia da semana: "))
match dia:
    case'segunda':
        atividade=Futebol
    case'terça':
        atividade:Ingles
    case'quarta':
        atividade:Python
    case'quinta':
        atividade:Musica
    case'sexta':
        atividade:Jogar
    case'sábado':
        atividade:descançar
    case'domingo':
        atividade:descançar
    case _:
        atividade=Inválido
print(atividade)