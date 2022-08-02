import PySimpleGUI as sg
import banco

sg.theme("DarkGrey")

def tela_principal():
    layout = [
        [sg.Text("Sistema de Cadastro de Escola")],
        [sg.Text("O que deseja fazer:"),sg.Button("Cadastra-se"),sg.Button("Vizualizar Dados"),sg.Button("Excluir Dados")]
    ]
    return sg.Window("Sistema de Cadastro",layout,finalize=True)

def tela_cadastro():
    layout = [
        [sg.Text("Obs: Por favor preencha todos os campos",background_color="red")],
        [sg.Text("Dados dos Alunos")],
        [sg.Text("Nome:"),sg.InputText("",key="nome_aluno")],
        [sg.Text("Idade:"),sg.InputText("",key="idade_aluno")],
        [sg.Text("Dados dos Professores")],                
        [sg.Text("Nome:"),sg.InputText("",key="nome_professor")],
        [sg.Text("Idade:"),sg.InputText("",key="idade_professor")],
        [sg.Text("Dados das Disciplinas")],
        [sg.Text("Nome:"),sg.InputText("",key="nome_disciplina")],
        [sg.Text("Turma:"),sg.InputText("",key="turma_disciplina")],
        [sg.Button("Voltar"),sg.Button("Cadastrar")]
    ]
    return sg.Window("Cadastre-se",layout,finalize=True)

def tela_excluir():
    layout = [
        [sg.Text("De qual tabela você quer excluir?")],
        [sg.Radio("Alunos","grupo_aluno",key="alunos")],
        [sg.Radio("Professores","grupo_professor",key="professores")],
        [sg.Radio("Disciplinas","grupo_disciplina",key="disciplinas")],
        [sg.Text("Qual o nome da pessoa ou disciplina que deseja excluir?"),sg.InputText("",key="nome",size=(10,5))],
        [sg.Button("Voltar"),sg.Button("Excluir")]
    ]
    return sg.Window("Excluir Dados",layout,finalize=True)

def tela_visualizar():
    layout = [
        [sg.Text("Qual tabela deseja visualizar?")],
        [sg.Radio("Alunos","grupo_alunos",key="alunos")],
        [sg.Radio("Professores","grupo_professores",key="professores")],
        [sg.Radio("Disciplinas","grupo_disciplinas",key="disciplinas")],
        [sg.Button("Voltar"),sg.Button("Consultar")],
        [sg.Text("",key="texto_colunas")],
        [sg.Listbox("",size=(40,20),key="visualizar")],
    ]
    return sg.Window("Consultar Dados",layout,finalize=True)

janela_principal = tela_principal()
janela_cadastro = None
janela_excluir = None
janela_consulta = None

while True:
    janelas,eventos,valores = sg.read_all_windows()
    if eventos == sg.WINDOW_CLOSED:
        break

    if janelas == janela_principal and eventos == "Cadastra-se":
        janela_principal.hide()
        janela_cadastro = tela_cadastro()

    if janelas == janela_cadastro and eventos == "Voltar":
        janela_cadastro.hide()
        janela_principal.un_hide()

    if janelas == janela_cadastro and eventos == "Cadastrar":
        nome_aluno = valores["nome_aluno"]
        idade_aluno = valores["idade_aluno"]
        nome_professor = valores["nome_professor"]
        idade_professor = valores["idade_professor"]
        nome_disciplina = valores["nome_disciplina"]
        turma_disciplina = valores["turma_disciplina"]
        
        if janelas == janela_cadastro and valores != "":
            banco.inserir_dados(nome_aluno,idade_aluno,nome_professor,idade_professor,nome_disciplina,turma_disciplina)
            sg.Popup("Dados inseridos com sucesso!")
    
    if janelas == janela_principal and eventos == "Excluir Dados":
        janela_principal.hide()
        janela_excluir = tela_excluir()

    if janelas == janela_excluir and eventos == "Voltar":
        janela_excluir.hide()
        janela_principal.un_hide()

    if janelas == janela_principal and eventos == "Vizualizar Dados":
        janela_principal.hide()
        janela_consulta = tela_visualizar()
    
    if janelas == janela_consulta and eventos == "Voltar":
        janela_consulta.hide()
        janela_principal.un_hide()

    if janelas == janela_consulta and eventos == "Consultar":

        if valores["alunos"] == True:
            tabela = "Alunos"
            consulta = banco.consulta_dados(tabela)
            janela_consulta["texto_colunas"].update("nome,idade,código")
            janela_consulta["visualizar"].update(consulta)
            janela_consulta["alunos"].update(False)
    
        if valores["professores"] == True:
            tabela = "professores"
            consulta = banco.consulta_dados(tabela)
            janela_consulta["texto_colunas"].update("nome,idade,código")
            janela_consulta["visualizar"].update(consulta)
            janela_consulta["professores"].update(False)

        if valores["disciplinas"] == True:
            tabela = "disciplinas"
            consulta = banco.consulta_dados(tabela)
            janela_consulta["texto_colunas"].update("nome,turma,código")
            janela_consulta["visualizar"].update(consulta)
            janela_consulta["disciplinas"].update(False)

    if janelas == janela_excluir and eventos == "Excluir":
        
        if valores["alunos"] == True:
            tabela = "alunos"
            dado = valores["nome"]
            banco.excluir_dados(tabela,dado)
            sg.Popup(f"O aluno {dado} foi excluido do banco")
            janela_excluir["alunos"].update(False)

        if valores["professores"] == True:
            tabela = "professores"
            dado = valores["nome"]
            banco.excluir_dados(tabela,dado)
            sg.Popup(f"O professsor {dado} foi excluido do banco")
            janela_excluir["professores"].update(False)

        if valores["disciplinas"] == True:
            tabela = "disciplinas"
            dado = valores["nome"]
            banco.excluir_dados(tabela,dado)
            sg.Popup(f"A disciplina {dado} foi excluida do banco")
            janela_excluir["disciplinas"].update(False)