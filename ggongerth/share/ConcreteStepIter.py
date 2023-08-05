
class StepIterator:
    def __init__(self, Ppointer, Robot_id, lines,browser):
        self.Ppointer = Ppointer
        self.Robot_id = Robot_id
        self.lines = lines
        self.index = -1
        self.browser = browser
        self.prev_i = None

    def __iter__(self):
        return self

    def __next__(self):
        from init import fRobMove
        if self.index + 1 < len(self.lines):
            self.index += 1
            if self.prev_i is not None:
                self.lines[self.prev_i] = self.lines[self.prev_i].replace(" <", "")
                fRobMove._StepBrowserParsing(self.browser, self.prev_i, self.lines[self.prev_i])
            self.lines[self.index] = self.lines[self.index] + " <"
            fRobMove._StepBrowserParsing(self.browser, self.index, self.lines[self.index])
            self.prev_i = self.index
            return self.lines[self.index]
        else:
            # return False
            raise StopIteration

    def Prev(self):
        from init import fRobMove
        if self.index - 1 >= 0:
            self.index -= 1
            if self.prev_i is not None:
                self.lines[self.prev_i] = self.lines[self.prev_i].replace(" <", "")
                fRobMove._StepBrowserParsing(self.browser, self.prev_i, self.lines[self.prev_i])
            self.lines[self.index] = self.lines[self.index] + " <"
            fRobMove._StepBrowserParsing(self.browser, self.index, self.lines[self.index])
            self.prev_i = self.index
            return self.lines[self.index]
        else:
            raise ValueError("Already at the first step")
    