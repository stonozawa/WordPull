from word_utils import *
class page_analyser():
    def __init__(self, wd):
        self.title = wd.title
        self.all_tags = wd.find_elements_by_xpath("//*")
        self.tag_id_dict = {
            "page_text":["p"] + ["h%s" % i for i in range(1,10)],
            "midasi_text":["h%s" % i for i in range(1,10)]
        }
    def load_sentences(self, tag2sentences):
        tagname_sentences_dict = {}
        for i, target_tag_names in self.tag_id_dict.items():
            target_sentences = []
            for tag in self.all_tags:
                if tag.tag_name in target_tag_names:
                    target_sentences += tag2sentences(tag)
            tagname_sentences_dict[i] = target_sentences
        self.tagname_sentences_dict = tagname_sentences_dict
    def get_tables(self, sentences2table):
        page_tables = {k:None for k in self.tag_id_dict.keys()}
        for type_id, page_sentences in self.tagname_sentences_dict.items():
            word_table = sentences2table(page_sentences)
            page_tables[type_id] = word_table
        return page_tables
