import sys

def main():
    while True:

        sys.stdout.write("$ ")

        command = input()

        if command == "exit":
            sys.exit(0)

        elif command.startswith("type "):
            cmd = command[5:]
            if cmd in ["type","echo","exit"]:
                print(f"{cmd} is a shell builtin")
            else:
                print(f"{cmd} not found")

        elif command.startswith("echo "):
            print(command[5:])

        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
