import sys

print(sys.argv[1:])

country = sys.argv[4]
print(country)

with open("Olympic Athletes - athlete_events.tsv", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)

