from random import randint


class Generator:
    def randomNumRange(self, amount, minRange, maxRange):
        result = []

        for i in range(amount):
            result.append(randint(minRange, maxRange))

        
        return f"Amount retuerned: {amount}\nStarting range: {minRange}\nEndring range: {maxRange}\nResult: " + ', '.join(str(s) for s in result)


if (__name__ == '__main__'):
    gen = Generator()
    print(gen.randomNumRange(5, 10, 30))









