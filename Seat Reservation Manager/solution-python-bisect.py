class SeatManager:
    def __init__(self, n):
        self.lista = [x for x in range(1, n + 1)]
        
    def reserve(self):
        return self.lista.pop(0)
        
    def unreserve(self, seatNumber):
        bisect.insort(self.lista, seatNumber)