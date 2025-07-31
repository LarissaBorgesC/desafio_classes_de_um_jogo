class hero():
    def __init__(self, name, age, tipo):
        self.name = name
        self.age = age
        self.tipo = tipo        
               
    def atacar(self):

        if self.tipo == "mago":
            attack = "magia"

        elif self.tipo == "guerreiro":
            attack = "espada"

        elif self.tipo == "monge":
            attack = "artes maciais"

        elif self.tipo == "ninja":
            attack = "shuriken"

        else:
            attack = "Ataque desconhecido"
        
        print(f"O {self.tipo} atacou usando {attack}")

while True:
    tipo = input("Informe a classe que deseja jogar (Mago, Guerreiro, Monge ou Ninja): ").lower()

    if tipo in ["mago", "ninja", "guerreiro", "monge"]:
        heroi = hero("Larissa", 28, tipo)
        heroi.atacar()
        break
    else:
        print("Escolha uma classe válida")
        continue