import pygame
from class_pantallas import *
from base_de_dstor import *
pygame.init()

#pantalla = Pantalla((800,600),"imagenes\\fondo 3.jpg")
def final(vidas_nave_gigante):
    pantalla = Pantalla((800,600),"imagenes\\imagen_final.jpg")
    run = True
    volver_inicio = False

    while run:
        pantalla.imagenFondo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 representa el clic izquierdo
                    x, y = event.pos
                    # Verificar si se hizo clic en el área de "Jugar"
                    if 45 <= x <= 245 and 400 <= y <= 440:
                        run = False
                        # Aquí puedes realizar acciones relacionadas con hacer clic en Jugar
                    # Verificar si se hizo clic en el área de "Salir"
                    elif 45 <= x <= 265 and 450 <= y <= 480:
                        volver_inicio = True
                    elif 45 <= x <= 125 and 500 <= y <= 540:
                        pygame.quit()
                        quit()
        # Dibujar texto e opciones 
        volver_a_jugar = pantalla.dibujar_rectangulo((0,0,0), (45, 400, 200, 40))
        pantalla.mostrar_texto(" VOLVER A JUGAR",30,(250,250,252),(45,410))
        pantalla_de_inicio = pantalla.dibujar_rectangulo((0,0,0), (45, 450, 220, 40))
        pantalla.mostrar_texto(" PANTALLA DE INICIO",30,(250,250,252),(45,460))
        salir = pantalla.dibujar_rectangulo((0,0,0), (45, 500, 80, 40),)
        pantalla.mostrar_texto(" SALIR",30,(250,250,252),(45,510))
        mejores_jugadores = obtener_mejores_jugadores()
        y_pos = 430
        pantalla.mostrar_texto("Mejores jugadores:", 30, (255, 255, 255), (400, 400))
        pantalla.mostrar_texto("JUEGO FINALIZADO",100,(250,250,252),(45,45))
        if vidas_nave_gigante >= 10:
            pantalla.mostrar_texto("GANASTE",50,(250,250,252),(60,115))
        else:
            pantalla.mostrar_texto("TAL VEZ LA PROXIMA TENGAS MAS SUERTE",40,(250,250,252),(45,115))
        for jugador in mejores_jugadores:
            nombre, puntaje = jugador
            texto_jugador = f"Nombre: {nombre}, Puntaje: {puntaje}"
            pantalla.mostrar_texto(texto_jugador, 25, (255, 255, 255), (400, y_pos))
            y_pos += 30
        if volver_inicio:
            return volver_inicio

        pygame.display.flip()