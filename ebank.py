from conta import Conta

class EBank:
  def __init__(self, nome):
    self.nome = nome
    self._contas = []
    self._contas_informacoes = {}
    self._transf_nao_inst = []


  # Cria uma nova conta e adiciona ao sistema  
  def abrir_conta(self, nome, nif):
    nova_conta = Conta(nome, nif)
    self._contas.append(nova_conta.numero_da_conta)
    self._contas_informacoes[nova_conta.numero_da_conta] = nova_conta
    return nova_conta
  

  # Permite aceder a uma conta existente, validando o número da conta e o PIN
  def aceder_conta(self, numero_de_conta, pin):
    conta = self._contas_informacoes.get(numero_de_conta)
     
    if conta is None:
      print("Numero de conta invalido.")
    
    elif conta._pin is None:
      print("Palavra passe nao definida.")
      
    elif not conta.acesso(pin):
      print("Palavra passe invalida.")
      
    else:
      return self._contas_informacoes[numero_de_conta]
  

  # Devolve o número de contas atualmente ativas
  def numero_de_contas_ativas(self):
    return len(self._contas)
  

  # Remove uma conta do sistema, se o PIN for válido
  def encerrar_conta(self, numero_de_conta, pin):
    conta = self._contas_informacoes.get(numero_de_conta)
    
    if conta is None:
      print("Numero de conta invalido.")
    
    elif conta._pin is None:
      print("Palavra passe nao definida.")
      
    elif not conta.acesso(pin):
      print("Palavra passe invalida.")
      
    else:
      self._contas.remove(numero_de_conta)
      del self._contas_informacoes[numero_de_conta]
      

  # Realiza uma transferência entre contas (instantânea ou não instantânea)
  def transferencia(self, numero_da_conta_1, numero_da_conta_2, valor, instantanea): 
    conta1 = self._contas_informacoes.get(numero_da_conta_1)
    conta2 = self._contas_informacoes.get(numero_da_conta_2)
    
    if conta1 is None or conta2 is None or valor <= 0 :
        print("Transferencia invalida.")
    
    else:
      if instantanea:
          conta1.levantar(valor)
          conta2.depositar(valor)
    
      else:
        self._transf_nao_inst.append((numero_da_conta_1, numero_da_conta_2, valor))
      
  
  # Processa todas as transferências não instantâneas pendentes    
  def processamento(self):  
    for transferencia in self._transf_nao_inst:
      numero_da_conta_1, numero_da_conta_2, valor = transferencia
      conta1 = self._contas_informacoes.get(numero_da_conta_1)
      conta2 = self._contas_informacoes.get(numero_da_conta_2)
      
      conta1._saldo -= valor
      conta2._saldo += valor
      
      conta1.numeroOperacoes += 1
      conta1.historico_de_operacoes.append(f"Operacao numero:  {conta1.numeroOperacoes} Valor:  {-valor}")
      
      conta2.numeroOperacoes += 1
      conta2.historico_de_operacoes.append(f"Operacao numero:  {conta2.numeroOperacoes} Valor:  {valor}")
      self._transf_nao_inst = []