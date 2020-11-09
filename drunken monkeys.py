import pygame,sys
from pygame.locals import *
from random import randint
from numpy import *
from collections import *

#GIANLUCCA AGUADO RENDON

#usar siempre antes de usar cualquier modulo
pygame.init()

#gargar una imagenes:
bloque=pygame.image.load("bloque.png")
mono_derecha= pygame.image.load("monoderecha.png")
mono_abajo= pygame.image.load("monoabajo.png")
mono_arriba= pygame.image.load("monoarriba.png")
mono_izquierda= pygame.image.load("monoizquierda.png")
mono_centro= pygame.image.load("monocentro.png")
tnt= pygame.image.load("tnt.png")
pared= pygame.image.load ("pared.png")
fondo= pygame.image.load ("fondo.png")
explocion= pygame.image.load ("explocion.png")
yisus= pygame.image.load ("yisus.png")
carnero= pygame.image.load ("carnero.png")
angel= pygame.image.load ("angel.png")
craneo= pygame.image.load ("craneo.png")
judio=pygame.image.load ("judio.png")
ganesha_dios = pygame.image.load ("ganesha_dios.png")
lgtbi = pygame.image.load ("lgtbi.png")

#MUSICA en midi completamente propia :3
pygame.mixer.music.load("monos-ebrios.mid")
pygame.mixer.music.play()

#MENSAJES para imprimir posteriormente
fuente = pygame.font.Font( None , 30 )
ganador = fuente.render ("¡GANASTE!", 0 ,(255,255,255))
ganador_dos = fuente.render ("encontraste al salvador ", 0 ,(255,255,255))
perdedor = fuente.render ("¡PECADOR!", 0 ,(0,0,0))

###guarda posicion inicial de los enemigos de forma global
enemigos_posicion = []
carnero_posicion=[]
cambios='izquierda'
ganesha_posicion=[]
lgtbi_posicion=[]
craneo_posicion=[]

#para disminuir la velocidad de ejecucion
reloj = pygame.time.Clock()


borrar=[]
##_____________________________________________________________________##


