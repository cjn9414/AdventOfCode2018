class Cart:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.choice = 0
        self.dir = dir
        self.crashed = False
        self.rot = ['<', '^', '>', 'v']
        if self.dir == '^' or self.dir == 'v':
            self.over = '|'
        else:
            self.over = '-'

    def update(self, tracks):
        next_track = self.get_next(tracks)
        tracks[self.y] = tracks[self.y][:self.x] + self.over + tracks[self.y][self.x+1:]
        if self.dir == '^':
            self.y -= 1
        elif self.dir == 'v':
            self.y += 1
        elif self.dir == '>':
            self.x += 1
        else:
            self.x -= 1

        if next_track == '\\':
            if self.dir == '^':
                self.dir = '<'
            elif self.dir == '>':
                self.dir = 'v'
            elif self.dir == '<':
                self.dir = '^'
            else:
                self.dir = '>'

        elif next_track == '/':
            if self.dir == '^':
                self.dir = '>'
            elif self.dir == 'v':
                self.dir = '<'
            elif self.dir == '<':
                self.dir = 'v'
            else:
                self.dir = '^'

        elif next_track == '+':
            if self.choice % 3 == 0:
                self.change_dir(-1)
            elif self.choice % 3 == 1:
                self.change_dir(0)
            else:
                self.change_dir(1)
            self.choice += 1

        self.over = tracks[self.y][self.x]
        tracks[self.y] = tracks[self.y][:self.x] + self.dir + tracks[self.y][self.x+1:]

    def had_collision(self):
        if self.over in '<>^v':
            return True

    def change_dir(self, direction):
        # simply get next element in the circular array rot
        # depends on initial direction
        self.dir = self.rot[(self.rot.index(self.dir)+direction) % len(self.rot)]

    def get_next(self, tracks):
        if self.dir == '^':
            return tracks[self.y-1][self.x]
        elif self.dir == 'v':
            return tracks[self.y+1][self.x]
        elif self.dir == '>':
            return tracks[self.y][self.x+1]
        else:
            return tracks[self.y][self.x-1]

    def fix_tracks(self, tracks):
        # remove cart from track
        tracks[self.y] = tracks[self.y][:self.x] + self.over + tracks[self.y][self.x+1:]
