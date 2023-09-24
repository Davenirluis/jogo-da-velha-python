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

def verifica():
						"""verifica se a casa ja nao foi ocupada anteriormente"""						
						global jogador
						if not jogador in jafoi:
							jafoi.append(jogador)
						else:
							while True:
								jogador=int(input('essa casa já foi ocupada, tente outra '))
								if not jogador in jafoi:
									jafoi.append(jogador)
									break
							
						
def gabarito():
	"""o desenho do jogo da velha propriamente dito, e ainda verifica vitória ou empate"""
	global tipo
	if  jogador ==1:
		global a
		a= tipo
	if jogador ==2:
		global b
		b=tipo
	if jogador ==3:
		global c
		c=tipo
	if jogador ==4:
		global d
		d=tipo
	if jogador ==5:
		global e
		e=tipo
	if jogador ==6:
		global f
		f=tipo
	if jogador ==7:
		global g
		g=tipo
	if jogador ==8:
		global h
		h=tipo
	if jogador ==9:
		global i
		i=tipo		
	print(f'  {a} | {b} | {c}   \n  {d} | {e} | {f} \n  {g} | {h} | {i}  \n')
	if a==b==c or d==e==f or g==h==i or a==d==g or b==e==h or c==f==i or a==e==i or c==e==g:	   
	   print('parabéns! ',tipo, 'venceu.')
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
	 
		
escolher=int(input('tecle 1 para jogar sozinho ou 2 para jogar com o computador'))
while escolher !=1 and escolher != 2:		
	escolher=int(input('só é possivel teclar 1 para jogar sozinho ou 2 para jogar com o computador'))
tipoprov=input('você gostaria de x ou o? ')
while tipoprov !='x' and tipo != 'o':		
	tipo=input('só é possivel escolher x ou o ')
	
if tipoprov =='x':
	tipo='o'
elif tipoprov=='o':
	tipo='x'	
	
if escolher ==1:
    	while True:
    		gabarito() 
    		if fim==1:
    			break  	
    		jogador=int(input('jogada do jogador 1 '))
    	
    		verifica()
	    	possivel=[1,2,3,4,5,6,7,8,9]
    		while  not jogador in possivel:
   	 		jogador=int(input('voce só pode escolher as posicões do tabuleiro! '))	
   	 	
   	 		verifica()    			
    		gabarito()
    		
    		
    		
    		
    		if fim==1:
    			break  	
   	 	jogador=int(input('jogada do jogador 2 ')) 
  
   	 	verifica()	
   	 	while  not jogador in possivel:
   	 		jogador=int(input('voce só pode escolher as posicões do tabuleiro! '))
 
   	 		verifica()
   	 	
   	 		
   
if escolher == 2:
   while True:
    		gabarito()
    		if fim==1:
    			break  	   	
    		jogador=int(input('jogada do jogador 1 ')) 
 
    		verifica()		
	    	possivel=[1,2,3,4,5,6,7,8,9]
    		while  not jogador in possivel:
   	 		jogador=int(input('voce só pode escolher as posicões do tabuleiro! '))
   	 		verifica()
   	 	gabarito()  	 		
   	 	

   	 	if fim==1:
    			break  	
   	 	jogador=randint(1,9)
   	 	if not jogador in jafoi:
   	 		jafoi.append(jogador)
   	 	else:
   	 		while True:
   	 			jogador=randint(1,9)
   	 			if not jogador in jafoi:
   	 				jafoi.append(jogador)
   	 				break
   	 	print('jogada do robô ',jogador)
   	 
   	 		   	 	
   	 		   	 		   	