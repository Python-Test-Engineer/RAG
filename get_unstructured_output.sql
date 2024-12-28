SELECT element_type, RIGHT(image_base64, 20),  embedding FROM public.tbl_doc_elements
ORDER BY id ASC 

SELECT element_id, element_type, element_text 
FROM public.tbl_doc_elements
ORDER BY id ASC 