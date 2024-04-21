from random import randint

def rollDice(times):
    rolls = []
    for i in range(times):
        rolls.append(randint(1, 6))
    return rolls

def getStats(rolls):
    stats = {
        "ones": 0,
        "twos": 0,
        "threes": 0,
        "fours": 0,
        "fives": 0,
        "sixes": 0
    }

    for i in range(len(rolls)):
        if rolls[i] == 1:
            stats["ones"] += 1
        elif rolls[i] == 2:
            stats["twos"] += 1
        elif rolls[i] == 3:
            stats["threes"] += 1
        elif rolls[i] == 4:
            stats["fours"] += 1
        elif rolls[i] == 5:
            stats["fives"] += 1
        elif rolls[i] == 6:
            stats["sixes"] += 1

    return stats

print("Welcome to my create task")
print("This app simulates rolling a dice")
while True:
    times = int(input("How many times will you roll the dice? "))
    rolls = rollDice(times)
    stats = getStats(rolls)
    print(f"Rolls: {rolls}")
    print(f"Stats: {stats}")