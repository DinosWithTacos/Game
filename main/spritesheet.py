class spritesheet:
    def __init__(self, surface, cols, rows):
        self.sheet = surface

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (int(w / 2), int(h / 2))

        self.cells = list([(index % cols * w, int(index / cols) * h, w, h)
                           for index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h), ])

    def draw(self, surface, cellIndex, x, y, speed, i=0, handle=0):

        # i += 1
        if (i % speed) == 0:
            surface.blit(
                self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
        print(i)
