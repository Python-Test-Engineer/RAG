
CREATE TABLE docstore (
	key VARCHAR NOT NULL, 
	value JSONB, 
	CONSTRAINT docstore_pkey PRIMARY KEY (key)
)

/*
3 rows from docstore table:
key	value

*/


CREATE TABLE document_data (
	doc_id UUID NOT NULL, 
	content TEXT NOT NULL, 
	embeddings REAL[], 
	added TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
	CONSTRAINT document_data_pkey PRIMARY KEY (doc_id)
)

/*
3 rows from document_data table:
doc_id	content	embeddings	added
c3065f25-34bd-433d-b6d3-71e5f7603e42	Here is a lot of text that we will embed	[0.023209529, 0.023142641, 0.031168992, 0.016092831, -0.019182976, 0.026192656, 0.0064378013, -0.031	2024-11-18 22:52:55.264561
*/


CREATE TABLE embeddings_table (
	id SERIAL NOT NULL, 
	track VARCHAR(255), 
	embeddings REAL[], 
	CONSTRAINT embeddings_table_pkey PRIMARY KEY (id)
)

/*
3 rows from embeddings_table table:
id	track	embeddings
1	May 5, 2023	[0.023209529, 0.023142641, 0.031168992, 0.016092831, -0.019182976, 0.026192656, 0.0064378013, -0.031
2	To Whom it May Concern:	[0.055838846, -0.021927774, 0.013120603, 0.0861577, -0.005887628, -0.037947115, -0.046684936, 0.0382
3	There were 20,000 bottles of water, 10,000 blankets, and 200 laptops delivered on January 23, 2023. 	[-0.00045886813, -0.0068087936, -0.008185398, 0.0072811577, -0.0027363386, -0.06461943, 0.011896831,
*/


CREATE TABLE employees (
	name VARCHAR(255) NOT NULL, 
	state VARCHAR(255) NOT NULL, 
	salary INTEGER
)

/*
3 rows from employees table:
name	state	salary
Ted	NC	5000
Pete	AZ	10000
*/


CREATE TABLE langchain_pg_collection (
	name VARCHAR, 
	cmetadata JSON, 
	uuid UUID NOT NULL, 
	CONSTRAINT langchain_pg_collection_pkey PRIMARY KEY (uuid)
)

/*
3 rows from langchain_pg_collection table:
name	cmetadata	uuid
vectordb	None	fca18967-f8b7-4720-83df-2027acf3b256
*/


CREATE TABLE langchain_pg_embedding (
	collection_id UUID, 
	document VARCHAR, 
	cmetadata JSON, 
	custom_id VARCHAR, 
	uuid UUID NOT NULL, 
	CONSTRAINT langchain_pg_embedding_pkey PRIMARY KEY (uuid), 
	CONSTRAINT langchain_pg_embedding_collection_id_fkey FOREIGN KEY(collection_id) REFERENCES langchain_pg_collection (uuid) ON DELETE CASCADE
)

/*
3 rows from langchain_pg_embedding table:
collection_id	document	cmetadata	custom_id	uuid
fca18967-f8b7-4720-83df-2027acf3b256	In the heart of the old quarter of Palermo, amidst the bustling market stalls and the echoes of live	{'source': './founder.txt'}	4f463563-1bda-4599-aae9-438e2a971a32	5642eafc-275f-4be8-879a-eeeb03b3ba2e
fca18967-f8b7-4720-83df-2027acf3b256	warmth of his Nonna Lucia's kitchen, young Amico was captivated by the symphony of flavors and aroma	{'source': './founder.txt'}	ec32c420-eec4-4367-88ce-dfe7324858d1	04abbc4b-9705-4903-a78b-2cfbf9f25d77
fca18967-f8b7-4720-83df-2027acf3b256	Amico's life was deeply entwined with the vibrant essence of Sicilian cuisine. In the rustic kitchen	{'source': './founder.txt'}	5c74fff3-8b33-4f44-b728-a69b6d8fe362	36367e90-9df1-4ead-829b-4950805c6662
*/


CREATE TABLE products (
	id INTEGER NOT NULL, 
	product_name VARCHAR(50), 
	price NUMERIC, 
	CONSTRAINT products_pkey PRIMARY KEY (id)
)

/*
3 rows from products table:
id	product_name	price

*/


CREATE TABLE publisher (
	publisher_id SERIAL NOT NULL, 
	publisher_name VARCHAR(255) NOT NULL, 
	publisher_estd INTEGER, 
	publsiher_location VARCHAR(255), 
	publsiher_type VARCHAR(255), 
	CONSTRAINT publisher_pkey PRIMARY KEY (publisher_id)
)

/*
3 rows from publisher table:
publisher_id	publisher_name	publisher_estd	publsiher_location	publsiher_type
1	Packt	1950	chennai	books
2	Springer	1950	chennai	books
3	Springer	1950	chennai	articles
*/


