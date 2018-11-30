from database import BancoDeDados

if __name__ == "__main__":
    banco = BancoDeDados()
    banco.conecta()
    banco.criarTabelas()

    banco.inserirCliente('José', '1342412411', 'jrfercar@gmail.com')
    banco.inserirCliente('Joyce', '43646456546', 'joyceapsantana@gmail.com')
    banco.inserirCliente('Teste', '1234', 'teste@gmail.com')

    banco.buscarCliente('43646456546')

    banco.removerCliente('1234')

    banco.buscarPorEmail('jrfercar@gmail.com')
    
    banco.desconecta()
