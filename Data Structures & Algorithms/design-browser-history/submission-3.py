class BrowserHistory:

    def __init__(self, homepage: str):
        self.fh = []
        self.bh = []
        self.bh.append(homepage)

    def visit(self, url: str) -> None:
        self.bh.append(url)
        self.fh.clear()

    def back(self, steps: int) -> str:
        if steps >= len(self.bh) - 1:
            for i in range(len(self.bh)-1):
                self.fh.append(self.bh.pop())
            return self.bh[-1]
        else:
            for i in range(steps):
                self.fh.append(self.bh.pop())
            return self.bh[-1]

    def forward(self, steps: int) -> str:
        if steps >= len(self.fh):
            for i in range(len(self.fh)):
                self.bh.append(self.fh.pop())
            return self.bh[-1]
        else:
            for i in range(steps):
                self.bh.append(self.fh.pop())
            return self.bh[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.bh(steps)
# param_3 = obj.fh(steps)