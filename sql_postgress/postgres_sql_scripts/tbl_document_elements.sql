CREATE TABLE IF NOT EXISTS tbl_doc_elements (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    element_id VARCHAR(50),
    text TEXT,
    filetype VARCHAR(50),
    languages JSONB,
    page_number INTEGER,
    filename VARCHAR(100),
    data_source_url VARCHAR(200),
    data_source_version VARCHAR(50),
    record_locator_path VARCHAR(200),
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    date_processed TIMESTAMP,
    permissions_data_mode INTEGER,
    filesize_bytes INTEGER
);