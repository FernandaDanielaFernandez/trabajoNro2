import pygame
from class_pantallas import *
pygame.init()

pantalla = Pantalla((800,600),"imagenes\\fondo 3.jpg")

def inicio():
    pantalla = Pantalla((800,600),"imagenes\\fondo 3.jpg")
    run = True
    ingresar_nombre = True
    nombre = ""
    audio = True

    while run:
        pantalla.imagenFondo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if ingresar_nombre:
                    if event.key == pygame.K_RETURN:
                        # Aquí puedes almacenar el nombre del jugador y continuar con tu juego
                        if len(nombre) > 0:
                            ingresar_nombre = False
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        if len(nombre) < 8:
                            nombre += event.unicode
            else:
                if ingresar_nombre == False:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 representa el clic izquierdo
                        x, y = event.pos
                        # Verificar si se hizo clic en el área de "Jugar"
                        if 45 <= x <= 125 and 200 <= y <= 240:
                            run = False
                            # Aquí puedes realizar acciones relacionadas con hacer clic en Jugar
                        # Verificar si se hizo clic en el área de "Salir"
                        elif 45 <= x <= 125 and 250 <= y <= 290:
                            pygame.quit()
                            quit()  # Puedes agregar más lógica aquí según tus necesidades
                        elif 45 <= x <= 253 and 300 <= y <= 340:
                            if audio:
                                audio = False
                            else:
                                audio = True

        # Dibujar texto e opciones 
        rectangulo_nombre = pantalla.dibujar_rectangulo((250,250,250), (45, 100, 150, 30),)
        jugar = pantalla.dibujar_rectangulo((0,0,0), (45, 200, 82, 40))
        pantalla.mostrar_texto(" JUGAR",30,(250,250,252),(45,210))
        salir = pantalla.dibujar_rectangulo((0,0,0), (45, 250, 75, 40))
        pantalla.mostrar_texto(" SALIR",30,(250,250,252),(45,260))
        audio_rectangulo = pantalla.dibujar_rectangulo((0,0,0), (45, 300, 208, 40),)
        pantalla.mostrar_texto(" DESACTIVAR AUDIO",30,(250,250,252),(45,310))
        pantalla.mostrar_texto("Ingresa tu nombre y presiona 'Enter' para continuar:",30,(250,250,252),(50,50))
        pantalla.mostrar_texto(nombre, 30, (0,0,0), (47,110))
        if audio:
            pantalla.mostrar_texto("AUDIO ACTIVADO",30,(250,250,252),(260,310))
        else:
            pantalla.mostrar_texto("AUDIO DESACTIVADO",30,(250,250,252),(260,310))

        pygame.display.flip()
    return nombre, audio