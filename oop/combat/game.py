import sys

from characters import Character
from monsters import Goblin, Troll, Dragon


class Game:
    def __init__(self):
        self.player = Character()
        self.monsters = [Goblin(), Troll(), Dragon()]
        self.monster = self.get_next_monster()

        # game loop
        while self.player.hit_points and (self.monster or self.monsters):
            print('\n' + '=' * 20)
            print(self.player)
            self.monster_turn()
            print('-' * 20)
            self.player_turn()
            self.cleanup()
            print('\n' + '=' * 20)

        if self.player.hit_points:
            print("You win!")
        elif self.monster or self.monsters:
            print("You lose!")

        sys.exit()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))
            if self.player.dodge():
                print("You dodged the attack!")
            else:
                print("You got hit anyway!")
                self.player.hit_points -= 1
        else:
            print("{} isn't attacking this turn".format(self.monster))

    def player_turn(self):
        action = input("Action ([A]ttack, [R]est, [Q]uit): ").lower()

        if action == 'a':
            print("You're attacking {}!".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You hit {} with your {}!".format(self.monster, self.player.weapon))
            else:
                print("You missed!")
        elif action == 'r':
            self.player.rest()
        elif action == 'q':
            print("Quited")
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()


if __name__ == '__main__':
    Game()
