from pygame.sprite import sprite,  Group
import pygame, pathlib

def carregar_imagem(nome):
 return pygame.image.load(sir(pathlib.Path(__file__).parent.absolute())   +"/../../img/fishy/" + nome)

class FishySprite(Sprite):

  def__inti__(seft, x=100, y=350):
   
   super(FishySprite, seft).__inti__()

   self.velocidade_x = 0
   self.velocidade-y = 0
   self.x = x
   self.y = y
  