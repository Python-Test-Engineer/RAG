CREATE TABLE documents (
    doc_id uuid DEFAULT gen_random_uuid(),
    filename VARCHAR NOT NULL,
    added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (doc_id)
);

CREATE TABLE document_data (
    doc_id uuid ,
    content TEXT NOT NULL,
    embeddings real[],
    added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (doc_id)
);