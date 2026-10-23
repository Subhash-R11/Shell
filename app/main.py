import sys
import os

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
                found = False

                for path in os.environ["PATH"].split(os.pathsep):
                    cmd_path = os.path.join(path, cmd)

                    if os.path.isfile(cmd_path) and os.access(cmd_path, os.X_OK):
                        print(f"{cmd} is {cmd_path}")
                        found = True
                        break
                    
                if not found:
                    print(f"{cmd}: not found")

        elif command.startswith("echo "):
            print(command[5:])

        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
