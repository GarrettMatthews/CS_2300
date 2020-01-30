"""
This program is meant to prove exhaustively that when presented with three doors (one prize, two not prizes), and after
selecting one, a wrong one is opened, your odds of getting the prize double when you switch rather than stay with
your door
"""

import random
import csv

# TODO: Ensure that it is making all choices
# TODO: Add Final Choice Column
# TODO: Write to a CSV file

class MontyHall(object):
    """Class to run the Monty Hall problem and proof"""

    def __init__(self):
        self.door_lyst = [1,2,3]
        self.winner = 0
        self.wrong_door = []
        self.first_choice = 1
        self.opened_door = 0
        self.remaining_door = []
        self.door_dict = {}
        self.switch = 0
        self.monty_hall_run()


    def door_list_gen(self):
        """Function to create the door list, choose the winner, and create the list of wrong doors"""
        self.winner = random.choice(self.door_lyst)
        self.wrong_door = []
        for i in self.door_lyst:
            if i != self.winner:
                self.wrong_door.append(i)


    def open_wrong_door(self):
        """Function that opens a wrong door, ensuring it is not the door chosen"""
        if self.first_choice in self.wrong_door:
            lyst_copy = self.wrong_door.copy()
            lyst_copy.remove(self.first_choice)
            self.opened_door = lyst_copy[0]
        else:
            self.opened_door = random.choice(self.wrong_door)
        self.remaining_door = []
        for i in self.door_lyst:
            if i != self.opened_door:
                self.remaining_door.append(i)

    def monty_hall_run(self):
        """Function that runs the Monty Hall program"""
        with open("monty_hall.csv",mode='w') as mh:
            mh_writer = csv.writer(mh)
            mh_writer.writerow(["Correct Door","Wrong Doors","Initial Choice","Opened Door","Final Choice","Switched",
                                "Correct"])
            for i in range(100):
                self.door_list_gen()
                self.first_choice = 1
                if self.winner not in self.door_dict:
                    for j in range(3):
                        self.door_dict[self.winner] = self.wrong_door
                        winner = self.winner
                        wrong_doors = self.wrong_door
                        choice = self.first_choice
                        self.open_wrong_door()
                        open_door = self.opened_door
                        lyst_copy = self.remaining_door.copy()
                        lyst_copy.remove(self.first_choice)
                        self.switch = lyst_copy[0]
                        switched = self.switch
                        if switched == winner:
                            switch_correct = "Yes"
                            keep_correct = "No"
                        elif choice == winner:
                            switch_correct = "No"
                            keep_correct = "Yes"
                        mh_writer.writerow([winner,wrong_doors,choice,open_door, switched, "Yes",  switch_correct])
                        mh_writer.writerow([winner, wrong_doors, choice, open_door, choice, "No", keep_correct])
                        self.first_choice += 1

def main():
    MH = MontyHall()
    MH

if __name__ == "__main__":
    main()


