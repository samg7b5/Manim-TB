from manimlib.imports import *

set_custom_quality(800,10)

OUTPUT_DIRECTORY = "TESTS/ANIMATIONS_TESTS"

class AnimationTest(Scene):
	def construct(self):
		t=Text("Hola")
		self.Oldplay(Escribe(t))
		self.wait()

class TypeWriterScene(Scene):
    def construct(self):
        texto=Text("\\tt Ojalá funcione")[0]
        self.wait()
        KeyBoard(self,texto,lag=0.1)
        self.wait()

class TextWhitoutFill(Text):
    CONFIG={
        "stroke_width": 1.5,
        "fill_opacity": 0,
    }
    

class NewOwnAnimations(Scene):
    def construct(self):
        text1=Formula("x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}")[0]
        text2=Text("Alexander")
        obj=Circle(color=RED,fill_opacity=1)

        VGroup(text1,text2,obj).arrange(DOWN)

        text1.move_to(ORIGIN)

        self.wait(0.2)

        """
        self.play(
            FadeIn(text1,submobject_mode="lagged_start",rate_func=linear),
            )

        self.play(
            LaggedStart(
            *[FadeInFromPoint(obj,point=[2,0,0])for obj in text1])
        )

        directions=[DL,DOWN,DR,RIGHT,UR,UP,UL,LEFT]
        cycle_directions=it.cycle(directions)
        reverse_directions=it.cycle(list(reversed(directions)))

        self.play(
            LaggedStart(
            *[FadeInFromPoint(obj,point=obj.get_center()+d)for obj,d in zip(text1,reverse_directions)])
        )
        """
        

        def get_vector_from(obj,point=ORIGIN,dist=2):
            vect=obj.get_center()-point
            return vect*dist

        self.play(
            LaggedStart(
            *[FadeInFromPoint(obj,point=get_vector_from(obj,dist=1.4))for obj in text1]),
            run_time=2
        )
        

        self.wait()

class Playground(Scene):
    def construct(self):
        squ = Square(fill_opacity=1, color=RED)
        self.play(FadeIn(squ))

class HelpKeys(Scene):
    def construct(self):
        formulas=VGroup(
            TexMobject("2t-5"),
            TexMobject("3t-4")
        ).arrange(DOWN)

        brace=Brace(formulas,LEFT,buff=SMALL_BUFF)

        self.add(formulas,brace)

class Trace(MovingCameraScene):
    def construct(self):
        Grid=NumberPlane()
        self.add(Grid)
        self.camera_frame.scale(.25)
        self.camera_frame.shift(np.array([2,1,0]))
        vec1=Vector(np.array([1,1,0])).shift(np.array([1,1,0]))
        vec2=Vector(np.array([1,1,0])).shift(np.array([2,1,0]))
        Grp=VGroup(vec1,vec2)
        vec1.scale(.5)
        self.add(Grp)
        self.wait()

class VectorScaling(Scene):
    def construct(self):
        vector=Vector(UR)
        self.play(vector.scale,2,{"about_point":vector[0].points[0]})


class Myobject(VMobject):
    def __init__(self, offset, **kwargs):
        self.offset= offset
        VMobject.__init__(self, **kwargs)
        self.generate_points()

    def generate_points(self):
        self.term = Square()
        self.term.set_style(fill_color=GREEN, fill_opacity=1)
        self.term.move_to(RIGHT*self.offset)
        self.add(self.term)


class MyExample(Scene):
    def construct(self):
        d1 = Square()
        d1.set_style(fill_color=GREEN, fill_opacity=1)
        self.add(d1)

        d2= Myobject(offset=3)
        self.add(d2)

class VectorScaling2(Scene):
    def construct(self):
        vector=Vector(UR)
        self.add(vector)

        self.wait()

        vector_origin=vector[0].points[0]
        vector.scale(0.25,about_point=vector_origin)

        self.wait()