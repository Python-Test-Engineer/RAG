## Process files

- get_and_store_file(filename) - get file from folder and store in db with any metadata.
- split_and_store(filename) - run through unstructured.io and store in DB. Contains tabular and iamge data.
- embed_and_store(doc) - create embedding for each chunk.
- ner(doc) - create NER for each chunk.
- process_image(doc) - run image through an LLM for more information.
- process_table(doc) - run table through an LLM for more information.
- summarise(doc) - if doc greater than a cetain length, summarise it and store in DB.

## Run Query

- rewrite_query(query, num_results) - rewrite query to get a set of similar questions
- semantic_search(query, num_results) - run semantic search and return num_results
- fts_search(keyword, num_results) - run Full Text Search and return num_results
- rerank_results(query, results, top_n) - for both semantic and keyword search rerank results
- combined_search(semantic_results, keyword_results) - combine semantic and keyword search results
- rag_pipeline(query, strategy) - run selected RAG strategy.

## Reporting

Based on user form selection, produce selected typt of final result for user.

## Feedback

For each response, user rates response which is stored in DB along with the initial query.