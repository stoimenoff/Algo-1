class BirthdayRanges:
    
    def __init__(self, items):
        self.n = 65536
        self.size = 2*65536 - 1
        self.items = [float("inf")] * self.size
#        for i in range(len(items)):
#            self.items[self.n - 1 + items[i]] += 1
#        for i in range(self.size - 1, 0, -2):
#            self.items[(i-1) >> 1] = self.items[i] + self.items[i - 1]
  # adds people who are born on a specific day
    def add(self, day, numberOfPeople):
        index_in_tree = self.n - 1 + day
        self.items[index_in_tree] += numberOfPeople
        i = index_in_tree
        while i > 0:
            self.items[(i - 1) >> 1] += numberOfPeople
            i = (i-1) >> 1
        
  # removes people who are born on a specific day
    def remove(self, day, numberOfPeople):
        index_in_tree = self.n - 1 + day
        max_del = self.items[index_in_tree]
        self.items[index_in_tree] -= numberOfPeople
        if self.items[index_in_tree] < 0:
            self.items[index_in_tree] = 0
            numberOfPeople = max_del
        i = index_in_tree
        while i > 0:
            self.items[(i-1) >> 1] -= numberOfPeople
            i = (i-1) >> 1

  # returns the number of people born in a range
    def count(self, startDay, endDay):
        return self.born_before(endDay + 1) - self.born_before(startDay)
    
  # returns the number of people born in the range [0, day)
    def born_before(self, day):
        index = self.n - 1 + day
        num = 0
        while index != 0:
            if index % 2 == 0:
                num += self.items[index - 1]
            index = (index - 1) >> 1
        return num
        
def main():
    n_m = [int(num) for num in input().split()]
    n = n_m[0]
    m = n_m[1]
    initial = [int(num) for num in input().split()]
    bit = BirthdayRanges(initial)
    for i in range(m):
        cmd = [item for item in input().split()]
        if cmd[0] == "add":
            bit.add(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove":
            bit.remove(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "count":
            print(bit.count(int(cmd[1]), int(cmd[2])))
main()
