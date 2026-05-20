def load_system_prompt(file_path: str) -> str:
    """
    Reads and returns the contents of a text file.

    Used for loading external system prompts
    such as supervisor prompts, coder prompts, etc.

    Parameters:
    -----------
    file_path : str
        Path to the prompt text file.

    Returns:
    --------
    str
        File contents as a string.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                prompt = file.read()

                if not isinstance(prompt, str):
                    raise TypeError(
                        "File content could not be converted to string."
                    )

                return prompt

            except Exception as read_error:
                print(f"[READ ERROR] Failed to read file content: {read_error}")
                return ""

    except FileNotFoundError:
        print(f"[FILE ERROR] File not found: {file_path}")
        return ""

    except PermissionError:
        print(f"[PERMISSION ERROR] Permission denied: {file_path}")
        return ""

    except Exception as open_error:
        print(f"[OPEN ERROR] Failed to open file: {open_error}")
        return ""

print(load_system_prompt("supervisor.txt"))