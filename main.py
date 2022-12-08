import sys

file_with_data = sys.argv[1]
print(sys.argv[1:])

country = sys.argv[3]
year = sys.argv[4]
medals = sys.argv[2]
print("country is", country, "year is", year, "medals are", medals)



# with open("Olympic Athletes - athlete_events.tsv", "r") as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

