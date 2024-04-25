from random import randint

def rollDice(times):
    rolls = []
    for i in range(times):
        rolls.append(randint(1, 6))
    return rolls

def getStats(rolls):
    stats = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(rolls)):
        if rolls[i] == 1:
            stats[1] += 1
        elif rolls[i] == 2:
            stats[2] += 1
        elif rolls[i] == 3:
            stats[3] += 1
        elif rolls[i] == 4:
            stats[4] += 1
        elif rolls[i] == 5:
            stats[5] += 1
        elif rolls[i] == 6:
            stats[6] += 1

    return stats

print("Welcome to my create task")
print("This app simulates rolling a dice")
while True:
    times = int(input("How many times will you roll the dice? "))
    rolls = rollDice(times)
    stats = getStats(rolls)
    print(f"Rolls: {rolls}")
    print(f"You rolled...")
    for i in range(1, 7):
        print(f"{i}: {stats[i]} times")
    mostRolled = 0
    for i in range(1, 7):
        if stats[i] > stats[mostRolled]:
            mostRolled = i
    print(f"{mostRolled} was rolled the most times")
    tied = []
    for i in range(1, 7):
        if i != mostRolled and stats[i] == stats[mostRolled]:
            tied.append(i)
    if len(tied) > 0:
        tied_strings = [str(tie) for tie in tied]
        print(f"{", ".join(tied_strings)} also tied")