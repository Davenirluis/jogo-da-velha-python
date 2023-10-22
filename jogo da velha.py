from random import randint
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
fim=0
acabou=0
jogador='semvalor'
tipo='xouo'
escolher='sozinhooucompc'
jafoi=[]
tipoprov='gambiarra'
possivel=['1','2','3','4','5','6','7','8','9']


def confere():
    """confere se a casa existe, depois se a casa já foi e por fim, valida a jogada"""
    global jogador
    if not jogador in possivel:
      jogador=input('você só pode jogar casas do tabuleiro, tente novamente ')
      confere()
    elif not jogador in jafoi:
        jafoi.append(jogador)
    else:
        jogador=input('esta casa já foi, tente outra ')
        confere()
    	    		
def gabarito():
	"""o desenho do jogo da velha propriamente dito, e ainda verifica vitória ou empate"""
	global tipo
	if  jogador =='1':
		global a
		a= tipo
	if jogador =='2':
		global b
		b=tipo
	if jogador =='3':
		global c
		c=tipo
	if jogador =='4':
		global d
		d=tipo
	if jogador =='5':
		global e
		e=tipo
	if jogador =='6':
		global f
		f=tipo
	if jogador =='7':
		global g
		g=tipo
	if jogador =='8':
		global h
		h=tipo
	if jogador =='9':
		global i
		i=tipo		
	print(f'\n  {a} | {b} | {c}   \n  {d} | {e} | {f} \n  {g} | {h} | {i}  \n')
	if a==b==c or d==e==f or g==h==i or a==d==g or b==e==h or c==f==i or a==e==i or c==e==g:	   
	   print('parabéns! ',tipo, 'venceu.')
	   global acabou
	   acabou=1
	   global fim
	   fim=1
	if len(jafoi) == 9 and acabou==0:
	   print('empatamos!')
	   fim=1
#inverte de x para o	   
	if tipo =='x':
		tipo='o'
	else:
	   tipo='x'

def robo():
	"""lances aleatórios do robô"""
	global jogador
	jogador=randint(1,9)
	jogador=str(jogador)
	if jogador in jafoi:
	    robo()
	if not jogador in jafoi:
	       jafoi.append(jogador)
	       print('jogada do robô ',jogador)
	   
escolher=input('tecle 1 para jogar sozinho ou 2 para jogar com o computador ')
while escolher != '1' and escolher != '2':
    escolher=input('só é possivel escolher 1 ou 2, tente novamente :) ')
tipoprov=input('você gostaria de x ou o? ')
while tipoprov !='x' and tipoprov != 'o':		
	tipoprov=input('só é possivel escolher x ou o ')	
if tipoprov =='x':
	tipo='o'
elif tipoprov=='o':
	tipo='x'		
while True: 
    gabarito()
    if fim==1:
        break  	
    jogador=input('jogada do jogador 1 ')
    confere()
    gabarito()
    if fim==1:
        break    
    if escolher =='1':        
            jogador=input('jogada do jogador 2 ')
            confere()	 		
    if escolher =='2':
            robo()
            if fim ==1:
                break
   	 
 