def sentences2table(sentences):
    page_text = " ".join(sentences)
    words = get_words(page_text)
    word_table = word_count_table(words)
    return word_table
