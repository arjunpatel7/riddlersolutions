#AKP

import random
import numpy as np

def check_all_zero(ls):
    return all(x == 0 for x in ls)

def check_all_ones(ls):
    return all(x == 1 for x in ls)

class QuarterGame:
    def __init__(self):
        #ones represent heads, zeros represent tails
        self.TL = 0
        self.TR = 0
        self.BL = 0
        self.BR = 0
    def random_init(self):
        #create a game, with some state that doesn't have all ones
        ls = [0,0,0,0]
        ls = [random.randint(0,1) for x in ls]
        while (check_all_ones(ls)):
            ls = [random.randint(0,1) for x in ls]
        self.TL = ls[0]
        self.TR = ls[1]
        self.BL = ls[2]
        self.BR = ls[3]

    def print_state(self):
        #testing function to see if everything under the hood is good
        tl = self.TL
        tr = self.TR
        bl = self.BL
        br = self.BR
        ls = [tl, tr, bl, br]
        print(ls)
    #each following flip function changes the state of the game
    def flip_TL(self):
        self.TL = not(self.TL)
        #self.print_state()

    def flip_TR(self):
        self.TR = not(self.TR)
        #self.print_state()

    def flip_BL(self):
        self.BL = not(self.BL)
        #self.print_state()

    def flip_BR(self):
        self.BR = not(self.BR)
        #self.print_state()

    def rotate_random(self):
        #rotates the board 0, 90, 80, 0r 270 degrees
        #uniformly picks one of the above
        mult90 = random.randint(1, 4) #choose from 1-4 multiples of 90 cw
        tl = self.TL
        tr = self.TR
        bl = self.BL
        br = self.BR
        if mult90 == 1:
            self.TL = bl
            self.TR = tl
            self.BR = tr
            self.BL = br
        elif mult90 == 2:
            self.TL = br
            self.TR = bl
            self.BR = tl
            self.BL = tr
        elif mult90 == 3:
            self.TL = tr
            self.TR = br
            self.BL = tl
            self.BR = bl
        else:
            pass
        return


    def win(self):
        #stop condition, when all heads
        tl = self.TL
        tr = self.TR
        bl = self.BL
        br = self.BR
        ls = [tl, tr, bl, br]
        return all(x == 1 for x in ls)

    def simGame(self):
        it = 0
        self.random_init()
        #strategy here
        #self.print_state()
        #simulate 500 moves, but stop if we win somewhere
        for x in range(500):
            if not(self.win()):
                self.flip_TL()
                self.rotate_random()
            else:
                it = x
                break
        if not(self.win()):
            #if we don't win by 500, it is reasonable to assume our strategy
            #doesn't work
            print("Failure to win in 500 steps")
        #self.print_state()
        return x


game = QuarterGame()
game.print_state()
ls = []
for x in range(10000):
    ls.append(game.simGame())
    #print(ls)
print(np.mean(ls))
print(np.std(ls))
print(np.min(ls))
print(np.max(ls))

#looks like our strategy works, since none of the 10000 games failed!
