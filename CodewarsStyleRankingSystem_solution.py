# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User():
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.rank_list = [i for i in range(-8,9) if i != 0]
    
    def rank_conv(self,rank):
        if rank in range(-8,0):
            return rank + 17
        elif rank in range(1,9):
            return rank + 16
        elif rank in range(9,17):
            return rank - 17
        elif rank in range(17,25):
            return rank -16
        else:
            return None
    
    def inc_progress(self,task_rank):
        if task_rank < -8 or task_rank > 8 or task_rank == 0:
            raise Exception('Invalid task rank value')
            pass
        elif self.rank < 8:    
            if self.rank_conv(task_rank) - self.rank_conv(self.rank) <= -2:
                pass
            elif self.rank_conv(task_rank) - self.rank_conv(self.rank) == -1:
                self.progress += 1
            elif task_rank - self.rank  == 0:
                self.progress += 3
            else:
                self.progress += 10*(self.rank_conv(task_rank) - self.rank_conv(self.rank))**2
            
            pot_upgrd = 24 - self.rank_conv(self.rank)
            print(self.progress)
            if self.progress >= 100:
                inc = self.progress // 100
                if inc > pot_upgrd:
                    self.rank = 8
                    
                else:
                    self.rank = self.rank_conv(self.rank_conv(self.rank) + inc)
                    self.progress = self.progress % 100
            if self.rank == 8:
                self.progress = 0