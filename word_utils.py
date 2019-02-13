import pandas as pd
import MeCab
import unicodedata
tagger = MeCab.Tagger()
tagger.parseToNode("")
def get_words(doc):
    tagger.parseToNode("")
    node = tagger.parseToNode(doc)
    words = []
    while node:
        w = node.surface
        h = node.feature.split(",")[0]    
        if w:
            words.append((w,h))
        node = node.next
    return words
def word_count_table(words):
    word_count_dict = {k:words.count(k) for k in set(words)}
    word_table = pd.DataFrame({
        'word':[k[0] for k in set(words)],
        'count':[word_count_dict[k] for k in set(words)],
        'hinsi':[k[1] for k in set(words)],
    })
    word_table = word_table.sort_values("count",ascending=False)
    return word_table
# strategy
def sentences2table(sentences):
    page_text = " ".join(sentences)
    words = get_words(page_text)
    word_table = word_count_table(words)
    return word_table
def tag2sentences(tag):
    sentence = unicodedata.normalize("NFKC", tag.text)
    return [sentence]
