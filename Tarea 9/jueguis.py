import pygame
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

pygame.init()
  
# Establecemos la altura y largo de la pantalla
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
 
pygame.display.set_caption("Rectángulo saltarín")
 
#Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False
  
# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
  
# Posición de partida del rectángulo
rect_x = 50
rect_y = 50
 
# Velocidad y dirección del rectángulo
rect_cambio_x = 5
rect_cambio_y = 5
 
# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
# Usamos esta variable booleana para avisar que el juego se acabó variable.
game_over = False;
 
# -------- Bucle Principal del Programa -----------
while not hecho:
     
    # --- Procesamiento de Eventos
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
             
        # Usaremos un click del ratón para indicar que el juego se acabó.
        # Reemplaza éste, y establece juego_terminado a verdadero en tu propio
        # juego cuando sepas que el juego se acabó. (Algo así como vidas==0)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            game_over = True
             
    # --- Lógica del Juego
 
    # Solo mueve y procesa la lógica del juego si éste no ha terminado.
    if game_over == False:
        # Mueve el punto de partida del rectángulo        
        rect_x += rect_cambio_x
        rect_y += rect_cambio_y
 
       # Rebota el rectángulo, si hace falta.
        if rect_y > 450 or rect_y < 0:
            rect_cambio_y = rect_cambio_y * -1
        if rect_x > 650 or rect_x < 0:
            rect_cambio_x = rect_cambio_x * -1
     
    # --- Dibuja el marco
 
    # Establecemos el color de fondo
    pantalla.fill(ROJO)
 
    # Dibujamos el rectángulo
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(pantalla, VERDE , [rect_x + 10, rect_y + 10, 30, 30])
 
    if game_over:
        # Si el juego finalizó, dibujamos 'el juego se acabó'.
        texto = fuente.render("Game Over", True, BLANCO)
        texto_rect = texto.get_rect()
        texto_x = pantalla.get_width() / 2 - texto_rect.width / 2
        texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
        pantalla.blit(texto, [texto_x, texto_y])
         
    else:
        # Si el juego no acabó, dibujamos lo siguiente.
        texto = fuente.render("Haz click para terminar el juego", True, BLANCO)
        texto_rect = texto.get_rect()
        texto_x = pantalla.get_width() / 2 - texto_rect.width / 2
        texto_y = pantalla.get_height() / 2- texto_rect.height / 2
        pantalla.blit(texto, [texto_x, texto_y])
 
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
    pygame.display.flip()
pygame.quit ()