class ventana :

      extremo_y,extremo_x = 0 , 0       
      
      #este metodo nos crea aleatoriamente el tamaño del tablero
      def tablero_aleatorio ():
              
              
              #creacion de extremos X desde 250  hasta 950
              extremo_x = 50 + (100 * randint (3,9) )
              #creacion de extremos Y desde 250  hasta 650
              extremo_y = 50 + (100 * randint (3,6) )
              #de esta forma aseguramos [(5*3)+(5c2)]=30  formas de que se creen tableros
              # el area del tablero debe ser divisile por 100 (para garantias)
              ventana.bloques(extremo_y,extremo_x)

              
              return extremo_y,extremo_x
              ##return 350,350

              
       

            
       ##_______________________________metodo bloques __________________________________________________##
            ##este metodo asigna un 15 donde debe ir un bloque en una matriz
            ##los bloques son los que no se destruyen 
      def bloques ( fila,columna):
            #numero de bloques creados
            num_bloques = 0

            
             
            #llenar tablero de ceros
            fila,columna = int(fila), int(columna)
            
            tablero= zeros ( ( fila,columna ))

            
            i=50
            
            
            while (i < fila):
              
              
              j=50    
              
              
              valide= 1
              while (j <  columna):
                
                
                tablero [i][j] = 15
                   
                   
                num_bloques +=1
                
                j+=100
                 
              i+=100
              

            
            
            return { 'tablero' : tablero , 'num_bloques' : num_bloques , }
            ##_____________________fin metodo bloques __________________________________##

          
       ##_____________________metodo pared __________________________________##
       ## crea las paredes y pone los enemigos antes de hacerlo
      def pared ( tablero, num_pared,extremo_y , extremo_x  ):
        
        x =  extremo_x   - 50 
        y =  extremo_y   - 50
        

        aleatorio_x = 0
        aleatorio_y = 0   
        lista_pared = []

        num_pared = num_pared * 2
        
        print ("paredes permitidas -> " , num_pared)
        #para que no pinte en la superior izquierda  paredes (donde esta el mono )
        tablero [0] [0] = 20
        tablero [0] [50] = 20
        tablero [50] [0] = 20
        #no cree paredes donde esta el judio
        tablero [extremo_y-50] [extremo_x-50] = 20
        tablero [extremo_y-50] [extremo_x-100] = 20
        tablero [extremo_y-100] [extremo_x-50] = 20
        
        carnero_puesto=False
        ganesha_puesto=False
        bandera_puesto= False
        craneo_puesto=False
        contador = 0
       #mientras no se pongan todos las paredes  
        while (num_pared >= 0 ):
          
          validacion= 0
          enemigo =0
          aleatorio_x =  (50 *  randint ( 0,   x/50 )   )
          aleatorio_y = (50 * randint ( 0 ,  y/50  ) )   
 
           
          #  si esta en un extremo pues ponchelo  (la pared) #
          if ((aleatorio_x== 0 )or(aleatorio_y== 0 )or(aleatorio_x== x )or(aleatorio_y== y ))and (  tablero [ aleatorio_y][ aleatorio_x ]  != 20 ):   #asigne una pared al tablero
             
             tablero [aleatorio_y] [aleatorio_x] = 10
             #adicione coordenada de la pared a una lista
             lista_pared.append ( [ aleatorio_x, aleatorio_y ] )
             num_pared-=1
           #Se verifica que elenimogo se ponga en una posicion sin bloques, paredes o enemigos  
          else :
            if  (  tablero [ aleatorio_y][ aleatorio_x ]  != 15 ) and (  tablero [ aleatorio_y][ aleatorio_x ]  != 10 ) and (  tablero [ aleatorio_y][ aleatorio_x ]  != 20 ) :

                   if carnero_puesto==False :

                         carnero_posicion.append(aleatorio_x)      
                         carnero_posicion.append(aleatorio_y)
                         enemigos_posicion.append(aleatorio_x)
                         enemigos_posicion.append(aleatorio_y)
                         carnero_puesto=True
                         contador+=1
                   if (ganesha_puesto==False)and(carnero_posicion[0]!=aleatorio_x) and(carnero_posicion[1]!=aleatorio_y):

                         ganesha_posicion.append(aleatorio_x)      
                         ganesha_posicion.append(aleatorio_y)
                         enemigos_posicion.append(aleatorio_x)
                         enemigos_posicion.append(aleatorio_y)
                         ganesha_puesto=True
                         contador+=1
                   if (bandera_puesto==False)and(carnero_posicion[0]!=aleatorio_x) and(carnero_posicion[1]!=aleatorio_y)and(ganesha_posicion[0]!=aleatorio_x) and(ganesha_posicion[1]!=aleatorio_y):

                         lgtbi_posicion.append(aleatorio_x)      
                         lgtbi_posicion.append(aleatorio_y)
                         enemigos_posicion.append(aleatorio_x)
                         enemigos_posicion.append(aleatorio_y)
                         bandera_puesto=True      
                         contador+=1
                   if (craneo_puesto==False)and(carnero_posicion[0]!=aleatorio_x) and(carnero_posicion[1]!=aleatorio_y)and(ganesha_posicion[0]!=aleatorio_x) and(ganesha_posicion[1]!=aleatorio_y)and(lgtbi_posicion[0]!=aleatorio_x) and(lgtbi_posicion[1]!=aleatorio_y): 

                         craneo_posicion.append(aleatorio_x)      
                         craneo_posicion.append(aleatorio_y)
                         enemigos_posicion.append(aleatorio_x)
                         enemigos_posicion.append(aleatorio_y)
                         craneo_puesto=True      
                         contador+=1
                         
                          #asigne pared al tablero
                   # Se valida para no poner una pared en el puesto de un enemigo
                   else :                   
                                     while (enemigo < 8 and contador==4):
                                           if (enemigos_posicion[enemigo]==aleatorio_x)and(enemigos_posicion[enemigo + 1]==aleatorio_y):
                                                  validacion = 1
                                           enemigo+=2
                                     # Si el enemigo no esta en la posicion se pinta la pared                
                                     if(validacion==0 and contador== 4):
                                                 
                                       tablero [aleatorio_y] [aleatorio_x] = 10
                                                         #adicione coordenada de la pared a una lista 
                                       lista_pared.append ( [ aleatorio_x, aleatorio_y ] )
                                       num_pared-=1
        
        #para que el mono se pueda volver a mover 
        tablero [0] [0] = 0
        tablero [0] [50] = 0
        tablero [50] [0] = 0
        tablero [extremo_y-50] [extremo_x-50] = 0
        tablero [extremo_y-50] [extremo_x-100] = 0
        tablero [extremo_y-100] [extremo_x-50] = 0
        #diccionario_______por si necesitamos el tablero con los bloques y paredes 
        return lista_pared
        
       ##________________________________________fin metodo pared_____________________________________________________##
          
       
