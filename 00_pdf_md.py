import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("test_nih.pdf")
pathlib.Path("test_nih_output.md").write_bytes(md_text.encode())
