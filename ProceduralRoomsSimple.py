from manim import *

class SimpleProcedural(Scene):
    def construct(self):
        # Parâmetros iniciais
        largura_mapa = 6
        altura_mapa = 4

        # Criar o mapa inicial
        mapa = Rectangle(width=largura_mapa, height=altura_mapa, fill_color=BLUE, fill_opacity=0.5, color=WHITE)
        self.play(Create(mapa))

        # Chamar o algoritmo BSP para dividir o espaço
        self.dividir_espaco(mapa, 5)

    def dividir_espaco(self, retangulo, nivel):
        if nivel == 0:
            return

        # Escolher aleatoriamente uma direção de divisão (horizontal ou vertical)
        divisao_horizontal = np.random.choice([True, False])

        # Calcular ponto de divisão
        if divisao_horizontal:
            altura_divisao = retangulo.get_height() * np.random.uniform(0.2, 0.8)
            linha_divisao = DashedLine(retangulo.get_bottom() + altura_divisao * UP, retangulo.get_top() + altura_divisao * UP, color=WHITE)
        else:
            largura_divisao = retangulo.get_width() * np.random.uniform(0.2, 0.8)
            linha_divisao = DashedLine(retangulo.get_left() + largura_divisao * RIGHT, retangulo.get_right() + largura_divisao * RIGHT, color=WHITE)

        # Dividir o retangulo
        self.play(Create(linha_divisao))
        self.wait(0.5)

        

        # Chamada recursiva para as sub-áreas
        self.dividir_espaco(superior, nivel - 1)
        self.dividir_espaco(inferior, nivel - 1) if divisao_horizontal else self.dividir_espaco(esquerda, nivel - 1), self.dividir_espaco(direita, nivel - 1)
