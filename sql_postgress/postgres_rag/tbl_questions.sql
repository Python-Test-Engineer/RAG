CREATE TABLE IF NOT EXISTS public.tbl_questions
(
    question_id uuid NOT NULL DEFAULT gen_random_uuid(),
    user_id uuid NOT NULL,
    question_text text COLLATE pg_catalog."default",
    response_text text COLLATE pg_catalog."default",
    archictecture_code character varying(50) COLLATE pg_catalog."default",
    date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT questions_pkey PRIMARY KEY (question_id)
)

INSERT INTO public.tbl_questions(
	user_id, question_text, response_text, archictecture_code)
VALUES (tbl_pr, 'DO What is the restaurant''s name?', 'THE answer is : The restaurant name is Titos', 'TR0002');