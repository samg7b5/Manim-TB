from manimlib.imports import *



class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This Alex is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

class PruebaText(Scene):
    def construct(self):
        grupo=VGroup(
            Text("Holiñá"),
            Formula("v\\to\\syx")
            ).arrange(DOWN)

        self.add(grupo)

class PruebaTikz(Scene):
    def construct(self):
        grupo=VGroup(
            SimpleTikz("\\draw(0,0)--(1,1);")
            ).arrange(DOWN)

        self.add(grupo)

class PruebaListing(Scene):
    def construct(self):
        grupo=VGroup(
            SimpleListings("""
            for i:=maxint to 0 do
            begin
                {  do nothing }
                end;
            Write('Case insensitive ');
            Write('Pascal keywords.');
            """))

        self.add(grupo)

class PruebaMusic(Scene):
    def construct(self):
        music=MusicTeX("""
                \\parindent10mm
                \\instrumentnumber{1}
                \\setname1{} 
                \\setstaffs1{2}
                \\setclef16
                \\startextract
                \\NOTEs\\zql{'C}\\qu G|\\zql{e}\\qu j\\en
                \\NOTEs\\zql{F}\\qu{''A}|\\zql{f}\\qu{'c}\\en
                \\NOTEs\\zql{G}\\qu{'G}|\\zql{d}\\qu{'b}\\en
                \\NOTEs\\zhl{C}\\hu{'G}|\\zhl{e}\\hu{'c}\\en
                \\endextract
            """)
        self.add(music)

class PruebaPB(Scene):
    def construct(self):
        p=Parentheses(Line(DOWN,UP),LEFT)
        self.add(p)

class Augie(GenericFont):
    CONFIG={
    "font":"\\ECFAugie",
    }

class PruebaEmerald(Scene):
    def construct(self):
        p=Augie("Hola mundi")
        self.add(p)

class PruebaFull(Scene):
    def construct(self):
        p=TextFull("\\ECFAugie Alexander")
        self.add(p)

# See old_projects folder for many, many more

test_text,test_tex=get_template_tex(
    "test",
    begin="\\begin{equation}\n",
    end="\\end{equation}\n"
    )

class TextTest(TexMobject):
    CONFIG={
    "template_tex_file_body":test_tex
    }

class PruebaTest(Scene):
    def construct(self):
        t=TextTest("v\\to x")
        self.add(t)

