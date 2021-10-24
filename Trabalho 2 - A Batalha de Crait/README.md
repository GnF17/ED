A Batalha de Crait

Após serem quase que completamente dizimados, os rebeldes - liderados pela general Leia Organa - estão em fuga e sendo perseguidos de perto por cruzadores da Primeira Ordem. A situação está desesperadora, com um número reduzido de naves de transporte, os poucos rebeldes sobreviventes conseguem se abrigar em uma antiga base abandonada, localizada no deserto do distante planeta Crait. Com o cerco da base pelo poderoso Exército da Primeira Ordem, só resta aos rebeldes um pedido desesperado de ajuda aos quatro cantos do universo.

Tendo apenas a disposição equipamentos obsoletos, você precisa ajudar os rebeldes a conseguirem codificar um sistema binário de representação à distância de números, letras e símbolos, conhecido como Código Morse.  Com vários equipamentos de comunicação avariados, você é a última esperança para os rebeldes conseguirem codificar/decodificar dados usando essa tecnologia. A aliança rebelde conta desesperadamente com sua ajuda, Jovem Padawan!
Código Morse
O código morse é um sistema de representação de letras, números e sinais de pontuação através de um sinal codificado enviado intermitentemente. Foi desenvolvido por Samuel Morse (o cara era pintor, acredita?) em 1835, criador do telégrafo elétrico (importante meio de comunicação a distância), dispositivo que utiliza correntes elétricas para controlar eletroímãs que funcionam para emissão ou recepção de sinais.

No código morse a ser utilizado pelos rebeldes, símbolos do alfabeto são utilizados para formar palavras e frases. Os símbolos "A", "R", "S", "T" e "W", podem ser utilizados para formar as palavras: "STAR" e "WARS", por exemplo. Cada símbolo do alfabeto é codificado através de uma sequência de pontos ".
" e traços "−" (sem aspas). Pontos e traços são denominados símbolos morse. Um conjunto de símbolos morse forma um código morse (−.−..) que está associado a um símbolo do alfabeto. Além disso, na mensagem codificada, os espaços em branco representam separadores dos códigos morse apresentados em sequencia. O símbolo especial  "/" (sem aspas) deve ser decodificado como um espaço em branco. Sendo assim: 
Sempre que encontrar um espaço em branco na mensagem codificada, significa que acabou o código morse relacionado a um símbolo do alfabeto. 
Sempre que encontrar "/" na mensagem codificada, um espaço em branco deve ser adicionado na mensagem decifrada. Sendo assim, a posição seguinte ao símbolo especial "/" contém o símbolo morse do código morse que representa o símbolo do alfabeto para a palavra seguinte (caso houver). Além disso, sempre antes do símbolo "/" existirá um espaço em branco indicando que o código morse do último símbolo do alfabeto para palavra anterior terminou. Por fim, uma mensagem codificada nunca pode começar com o símbolo "/".

C-3PO teve uma sacada importante,  o código morse pode ser representado por uma árvore de decisão (binária). Uma árvore de decisão é uma estrutura de dados utilizada para expressar quais decisões levaram a determinado estado. Ou seja, qual caminho foi tomado para que aquele resultado fosse obtido. Desta forma, você deve construir uma árvore de decisão que represente o alfabeto em código morse e, posteriormente, utilizá-la para codificar e decodificar mensagens rebeldes. Nesta estrutura, os nós da árvore representam os símbolos do alfabeto e suas ramificações indicam as decisões tomadas (códigos morse).  Utilize a seguinte convenção: esquerda para representar ponto ".
" e direita para representar traço "−". 


Entrada:
  A entrada consiste em um número inteiro n de símbolos do alfabeto, seguido de n linhas contendo, cada uma, um símbolo do alfabeto e a sua representação correspondente em código morse. Seus valores são separados por um espaço, sendo garantido que não há símbolos do alfabeto repetidos e que 0≤n. A entrada segue, sendo fornecido o número inteiro m, tal que m∈{0,1}, onde o valor 0 define que a mensagem s precisa ser decodificada e o valor 1 que a mensagem s precisa ser codificada. Por fim, a entrada termina com a mensagem s, tal que 1≤len(s).
  <br>Obs 1:</br> não há garantias de que a relação de n símbolos do alfabeto está completa para permitir codificar ou decodificar a mensagem s.
  <br>Obs 2:</br> Na mensagem a ser codificada, caso exista mais de um espaço em branco consecutivo, deve-se considerar apenas um espaço e ignorar os demais.

Saída:
  A saída consiste da mensagem s codificada ou decodificada (de acordo com a entrada), seguido, na próxima linha,  da impressão da árvore de decisão. A impressão da árvore de decisão consiste na impressão dos valores dos seus nós, seguindo o percurso em largura (por nível) e separados por espaço em branco. Para o nó que não possua um símbolo do alfabeto associado, o símbolo "*" (sem aspas) deve ser impresso em seu lugar. 

Observações:
  - Caso a mensagem s não possa ser codificada, a seguinte mensagem deve ser exibida: Impossível codificar a mensagem!
  - Caso a mensagem s não possa ser decodificada, a seguinte mensagem deve ser exibida: Impossível decodificar a mensagem!
  - A árvore de decisão deve ser sempre impressa, caso seja possível.
  
<br>For example:
Input:</br>
5
A .
C -
R .-
T ..
! -.
0
. .. . - . .- -. 

<br>Result:</br>
ATACAR!
* A C T R !


<br>Input:</br>
10
A .
B -.
C .-
D ...
E --
L .--
R ..
S -.-
T -
! ---
0
. - . .- . .. /.. -- -. -- .-- ... -- -.- --- 
	
<br>Result:</br>
ATACAR REBELDES!
* A T R C B E D L S !


<br>Input:</br>
5
A .
C -
R .-
T ..
! -.
1
ATACAR!

<br>Result:</br>
. .. . - . .- -. 
* A C T R !


<br>Input:</br>
10
A .
B -.
C .-
D ...
E --
L .--
R ..
S -.-
T -
! ---
1
ATACAR REBELDES!

<br>Result:</br>
. - . .- . .. /.. -- -. -- .-- ... -- -.- --- 
* A T R C B E D L S !
