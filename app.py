import os

from modelos.restaurante import Restaurante

restaurantes = []

def exibir_nome_programa():
    print('''
                    
            ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
            ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
            ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
            ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
            ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
            ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
                        ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Estado do Restaurante')
    print('''4. Sair
            ''')

def finalizar_app():
    exibir_subtitulo('''Finalizando o app
        ''')

def opcao_invalida():
    print('Opção Inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para retornar ao menu principal.')
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\n✔ O restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes cadastrados: ')

    print(f"{'Nome do Restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | Status")
    print()

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'✔ - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante...')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso! ' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso! '
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        print()
        #opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Emi',8)
restaurante_praca.receber_avaliacao('Lais',5)
restaurante_oshiro = Restaurante('Oshiro Sushi','Sushi')
restaurante_oshiro.alternar_estado()
restaurante_dory = Restaurante('Dory Sushi','Sushi Gourmet')

Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()