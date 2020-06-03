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
                list_description.append(all_count)

    for words in list_description:
        counts = {words: list_description.count(words)}
        count_words.update(counts)

    list_count = list(count_words.items())
    list_count.sort(key=lambda i: i[1], reverse=True)
    all_list_count = list_count[:10]

    for i in all_list_count:
        print(i[0], ':', i[1])




