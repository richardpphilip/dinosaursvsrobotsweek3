class Weapon:
    def __init__(self, weapon_name,):
        self.weapon_name = weapon_name
        self.weapon_attack_power = ''
        if weapon_name == '1':
            weapon_name = 'sword'
            weapon_attack_power = 10
            pass
        elif weapon_name == '2':
            weapon_name = 'crossbow'
            weapon_attack_power = 2