###################################################################################################################
#CLASE 

class Clase_enemigos :
     
      
      def movimiento_craneo(tablero_bloques,extremo_x,extremo_y,craneo_posicion,mono_x,mono_y):
                                      
            x =craneo_posicion[0]
            y =craneo_posicion[1]
            tablero_bloques [y] [x] = 666
            peso=0
            if (mono_x== x and mono_y == y):
                  tablero_bloques [y] [x] = 666
            #derecha
            elif ( x  != extremo_x-50)and((abs((x+50) - mono_x) + abs(y-mono_y) < (abs(x- mono_x) + abs((y-50)-mono_y)))and(tablero_bloques[y][x+50] == 0)and (abs((x+50) - mono_x) + abs(y-mono_y) < (abs(x - mono_x) + abs((y+50)-mono_y)))and (abs((x+50) - mono_x) + abs(y-mono_y) < (abs((x-50) - mono_x) + abs((y-50)-mono_y)))):
                     
                              craneo_posicion[0]=x+50
                              
                              window.blit( craneo , ( x,y) )
                              
                              window.blit(fondo,(x,y))
                              
                              tablero_bloques [y] [x] = 0

             #izquierda              
            elif ((abs((x-50) - mono_x) + abs(y-mono_y) < (abs(x- mono_x) + abs((y-50)-mono_y))) and(x != 0 )and(tablero_bloques[y][x-50] == 0)and (abs((x-50) - mono_x) + abs(y-mono_y) < (abs(x - mono_x) + abs((y+50)-mono_y)))): 
                       
                              craneo_posicion[0]=x-50
                              
                              window.blit( craneo , ( x,y) )
                              
                              window.blit(fondo,(x,y))

                              tablero_bloques [y] [x] = 0

            #arriba           
            elif ((abs(x- mono_x) + abs((y-50)-mono_y) < (abs(x - mono_x) + abs((y+50)-mono_y)))and(tablero_bloques[y-50][x] == 0)and( y!=0 )):
                  
                        
                              craneo_posicion[1]=y-50
                              
                              window.blit( craneo , ( x,y) )
                              
                              window.blit(fondo,(x,y))

                              tablero_bloques [y] [x] = 0
             #abajo                 
            elif ( y  != extremo_y-50):
                  if ((tablero_bloques[y+50][x] == 0)):

                      
                              craneo_posicion[1]=y+50
                              
                              window.blit( craneo , ( x,y) )
                              
                              window.blit(fondo,(x,y))

                              tablero_bloques [y] [x] = 0
                            
            
      def movimiento_carnero(tablero_bloques,extremo_x,extremo_y,carnero_posicion,cambios):
            
            x=carnero_posicion[0]
            y=carnero_posicion[1]
            
            tablero_bloques [y] [x] = 666
            

            
            

            #mueva a la izquierda
            if (x != 0 ) and (tablero_bloques[y][x-50] == 0)and(cambios=='izquierda'):
               
                   
                   window.blit( fondo , ( x+5,y) )
                   window.blit( carnero , ( x,y) )
                   carnero_posicion[0]=x-1

                   tablero_bloques [y] [x] = 0
                   
                   
                   return 'izquierda'

            elif (cambios == 'izquierda'):
              cambios='arriba'
                  
                  
                 
                 
            #mueve arriba  
            if ( y!=0 )and(tablero_bloques[y-50][x] == 0)and (cambios=='arriba'):
                      
                      window.blit( fondo , ( x,y+5) )
                      window.blit( carnero , ( x,y) )
                      carnero_posicion[1]=y-1
                      
                      tablero_bloques [y] [x] = 0
                      
                      
                      return 'arriba'

            elif (cambios == 'arriba'):
                  cambios='derecha'


            # Es para ir a la derecha
            
            if (( x  == extremo_x-50)or(tablero_bloques[y][x+50] != 0))and (cambios=='derecha'):
              
                   
              cambios='abajo'
              return 'abajo'
            
              
            elif (cambios=='derecha'):
              
              if(tablero_bloques[y][x+50] == 0):
                        
                        window.blit( fondo , ( x-5,y) )
                        window.blit( carnero , ( x,y) )
                        carnero_posicion[0]=x+1
                        tablero_bloques [y] [x] = 0
                        
                        
                        return 'derecha'
               
            #es para ir para abajo
            if (( y  == extremo_y-50)or(tablero_bloques[y+50][x] != 0))and (cambios=='abajo'):
              
              cambios='izquierda'
              return 'izquierda'
              
            elif (cambios =='abajo'):
              
              if(tablero_bloques[y+50][x] == 0):
                        
                        window.blit( fondo , ( x-5,y) )
                        window.blit( carnero , ( x,y) )
                        carnero_posicion[1]=y+1
                        tablero_bloques [y] [x] =0
                        
                        
                        return 'abajo'
            else:
                  window.blit( carnero , ( x,y) )
                      
      def movimiento_hitler (tablero,extremo_x,extremo_y,lgtbi_posicion):
        
        x=lgtbi_posicion[0]
        y=lgtbi_posicion[1]
        tablero_bloques [y] [x] = 666
                   
        num_aleatorio=int( randint ( 1, 20 ) )
        
        #uno para arriba
        if (num_aleatorio==1)and (tablero[y-50] [x] == 0) and (y != 0 ) :
          
                        lgtbi_posicion[1]=y-50
                        
                        window.blit( lgtbi , ( x,y) )
                        
                        window.blit(fondo,(x+50,y))
                        window.blit(fondo,(x-50,y))
                        window.blit(fondo,(x,y+50))
                        window.blit(fondo,(x,y-50))
                        tablero_bloques [y] [x] = 0
                      
        #dos pa abajo                
        elif (num_aleatorio==2) and (y != extremo_y-50 ) :
           if (tablero[y+50] [x] == 0): 
                        lgtbi_posicion[1]=y+50
                        
                        window.blit( lgtbi , ( x,y) )

                        window.blit(fondo,(x+50,y))
                        window.blit(fondo,(x-50,y))
                        window.blit(fondo,(x,y+50))
                        window.blit(fondo,(x,y-50))
                        tablero_bloques [y] [x] = 0
                        
        #tres pa izquierda  
        elif (num_aleatorio==3)and ((tablero[y][x-50] == 0) and (x != 0 ) ):
          
                        lgtbi_posicion[0]=x-50
                        
                        window.blit( lgtbi , ( x,y) )

                        window.blit(fondo,(x+50,y))
                        window.blit(fondo,(x-50,y))
                        window.blit(fondo,(x,y+50))
                        window.blit(fondo,(x,y-50))
                        tablero_bloques [y] [x] = 0
                        
                      
        #cuatro pa derecha
        elif (num_aleatorio==4 ) and (x != extremo_x-50) :
          if (tablero[y][x+50]== 0) :
                        lgtbi_posicion[0]=x+50
                        
                        window.blit( lgtbi , ( x,y) )
                        
                        window.blit(fondo,(x+50,y))
                        window.blit(fondo,(x-50,y))
                        window.blit(fondo,(x,y+50))
                        window.blit(fondo,(x,y-50))
                        tablero_bloques [y] [x] = 0
        else :
          window.blit( lgtbi , ( x,y) )
          window.blit(fondo,(x+50,y))
          window.blit(fondo,(x-50,y))
          window.blit(fondo,(x,y+50))
          window.blit(fondo,(x,y-50))
          
      def  ganesha (tablero,posicion_ganesha):

        num_alea= int( randint ( 1 , 3 ) )

        if ( num_alea == 1 ):
           window.blit(angel, (posicion_ganesha[0],posicion_ganesha[1]))
           tablero[ posicion_ganesha[1]+1  ]  [ posicion_ganesha[0]+1   ] = 444
                      
        else :
          window.blit(ganesha_dios , (posicion_ganesha[0],posicion_ganesha[1]))
          tablero [ posicion_ganesha[1]+1  ]  [ posicion_ganesha[0]+1   ] = 666
        

        
