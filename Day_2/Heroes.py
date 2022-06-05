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
        print(f"My name is: {self.name}. {self.motto}")
    

piszczalka = Hero("Diabeł Piszczałka", 5, 100, 100, 12, 1000, "Ja kudłaty, durnowaty reperuję stare graty!")
szkieletor = Hero("Szkieletor", 7, 100, 100, 10, 1200, "He-Man ty s...")
he_man = Hero("He-Man", 10, 100, 100, 5, 800, "Na potęgę posępnego czerepu mocy przybywaj!")

he_man.introduce_yourself()
