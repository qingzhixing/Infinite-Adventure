def ClearScreen():
    """Clears the console screen."""
    import os

    os.system("cls" if os.name == "nt" else "clear")


def Pause():
    """Pauses the console until the user presses Enter."""
    input("Press ENTER to continue...")
    # 删除上一行
    print("\033[F\033[K", end="")  # ANSI escape codes to move cursor up and clear line


def TypingEffectPrint(text: str, delay_s: float = -1, end: str = "\n"):
    """
    Prints the text with a typing effect.
    :param text: The text to print.
    :param delay_s: Delay between each character. If < 0, auto-adjusts based on text length. If = 0, prints instantly.
    :param end: The string appended after the last character.
    """
    import time

    if text == "":
        return

    if delay_s < 0:
        delay_s = 0.05
        if len(text) >= 10:
            delay_s = 0.02

        if len(text) >= 30:
            delay_s = 0.01

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay_s)

    print(end, end="", flush=True)
