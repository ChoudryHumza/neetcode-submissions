class BrowserHistory:

    def __init__(self, homepage: str):
        self.forwardh = []
        self.backh = [homepage]

    def visit(self, url: str) -> None:
        self.backh.append(url)
        self.forwardh.clear()

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.backh)-1)
        for i in range(steps):
            self.forwardh.append(self.backh.pop())
            steps -=1
        return self.backh[-1]
        

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.forwardh))

        for i in range(steps):
            self.backh.append(self.forwardh.pop())
        return self.backh[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)