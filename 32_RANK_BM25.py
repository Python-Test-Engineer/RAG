from rank_bm25 import BM25Okapi

corpus = [
    "Hello there good man in the windy rain who is from London and is looking for a job!",
    "It is quite windy in London",
    "How is the weather today?",
]

tokenized_corpus = [doc.split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)
query = " man windy job London"
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)
for i in range(len(doc_scores)):
    doc_scores[i] = round(doc_scores[i], 2)
    print(f"Document {i + 1}: {doc_scores[i]}")

print("====================")
bm25.get_top_n(tokenized_query, corpus, n=1)
print(f"{bm25.get_top_n(tokenized_query, corpus, n=1)}")
