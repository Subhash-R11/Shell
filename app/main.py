import sys

def main():
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        if cmd == "exit":
            sys.exit(0)
        elif cmd[5:] in ["type","echo","exit"]:
            print(f"{cmd[5:]} is a shell builtin")
        elif cmd.startswith("echo "):
            print(cmd[5:])
        else:
            print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
