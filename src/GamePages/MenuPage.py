import ConsoleUtils
import GameInfo
import GamePage
import PageSwitcher
import PlayerInfo
from Global import player


class MenuPage(GamePage.BaseGamePage):
    def next_loop(self):
        selections = {
            "移动": MenuPage.MoveSelection,
            "查看状态": MenuPage.StatusSelection,
            "游戏信息": MenuPage.GameDetailSelection,
            "退出游戏": MenuPage.ExitGameSelection,
        }
        ConsoleUtils.ClearScreen()
        print("[初始之地: Starting Area]")
        print("这里似乎是你出现在这个世界的位置...")
        print("=" * 60)
        for id, element in enumerate(selections.keys(), start=1):
            print(f"{id}. {element}", end="  " if id % 4 != 0 else "\n")
        print("=" * 60)

        input_check = False
        choice = 0
        while not input_check:
            try:
                choice = int(input("请输入你的选择: "))
                if 1 <= choice <= len(selections):
                    input_check = True
                else:
                    print("选择无效，请输入有效的数字.")
            except ValueError:
                print("输入无效，请输入数字.")

        selections[list(selections.keys())[choice - 1]]()

    @staticmethod
    def MoveSelection():
        print("移动功能尚未实现。")
        ConsoleUtils.Pause()

    @staticmethod
    def StatusSelection():
        ConsoleUtils.ClearScreen()
        PlayerInfo.PrintPlayerInfo(player)
        ConsoleUtils.Pause()

    @staticmethod
    def GameDetailSelection():
        GameInfo.PrintGameInfo()
        ConsoleUtils.Pause()

    @staticmethod
    def ExitGameSelection():
        confirm = input("你确定要退出游戏吗？(y/n): ").strip().lower()
        if confirm == "y":
            PageSwitcher.SetGameOver()
