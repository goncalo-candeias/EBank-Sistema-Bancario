class Conta:
  numeroConta = 0
  def __init__(self, nome, nif):
    self.nome = nome
    self.nif = nif
    self._pin = None
    self.numeroOperacoes = 0
    Conta.numeroConta += 1
    self.numero_da_conta = Conta.numeroConta
    self._saldo = 0
    self.historico_de_operacoes = []
  

  # Permite levantar dinheiro da conta, se houver saldo e PIN definido
  def levantar(self, valor):

    if self._pin is None:
      print("Palavra passe nao definida.")
      return
    
    if valor > self._saldo:
      print("Saldo insuficiente em conta.")
      return
    
    if valor <= 0:
      return 
     
    self._saldo -= valor
    self.numeroOperacoes += 1
    self.historico_de_operacoes.append(f"Operacao numero:  {self.numeroOperacoes} Valor:  {-valor}")


  # Permite adicionar dinheiro à conta
  def depositar(self, valor):
    if valor <= 0:
      print("Deposito invalido.")
      
    else:
      self._saldo += valor
      self.numeroOperacoes += 1
      self.historico_de_operacoes.append(f"Operacao numero:  {self.numeroOperacoes} Valor:  {valor}")
  
  
  # Devolve o saldo atual da conta
  def consulta(self):
    return self._saldo
  
  
  # Define o PIN da conta, validando os requisitos
  def definir_pin(self, pin):
    if len(pin) < 6:
      print("Palavra passe precisa ter tamanho minimo de 6.")
    
    if len(pin) > 8:
      print("Palavra passe nao pode ter tamanho superior a 8.") 
    
    temLetraMaiuscula = any(letra.isupper() for letra in pin)
    
    if not temLetraMaiuscula:
      print("Palavra passe precisa conter uma letra maiuscula.")
    
    temLetraMinuscula = any(letra.islower() for letra in pin)
    
    if not temLetraMinuscula:
      print("Palavra passe precisa conter uma letra minuscula.") 
    
    caracteresEspeciais = ['$', '@', '#', '%', '!', '*']
    temCaracteresEspeciais = any(letra in caracteresEspeciais for letra in pin)
    
    if not temCaracteresEspeciais:
      print("Palavra passe precisa conter pelo menos um caratere especial ['$', '@', '#', '%', '!', '*'] .")
      
    else:
      self._pin = pin
  
  
  # Verifica se o PIN fornecido é o correto
  def acesso(self, pin):
    return self._pin == pin
  
  
  # Imprime o histórico de operações e o saldo atual da conta
  def historico(self):
    for operacao in self.historico_de_operacoes:
      print(operacao)
      
    print(f"Saldo atual:  {self._saldo}")