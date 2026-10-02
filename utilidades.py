lista_de_aluno = []

#VERIFICAÇÃO SE IDADE E NOTA SÃO NÚMEROS CONSIDERADOS VÁLIDOS
def ler_idade():
    while True:
        try:
            idade = int(input('Digite a idade do aluno: '))
        except ValueError:
            print('Digite um número inteiro válido! ')
            continue
        if idade > 0:
            return idade
        print('A idade deve ser maior que zero! ')

#LÊ A NOTA E COLOCA "." NO LUGAR DE "," PARA NÃO DAR ERRO
 
def ler_nota():
    while True:
        try:
            nota = float(input('Digite a nota do aluno (0 a 10): ').replace(',', '.'))
        except ValueError:
            print('Digite um número válido! ')
            continue
        if 0 <= nota <= 10:
            return nota
        print('A nota deve estar entre 0 e 10! ')

#PROCURA O ALUNO PELO NOME NA LISTA, TRANSFORMANDO O VALOR EM MINÚSCULO E COMPARA COM OUTROS 

def encontrar_aluno(nome):
    for aluno in lista_de_aluno:
        if aluno['nome'].lower() == nome.lower():
            return aluno
    return None

#A FUNÇÃO STRIP SERVE PRA REMOVER OS ESPAÇOS POSSÍVEIS NAS RESPOSTAS DAS PERGUNTAS, PARA EVITAR ERROS
#CONFERE SE TEM RESPOSTA 

def adicionar_aluno():
    print('Você escolheu adicionar um aluno!')

    nome_aluno = input('Digite o nome do aluno: ').strip()
    if not nome_aluno:
        print('O nome não pode ficar vazio! ')
        return

    if encontrar_aluno(nome_aluno):
        print('Este aluno já está no sistema! ')
        return

    idade_aluno = ler_idade()
    nota_aluno = ler_nota()

    aluno = {
        'nome': nome_aluno,
        'idade': idade_aluno,
        'nota': nota_aluno
    }

    lista_de_aluno.append(aluno)
    print(f'Você adicionou o aluno {nome_aluno}! ')


def listar_alunos():
    if not lista_de_aluno:
        print('Nenhum aluno cadastrado. ')
        return

    for aluno in lista_de_aluno:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")


def buscar_alunos():
    busca_aluno = input('Qual aluno você quer buscar? ').strip()
    aluno = encontrar_aluno(busca_aluno)

    if aluno:
        print('Aluno encontrado! ')
        print('Nome:', aluno['nome'])
        print('Idade:', aluno['idade'])
        print('Nota:', aluno['nota'])
    else:
        print('O aluno não está cadastrado! ')


def remover_aluno():
    remove_aluno = input('Qual aluno você quer remover? ').strip()
    aluno = encontrar_aluno(remove_aluno)

    if aluno:
        lista_de_aluno.remove(aluno)
        print(f"O aluno {aluno['nome']} foi removido! ")
    else:
        print('O aluno não está cadastrado! ')


def media_notas():
    if not lista_de_aluno:
        print('Nenhum aluno cadastrado, não há média para calcular. ')
        return

    media = sum(aluno['nota'] for aluno in lista_de_aluno) / len(lista_de_aluno)
    print(f'A média de notas de todos os alunos é de: {media:.2f} ')