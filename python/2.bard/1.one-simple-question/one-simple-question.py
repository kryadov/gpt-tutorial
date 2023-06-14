from bardapi import Bard

# model = "LaMDA" # https://en.wikipedia.org/wiki/LaMDA
bard_output = Bard().get_answer("Is there life on Mars?")['content']
print(bard_output)
