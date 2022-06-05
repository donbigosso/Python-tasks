class Hero:
    def __init__(self, name, damage, health, mana, magic_attack_strength, money, motto):
        self.name = name
        self.damage = damage
        self.health = health
        self.mana = mana
        self.money = money
        self.motto = motto
        self.magic_attack_strength = magic_attack_strength

    def introduce_yourself(self):
        print(
            f"My name is: {self.name}. My health is: {self.health}. My mana is: {self.mana}. I have {self.money} gold. {self.motto}.")

    def rest(self):
        if self.health < 100:
            self.health += 10
        if self.mana < 100:
            self.mana += 10

    def phy_attack(self, enemy):
        enemy.health -= self.damage
        print(f"{self.name} inflicted {self.damage} damage on {enemy.name}")

    def magic_attack(self, enemy):
        enemy.health -= self.magic_attack_strength
        self.mana -= self.magic_attack_strength
        print(f"{self.name} inflicted {self.magic_attack_strength} magic damage on {enemy.name}")


piszczalka = Hero("Diabeł Piszczałka", 5, 100, 100, 12, 1000, "Ja kudłaty, durnowaty reperuję stare graty!")
szkieletor = Hero("Szkieletor", 7, 100, 100, 10, 1200, "He-Man ty s...")
he_man = Hero("He-Man", 10, 100, 100, 5, 800, "Na potęgę posępnego czerepu mocy przybywaj!")

he_man.phy_attack(piszczalka)
piszczalka.introduce_yourself()
szkieletor.introduce_yourself()
piszczalka.magic_attack(he_man)
he_man.introduce_yourself()
piszczalka.introduce_yourself()
