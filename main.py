import sys

file_with_data = sys.argv[1]
country = sys.argv[3]
year = sys.argv[4]

# print(sys.argv[1:])

print("country is", country, "year is", year)



with open(file_with_data, 'r') as file:
    line = file.readline()
    while line != "":
        line_splitted = line.split("\t")
        if country == line_splitted[7]:
            print(line_splitted)

        line = file.readline()


#     current_country = [6]
# print(current_country)

