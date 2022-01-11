import random
import pylab as pl
import numpy as np

x_tesouro = int(random.uniform (1,10))
y_tesouro = int(random.uniform (1,10))

def graf ():
    pl.figure(figsize=(7,5))
    pl.axis(xmin=0, xmax=10, ymin=0, ymax=10)
    pl.xticks(np.arange(1,10,1))
    pl.yticks(np.arange(1,10,1))
    pl.grid()
    pl.title ("Caça ao tesouro! \n Digite seus palpites de onde o baú do tesouro está!")
    pl.xlabel("colunas")
    pl.ylabel("linhas")

Xcoord_dica = 0
Ycoord_dica = 0

def dica ():
  soma_dica = int(random.uniform (1,3))
  Xcoord_dica = x_tesouro + soma_dica
  Ycoord_dica = y_tesouro + soma_dica

  if (x_tesouro == 1) or (x_tesouro ==2):
    Xcoord_dica = x_tesouro + soma_dica
  if (y_tesouro == 1) or (y_tesouro == 2):
    Ycoord_dica = y_tesouro + soma_dica
  if (x_tesouro == 8) or (x_tesouro == 9):
    Xcoord_dica = x_tesouro - soma_dica
  if (y_tesouro == 8) or (y_tesouro == 9):
    Ycoord_dica = y_tesouro - soma_dica
  pl.scatter (Xcoord_dica, Ycoord_dica, color='g', marker = 's')
  return Xcoord_dica,Ycoord_dica

tentativa = 0

print ("Um rei escondeu um tesouro em uma das intersecções abaixo, será que você consegue achá-lo antes dos outros piratas?")

graf()
pl.show()

for i in range (0,10):
  x1 = int(input ("Em qual coluna você deseja cavar? "))
  y1 = int(input ("E em qual linha? "))
  tentativa = tentativa + 1

  if (x_tesouro,y_tesouro) == (x1,y1):
      graf()
      pl.scatter(x_tesouro,y_tesouro , marker='o', color = 'c')
      pl.show()

      print ("Parabéns, você achou o baú do tesouro!")
      if tentativa <8:
        moedas = int(random.uniform (20,1000))
        print ("E nele você achou", moedas,"moedas de ouro!")
      else: 
        print ("Você acabou demorando muito, o tesouro já foi saqueado!")
      break
    
  else:
    if tentativa < 10:
      graf()
      pl.scatter(x1,y1 , marker='x', color ='r')
      
      if tentativa == 5:
        print("Dia de sorte! Você achou um mapa que dizia que o tesouro está perto da posição" ,dica(), "da ilha! Continue tentando!")
      pl.show()
      print ("Você errou, tente mais uma vez!")

    else:
      graf()
      pl.scatter(x_tesouro,y_tesouro , marker='o', color = 'c')
      pl.show ()
      print("O tesouro estava em (",x_tesouro,",",y_tesouro,")")
      print("Você perdeu, jogue novamente")
