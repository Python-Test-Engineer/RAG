CREATE TABLE IF NOT EXISTS public.tbl_question_rating
(
    id uuid NOT NULL DEFAULT gen_random_uuid()
    question_id uuid NOT NULL,
    first_feedback VARCHAR(10),
    is_accurate BOOLEAN,
    is_complete BOOLEAN,
    is_relevant BOOLEAN,
    comments TEXT,
    date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT questions_pkey PRIMARY KEY (question_id)
)

INSERT INTO public.tbl_question_rating(
	question_id, first_feedback, is_accurate, is_complete, is_relevant, comments)
VALUES ('2f524c61-ef85-404e-b487-fb0fe304d8e2', 'GOOD', 'Yes', 'No', 'Yes', 'Here is some additonal info...');