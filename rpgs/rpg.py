class Personagem:
    def __init__(self, lvl, s, p, e, c, i, a, u):
        self.lvl = lvl
        self.s = s
        self.p = p
        self.e = e
        self.c = c
        self.i = i
        self.a = a
        self.u = u
        self.vida = 70 + (e * 5) + (lvl - 1) * (e / 2 + 1.5)
        self.mana = 50 + (10 * a)
        self.Guns = 2 + (2 * a) + (u / 2)
        self.Explosives = 2 + (2 * p) + (u / 2)
        self.Melee_Wp = 2 + (2 * s) + (u / 2)
        self.Barter = 2 + (2 * a) + (u / 2)
        self.Speech = 2 + (2 * a) + (u / 2)
        self.Repair = 2 + (2 * i) + (u / 2)
        self.Lockpick = 2 + (2 * p) + (u / 2)
        self.Science = 2 + (2 * i) + (u / 2)
        self.Sneak = 2 + (2 * a) + (u / 2)
        self.Medicine = 2 + (2 * i) + (u / 2)
        self.Peso = 70 + (10 * s)
        self.SR = 10 + (i * 0.5)
        self.CC = (u * 10) / 3


    def __repr__(self):
        return f'''
Vida: {self.vida}
Mana: {self.mana}
S: {self.s}
P: {self.p}
E: {self.e}
C: {self.c}
I: {self.i}
A: {self.a}
L: {self.u}
Guns: {self.Guns}
Explosives: {self.Explosives}
Melee: {self.Melee_Wp}
Barter: {self.Barter}
Speech: {self. Speech}
Repair: {self.Repair}
Lockpick: {self.Lockpick}
Science: {self.Science}
Sneak: {self.Sneak}
Medicine: {self.Medicine}

PESO: {self.Peso} Kg
Skill Rate: {self.SR} pontos por nível
Critical Chance: {self.CC} %
'''

ligma = Personagem(1,0,5,5,5,10,8,7)
le_mignon = Personagem(1,7,4,6,8,5,6,4)
tocka = Personagem(1,9,8,8,2,4,9,0)
zuck = Personagem(1,4,9,4,4,8,8,4)

print(zuck)

