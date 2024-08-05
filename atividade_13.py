'''Crie um programa em que o usuário possa cadastrar uma lista de tarefas a fazer no dia. Após terminar, envie o link do repositório no GitHub.'''

# lista de tarefas
tarefas = []

# início do loop
while True:
    # menu
    print('1 - Inserir nova tarefa.')
    print('2 - Exibir lista de tarefas em ordem alfafabética')
    print('3 - Sair do programa.')

    # opção usuário 
    opcao = input('Opção do usuário: ')

    # verifica a opçãp escolhida
    match opcao:
        case '1':
            nova_tarefa = input('Insira a nova tarefa: ').capitalize()
            tarefas.append(nova_tarefa)
            print(f'{nova_tarefa} inserida com sucesso.')
            continue
        case '2':
            print('\n Lista de Tarefas em ordem alfabética')
            tarefas.sort()
            for tarefa in tarefas:
                print(tarefa)
            continue
        case '3':
            print('Programa encerrado')
            break
        case _:
            print('Opção inválida')

            