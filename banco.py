import sqlite3
banco = sqlite3.connect("escola.db")
cursor = banco.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS alunos(
    nome TEXT,
    idade INTEGER,
    codigo INTEGER PRIMARY KEY AUTOINCREMENT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS professores(
    nome TEXT,
    idade INTEGER,
    codigo INTEGER PRIMARY KEY AUTOINCREMENT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS disciplinas(
    nome TEXT,
    turma TEXT,
    codigo INTEGER PRIMARY KEY AUTOINCREMENT
)""")
banco.commit()

def inserir_dados(nome_aluno,idade_aluno,nome_professor,idade_professor,nome_disciplina,turma_disciplina):
    cursor.execute('INSERT INTO alunos (nome,idade) VALUES ("'+nome_aluno+'",'+idade_aluno+')')
    cursor.execute('INSERT INTO professores (nome,idade) VALUES ("'+nome_professor+'",'+idade_professor+')')
    cursor.execute('INSERT INTO disciplinas (nome,turma) VALUES ("'+nome_disciplina+'","'+turma_disciplina+'")')
    banco.commit()

def consulta_dados(tabela):
    cursor.execute('SELECT * FROM '+tabela+'')
    consulta = cursor.fetchall()
    banco.commit()
    return consulta

def excluir_dados(tabela,dado):
    if tabela == "alunos":
        cursor.execute('DELETE FROM alunos WHERE nome = "'+dado+'"')
    elif tabela == "professores":
        cursor.execute('DELETE FROM professores WHERE nome = "'+dado+'"')
    else:
        cursor.execute('DELETE FROM disciplinas WHERE nome = "'+dado+'"')
    banco.commit()