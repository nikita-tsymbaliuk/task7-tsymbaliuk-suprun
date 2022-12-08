import sys

file_with_data = sys.argv[1]
country = sys.argv[3]
year = sys.argv[4]

# print(sys.argv[1:])

print("country is", country, "year is", year)


year_set = set()
with open(file_with_data, 'r') as file:
    line = file.readline()
    line = file.readline()
    while line != "":
        line_splitted = line.split("\t")
        year = int(line_splitted[9])
        year_set.add(year)
        line = file.readline()

year_list = sorted(year_set)
for i,y in enumerate(year_list[:10], 1):
    print(i, "\t", y)

# set cortage
#     current_country = [6]
# print(current_country)

