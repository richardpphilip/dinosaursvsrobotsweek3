from fleet import Fleet
from herd import Herd

if __name__ == '__main__':
    dinosaur_herd = Herd()
    robot_fleet = Fleet()


    def dinosaurs_win(dinosaur, robot):
        i = 0
        while i <= 2:
            dinosaur.dino_attack(robot[0])
            if robot[0].robot_health <= 0:
                del robot[0]
                i += 1
        else:
            print('all robots are dead.  Dinosaurs win!')


    def robots_win(robot, dinosaur):
        j = 0
        while j <= 2:
            robot.robot_attack(dinosaur[0])
            if dinosaur[0].dinosaur_health <= 0:
                del dinosaur[0]
                j += 1
        else:
            print('all dinosaurs are dead.  Robots win!')


    prompt = input("Who do you want to win the game? dinosaurs or robots?")
    while prompt != 'dinosaurs' or 'robots':
        if prompt == 'dinosaurs':
            dinosaurs_win(dinosaur_herd.dinosaur_herd_list[0], robot_fleet.robot_fleet_list)
            break

        if prompt == 'robots':
            robots_win(robot_fleet.robot_fleet_list[0], dinosaur_herd.dinosaur_herd_list)
            break

        else:
            print('Sorry that is not an option.  Please choose dinosaurs or robots.')
            prompt = input("Who do you want to win the game? dinosaurs or robots?")