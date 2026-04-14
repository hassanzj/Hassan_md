import itertools


names = ["Ali", "Mustafa"]
years = ["1990"]
football = ["Messi"]
cars = ["Nissan"]
cats = ["Siri"]
sons = ["Ahmed"]


words = names + years + football + cars + cats + sons


symbols = ["@", "#", "$", "_"]
numbers = ["123", "321", "007", "99"]

passwords = set()


for i in range(2, 5):
    for combo in itertools.permutations(words, i):
        base = "".join(combo)

     
        for sym in symbols:
            for num in numbers:
                passwords.add(base)
                passwords.add(base + num)
                passwords.add(base + sym)
                passwords.add(base + sym + num)
                passwords.add(num + base)
                passwords.add(sym + base)


with open("passwords.txt", "w") as f:
    for p in passwords:
        f.write(p + "\n")

print(f"{len(passwords)} ")
