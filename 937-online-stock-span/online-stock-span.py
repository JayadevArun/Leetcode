class StockSpanner:

    def __init__(self):
        self.st=[]#(price,count)

    def next(self, price: int) -> int:
        c=1
        while self.st and self.st[-1][0]<=price:
            e=self.st.pop()
            c+=e[1]
        self.st.append((price,c))
        return c

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)