import os
import json
from flatten_json import flatten
from rich.console import Console
import pandas as pd

console = Console()

FILENAME = "./pdf_output/fake-memo.pdf.json"
FILENAME = "./pdf_output/nih/TMCB_43_2256640.pdf.json"
FILENAME = "./pdf_output/nih/nihms-1610503.pdf.json"
FILENAME = "./pdf_output/msft_openai.pptx.json"
FILE = "msft_openai.pptx.json"


filename_without_extension = os.path.splitext(FILE)[0]

print(filename_without_extension)
# Open the JSON file
with open(FILENAME, "r") as file:
    data = json.load(file)
    # print(type(data))

flattened_list = [flatten(item) for item in data]

# for i in range(7):
# console.print(flattened_list[i])

"""

Parsing complex json structure with pydantic.

Using example json file from from nobelprize.org
### laureate.json from http://api.nobelprize.org/v1/laureate.json

Original data looked like this:

------------

{
"laureates" : [
       {
       "id":"1",
       "firstname":"Wilhelm Conrad",
       "surname":"R\u00f6ntgen",
       "born":"1845-03-27",
       "died":"1923-02-10",
       "bornCountry":"Prussia (now Germany)",
       "bornCountryCode":"DE",
       "bornCity":"Lennep (now Remscheid)",
       "diedCountry":"Germany",
       "diedCountryCode":"DE",
       "diedCity":"Munich",
       "gender":"male",
       "prizes":[
          {
             "year":"1901",
             "category":"physics",
             "share":"1",
             "motivation":"\"in recognition of the extraordinary services he has rendered by the discovery of the remarkable rays subsequently named after him\"",
             "affiliations":[
                {
                   "name":"Munich University",
                   "city":"Munich",
                   "country":"Germany"
                }
             ]
          }
       ]
    }
}
---------------------------

"""


import json

from enum import Enum
from typing import List

from pydantic import BaseModel


class Category(str, Enum):
    physics = "physics"
    math = "math"
    economics = "economics"
    medicine = "medicine"
    peace = "peace"
    chemistry = "chemistry"
    literature = "literature"


class Prize(BaseModel):
    year: int
    category: Category
    share: int
    motivation: str
    affiliations: list


class Laureate(BaseModel):
    """fields with no values are required"""

    id: int
    firstname: str
    surname: str = ""
    born: str = None
    died: str = None
    bornCountry: str = None
    bornCountryCode: str = None
    bornCity: str = None
    diedCountry: str = None
    diedCountryCode: str = None
    diedCity: str = None
    gender: str = None
    prizes: List[Prize]


class Laureates(BaseModel):
    laureates: List[Laureate]


# Load data
with open("./laureate.json") as f:
    datax = json.load(f)
    laureates_data = Laureates(**datax)
    console.print(Laureates(**datax))
    console.print(laureates_data.laureates[0].prizes[0].category)
    console.print(Laureates(**datax).laureates[0].prizes[0].year)
