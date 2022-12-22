# import argparse
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
        open(out_file, 'w').close()
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



def total():
        year = sys.argv[3]
        with open(filename, 'r') as file:
            file.readline()
            line = file.readline()
            data = []

            while line != "":
                line_split = line.split("\t")
                data.append(line_split)
                line = file.readline()

            sorted_data = []

            for line in data:
                current_year = line[9]
                medal = line[14]
                if current_year == year and medal != "NA\n":
                    sorted_data.append(line)

            for line in sorted_data:
                if '-' in line[6]:
                    line[6] = line[6].split('-')[0]

            country_dictionary = {}  #  dictionary
            for line in sorted_data:
                current_country = line[6]
                medal = line[14]

                if current_country not in country_dictionary.keys():
                    country_dictionary[current_country] = [0, 0, 0]
                else:
                    if medal == "Bronze\n":
                        country_dictionary[current_country][0] += 1
                    elif medal == "Silver\n":
                        country_dictionary[current_country][1] += 1
                    elif medal == "Gold\n":
                        country_dictionary[current_country][2] += 1

            for key, x in country_dictionary.items():  # going through dictionary, returning keys and values
                print(f"{key} has won {x[0]} Bronze, {x[1]} Silver, {x[2]} Gold medals")

        # for line in lines:
        #     participant = Participant(*line.strip().split("\t"))
        #     if (participant.team == country or participant.noc == country) and participant.year == year and participant.medal != "NA":
        #         country_list.append(participant)
        #     elif country not in country_list
# def total():
#     year = sys.argv[3]
#     for line in lines:
#         line = line.split("\t")
#         if year == line[9]:
#             print(line)
###################################################
def overall():
    leaders = {}
    filename = sys.argv[1]
    countries = sys.argv[3:]
    for country in countries:
        with open(filename, 'r') as file:
            line = file.readline()
            line = file.readline()
            while line != "":
                line_split = line.split("\t")
                country_line = line_split[6]
                medal_line = line_split[-1][:-1]
                year_line = line_split[9]
                if country_line == country and year_line not in leaders:
                    leaders[year_line] = 0
                elif country_line == country and medal_line != "NA" and year_line in leaders:
                    leaders[year_line] += 1
                line = file.readline()
        keys_leaders = [int(key) for key in leaders.keys()]
        x_leaders = [int(key) for key in leaders.values()]
        max_leaders = max(x_leaders)
        print(f'{country}, {max_leaders}, {keys_leaders[x_leaders.index(max_leaders)]}')
        leaders.clear()

############################################################


##############################################################
def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("filename")
    # parser.add_argument("-medals", nargs="*", required=False)
    # parser.add_argument("-total", action="store_true", required=False)
    #
    # args = parser.parse_args()
    # country_and_year_list = args.medals
    # filename = args.filename
####################
    # data_file = sys.argv[1]
    # # country = sys.argv[3]
    # year = sys.argv[3]
    #
    # if len(sys.argv) > 5:
    #     out_file = sys.argv[6]
    # else:
    #     out_file = None
#######################
    # year = int(country_and_year_list[1])
    # output = country_and_year_list[6]
    # medals(filename, country, year, out_file)
    total()
    overall()
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
