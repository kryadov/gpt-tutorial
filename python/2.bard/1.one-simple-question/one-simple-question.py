import os

from bardapi import Bard

# also read https://github.com/dsdanielpark/Bard-API/issues/155
# model = "LaMDA" # https://en.wikipedia.org/wiki/LaMDA
bard_output = Bard(token='os.environ.get("_BARD_API_KEY")').get_answer("Is there life on Mars?")['content']
print(bard_output)
