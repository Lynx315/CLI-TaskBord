import operations

print("coyright (c) 2024 by DozyLynx")
print("""
  /$$$$$$  /$$       /$$$$$$       /$$$$$$$$                  /$$                
 /$$__  $$| $$      |_  $$_/      |__  $$__/                 | $$                
| $$  \__/| $$        | $$           | $$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$$
| $$      | $$        | $$           | $$ |____  $$ /$$_____/| $$  /$$/ /$$_____/
| $$      | $$        | $$           | $$  /$$$$$$$|  $$$$$$ | $$$$$$/ |  $$$$$$ 
| $$    $$| $$        | $$           | $$ /$$__  $$ \____  $$| $$_  $$  \____  $$
|  $$$$$$/| $$$$$$$$ /$$$$$$         | $$|  $$$$$$$ /$$$$$$$/| $$ \  $$ /$$$$$$$/
 \______/ |________/|______/         |__/ \_______/|_______/ |__/  \__/|_______/ 
""")
print("Type /help for a list of commands")

while True:

    userInput = input("> ")
    if userInput.startswith("/"):
        stripInput = userInput[1:].strip()
        splitInput = stripInput.split(" ", 1)
        userCommand = splitInput[0]
        args = splitInput[1] if len(splitInput) > 1 else None

    func = operations.commands.get(userCommand)
    if func:
        if args:
            func(args)   # functions that take 1 argument
        else:
            func()  # functions that take no arguments
    