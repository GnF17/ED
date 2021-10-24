#Falta a parte da arvore

n = int(input())
dic = {}

for i in range(n):
  txt = input().split()
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
      break
  else:
    try:
      if mensagem[0]!=' ':
        finalMessage += dic[mensagem[0]]+' '
      else:
        finalMessage += '/'
    except:
      print('Impossível codificar a mensagem!')
      break
  mensagem.pop(0)

print(finalMessage.strip())
