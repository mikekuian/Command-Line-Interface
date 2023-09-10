# contacts
contacts = {}

# decorator for possible errors in input
def handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func
        except KeyError:
            return "Input users name"
        except ValueError:
            return "Input name and phone please"
        except IndexError:
            return "Incorrect input format"
    return wrapper(func)


@handler_decorator
def greeting():
    return "How can I help you?"


@handler_decorator
def add_contact(name, phone):
    contacts[name] = phone
    return f"added {name} with number {phone}"

@handler_decorator
def edit_contact(name, phone):
    if name in contacts.keys():
        contacts[name] = phone
    else:
        return f"changed number of {name} with number{phone}"

@handler_decorator
def get_phone(name):
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}"
    else:
        return f"{name} not found in contacts"


@handler_decorator
def get_all_phones():
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


@handler_decorator
def terminate_bot():
    return "Good bye!"


def main():
    while True:
        command = input().lower()  # transform input into lowercase
        if command in ["good bye", "close", "exit", "bye"]:
            print(terminate_bot()) # terminate the bot
            break
        elif command in ["hello", "hi", "hey"]:
            print(greeting())
        elif command.startswith("add"):
            args = command.split()[1:]
            if len(args) == 2:
                name, phone = args
                print(add_contact(name, phone))
            else:
                print("Incorrect input format")
        elif command.startswith("change"):
            args = command.split()[1:]
            if len(args) == 2:
                name, phone = args
                print(edit_contact(name, phone))
            else:
                print("Incorrect input format")
        elif command.startswith("phone"):
            name = command.split()[1]
            print(get_phone(name))
        elif command == "show all":
            print(get_all_phones())
        else:
            print("Command not recognized. Type 'hello' for assistance.")


if __name__ == "__main__":
    main()