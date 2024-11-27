
CREATE TABLE IF NOT EXISTS public.tbl_embeddings
(
    id integer NOT NULL DEFAULT nextval('embeddings_table_id_seq'::regclass),
    document_id UUID NOT NULL,
    embeddings real[],
    CONSTRAINT embeddings_pkey PRIMARY KEY (id)
)

INSERT INTO public.tbl_embeddings(
	document_id, embeddings)
VALUES ('2f524c61-ef85-404e-b487-fb0fe304d8e2', ARRAY[1, 2]);

