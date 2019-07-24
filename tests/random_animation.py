from manimlib.imports import *

set_custom_quality(800,10)

OUTPUT_DIRECTORY = "TESTS/ANIMATIONS_TESTS"

class AnimationTest(Scene):
	def construct(self):
		t=Text("Hola")
		self.Oldplay(Escribe(t))
		self.wait()

class AnimationTest2(Scene):
	def construct(self):
		t=Text("Hola1")
		self.Oldplay(Escribe(t))
		self.wait()