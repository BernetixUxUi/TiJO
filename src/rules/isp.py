from abc import ABC, abstractmethod

class IWork(ABC):
    @abstractmethod
    def work(self):
        pass

class IEat(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(IWork, IEat):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class RobotWorker(IWork):
    def work(self):
        print("Robot working")

# Użycie
human = HumanWorker()
robot = RobotWorker()

human.work()
human.eat()
robot.work()