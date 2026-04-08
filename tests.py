from ebank import EBank

try:

    # criação do banco
    bancoLB = EBank('Banco Luso-Brasileiro das Ilusoes')
    
    print("---- Testes de criação e encerramento de contas ----")    
    
    conta_Huguinho = bancoLB.abrir_conta("Huguinho", "123456789")
    assert bancoLB.numero_de_contas_ativas() == 1
    
    bancoLB.encerrar_conta(conta_Huguinho.numero_da_conta, "123")
    
    conta_Huguinho.definir_pin("Abc123!")
    
    bancoLB.encerrar_conta(conta_Huguinho.numero_da_conta, "Abc")
    bancoLB.encerrar_conta(conta_Huguinho.numero_da_conta, "Abc123!")
    
    assert bancoLB.numero_de_contas_ativas() == 0

    print("---- Criação e encerramento de conta concluído ----\n")

    print("---- Testes de abertura de novas contas ----")

    conta_Zezinho = bancoLB.abrir_conta("Zezinho", "123456789")
    conta_Luisinho = bancoLB.abrir_conta("Luisinho", "987654321")
    assert bancoLB.numero_de_contas_ativas() == 2
    assert conta_Zezinho.nome == "Zezinho"
    assert conta_Luisinho.nif == "987654321"

    print("---- Contas criadas e dados validados ----\n")

    print("---- Testes de definição de PIN e operações bancárias ----")

    conta_Zezinho.definir_pin("123")
    conta_Zezinho.definir_pin("Abc123!")
    conta_Luisinho.definir_pin("abC123*")

    conta_Zezinho.depositar(5000)
    assert conta_Zezinho.consulta() == 5000

    conta_Zezinho.levantar(30)
    assert conta_Zezinho.consulta() == 4970

    print("---- Definição de PIN e operações concluídos ----\n")

    print("---- Testes de transferências e processamento ----")

    bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Luisinho.numero_da_conta, 1000, False)

    assert conta_Zezinho.consulta() == 4970

    bancoLB.processamento()

    assert conta_Luisinho.consulta() == 1000
    assert conta_Zezinho.consulta() == 3970

    print("---- Transferências validadas ----\n")

    print("---- Testes de acesso e autenticação ----")

    conta_Patricia = bancoLB.abrir_conta("Cliente3", "192837465")
    assert bancoLB.numero_de_contas_ativas() == 3

    acesso = bancoLB.aceder_conta(conta_Patricia.numero_da_conta, "123")
    assert not acesso

    ps = "Ab1$@!*"
    conta_Patricia.definir_pin(ps)

    bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Patricia.numero_da_conta, 500, True)

    assert conta_Zezinho.consulta() == 3470
    assert conta_Patricia.consulta() == 500

    conta_PatriciaB = bancoLB.aceder_conta(4, ps)
    assert conta_Patricia == conta_PatriciaB

    bancoLB.encerrar_conta(conta_PatriciaB.numero_da_conta, ps)
    assert bancoLB.numero_de_contas_ativas() == 2

    conta_Zezinho.historico()

    print("---- Acesso e autenticação concluídos ----\n")

    print("---- Testes de transferências adicionais e casos especiais ----")
    bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Patricia.numero_da_conta, 500, True)
    assert conta_Zezinho.consulta() == 3470

    conta_Patricia = bancoLB.aceder_conta(4, "Ab1$@!*")
    
    bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Luisinho.numero_da_conta, -1000, False)
    
    bancoLB.processamento()
    
    assert conta_Luisinho.consulta() == 1000
    assert conta_Zezinho.consulta() == 3470
    
    bancoLB.transferencia(conta_Zezinho.numero_da_conta, conta_Luisinho.numero_da_conta, 4000, False)
    
    assert conta_Luisinho.consulta() == 1000
    assert conta_Zezinho.consulta() == 3470
    
    bancoLB.processamento()
    
    assert conta_Luisinho.consulta() == 5000
    assert conta_Zezinho.consulta() == -530

    print("---- Validação da estrutura do código ----")

    assert 'nome' in dir(bancoLB)
    assert '_contas' in dir(bancoLB)
    assert 'abrir_conta' in dir(bancoLB)
    assert 'numero_de_contas_ativas' in dir(bancoLB)
    assert 'transferencia' in dir(bancoLB)
    assert 'processamento' in dir(bancoLB)
    assert 'encerrar_conta' in dir(bancoLB)
    assert 'nome' in dir(conta_Zezinho)
    assert 'nif' in dir(conta_Zezinho)
    assert '_pin' in dir(conta_Zezinho)
    assert 'numero_da_conta' in dir(conta_Zezinho)
    assert '_saldo' in dir(conta_Zezinho)
    assert 'levantar' in dir(conta_Zezinho)
    assert 'depositar' in dir(conta_Zezinho)
    assert 'consulta' in dir(conta_Zezinho)
    assert 'definir_pin' in dir(conta_Zezinho)
    assert 'acesso' in dir(conta_Zezinho)
    assert 'historico' in dir(conta_Zezinho)

    print("---- Estrutura Validada ----")

except:
    pass