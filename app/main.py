def copy_file(command: str) -> None:
    if len(command.split(" ")) < 3:
        return

    cmd, current_file, new_file = command.split(" ")

    if cmd == "cp":
        if current_file != new_file:
            try:
                with open(current_file, "r") as f:
                    with open(new_file, "w") as new_f:
                        new_f.write(f.read())
            except FileNotFoundError:
                return
