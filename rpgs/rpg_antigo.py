import math
import random

escolha = input("""Escolha:
 1.Ataque
 2.Defesa\n""")


if escolha == "1":

    res = None

    rf = int(input("Resistencia Física do Oponente: "))

    ar = int(input("Armadura do Oponente: "))

    vida = int(input("Vida do Oponente: "))

    while vida > 0:

    d20 = int(input("Dado de Defesa do Oponente: "))

    atkr = input("""Qual Ataque?
Zebba:
(1) Bastão de Mei Houwang: 220 // (2) Crit {550}
(3) Bastão de Mei Houwang+ Dano de Vento: Normal {240} // (4) Crit {600}
(5) Clone: 55 de Dano
.
Alisson: 
(6) Marreta do Zoio: Normal {60} // (7) Crit {150}
(8) Marreta do Zoio contra Armor: Normal {180} // (9) Crit {360}
.
Trousle:
(10) Enma e Shusui: Normal {220} // (11) Crit {550}
(12) Enma ou Shusui estopada: Normal {240} // (13) Crit {600}
(14) Enma ou Shusui estopada com queimadura: Normal {310} // (15) Crit {780}
(16) Enma e Shusui estopadas com queimadura Normal {340} // (17) Crit {850}
(18) Sinalizador: Normal {155} // (19) Crit {390}
(20) Sinalizador Queimando: {200} // (21) Crit {500}
.
Visconti:
(22) Shadow Daggers: Normal {160} // (23) Crit {480}
.
Tales:
(24) Vara do Raul: Normal {70} // (25) Crit {175}
(26) Vara do Raul com Buff: Normal {85} // (27) Crit {215}
.
Scyther:
(28) Ataque Base: Normal {30 T.D} // (29) Crit {75 T.D}
(30) Ataque Base SM: Normal {35 T.D} // (31) Crit {90 T.D}
(32) Dona Morte: Normal {85 T.D} // (33) Crit {210 T.D}
(34) Dona Morte SM: Normal {100 T.D } // (35) Crit {250 T.D}
(36) Julgamento: Normal {50 T.D} // (37) Crit {125 T.D}
(38) Julgamento SM: Normal {60 T.D} // (39) Crit {150 T.D}

Trix:
(40) Flecha Carregada: Normal {75} // (41) Crit {190}
(42) Flecha Carregada SM: Normal {90} // (43) Crit {225}
(44) Flecha Envenenada: Normal {75} // (45) Crit {190}
(46) Flecha Envenenada SM: Normal {90 T.D} // (47) Crit {225 T.D}
(48) Flecha Flamejante: Normal {75} // (49) Crit {190}
(50) Flecha Flamejante SM: Normal {90} // (51) Crit {225}

Tiny:
(52) Esmaga: Normal {85} // (53) Crit {210}
(54) Esmaga SM: Normal {100} // (55) Crit {250}
(56) Força Demoniaca: Normal {95 T.D} // (57) Crit {240 T.D}
(58) Força Demoniaca SM: Normal {115 T.D} // (59) Crit {290 T.D}\n""")

    if atkr == "1":

        res = 180 - rf - ar - d20
        td = 0

    elif atkr == "2":

        res = 700 - rf - ar - d20
        td = 0

    elif atkr == "3":

        res = 300 - rf - ar - d20
        td = 0

    elif atkr == "4":

        res = 750 - rf - ar - d20
        td = 0

    elif atkr == "5":

        res = 0
        td = 55

    elif atkr == "6":

        res = 60 - rf - ar - d20
        td = 0

    elif atkr == "7":

        res = 150 - rf - ar - d20
        td = 0

    elif atkr == "8":

        res = 180 - ar
        td = 0

    elif atkr == "9":

        res = 360 - ar
        td = 0

    elif atkr == "10":

        res = 220 - 2 * rf - ar - d20
        td = 0

    elif atkr == "11":

        res = 550 - 2 * rf - ar - d20
        td = 0

    elif atkr == "12":

        res = 240 - 2 * rf - ar - d20
        td = 0

    elif atkr == "13":

        res = 600 - 2 * rf - ar - d20
        td = 0

    elif atkr == "14":

        res = 310 - 2 * rf - ar - d20 - 15
        td = 0

    elif atkr == "15":

        res = 780 - 2 * rf - ar - d20 - 15
        td = 0

    elif atkr == "16":

        res = 340 - 2 * rf - ar - d20 - 15
        td = 0

    elif atkr == "17":

        res = 850 - 2 * rf - ar - d20 - 15
        td = 0

    elif atkr == "18":

        res = 155 - ar - d20
        td = 0

    elif atkr == "19":

        res = 390 - rf - ar - d20
        td = 0

    elif atkr == "20":

        res = 200 - ar - d20 - 15
        td = 0

    elif atkr == "21":

        res = 500 - rf - ar - d20 - 15
        td = 0

    elif atkr == "22":

        res = 160 - 2 * rf - ar - d20 - 20
        td = 0

    elif atkr == "23":

        res = 480 - 2 * rf - ar - d20 - 20
        td = 0

    elif atkr == "24":

        res = 70 - rf - ar - d20
        td = 0

    elif atkr == "25":

        res = 175 - rf - ar - d20
        td = 0

    elif atkr == "26":

        res = 85 - rf - ar - d20
        td = 0

    elif atkr == "27":

        res = 215 - rf - ar - d20
        td = 0

    elif atkr == "28":

        res = 0
        td = 30

    elif atkr == "29":

        res = 0
        td = 75

    elif atkr == "30":

        res = 0
        td = 35

    elif atkr == "31":

        res = 0
        td = 90

    elif atkr == "32":

        res = 0
        td = 85

    elif atkr == "33":

        res = 0
        td = 210

    elif atkr == "34":

        res = 0
        td = 100

    elif atkr == "35":

        res = 0
        td = 250

    elif atkr == "36":

        res = 0
        td = 50

    elif atkr == "37":

        res = 0
        td = 125

    elif atkr == "38":

        res = 0
        td = 60

    elif atkr == "39":

        res = 0
        td = 150

    elif atkr == "40":

        res = 75 - ar - d20
        td = 0

    elif atkr == "41":

        res = 190 - rf - ar - d20
        td = 0

    elif atkr == "42":

        res = 90 - ar - d20
        td = 0

    elif atkr == "43":

        res = 225 - rf - ar - d20
        td = 0

    elif atkr == "44":

        res = 0
        td = 75

    elif atkr == "45":

        res = 0
        td = 190

    elif atkr == "46":

        res = 0
        td = 90

    elif atkr == "47":

        res = 0
        td = 225

    elif atkr == "48":

        res = 75 - ar - d20
        td = 0

    elif atkr == "49":

        res = 190 - rf - ar - d20
        td = 0

    elif atkr == "50":

        res = 90 - ar - d20
        td = 0

    elif atkr == "51":

        res = 225 - rf - ar - d20
        td = 0

    elif atkr == "52":

        res = 85 - ar - d20
        td = 0

    elif atkr == "53":

        res = 210 - ar - d20
        td = 0

    elif atkr == "54":

        res = 100 - ar - d20
        td = 0

    elif atkr == "55":

        res = 250 - ar - d20
        td = 0

    elif atkr == "56":

        res = 0
        td = 95

    elif atkr == "57":

        res = 0
        td = 240

    elif atkr == "58":

        res = 0
        td = 115

    elif atkr == "59":

        res = 0
        td = 290

    if td >= 1:

        armor = ar

        vida1 = vida - td

        dano = td

        print("O dano causado foi: " + str(dano))

        print("PdA restante: " + str(armor))

        print("PdV restante: " + str(vida1))

    else:

        dano = res

        if dano <= 0:
            dano = 0

        print("O dano causado foi: " + str(dano))

        armor = res

        if armor <= 0:
            armor = armor * (-1)

        elif armor >= 0:
            armor = 0

        print("PdA restante: " + str(armor))

        if res <= 0:
            res = 0

        vida1 = vida - res

        print("PdV restante: " + str(vida1))

