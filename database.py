import sqlite3

class BancoDeDados:
    """
Classe que representa o banco de dados (database) da aplicaçao
"""

    def __init__(self, nome = 'banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        #conecta passando o nome do arquivo
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        #Desconecata do banco
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criarTabelas(self):
        #Cria as tabelas do banco
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
                    email TEXT NOT NULL
                );
            """)
        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def inserirCliente(self, nome, cpf, email):
        #Insere cliente no banco
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute("""
                    INSERT INTO clientes(nome, cpf, email)
                        VALUES(?,?, ?)
                """, (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe' % cpf)                

            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes')

    def buscarCliente(self, cpf):
        #Busca um cliente pelo cpf
        try:
            cursor = self.conexao.cursor()

            #obtém todos os dados
            cursor.execute("""
                SELECT * FROM clientes;
            """)

            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print('Cliente %s encontrado.' % linha[1])
                    break
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def removerCliente(self, cpf):
        #Remove Cliente pelo cpf
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""DELETE FROM clientes WHERE cpf = ?""", [cpf])

            self.conexao.commit()

            print("Cliente com cpf %s foi removido com sucesso" % cpf)
        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes')

    def buscarPorEmail(self, email):
        #Buscar pessoa por Email
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
                SELECT * FROM clientes WHERE email = ?
            """, [email])

            for linha in cursor.fetchall():
                id = linha[0]
                nome = linha[1]
                cpf = linha[2]
                email = linha[3]
                
                print("{0}\n{1}\n{2}\n{3} \n".format(id, nome, cpf, email))
        except AttributeError:
            print("Faça a conexão do banco antes de inserir clientes")
