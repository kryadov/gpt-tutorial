from bardapi import Bard

bard_output = Bard().get_answer("Is there life on Mars?")['content']
print(bard_output)
