# TODO: implement dialog with roles, parameters and context

print("Ask me something!")


def get_answer(p_message):
    # TODO: implement getting answer!
    return f"You asked: {p_message}"


message = None
while message != "/quit":
    print("> ", end="")
    message = input()
    print(f"< {get_answer(message)}")
