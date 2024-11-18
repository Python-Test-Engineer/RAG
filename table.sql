CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE items (id bigserial PRIMARY KEY, track varchar(255), embedding vector(1536));