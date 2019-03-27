class Disciplina:
  def __init__(self):
    self.cadastradas = []
  def inserir(self, novo):
    self.cadastradas.append(novo)
  def remover(self,codigo):
    for elemento in self.cadastradas:
      if codigo == elemento['Código']:
        self.cadastradas.remove(elemento)
  def alterar(self, antigo, novo):
    for elemento in self.cadastradas:
      if antigo == elemento['Código']:
        self.cadastradas.append(novo)
        self.cadastradas.remove(elemento)
  def localizar(self, codigo):
    for elemento in self.cadastradas:
      if codigo == elemento['Código']:
        print('\t'+'='*45)
        for chave, valor in elemento.items():
          print("\t• {} : {}".format(chave, valor))
        print('\t'+'='*45)
              
  def listar(self):
    total_disc = []
    total_CH = []
    total_nota = []

    for elemento in self.cadastradas:
      for chave, valor in elemento.items():
        print("\t• {} : {}".format(chave, valor))
      print('\n')
    
      total_disc.append(elemento['Disciplina'])
      total_CH.append(elemento['CH'])
      total_nota.append(elemento['Nota'])
    
    print('\t'+'='*45)
    print("\t=================== Total ===================")
    print('\t'+'='*45)
    print("\t• Disciplinas : {}\n\t• CH : {}\n\t• Nota: {:.2f}".format(len(total_disc), sum(total_CH), sum(total_nota)/len(total_nota)))

  def menu(self):
    return '''
\t=============================================
\t►                   MENU                    ◄         
\t=============================================  
\t[1] Listar disciplinas
\t[2] Localizar disciplinas pelo código
\t[3] Adicionar disciplina
\t[4] Excluir disciplinas
\t[5] Alterar disciplinas
\t[6] Sair
\t============================================='''


print('''
  \t╠══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩═╣
  \t╬   BEM-VINDO(A) AO SISTEMA DE DISCIPLINAS  ╬
  \t╠══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦═╣
  ''')

calculo = {
  'Disciplina': 'Cálculo',
  'Nota': 7,
  'CH': 60,
  "Código": 'DECAL32356'
}

quimica = {
  'Disciplina': 'Química',
  'Nota': 9,
  'CH': 60,
  "Código": 'DEQUI45667'
}

fisica = {
  'Disciplina': 'Física',
  'Nota': 8,
  'CH': 60,
  "Código": 'DEFIS98779'
}

d1 = Disciplina()
d1.inserir(calculo)
d1.inserir(quimica)
d1.inserir(fisica)

while True:

  print(d1.menu())
  opcao = int(input("\t• Opção: "))
  print('\t'+'='*45)

  if opcao == 1:
    print('\n')
    print('\t'+'='*45)
    print('\t===========  Disciplinas cursadas ===========')
    print('\t'+'='*45)
    print('\n')
    d1.listar()

    continue

  elif opcao == 2:
    cod = str(input("\n\t► Digite o código da disciplina: "))
    contador = len(d1.cadastradas)

    for elemento in d1.cadastradas:
      if cod == elemento['Código']:
        d1.localizar(cod)
        contador = contador - 1
        continue
    
    if contador == len(d1.cadastradas):
      print("\n\t• Código inválido")
      continue
      
  elif opcao == 3:
    print('\n')
    print('\t'+'='*45)
    print("\t►     Adicione as seguintes informações     ◄")
    print('\t'+'='*45)
    print('\n')
    adicionada = {
        'Disciplina': input("\t• Disciplina: "),
        'Nota': float(input('\t• Nota: ')),
        'CH': int(input('\t• CH: ')),
        "Código": str(input('\t• Código: ')),
      }
    d1.inserir(adicionada)
    print('\n')
    print('\t'+'='*45)
    print("\t================ Adicionada =================")
    print('\t'+'='*45)
    print('\n')
    d1.listar()
    continue

  elif opcao == 4:
    print('\n')
    print('\t'+'='*45)
    print("\t================= Excluir ===================")
    print('\t'+'='*45)

    print('\n')
    print('\t'+'='*45)
    cod = str(input("\t► Digite o código da disciplina: "))
    print('\t'+'='*45)
    contador = False

    for elemento in d1.cadastradas:
      if cod == elemento['Código']:
        contador = True
        print('\n')
        for chave, valor in elemento.items():
          print("\t{} : {}".format(chave, valor))

        d1.remover(cod)
        print('\n')
        print('\t'+'='*45)
        print("\t================= Excluída ==================")
        print('\t'+'='*45)
        print('\n')
        continue
    
    if contador == False:
      print("\n\t• Código inválido")
      continue
    
  elif opcao == 5:
    print('\n')
    print('\t'+'='*45)
    print('\t================= Alteração =================')
    print('\t'+'='*45)
    print('\n')

    print('\t'+'='*45)    
    cod = str(input("\t► Digite o código da disciplina: "))
    print('\t'+'='*45)
    contador = False

    for elemento in d1.cadastradas:
      if cod == elemento['Código']:
        contador = True
        print('\n')
        for chave, valor in elemento.items():
          print("\t {} : {}".format(chave, valor))
        
        print('\n')
        print('\t'+'='*45)
        print('\t============= Faça as alterações ============')
        print('\t'+'='*45)
        print('\n')

        alteracao = {
          'Disciplina': input("\t• Novo nome: "),
          'Nota': float(input('\t• Nova nota: ')),
          'CH': int(input('\t• Nova CH: ')),
          'Código': str(input('\t• Novo código: ')),
        }

        d1.alterar(cod, alteracao)
        print('\n')
        print('\t'+'='*45)
        print('\t================= Alterado ==================')
        print('\t'+'='*45)
        print('\n')
        d1.listar()
        continue

    if contador == False:
      print("\n\t► Código inválido")
      continue

  elif opcao == 6:
    print('\n')
    print('\t'+'='*45)
    print("\tSISTEMA FINALIZADO, OBRIGADO PELA PREFERÊNCIA")
    print('\t'+'='*45)
    print('\n')
    break

  else:
    print('\n')
    print('\t'+'='*45)
    print("\t============== Opção inválida ===============")
    print('\t'+'='*45)
    print('\n')
    continue
