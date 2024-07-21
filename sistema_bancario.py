class Cadastro_conta_bancaria:
   _numero_conta = 0
   _agencia_conta = 0
   _usuario_conta = ""

   def __init__(self, numero_conta, agencia_conta, usuario_conta):
      self._numero_conta = numero_conta
      self._agencia_conta = agencia_conta
      self.usuario_conta = usuario_conta

   def get_numero_conta(self):
      return self._numero_conta
   
   def get_numero_conta(self):
      return self._agencia_conta
   
   def get_usuario_conta(self):
      return self._usuario_conta
   
   def set_usuario_conta(self, usuario_conta):
      self._usuario_conta = usuario_conta

class Cadastro_chave_pix:
   #cadatrar  chave do usuario e chave de contatos salvos do usuario
   chave_pix = "Rafael - 15632165818"


class Operacoes_bancarias(Cadastro_conta_bancaria, Cadastro_chave_pix):
   
   _saldo_bancario = 0.0
   _historico_transacoes = []

   def __init__(self, _saldo_bancario):
      self._saldo_bancario += _saldo_bancario

   def get_saldo_bancario(self):
      return self._saldo_bancario

   def get_historico_transacoes(self):
      return self._historico_transacoes


   def depositar(self, valor_depositado):
      self._saldo_bancario += valor_depositado

   def sacar(self, valor_sacado):
      if valor_sacado <= self._saldo_bancario:
         self._saldo_bancario -= valor_sacado
         self._historico_transacoes.append(valor_sacado)
      else:
         print(f"Não foi possível concluir seu saque, saldo atual {self._saldo_bancario}")

   def mostrar_saldo_bancario(self):
      print(f"Seu saldo atual é de R$ {self._saldo_bancario}")
   
   def mostrar_hisotrico_transacoes(self):
      print("Histórico de Transações")
      for historico in self._historico_transacoes:
         print(historico)



operacao_bancaria = Operacoes_bancarias(5000.5)
operacao_bancaria.sacar(50)
operacao_bancaria.sacar(100)

operacao_bancaria.mostrar_hisotrico_transacoes()
