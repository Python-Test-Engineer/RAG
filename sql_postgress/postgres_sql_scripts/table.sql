CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE embeddings_table (id bigserial PRIMARY KEY, track varchar(255), embeddings vector(1536));