import argparse
import sys

from classes import Participant

filename = "data_file.tsv"


def task1(filename, country, year):
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


def medals(filename, country, year, out_file):
    gold_counter = 0
    silver_counter = 0
    bronze_counter = 0
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = lines[1:]
    for line in lines:
        line = line.split("\t")
        # print(line)
        if year == line[9] and country == line[7]:
            type_of_medal = line[14]
            if type_of_medal == 'Gold\n':
                gold_counter += 1
            elif type_of_medal == 'Silver\n':
                silver_counter += 1
            elif type_of_medal == 'Bronze\n':
                bronze_counter += 1
    print(gold_counter, silver_counter, bronze_counter)

    participant_list = []
    for line in lines:
        participant = Participant(*line.strip().split("\t"))
        if (participant.team == country or participant.noc == country) and participant.year == year and participant.medal != "NA":
            participant_list.append(participant)
            # for i, y in enumerate(participant_list[:10], 1):

    if out_file:
        ff = open(out_file, 'a')
    for x in participant_list[:10]:
        print(x.name, x.sport, x.medal)
        if out_file:
            ff.write(f'{x.name}, {x.sport}, {x.medal}\n')
    if out_file:
        ff.close()



# def data(filename, output):
#     counter = 0
#     type_of_medals = []
#     names = []
#
#     with open(filename, "r") as file:
#         file.readline()
#         lines = file.readlines()
#     for line in lines:
#         line = line.split("\t")
#         type_of_medal = line[14]
#         name = line[1]
#         sport = line[-3]
#         year = line[9]
#         country = line[7]
#
#         if country in line and year in line:
#             if counter < 10:
#                 if name not in names and type_of_medal != "NA":
#                     # if output is not None:
#                     #     with open(filename_out, "a") as output_file:
#                     #         output_file.write(f'{counter + 1}, {name}, {sport}, {type_of_medal}\n')
#                     counter += 1
#                     print(f'{counter}, {name}, {sport}, {type_of_medal}')
#
#                     names.append(name)
#             type_of_medals.append(type_of_medal)
#         lines = file.readlines()
#     if len(names) == 0:
#         print("There is no such a country")
#         quit()
#     if counter < 10:
#         print(f'in {year} {country} and there were {counter} medalists')
#     medals(year)
#
# data(filename, "out")




def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("filename")
    # parser.add_argument("-medals", nargs="*", required=False)
    # parser.add_argument("-total", action="store_true", required=False)
    #
    # args = parser.parse_args()
    # country_and_year_list = args.medals
    # filename = args.filename

    data_file = sys.argv[1]
    country = sys.argv[3]
    year = sys.argv[4]
    if len(sys.argv) > 5:
        out_file = sys.argv[6]
    else:
        out_file = None

    # year = int(country_and_year_list[1])
    # output = country_and_year_list[6]
    medals(filename, country, year, out_file)

    # data(filename, "out.txt")


    # year_set = set()
    # with open(filename, 'r') as file:
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


if __name__ == "__main__":
    main()
