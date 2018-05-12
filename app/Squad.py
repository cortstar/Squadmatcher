import math
import random

class SquadList:


    def __init__(self, users, size):

        self.squads = []

        num_squads = math.ceil(len(users)/size)
        squad_size = math.ceil(len(users)/num_squads)

        random.shuffle(users)
        for i in range(0, int(num_squads)):
            self.squads.append(users[i*squad_size:i*squad_size+squad_size])


    def toString(self):
        message = "{} squad(s): \n".format(len(self.squads))

        for i in range(0, len(self.squads)):
            message += "Squad {}: ".format(i+1)
            for player in self.squads[i]:
                message += "{}, ".format(player)
            message += "\n"

        return message


if __name__ == "__main__":

    test1 = ["cort"]
    test3 = ["cort", "troy", "ryane"]
    test4 = ["cort", "troy", "ryane", "nate"]
    test5 = ["cort", "troy", "ryane", "nate", "chris"]
    test6 = ["cort", "troy", "ryane", "nate", "chris", "kirra"]

    print(SquadList(test1, 4).toString())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(SquadList(test3, 4).toString())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(SquadList(test4, 4).toString())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(SquadList(test5, 4).toString())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(SquadList(test6, 4).toString())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

