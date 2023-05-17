class Bomb:
    frame = 0

    def __init__(self, r, x, y, map, bomber):
        self.range = r
        self.pos_x = x
        self.pos_y = y
        self.time = 3200
        self.bomber = bomber
        self.sectors = []
        self.get_range(map)

    def update(self, dt):

        self.time = self.time - dt
        if self.time < 700:
            self.frame = 7
        elif self.time < 1200:
            self.frame = 6
        elif self.time < 1600:
            self.frame = 5
        elif self.time < 2000:
            self.frame = 4
        elif self.time < 2400:
            self.frame = 3
        elif self.time < 2800:
            self.frame = 2
        elif self.time < 3100:
            self.frame = 1
           

    def get_range(self, map):

        self.sectors.append([self.pos_x, self.pos_y])

        for x in range(1, self.range):
            if map[self.pos_x + x][self.pos_y] == 1:
                break
            elif map[self.pos_x + x][self.pos_y] == 0 or map[self.pos_x - x][self.pos_y] == 3:
                self.sectors.append([self.pos_x + x, self.pos_y])
            elif map[self.pos_x + x][self.pos_y] == 2:
                self.sectors.append([self.pos_x + x, self.pos_y])
                break
        for x in range(1, self.range):
            if map[self.pos_x - x][self.pos_y] == 1:
                break
            elif map[self.pos_x - x][self.pos_y] == 0 or map[self.pos_x - x][self.pos_y] == 3:
                self.sectors.append([self.pos_x - x, self.pos_y])
            elif map[self.pos_x - x][self.pos_y] == 2:
                self.sectors.append([self.pos_x - x, self.pos_y])
                break
        for x in range(1, self.range):
            if map[self.pos_x][self.pos_y + x] == 1:
                break
            elif map[self.pos_x][self.pos_y + x] == 0 or map[self.pos_x][self.pos_y + x] == 3:
                self.sectors.append([self.pos_x, self.pos_y + x])
            elif map[self.pos_x][self.pos_y + x] == 2:
                self.sectors.append([self.pos_x, self.pos_y + x])
                break
        for x in range(1, self.range):
            if map[self.pos_x][self.pos_y - x] == 1:
                break
            elif map[self.pos_x][self.pos_y - x] == 0 or map[self.pos_x][self.pos_y - x] == 3:
                self.sectors.append([self.pos_x, self.pos_y - x])
            elif map[self.pos_x][self.pos_y - x] == 2:
                self.sectors.append([self.pos_x, self.pos_y - x])
                break
