from Heroes import Hero


class Piszczalka(Hero):
    def __init__(self, name, damage, health, mana, magic_attack_strength, money, pitchfork_attack_str, motto):
        super().__init__(name, damage, health, mana, magic_attack_strength, money, motto)
        self.pitchfork_attack_str = pitchfork_attack_str

    def pitchfork_attack(self, enemy):
        enemy.health -= self.pitchfork_attack_str
        print(f"{self.name} inflicted {self.pitchfork_attack_str} damage on {enemy.name} using his pitchfork")
