from blockext import run, reporter, command


message = ""


@command("set message %s")
def set_message(m):
    global message
    message = m


@reporter("get message")
def get_message():
    return message


if __name__ == "__main__":
    run("Extension Test", "extension_test", 5678)