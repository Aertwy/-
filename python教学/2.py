numbers=[2,2,2,2]
operators=["×","÷","×"]
opera1 = 0
while len(operators) !=0:
        if operators[opera1] == "×":
            result = numbers[opera1] * numbers[opera1 + 1]
        elif operators[opera1] == "÷":
            result = numbers[opera1] / numbers[opera1 + 1]
        numbers[opera1] = result
        numbers.pop(opera1+1)
        operators.pop(opera1)
