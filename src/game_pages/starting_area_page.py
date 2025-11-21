import console_utils
import game_info
from game_pages import base_game_page
from game_pages.map_page import MapPage
import page_switcher
import player_info
from global_data import player


class StartingAreaPage(base_game_page.BaseGamePage):
    @staticmethod
    def NextLoop():
        selections = {
            "打开地图": StartingAreaPage.OpenMapSelection,
            "查看状态": StartingAreaPage.StatusSelection,
            "游戏信息": StartingAreaPage.GameDetailSelection,
            "退出游戏": StartingAreaPage.ExitGameSelection,
        }
        console_utils.ClearScreen()
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
    def OpenMapSelection():
        page_switcher.SwitchTo(MapPage.NextLoop)

    @staticmethod
    def StatusSelection():
        console_utils.ClearScreen()
        player_info.PrintPlayerInfo(player)
        console_utils.Pause()

    @staticmethod
    def GameDetailSelection():
        game_info.PrintGameInfo()
        console_utils.Pause()

    @staticmethod
    def ExitGameSelection():
        confirm = input("你确定要退出游戏吗？(y/n): ").strip().lower()
        if confirm == "y":
            page_switcher.SetGameOver()
