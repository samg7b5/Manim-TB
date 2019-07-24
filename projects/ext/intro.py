from manimlib.imports import *

class ManimFAQS(Scene):
	def construct(self):
		self.add(
			Text("Manim \\\\\\sc FAQ").scale(6).set_color_by_gradient(RED_A,RED_E)
		)

class VisualTools(Scene):
    def construct(self):
        texto=Text("Manim tutorial\\\\","\\sc 5\\\\ Visual tools\\\\ \\& Documentation")\
             .scale(3.3).set_color_by_gradient(PURPLE,BLUE,TEAL)
        texto[1].scale(0.9)
        VGroup(texto[0],texto[1]).move_to(ORIGIN)
        self.add(texto)

class ManimFAQ(Scene):
	def construct(self):
		self.add(
			Text("Manim \\\\\\sc Preguntas\\\\ frecuentes").scale(4).set_color_by_gradient(RED_A,RED_E)
		)

class VisualTools2(Scene):
    def construct(self):
        texto=Text("Tutorial de Manim\\\\\\sc 5\\\\"," Herramientas visuales\\\\","\\& Documentación")\
             .scale(3.3).set_color_by_gradient(PURPLE,BLUE,TEAL)
        texto[1].scale(0.7)
        texto[2].scale(0.9)
        VGroup(texto[0],texto[1],texto[2]).move_to(ORIGIN)
        self.add(texto)

class Indice(EscenaContenido):
    CONFIG={
    "escala":0.9,
    "mover_contenido":[2,-0.5,0],
    "font_titulo":"\\rm",
    "salida":True,
    "tiempo_espera":3,
    }
    def setup(self):
        self.contenido=[
            "¿Qué es \\tt CONFIG?",
            "--",
            "¿Cómo cambiar el color de fondo?",
            "--",
            "¿Cómo quitar el fondo negro de las palabras?",
            "--",
            "¿Cómo ordenar múltiples objetos?",
            "--",
            "¿Cómo cambiar la posición y tamaño de la cámara?",
            "--",
            "¿Cómo hacer una transformación lineal?",
            "--",
            "¿Cómo remover todos los objetos de la pantalla?",
            "--",
            "¿Cómo hacer el efecto lupa?",
            "--",
            "\\,"
            ]
