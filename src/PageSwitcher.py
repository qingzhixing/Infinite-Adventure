import GamePage

current_page: GamePage.BaseGamePage | None = None


def SwitchTo(page: GamePage.BaseGamePage):
    global current_page
    current_page = page


def NextLoop():
    if current_page is not None:
        current_page.next_loop()


def SetGameOver():
    global current_page
    current_page = None


def IsGameOver():
    return current_page is None
