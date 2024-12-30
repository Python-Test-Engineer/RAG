SELECT created_at, file_id, element_type, element_text, embedding FROM public.tbl_doc_elements
ORDER BY created_at, file_id  DESC 

SELECT created_at, file_id, element_type, element_text, embedding FROM public.tbl_doc_elements
WHERE element_type = 'NARRATIVETEXT'
ORDER BY created_at, file_id  DESC 