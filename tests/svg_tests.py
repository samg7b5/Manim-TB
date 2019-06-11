from manimlib.imports import *

set_custom_quality(1400,20)

OUTPUT_DIRECTORY = "TESTS/SVG_TESTS"

class CheckSpeach(CheckSVGPoints):
	CONFIG={
    "file":"mix/Speach.svg",
	"scale":1.5,
    "shadow_point_number":1,
	"show_element_points":[0],
    "get_cero":True,
	}

class Conversacion(Scene):
    def construct(self):
        conversation = Conversation(self)
        conversation.add_bubble("Hola!")
        self.wait(2)
        conversation.add_bubble("Hola, qué tal?")
        self.wait(2)
        conversation.add_bubble("Esta es mi primera animación de\\\\ conversación.")
        self.wait(3) # 41
        conversation.add_bubble("Está muy bien!")
        self.wait(2) # 48
        conversation.add_bubble("x")
        self.wait(2)
        #self.play(FadeOut(conversation.dialog[:]))
        self.wait()
