class Dinosaur:
    def __init__(self, dinosaur_type='mean'):
        self.dinosaur_type = dinosaur_type
        self.dinosaur_health = 100
        self.dinosaur_energy = 10
        self.dinosaur_attack_power = 5

    def dino_attack(self, robot, ):
        while robot.robot_health > 0:
            robot.robot_health -= self.dinosaur_attack_power
            print(robot.robot_health)

        else:
            print('the robot is dead')
