CREATE TABLE IF NOT EXISTS public.tbl_prompts
(
    prompt_id uuid NOT NULL DEFAULT gen_random_uuid(),
    prompt_code VARCHAR(50),
    llm VARCHAR(255),
    prompt text ,
    date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    date_modified TIMESTAMP,
    CONSTRAINT prompts_pkey PRIMARY KEY (prompt_id)
)

INSERT INTO public.tbl_prompts(
	prompt_id, prompt_code, llm, prompt)
VALUES ('429828f5-052d-428f-b882-8ed219ece547', 'OPEN-01-VARIED', 'OPENAI', 'You are a specialist {context} and you have the following question: {question}');