import functools

def join(doc_so_far, sentence):
    return f"{doc_so_far}. {sentence}"

def join_first_sentences(sentences, n):
    return "" if n == 0 else f"{functools.reduce(join, sentences[:n])}."

print(join_first_sentences(["hello world", "How are you", "I hope well", "anyways, bye"], 2))
