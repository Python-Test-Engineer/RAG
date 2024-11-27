
CREATE TABLE IF NOT EXISTS public.tbl_documents
(
    doc_id uuid NOT NULL DEFAULT gen_random_uuid(),
    filename TEXT,
    date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active boolean NOT NULL DEFAULT true,
    CONSTRAINT documents_pkey PRIMARY KEY (doc_id)
)


INSERT INTO public.tbl_documents(
	doc_id, filename)
VALUES ('429828f5-052d-428f-b882-8ed219ece547', 'NIH-research.pdf');