import bs4
from pprint import pprint
import json

with open("student_pager.html", "r", encoding="utf-8") as fp:
    soup = bs4.BeautifulSoup(fp.read())

# print(json.dumps(sorted([
#     {
#         "name": li.find("h4").text,
#         "image": "web/img_%s.jpg" % li.find("div", class_="students")['id'],
#         "desc": li.find("p", class_="desc").text,
#         "post": li.find("p", class_="from").text,
#     }
#     for li in soup.findAll("li", class_="slide")
# ], key=lambda d: d['image']), indent=4))

with open("team_pager.html", "r", encoding="utf-8") as fp:
    soup = bs4.BeautifulSoup(fp.read())

print(json.dumps(sorted([
    {
        "name": li.find("h4").text,
        "image": "web/img_%s.jpg" % li.find("div", class_="students")['id'],
        "desc": li.find("p", class_="desc").text,
    }
    for li in soup.findAll("li", class_="slide")
], key=lambda d: d['image']), indent=4))
