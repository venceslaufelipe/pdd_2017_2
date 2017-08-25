class Fruta:
    def __init__(self, nome = "abacate", cor = "verde", saciar = 1):
        self.cor = cor
        self.nome = nome
        self.saciar = saciar
        self.existe = True
    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, fome, preferencia):
        self.nome = nome
        self.fome = fome
        self.preferencia = preferencia

    def esperar(self):
        self.fome += 1

    def oferecerFrutas(self, lista_frutas):
        for fruta in lista_frutas:
            if ((self.preferencia == fruta.nome) \
                or (self.preferencia == fruta.cor)) \
                and fruta.existe and (self.fome > 0):
                    if fruta.saciar > 1:
                        self.fome -= fruta.saciar
                    else:
                        self.fome -= 1
                    fruta.existe = False
                    print(self.nome, "comeu", fruta.nome)

class Zoologico:
    def alimentar(self, frutas, animais):
        for animal in animais:
            animal.oferecerFrutas(frutas)
        for i in range(len(frutas) - 1, -1, -1):
            if not frutas[i].existe:
                del frutas[i]


frutas = [Fruta("banana", "amarela", 1), Fruta("uva", "roxa", 1), Fruta("laranja", "amarela", 1),\
          Fruta ("uva", "verde", 1), Fruta("tangerina", "laranja", 2)]
frutas[0].nome = 'Banana'
animais = [Animal("macaco", 5, "amarela"), Animal("xiwahwah", 7, "uva"), Animal("leão", 8, "tangerina")]
zoo = Zoologico()
zoo.alimentar(frutas, animais)
animais[1].esperar()
zoo.alimentar(frutas, animais)

for fruta in frutas:
    print(fruta.nome, fruta.cor)