##______________________________________________________________________##


#instanciacion de clase ventana_______________________________     
ins_c_ale = ventana
#asignar a 'x y' el retorno de motodo tablero_aleatorio (los extremos)
extremo_y,extremo_x = ins_c_ale.tablero_aleatorio()
#pintar matriz ->tablero
tablero_bloques =     ins_c_ale.bloques(extremo_y,extremo_x)['tablero']
#________________________________________________________



#creacion de ventana________________________________
window= pygame.display.set_mode ((extremo_x,extremo_y))
#mensaje a la ventana:
pygame.display.set_caption("Drunken Monkeys")
#________________________________________________

#numero de bloques:
num_bloques = ins_c_ale.bloques(extremo_y,extremo_x)['num_bloques']
#obtener lista pared
lista_pared = ins_c_ale.pared(tablero_bloques, num_bloques , extremo_y, extremo_x)
###print (lista_pared)

#donde estara la meta#
posicion_yisus = lista_pared [ int ( randint (1 , len (lista_pared ) -1 ) ) ]
 




#instanciacion de clase carnero_______________________________
Enemigos = Clase_enemigos
##movimiento_carne = Carnero.movimiento_carnero(tablero_bloques,750,550,carnero_posicion)
##___________

print ( "area " ,  ((extremo_x/50 ) * (extremo_y/50) ) , "  Y = " ,  extremo_y/50  , "  X =" , extremo_x/50 )
#print (tablero_bloques)

