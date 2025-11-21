from typing import Callable

page_loop_function: Callable[[], None] | None = None


def SwitchTo(loop_function: Callable[[], None]):
    global page_loop_function
    page_loop_function = loop_function


def NextLoop():
    if page_loop_function is not None:
        page_loop_function()


def SetGameOver():
    global page_loop_function
    page_loop_function = None


def IsGameOver():
    return page_loop_function is None
