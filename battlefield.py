from fleet import Fleet
from herd import Herd


class Battlefield:

    dinosaur_herd = Herd()
    robot_fleet = Fleet()

    i = 0
    j = 0

    def dinosaurs_win(self, dinosaur, robot):
        while i <= 2:
            dinosaur.dino_attack(robot)
            if robot.health <= 0:
                del robot
                i += 1
        else:
            print('all robots are dead.  Dinosaurs win!')
    #     while i <= 2:
    #         dinosaur_herd.dinosaur_herd_list[0].dino_attack(robot_fleet.robot_fleet_list[0])
    #         if robot_fleet.robot_fleet_list[0].robot_health <= 0:
    #             del robot_fleet.robot_fleet_list[0]
    #             i += 1
    #     else:
    #         print('all robots are dead.  Dinosaurs win!')
    #
    # def robots_win(self):
    #     while j <= 2:
    #         robot_fleet.robot_fleet_list[0].robot_attack(dinosaur_herd.dinosaur_herd_list[0])
    #         if dinosaur_herd.dinosaur_herd_list[0].dinosaur_health <= 0:
    #             del dinosaur_herd.dinosaur_herd_list[0]
    #             j += 1
    #     else:
    #         print('all dinosaurs are dead. Robots win!')
