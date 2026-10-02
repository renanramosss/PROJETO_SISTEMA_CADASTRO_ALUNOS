#SISTEMA DE CADASTRO DE ALUNOS

from utilidades import adicionar_aluno, listar_alunos, buscar_alunos, remover_aluno, media_notas

while True:
    print('''
     SISTEMA DE CADASTRO DE ALUNOS!
     1. Adicionar aluno
     2. Listar todos os alunos
     3. Buscar aluno pelo nome
     4. Remover aluno
     5. Mostrar média geral das notas
     6. Sair ''')

    opcao = input('Digite o número correspondente ao que deseja: ').strip()

    if opcao == '1':
        adicionar_aluno()

    elif opcao == '2':
        listar_alunos()

    elif opcao == '3':
        buscar_alunos()

    elif opcao == '4':
        remover_aluno()

    elif opcao == '5':
        media_notas()

    elif opcao == '6':
        print('Encerrando... ')
        break

    else:
        print('Digite uma opção válida! ')