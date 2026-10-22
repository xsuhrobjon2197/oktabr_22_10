#16-misol
class Result:
    def __init__(self, ok, message):
        self.ok = ok
        self.message = message

class Wallet:
    def __init__(self, balance):
        self._balance = balance

    def pay(self, amount):
        if amount <= 0:
            return Result(False, "amount 0 dan katta bo'lsin")
        if amount > self._balance:
            return Result(False, "pul yetarli emas")
        self._balance -= amount
        return Result(True, "to'lov muvaffaqiyatli")

w = Wallet(50)
res = w.pay(100)
print(res.ok, res.message)  
