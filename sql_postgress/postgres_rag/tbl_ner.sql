CREATE TABLE IF NOT EXISTS tbl_ner (
    ner_id uuid NOT NULL DEFAULT gen_random_uuid(),
    element_id uuid NOT NULL,
    word_text VARCHAR(100),
    word_label VARCHAR(100),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT ner_pk PRIMARY KEY (ner_id)
);

INSERT INTO public.tbl_ner(
	element_id, word_text, word_label)
	VALUES ('5f7b3a23dbc1a50d9f52f8b08baa024c', 'Javed Khan', 'PERS');