elif escolha == "2":

    res2 = None

    escolha2 = input("""Escolha:
     1. Desviar
     2. Tankar\n""")

    if escolha2 == "1":

        dano_oponente = int(input("Dano do Oponente: "))

        defensor = input("Quem está defendendo? ")

        vida_defensor = int(input("Vida de {}: ".format(defensor)))

        resistencia_defensor = int(input("Resitência Física de {}: ".format(defensor)))

        armadura_defensor = int(input("Armadura do {}: ".format(defensor)))

        res2 = dano_oponente - resistencia_defensor - armadura_defensor # x = 100 - 45 - 200

        dano = res2

        if dano <= 0:
            dano = 0

        print("O dano causado em {0} foi {1}.".format(defensor,dano))

        vida_sobrando = vida_defensor - dano

        print("A vida de {0} é de {1} PdV.".format(defensor,vida_sobrando))

        armor = res2

        if armor <= 0:
            armor = armor * (-1)

        elif armor >= 0:
            armor = 0

        print("PdA restante: " + str(armor))


    elif escolha2 == "2":

        dano_oponente = int(input("Dano do Oponente: "))

        defensor = input("Quem está defendendo? ")

        vida_defensor = int(input("Vida de {}: ".format(defensor)))

        resistencia_defensor = int(input("Resitência Física do {}: ".format(defensor)))

        armadura_defensor = int(input("Armadura do {}: ".format(defensor)))

        d20 = int(input("Dado de Defesa: "))

        res2 = dano_oponente - resistencia_defensor - armadura_defensor - d20

        dano = res2

        if dano <= 0:
            dano = 0

        print("O dano causado em {0} foi {1}.".format(defensor, dano))

        vida_sobrando = vida_defensor - dano

        print("A vida de {0} é de {1} PdV.".format(defensor, vida_sobrando))

        armor = res2

        if armor <= 0:
            armor = armor * (-1)

        elif armor >= 0:
            armor = 0

        print("PdA restante: " + str(armor))