from youtube_search import YoutubeSearch
import json

title = []

#take keywords as param, fetch from youtube and filter out videos above 50k
def add_title(keywords):
  results = YoutubeSearch(keywords).to_dict()

  for result in results:
    view = int(result['views'][:-5].replace(",",""))
    if (view >= 50000):
      title.append(result['title'])

#replace the input with the search query you wanted
add_title("THE SEARCH QUERY YOU WANTED")

#use NLP to count and filter data (for mandarin results)
from collections import Counter
import jieba

all_titles = " ".join(title)
seg_list = jieba.cut(all_titles, cut_all=False)
word_list = list(seg_list)

# Remove common stop words & find word freq
stop_words = ['的', '了', '在', '是', '我', '你', '他', '她', '它', '們', '我們', '你們', '他們', '和', '與', '跟', '或', '及', '之', '不', '沒有', '有', '個', '個', '一', '一個', '這', '那', '那些', '這個', '那個', '這些', '都', '很', '非常', '更', '最', '上', '下', '左', '右', '前', '後', '內', '外', '裡', '裏', '中', '大', '小', '多', '少', '來', '去', '出', '進', '高', '低', '遠', '近', '長', '短', '新', '舊', '好', '壞', '對', '錯', '是', '不是', '要', '不要', '能', '不能', '會', '不會', '可以', '不可以', '用', '使用', '讓', '被', '把', '將', '與', '及', '而', '但', '可是', '然而', '因為', '由於', '所以', '因此', '如果', '假如', '雖然', '即使', '以便', '以免', '於是', '接著', '然後', '此外', '另外', '例如', '比如', '就是', '只是', '只有', '只要', '除非', '否則', '不如', '不論', '不管', '儘管', '關於', '對於', '至於', '除了', '除非', '以便', '以免', '為了', '為了', '透過', '根據', '按照', '隨著', '以來', '以來', '當', '從', '自從', '直到', '等到', '無論', '不管', '即使', '既然', '以便', '以免', '於是', '因此', '所以', '由於', '因為', '而', '但', '可是', '然而', '如果', '只要', '只有', '除非', '否則', '不如', '不論', '不管', '儘管', '關於', '對於', '至於', '除了', '除非', '以便', '以免', '為了', '為了', '透過', '根據', '按照', '隨著', '以來', '以來', '當', '從', '自從', '直到', '等到', '無論', '不管', '即使', '既然', '以便', '以免', '於是', '因此', '所以', '由於', '因為', '的', '一', '在', '不', '是', '了', '有', '和', '人', '為', '上', '個', '中', '大', '來', '以', '要', '與', '能', '對於', '會', '我們', '無', '我', '他', '新', '知', '無', '沒有', '個', '很', '也']
filtered_words = [word for word in word_list if word not in stop_words and len(word) > 1]

word_counts = Counter(filtered_words)
most_common_keywords = word_counts.most_common(50)

#output
print("Most common keywords in out of " + str(len(title))+" titles:")
for keyword, count in most_common_keywords:
    print(f"{keyword}: {count}")
