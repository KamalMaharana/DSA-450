class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height) - 4
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        curr = self.pos
        if curr < self.w:
            return [curr, 0]
        curr -= (self.w - 1)
        if curr < self.h:
            return [self.w - 1, curr]
        curr -= (self.h - 1)
        if curr < self.w:
            return [self.w - 1 - curr, self.h - 1]
        curr -= (self.w - 1)
        return [0, self.h - 1 - curr]

    def getDir(self) -> str:
        # Initial state before any movement
        if not self.moved:
            return "East"
        
        # Check specific boundaries for direction
        # Note: (0,0) after movement is always "South" due to the loop
        if self.pos == 0:
            return "South"
        if 1 <= self.pos < self.w:
            return "East"
        if self.w <= self.pos < self.w + self.h - 1:
            return "North"
        if self.w + self.h - 1 <= self.pos < 2 * self.w + self.h - 2:
            return "West"
        return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()