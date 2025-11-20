def ClearScreen():
    """Clears the console screen."""
    import os

    os.system("cls" if os.name == "nt" else "clear")


def Pause():
    """Pauses the console until the user presses Enter."""
    input("按下回车键继续...")
    # 删除上一行
    print("\033[F\033[K", end="")  # ANSI escape codes to move cursor up and clear line
