from dinosaur import Dinosaur
from fleet import Fleet


class Herd:
    dinosaur_one = Dinosaur('dinosaur 1')
    dinosaur_two = Dinosaur('dinosaur 2')
    dinosaur_three = Dinosaur('dinosaur 3')
    dinosaur_herd_list = [dinosaur_one, dinosaur_two, dinosaur_three]
    i = 0
    def dinosaurs_win(self):
        while i <= len(robot_fleet.robot_fleet_list):
            dinosaur_herd.dinosaur_herd_list[0].dino_attack(robot_fleet.robot_fleet_list[0])
            if robot_fleet.robot_fleet_list[0].robot_health <= 0:
                del robot_fleet.robot_fleet_list[0]
                i += 1
        else:
            print('all robots are dead.  Dinosaurs win!')

