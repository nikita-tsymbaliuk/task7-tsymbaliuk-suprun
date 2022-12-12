import sys

def leaders(filename, country, year):
    head = None
    is_first_line = True
    with open(filename, "r") as file:
        for line in file.readlines():
            data = line.strip().split("\t")
            if is_first_line:
                head = data
                is_first_line = False
                continue

            if country == data[head.index("country-data")] and year == data[head.index("years")]:
                pass

def main():
    args = sys.argv
    if args[1] == "-medals":
        filename = args[args.index("-filename") + 1]
        country = args[args.index("-country") + 1]
        year = args[args.index("-year") + 1]
        leaders(filename, country, year)
# def total():
#     year = sys.argv[3]
#     for line in lines:
#         line = line.split("\t")
#         if year == line[9]:
#             print(line)
# def medals():
#     country = sys.argv[3]

file_with_data = sys.argv[1]
year_set = set()
with open(file_with_data, 'r') as file:
    lines = file.readlines()
    line = file.readline()
    line = file.readline()
    while line != "":
        line_splitted = line.split("\t")
        year = int(line_splitted[9])
        year_set.add(year)
        line = file.readline()
mode = sys.argv[2]

# if mode == "-total":
#     total()
# else:
#     medals()

# country = sys.argv[3]
# year = sys.argv[4]
#
# # print(sys.argv[1:])
#
# print("country is", country, "year is", year)


# year_set = set()
# with open(file_with_data, 'r') as file:
#     line = file.readline()
#     line = file.readline()
#     while line != "":
#         line_splitted = line.split("\t")
#         year = int(line_splitted[9])
#         year_set.add(year)
#         line = file.readline()
#
# year_list = sorted(year_set)
# for i,y in enumerate(year_list[:10], 1):
#     print(i, "\t", y)

# set cortage
#     current_country = [6]
# print(current_country)

# print(f'{counter +1}. {name_athlete} - {sport_athlete} - {medal-line}').

if __name__ == "__main__":
    main()
