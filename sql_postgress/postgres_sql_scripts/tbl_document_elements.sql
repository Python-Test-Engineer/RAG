CREATE TABLE IF NOT EXISTS tbl_doc_elements (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    file_id uuid NOT NULL,
    element_id VARCHAR(150),
    element_type VARCHAR(50),
    element_text TEXT,
    page_number INTEGER,
    filename VARCHAR(150),
    filetype VARCHAR(50),
    processed_text TEXT,
    keywords TEXT [],
    embedding REAL [],
    image_base64 TEXT,
    CONSTRAINT doc_elements_pk PRIMARY KEY (id)
);

INSERT INTO tbl_doc_elements (
	file_id, element_id, element_type, element_text, image_base64, embedding)
VALUES ('5f524c61-ef85-404e-b487-fb0fe304d8e2','be34cd2d71310ec72bfef3d1be2b2b36', 'TEXT', 'Hello World','iVBORw0KG', ARRAY[1, 2]);