class SeatManager:

    def __init__(self, n: int):
        self.lista = [x for x in range(1, n + 1)]
        

    def reserve(self) -> int:
        return heapq.heappop(self.lista)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.lista, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)