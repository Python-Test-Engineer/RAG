import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("test.pdf")
pathlib.Path("test_output.md").write_bytes(md_text.encode())

