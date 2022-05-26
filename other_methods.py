class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's multiply")
        return self.num * num2.num

    def __str__(self):
        print(f"Decimal number: {self.num}")

    def __len__(self):
        return 1


# n1 = Number(5)
# n2 = Number(6)
# sum = n1 + n2
# print(sum)
# mul = n1 * n2
# print(mul)
n = Number(5)
print(len(n))
# print(len(n))