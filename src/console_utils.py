def ClearScreen():
    """Clears the console screen."""
    import os

    os.system("cls" if os.name == "nt" else "clear")


def Pause():
    """Pauses the console until the user presses Enter."""
    input("Press ENTER to continue...")
    # 删除上一行
    print("\033[F\033[K", end="")  # ANSI escape codes to move cursor up and clear line


def TypingEffectPrint(text: str, delay_s: float = 0.05, end: str = "\n"):
    """Prints the text with a typing effect."""
    import time

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay_s)

    print(end, end="", flush=True)