print("angel/demonio - >",ganesha_posicion)
print ("carnero ---> ", carnero_posicion)
print("hitler ->",lgtbi_posicion)




##_____________________________________________________________________##
##funcion que pintara los bloques que no se destruyen en la ventana 
def pinte_bloques ():
      
      i=0
  
  #llena la matriz con los bloques 
      while (i < extremo_x-50 ):
              i=i+50
              j=50
              while (j <  extremo_y-50 ):
                #pinte el bloque
                      
                      window.blit(bloque,(i,j))
                      j+= 100
              i+= 50
  
      return 0
##_____________________________________________________________________##      
            
def TNT (lista_tnt):
      j= 0
      
      for i in lista_tnt:
            window.blit(tnt, ( lista_tnt [ j] [  0 ],  lista_tnt [ j ] [  1 ] ) )
            j+= 1
   

      return 0
##_____________________________________________________________________##

def pinte_pared (lista_pared ):

      j= 0 
      for i in lista_pared:
           
            if tablero_bloques [    lista_pared [ j ] [  1 ] , lista_pared [ j] [  0 ]   ] == 10 :
              
               window.blit(pared, ( lista_pared [ j] [  0 ],  lista_pared [ j ] [  1 ] ) )
            j+= 1

  
##_____________________________________________________________________##  
    

##_____________________________________________________________________##  

