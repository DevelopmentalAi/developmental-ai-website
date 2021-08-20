import csv

csv_name = "Review Paper Import Portal Responses - Form Responses 1.csv"


authors = {}
with open(csv_name, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    cnt = 0
    
    for row in reader:
        for author in row[27].split(", "):
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1

leaderboard = []
for k, v in sorted(authors.items(), key=lambda item: item[1], reverse=True) :
    leaderboard.append("{}, {}\n".format(k, v))

with open("leaderboard.txt", "w+", encoding="utf-8") as f:
    f.writelines(leaderboard)
