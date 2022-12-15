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
def task():
    pass
def medals(filename, country, year):
    gold_counter = 0
    silver_counter = 0
    bronze_counter = 0
    with open(filename, "r") as file:
        file.readline()
        lines = file.readlines()
        for line in lines:
            line = line.split("\t")
            if year == int(line[9]) and country == line[7]:
                type_of_medal = line[14]
                if type_of_medal == 'Gold\n':
                    gold_counter += 1
                elif type_of_medal == 'Silver\n':
                    silver_counter += 1
                elif type_of_medal == 'Bronze\n':
                    bronze_counter += 1
        print(gold_counter, silver_counter, bronze_counter)

        participant_list = []
        with open(filename, "r") as file:
            file.readline()
            lines = file.readlines()
            for line in lines:
                participant = Participant(*line.strip().split("\t"))
                if (participant.team == country or participant.noc == country) and participant.year == year and participant.medal != "NA":
                    participant_list.append(participant)
                    print(participant_list)


def data(filename, output1):
    counter = 0
    type_of_medals = []
    names = []

    with open(filename, "r") as file:
        file.readline()
        lines = file.readlines()
        while lines:
            line = line.split("\t")
            type_of_medal = line[9]
            name = line[1]
            sport = line[-3]
            year = line[7]
            country = line[9]

            if country in line and year in line:
                if counter < 10:
                    if name not in names and type_of_medal != "NA":
                        if output1 is not None:
                            with open(filename, "a") as output_file:
                                output_file.write(f'{counter + 1}, {name}, {sport}, {type_of_medal}\n')
                        print(f'{counter + 1}, {name}, {sport}, {type_of_medal}')
                        counter += 1
                        names.append(name)
                type_of_medals.append(type_of_medal)
            lines = file.readlines()
        if len(names) == 0:
            print("There is no such a country")
            quit()
        if counter < 10:
            print(f'in {year} {country} and there were {counter} medalists')
    medals(year)

    data(filename, output1)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-medals", nargs="*", required=False)
    parser.add_argument("-total", action="store_true", required=False)

    args = parser.parse_args()
    country_and_year_list = args.medals
    filename = args.filename
    country = country_and_year_list[0]
    year = int(country_and_year_list[1])
    medals(filename, country, year)




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
