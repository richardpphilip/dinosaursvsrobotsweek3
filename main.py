from fleet import Fleet
from herd import Herd

if __name__ == '__main__':
    class Battlefield:
        dinosaur_herd = Herd()
        robot_fleet = Fleet()
        i = 0

        def dinosaurs_win(self):
            while i <= len(robot_fleet.robot_fleet_list):
                dinosaur_herd.dinosaur_herd_list[0].dino_attack(robot_fleet.robot_fleet_list[0])
                if robot_fleet.robot_fleet_list[0].robot_health <= 0:
                    del robot_fleet.robot_fleet_list[0]
                    i += 1
            else:
                print('all robots are dead.  Dinosaurs win!')

        dinosaur_herd.dinosaurs_win()