def explociones (donde,extremo_x,extremo_y,imagen,v) :

  x,y=donde[0],donde[1]
  
  if ( y == 0 ) and (x ==0):
    #explo sup izq
     window.blit(imagen,(0,0 ))
     window.blit(imagen,(0,50))
     window.blit(imagen,(50,0 ))
     
      
     tablero_bloques[y,x]= v
     tablero_bloques[0,50]= v
     tablero_bloques[50,0]= v
     
  elif ( y== 0 ) and (x ==extremo_x-50):
    #explo sup der
     window.blit(imagen,(extremo_x-50,0 ))
     window.blit(imagen,(extremo_x-100,0 ))
     window.blit(imagen,(extremo_x-50,50 ))
     
     
     tablero_bloques[0,extremo_x-50]= v
     tablero_bloques[0,extremo_x-100]= v
     tablero_bloques[50,extremo_x-50]= v
     
  elif ( y == extremo_y-50 ) and (x ==0):
    #explo inf izq
     window.blit(imagen,(0,extremo_y-50 ))
     window.blit(imagen,(0,extremo_y-100 ))
     window.blit(imagen,(50,extremo_y-50  ))

     
     tablero_bloques[extremo_y-50,0]= v
     tablero_bloques[extremo_y-100,0]= v
     tablero_bloques[extremo_y-50,50]= v

  elif ( y== extremo_y-50  ) and (x == extremo_x-50 ):
    #explo inf der 
     window.blit(imagen,(extremo_x-50 ,extremo_y-50  ))
     window.blit(imagen,(extremo_x-100 ,extremo_y-50  ))
     window.blit(imagen,(extremo_x-50 ,extremo_y-100  ))

     
     tablero_bloques[extremo_y-50,extremo_x-50]= v
     tablero_bloques[extremo_y-50,extremo_x-100]= v 
     tablero_bloques[extremo_y-100,extremo_x-50]= v
       
 #__________________________________________#
     
  elif(x== 0 ) and(tablero_bloques[y,x+50]==15):
     
     #explo vertical    
     window.blit(imagen,(x,y))
     window.blit(imagen,(x,y+50 ))
     window.blit(imagen,(x,y-50))

     tablero_bloques[y,x]= v
     tablero_bloques[y+50,x]= v
     tablero_bloques[y-50,x]= v

  elif (x == 0 ) and (tablero_bloques[y+50,x+50]==15):
     
     #explo horizontal-vertical  en  x=0
     window.blit(imagen,(x,y))
     window.blit(imagen,(x,y-50 ))
     window.blit(imagen,(x+50,y ))
     window.blit(imagen,(x,y+50))
     
     tablero_bloques[y,x]= v
     tablero_bloques[y-50,x]= v
     tablero_bloques[y,x+50]= v
     tablero_bloques[y+50,x]= v

  elif  (y==0 ) and  (tablero_bloques[y+50,x]==15):
     
     #explo vertical    
     window.blit(imagen,(x,y))
     window.blit(imagen,(x-50,y ))
     window.blit(imagen,(x+50,y ))

     tablero_bloques[y,x]= v
     tablero_bloques[y,x-50]= v
     tablero_bloques[y,x+50]= v

  elif (y == 0 ) and (tablero_bloques[y+50,x+50]==15):
     
     #explo horizontal-vertical  y=0
     window.blit(imagen,(x,y))
     window.blit(imagen,(x-50,y ))
     window.blit(imagen,(x,y+50 ))
     window.blit(imagen,(x+50,y))

     
     tablero_bloques[y,x]= v
     tablero_bloques[y,x-50]= v
     tablero_bloques[y+50,x]= v
     tablero_bloques[y,x+50]= v
     
  elif  (x==extremo_x-50) and  (tablero_bloques[y+50,x-50]==15):
       
     #explo vertical en extremo x
        
     window.blit(imagen,(x,y))
     window.blit(imagen,(x,y-50 ))
     window.blit(imagen,(x,y+50))
     window.blit(imagen,(x-50,y))
     
     tablero_bloques[y,x]= v
     tablero_bloques[y-50,x]= v
     tablero_bloques[y+50,x]= v
     tablero_bloques[y,x-50]= v
     
  elif  (y==extremo_y-50) and  (tablero_bloques[y-50,x+50]==15):
       
     #explo vertical en extremo x
        
     window.blit(imagen,(x,y))
     window.blit(imagen,(x-50,y ))
     window.blit(imagen,(x+50,y))
     window.blit(imagen,(x,y-50))
     
     tablero_bloques[y,x]= v
     tablero_bloques[y,x-50]= v
     tablero_bloques[y,x+50]= v
     tablero_bloques[y-50,x]= v  

  elif   (tablero_bloques[y,x-50]==15):
     window.blit(imagen,(x,y))
     window.blit(imagen,(x,y-50 ))
     window.blit(imagen,(x,y+50 ))

     tablero_bloques[y,x]= v
     tablero_bloques[y-50,x]= v
     tablero_bloques[y+50,x]= v 
     #explo vertical    
     
     
  elif   (tablero_bloques[y-50,x]==15):
     
     #explo horizontal
     window.blit(imagen,(x,y))
     window.blit(imagen,(x-50,y ))
     window.blit(imagen,(x+50,y ))

     tablero_bloques[y,x]= v
     tablero_bloques[y,x-50]= v
     tablero_bloques[y,x+50]= v 
       
  else:

    window.blit(imagen,(x,y))
    window.blit(imagen,(x+50,y))
    window.blit(imagen,(x-50,y))
    window.blit(imagen,(x,y+50))
    window.blit(imagen,(x,y-50))

    
    tablero_bloques[y,x]= v
    tablero_bloques[y,x+50]= v
    tablero_bloques[y,x-50]= v
    tablero_bloques[y+50,x]= v
    tablero_bloques[y-50,x]= v



