import json
from pprint import pprint

with open('newsafr.json') as f:
    afr = json.load(f)

    list_description = []
    count_words = {}

    for descript in afr['rss']['channel']['items']:
        descript = descript['description'].split()
        for all_count in descript:
            if len(all_count) > 6:
                list_description.append(all_count.lower())

    for words in list_description:
        counts = {words: list_description.count(words)}
        count_words.update(counts)

    list_count = list(count_words.items())
    list_count.sort(key=lambda i: i[1], reverse=True)
    all_list_count = list_count[:10]

    print("Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:")
    for i in all_list_count:
        print(i[0], ':', i[1])

import xml.etree.ElementTree as ET

from pprint import pprint

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
channel = root.find("channel")
items = channel.findall("item")
list_description = []
count_words = {}

for descr in items:
    descript = ((descr.find("description").text).split())
    for all_count in descript:
        if len(all_count) > 6:
            list_description.append(all_count.lower())

for word in list_description:
    counts = {word: list_description.count(word)}
    count_words.update(counts)

list_count = list(count_words.items())
list_count.sort(key=lambda i: i[1], reverse=True)
all_list_count = list_count[:10]

print("Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:")
for i in all_list_count:
    print(i[0], ':', i[1])


