CREATE TABLE IF NOT EXISTS public.tbl_question_ratings
(
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    question_id uuid NOT NULL,
    is_first BOOLEAN DEFAULT TRUE,
   feedback TEXT,
    is_accurate BOOLEAN,
    is_complete BOOLEAN,
    is_relevant BOOLEAN,
    comments TEXT,
    date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT question_ratings_pkey PRIMARY KEY (id)
)

INSERT INTO public.tbl_question_ratings(
	 question_id, is_first, feedback, is_accurate, is_complete, is_relevant, comments)
VALUES ('2f524c61-ef85-404e-b487-fb0fe304d8e2','YES','GOOD', 'Yes', 'No', 'Yes', 'Here is some additonal info...');