##_____________________________________________________________________##  
    

#inicializar la coordenada del mono
mono_x , mono_y = 0 , 0
#judio inicial
judio_x, judio_y= extremo_x-50,extremo_y-50

#velocidad de movimiento del mono
mono_velocidad= 50

#pintar color ventana fondo
window.fill( (205, 133,63))


#atributos globales de tnt 
tiempo_tnt= 0
hay_bomba='no'
exploto_bomba='no'
numero_de_tnt = 0
poner_bomba = True

ejey,ejex= 0,0
lista_tnt = []
boleano = False
##________________##

#una lista de dos datos que dan la coordenada donde esta la bomba
donde = [ ]

#mostrar la ventana:-----------------------------------------------------------------------------------


#CANO,aqui cree la clase judio que tiene los metodos de moverse que hay en los eventos y explotar....




juego = True


forma_mono= mono_derecha
pausa_craneo=0




while juego :

   window.blit ( judio, (judio_x,judio_y))
  
  
   window.blit ( forma_mono, (mono_x,mono_y))
   
   ##pierda
   if ( tablero_bloques[mono_y][mono_x]==666)or( tablero_bloques[mono_y+1][mono_x+1]==666):
            window.blit( perdedor  ,(0, 0) )
            juego = False
   ##gane         
   if ( tablero_bloques[mono_y+1][mono_x+1]==444):
            window.blit( ganador  ,(0, 0) )
            juego = False
            
   reloj.tick(40)
   
   cambios = Enemigos.movimiento_carnero(tablero_bloques,extremo_x,extremo_y,carnero_posicion,cambios)
 
   window.blit ( forma_mono, (mono_x,mono_y))
   #PERDIO POR EL CRANEO
   if ((mono_x== craneo_posicion[0]) and (mono_y == craneo_posicion[1])):
         window.blit( perdedor  ,(0, 0) )
         juego = False
   #PERDIO POR EL CARNERO   
   if ((mono_x== carnero_posicion[0]) and (mono_y ==carnero_posicion[1])):
         window.blit( perdedor  ,(0, 0) )
         juego = False
         
   if(pausa_craneo==30):
         Enemigos.movimiento_craneo(tablero_bloques,extremo_x,extremo_y,craneo_posicion,mono_x,mono_y)
         pausa_craneo=0
   
   pausa_craneo+=1
   Enemigos.movimiento_hitler(tablero_bloques,extremo_x,extremo_y,lgtbi_posicion)
   window.blit ( craneo, (craneo_posicion[0],craneo_posicion[1]))
   window.blit ( carnero, (carnero_posicion[0],carnero_posicion[1]))
   
   Enemigos.ganesha(tablero_bloques , ganesha_posicion)
  
   window.blit ( forma_mono, (mono_x,mono_y))
   
  ##__________pinte todo esto en cada whilaso__________##
  
   pinte_bloques()
   
   pinte_pared(lista_pared)
   
   ##___________________GANE______________________________##
   
   if tablero_bloques [ posicion_yisus [1], posicion_yisus [0] ] == 0 :
     
        window.blit(yisus,(posicion_yisus [0],posicion_yisus [1]))
        
        if (posicion_yisus [1]== mono_y)and (posicion_yisus [0]== mono_x) :
            window.blit( ganador , (0,0) )
            window.blit( ganador_dos , (0,20) )
            juego = False 
   ##_________________________________________________________   
    
      
   tiempo = int (pygame.time.get_ticks()/1000 )
   
   
   
   #quite la bomba que tenia puesta a los 6 segundos ________________
   if  (tiempo-tiempo_tnt == 2 ) and (hay_bomba == 'si'):
         
         donde= lista_tnt.pop(0)
         
         

         #vaya a explociones
         explociones (donde,extremo_x,extremo_y,explocion,666)

         ##___________perder_______________##
         if tablero_bloques[mono_y][mono_x]==666:
            window.blit( perdedor  , ((extremo_x/2)-50, (extremo_y/2)) )
            juego = False
           
         hay_bomba ='no'
         exploto_bomba='si'
         numero_de_tnt =0
         poner_bomba= False
    ##_______________________________________________________     
   
         
   ##__explociones _________________________##
         
   if  (tiempo-tiempo_tnt == 3 )and (exploto_bomba == 'si'):
     
       #vaya a explociones
        explociones (donde,extremo_x,extremo_y,fondo,0)
        exploto_bomba ='no'
        poner_bomba = True 


  
   #lista de eventos:
   for evento in pygame.event.get():

        #si pulsan la X
     if evento.type == QUIT :
           pygame.quit()
           sys.exit()

        # si precionan una tecla
     if evento.type == pygame.KEYDOWN :

      #evento.key para  obtener que tecla fue oprimida
       
            
            
            ##lanzar tnt     
            if (evento.key == K_z )and (numero_de_tnt == 0 )and poner_bomba :
               
               #window.fill( (205, 133,63))
               
               tiempo_tnt = tiempo 
               lista_tnt.append( [mono_x,mono_y ] )
               tablero_bloques[ mono_y,mono_x] = 30 
               #print (lista_tnt)
               #print ( lista_tnt [ 0 ] [  0 ])              
               TNT(lista_tnt)
               window.blit(mono_centro,(mono_x,mono_y))
               hay_bomba = 'si'
               numero_de_tnt = 1
               forma_mono= mono_centro

               

               
                # valida tecla oprimida#       #valida bordes#     #__________valida bloques______________#      #_____Valida las paredes ________#
            if   (evento.key == K_LEFT) and (mono_x >0 )and (tablero_bloques[ mono_y,mono_x-50] == 0 )and(tablero_bloques[ mono_y,mono_x-50] == 0 ) :
                
                 #pinte el fondo
                 window.blit(fondo,(mono_x,mono_y))
                 #pinte tnt
                 TNT(lista_tnt)            
                 #pinte el mono
                 mono_x -= mono_velocidad
                 window.blit(mono_izquierda,(mono_x,mono_y))
                 forma_mono= mono_izquierda 
                 
                 

            if  (evento.key == K_RIGHT)and (mono_x< extremo_x - 50)and (tablero_bloques[ mono_y,mono_x+50] == 0 ) and(tablero_bloques[ mono_y,mono_x+50] == 0 ):
                
                #window.fill( (205, 133,63))
                window.blit(fondo,(mono_x,mono_y))
                TNT(lista_tnt)
                mono_x +=  mono_velocidad
                window.blit(mono_derecha,(mono_x,mono_y))
                forma_mono= mono_derecha
                

            if   (evento.key == K_UP)and (mono_y> 0 ) and (tablero_bloques[ mono_y-50,mono_x] == 0 )and(tablero_bloques[ mono_y-50,mono_x] == 0 ):
                 
                 #window.fill( (205, 133,63))
                 window.blit(fondo,(mono_x,mono_y))
                 TNT(lista_tnt)
                 mono_y -=  mono_velocidad
                 window.blit(mono_arriba,(mono_x,mono_y))
                 forma_mono= mono_arriba
                 
                 

            if  (evento.key == K_DOWN) and (mono_y<extremo_y-50 ) and (tablero_bloques[ mono_y+50,mono_x] == 0 )and(tablero_bloques[ mono_y+50,mono_x] == 0 ):
                
                #window.fill( (205, 133,63))
                window.blit(fondo,(mono_x,mono_y))
                TNT(lista_tnt)
                mono_y +=  mono_velocidad
                window.blit(mono_abajo,(mono_x,mono_y))
                forma_mono= mono_abajo
   
                  
## termina while ##            
                
                
                
            







   #mostrar todo basicamente (se mantiene actualizando con ese metodo)
   pygame.display.update()


"""
   if mono_x<extremo_x:
     #desplazar a la derecha
     mono_x += mono_velocidad
   else if mono_y<extremo_y:
     #desplazar a la derecha
     mono_x += mono_velocidad
   if mono_x>extremo_x:
     #desplazar a la derecha
     mono_x += mono_velocidad
   if mono_x<extremo_x:
     #desplazar a la derecha
     mono_x += mono_velocidad

"""













