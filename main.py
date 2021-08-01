import requests
from bs4 import BeautifulSoup

URL = "https://olympics.com/tokyo-2020/olympic-games/en/results/swimming/entries-by-event-men-s-100m-breaststroke.htm"

#URL = "https://olympics.com/tokyo-2020/olympic-games/en/results/swimming/entries-by-event-men-s-100m-backstroke.htm"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
output1 = soup.find_all("tr", class_="Res1")
output2 = soup.find_all("tr", class_="Res2")

FINAL_OUTPUT = {}

for output in output1:
    time = output.find_all(
        "td", class_="text-center d-none d-md-table-cell")[2].text.strip()
    name = output.find("span", class_="d-none d-md-inline").text.strip()
    FINAL_OUTPUT[name] = time

for output in output2:
    time = output.find_all(
        "td", class_="text-center d-none d-md-table-cell")[2].text.strip()
    name = output.find("span", class_="d-none d-md-inline").text.strip()
    FINAL_OUTPUT[name] = time

#print(FINAL_OUTPUT)

final = dict(sorted(FINAL_OUTPUT.items(), key=lambda item: item[1]))
#print(final)

standing = 1
for tup in final.items():
    print(standing, tup[0], tup[1])
    standing += 1

# file = open("output1.txt", "w")
# file.write(output1.text)
# file.close()

# file = open("output2.txt", "w")
# file.write(output2.text)
# file.close()

# outputs = soup.find(id="top-ratios").find_all("li",
#                                               class_="flex flex-space-between")
# for output in outputs:
#     print(
#         output.find(class_="name").text.strip(),
#         output.find(class_="number").text.strip())
