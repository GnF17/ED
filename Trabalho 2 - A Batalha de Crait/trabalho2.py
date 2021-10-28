#author: Giovanna Nogueira

class tree:
  def __init__(self,rt, e = None, d = None):
    self.root = rt
    self.esq = e
    self.dir = d

  def mudarRoot(self, dado):
    self.root = dado 

def criar(dic, arvore):
  if len(dic[1])>0:
    if dic[1][0]=='.':
      if arvore.esq==None:
        arvore.esq=tree('*')
      criar([dic[0],dic[1][1:]],arvore.esq)
    
    if dic[1][0]=='-':
      if arvore.dir==None:
        arvore.dir=tree('*')
      criar([dic[0],dic[1][1:]],arvore.dir)
  else:
    arvore.mudarRoot(dic[0])

arvore = tree('*')

n = int(input())
dic = {}
error = True

for i in range(n):
  txt = input().split()
  criar([txt[0],txt[1]],arvore)
  dic[txt[0]] = txt[1]


escolha = int(input())
if escolha==0:
  mensagem = input().split()
else:
  mensagem = list(input())

finalMessage = ''

def get_key(val):
  for key, value in dic.items():
    if val == value:
      return key

while len(mensagem)>0:
  if escolha==0:
    try:
      if '/' in mensagem[0]:
        aux = list(mensagem[0])
        aux.remove('/')
        aux2 = ''
        for i in range(len(aux)):
          aux2 += str(aux[i])
        finalMessage += ' '+get_key(aux2)
      else:
        finalMessage += get_key(mensagem[0])
    except:
      print('Impossível decodificar a mensagem!')
      finalMessage = ''
      error = False
      break
  else:
    try:
      if mensagem[0]!=' ':
        finalMessage += dic[mensagem[0]]+' '
      else:
        if mensagem[1]!=' ':
          finalMessage += '/'
    except:
      print('Impossível codificar a mensagem!')
      finalMessage = ''
      error = False
      break
  mensagem.pop(0)

print(finalMessage.strip())

barra = ''
altura = 0

def alturA(a):
  global barra
  global altura

  if len(barra)/2 > altura:
    altura = len(barra)/2 -1
  barra += '__'
  if a != None:
    alturA(a.esq)
    alturA(a.dir)
  barra = barra[:len(barra)-2]

alturA(arvore)

def mostrar(a, i):
  global barra

  if a != None:
    if len(barra)/2==i:
      print(a.root, end=' ')

  barra += '__'
  if a != None:
    mostrar(a.esq, i)
    mostrar(a.dir, i)
  barra = barra[:len(barra)-2]

if error:
  for i in range(int(altura)+1):
    mostrar(arvore, i)