class OmegaDice(Scene):
    def construct(self):
        Ale=Alex().to_edge(DOWN)
        palabras_ale = TextMobject("Learn to do \\\\animations with me!!")
        self.add(Ale)
        self.play(OmegaCreatureSays(
            Ale, palabras_ale, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)

class ProgressionChords(MusicalScene):
    CONFIG = {"include_sound": True}
    def construct(self):
        self.teclado_transparente=self.definir_teclado(4,self.prop,0).set_stroke(None,0)
        self.teclado_base=self.definir_teclado(4,self.prop,1)
        self.teclado_base.move_to(ORIGIN+DOWN*3)
        self.teclado_transparente.move_to(ORIGIN+DOWN*3)

        self.agregar_escenario()
        self.primer_paso(simbolos_faltantes=[14,15,16,17,18,19,20,21])
        self.add_sound("armonicos/pI",gain=-12)
        self.progresion(0,run_time=2)
        self.add_sound("armonicos/pIV",gain=-12)
        self.progresion_con_desfase(paso=1,desfase=22,y1=8,x2=8,y2=16,run_time=2)
        self.add_sound("armonicos/pV",gain=-12)
        self.progresion_con_desfase(paso=2,desfase=30,y1=8,x2=10,y2=18,simbolos_faltantes=[38,39],run_time=2)
        self.add_sound("armonicos/pI2",gain=-12)

        self.intervalos()

        self.salida_teclado()
        


    def importar_partitura(self):
        self.partitura=MusicTeX("""
                \\parindent10mm
                \\instrumentnumber{1}
                \\setname1{} 
                \\setstaffs1{2}
                \\setclef16
                \\startextract
                \\NOTEs\\zql{'C}\\qu G|\\zql{e}\\qu j\\en
                \\NOTEs\\zql{F}\\qu{''A}|\\zql{f}\\qu{'c}\\en
                \\NOTEs\\zql{G}\\qu{'G}|\\zql{d}\\qu{'b}\\en
                \\NOTEs\\zhl{C}\\hu{'G}|\\zhl{e}\\hu{'c}\\en
                \\endextract
            """,color=BLACK,background_stroke_width=0)[0].shift(UP).scale(0.8)

    def definir_cambios_notas(self):
        self.cambios_notas=[[[
                (   14, 15, 17, 16, 18, 19, 21, 20, ),
                (   22, 23, 25, 24, 26, 27, 29, 28, )
        ]]]
        tt=self.definir_notas(4)
        self.teclas=[[tt[0][1],tt[7][1],28,36],
                    [tt[5][0],tt[9][1],tt[5][2],tt[0][3]],
                    [tt[7][0],tt[7][1],tt[2][2],tt[11][2]],
                    [tt[0][0],tt[7][1],28,36]]

    def definir_colores(self):
        
        self.colores_notas=[
                       ([21,20,29,28,36,37,47,46],self.colores[3]),
                       ([18,19,26,27,34,35,44,45],self.colores[2]),
                       ([17,16,25,24,33,32,43,42],self.colores[1]),
                       ([14,15,22,23,30,31,40,41,38,39],self.colores[0])
                      ]


    def definir_cifrado(self):
        cifrado=VGroup(
            TexMobject("\\mbox{I}",color=BLACK),
            TexMobject("\\mbox{IV}",color=BLACK),
            TexMobject("\\mbox{V}",color=BLACK),
            TexMobject("\\mbox{I}",color=BLACK)
            )
        
        bajo=[15,23,31,41]
        cifrado[0].next_to(self.partitura[15],DOWN,buff=1.3)
        cords_x=[*[self.partitura[w].get_center()[0]for w in bajo]]
        
        for i in range(1,4):
            cifrado[i].move_to(cifrado[i-1])
            dis=cords_x[i]-cords_x[i-1]
            cifrado[i].shift(np.array([dis,0,0]))

        self.cifrado=cifrado        

    def agregar_escenario(self):
        self.grupoA=VGroup(*[self.partitura[cont]for cont in [12,13]])
        titulo=TextMobject("\\sc Progression chords scene.",color=BLACK).to_corner(UL)

        self.mandar_frente_sostenido(4,self.teclado_base)
        self.mandar_frente_sostenido(4,self.teclado_transparente)

        self.play(*[LaggedStartMap(GrowFromCenter, self.partitura[i],run_time=2)for i in range(1,11)],
            LaggedStartMap(DrawBorderThenFill,self.teclado_base),LaggedStartMap(DrawBorderThenFill,self.teclado_transparente),
            Write(titulo),*[GrowFromCenter(x)for x in self.grupoA]
            )



    def intervalos(self):
        i6m_v=self.intervalo_v(21,15,"8\\rm J")
        i5J_v=self.intervalo_v(25,29,"3-",direccion=RIGHT)

        i2m_h=self.intervalo_h(17,25,"2+")
        i5J_h=self.intervalo_h(15,23,"5\\rm J")

        self.ap_inter_v(i6m_v)
        self.play(ReplacementTransform(i6m_v.copy(),i5J_v))
        self.ap_inter_h(i2m_h)
        self.play(ReplacementTransform(i2m_h,i5J_h))
        
    def salida_teclado(self):
        self.play(*[
                ApplyMethod(
                    self.teclado_transparente[i].set_fill,None,0
                    )
                for i,color in self.cambios_colores_teclas[3]
                ],
            run_time=1
        )
        self.remove_foreground_mobjects(self.teclado_transparente)
        self.remove_foreground_mobjects(self.teclado_base)
        self.remove(self.teclado_transparente)
        self.mandar_frente_sostenido_parcial(4,self.teclado_base)
        self.play(
            *[LaggedStartMap(FadeOut,objeto,run_time=1)for objeto in self.mobjects],
            )

class PruebaImages(Scene):
    def construct(self):
        im=Patreon()
        self.add(im)