CREATE TABLE tbl_documents (
	doc_id UUID DEFAULT gen_random_uuid() NOT NULL, 
	filename TEXT, 
	date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
	is_active BOOLEAN DEFAULT true NOT NULL, 
	CONSTRAINT documents_pkey PRIMARY KEY (doc_id)
)

/*
3 rows from tbl_documents table:
doc_id	filename	date_added	is_active
429828f5-052d-428f-b882-8ed219ece547	NIH-research.pdf	2024-11-27 17:00:35.500828+00:00	True
*/


CREATE TABLE tbl_embeddings (
	id SERIAL NOT NULL, 
	document_id UUID NOT NULL, 
	content TEXT, 
	embeddings REAL[], 
	CONSTRAINT embeddings_pkey PRIMARY KEY (id)
)

/*
3 rows from tbl_embeddings table:
id	document_id	content	embeddings
68	2f524c61-ef85-404e-b487-fb0fe304d8e2	This is the content of the document	[0.023209529, 0.023142641, 0.031168992, 0.016092831, -0.019182976, 0.026192656, 0.0064378013, -0.031
69	d3065f25-34bd-433d-b6d3-71e5f7603e42	Here is a lot of text that we will embed	[0.023209529, 0.023142641, 0.031168992, 0.016092831, -0.019182976, 0.026192656, 0.0064378013, -0.031
*/


CREATE TABLE tbl_prompts (
	prompt_id UUID DEFAULT gen_random_uuid() NOT NULL, 
	prompt_code VARCHAR(50), 
	llm VARCHAR(255), 
	prompt TEXT, 
	date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
	date_modified TIMESTAMP WITHOUT TIME ZONE, 
	CONSTRAINT prompts_pkey PRIMARY KEY (prompt_id)
)

/*
3 rows from tbl_prompts table:
prompt_id	prompt_code	llm	prompt	date_added	date_modified
429828f5-052d-428f-b882-8ed219ece547	OPEN-01-VARIED	OPENAI	You are a specialist {context} and you have the following question: {question}	2024-11-27 16:45:47.383615+00:00	None
*/


CREATE TABLE tbl_question_ratings (
	id UUID DEFAULT gen_random_uuid() NOT NULL, 
	question_id UUID NOT NULL, 
	is_first BOOLEAN DEFAULT true, 
	feedback TEXT, 
	is_accurate BOOLEAN, 
	is_complete BOOLEAN, 
	is_relevant BOOLEAN, 
	comments TEXT, 
	date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
	CONSTRAINT question_ratings_pkey PRIMARY KEY (id)
)

/*
3 rows from tbl_question_ratings table:
id	question_id	is_first	feedback	is_accurate	is_complete	is_relevant	comments	date_added
00bfa1cc-eb2a-4be6-9b3d-a0b7fb3b7e58	2f524c61-ef85-404e-b487-fb0fe304d8e2	True	GOOD	True	False	True	Here is some additonal info...	2024-11-27 16:55:08.754203+00:00
*/


CREATE TABLE tbl_questions (
	question_id UUID DEFAULT gen_random_uuid() NOT NULL, 
	user_id UUID NOT NULL, 
	question_text TEXT, 
	response_text TEXT, 
	archictecture_code VARCHAR(50), 
	date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
	CONSTRAINT questions_pkey PRIMARY KEY (question_id)
)

/*
3 rows from tbl_questions table:
question_id	user_id	question_text	response_text	archictecture_code	date_added
d25f00f5-122d-44e5-8fdc-4ab1e01ed91b	9f524c61-ef85-404e-b487-fb0fe304d8e2	DO What is the restaurant's name?	The restaurant
name is Titos	TR0001	2024-11-27 15:16:38.801576+00:00
87f3cb08-a575-4b7c-84cb-5c50be29afa8	2f524c61-ef85-404e-b487-fb0fe304d8e2	DO What is the restaurant's name?	THE answer is : The restaurant name is Titos	TR0002	2024-11-27 15:18:01.025763+00:00
*/


CREATE TABLE tbl_users (
	user_id UUID DEFAULT gen_random_uuid() NOT NULL, 
	first_name VARCHAR(50) NOT NULL, 
	last__name VARCHAR(50) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	password VARCHAR(255) NOT NULL, 
	created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL, 
	updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL, 
	CONSTRAINT tbl_users_pkey PRIMARY KEY (user_id), 
	CONSTRAINT tbl_users_email_key UNIQUE (email)
)

/*
3 rows from tbl_users table:
user_id	first_name	last__name	email	password	created_at	updated_at

*/


CREATE TABLE tracks (
	id SERIAL NOT NULL, 
	track VARCHAR(50), 
	embeddings REAL[], 
	CONSTRAINT tracks_pkey PRIMARY KEY (id)
)

/*
3 rows from tracks table:
id	track	embeddings

*/