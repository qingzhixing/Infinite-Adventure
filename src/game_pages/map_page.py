from game_pages import base_game_page, starting_area_page
import console_utils
import page_switcher


class MapPage(base_game_page.BaseGamePage):
    @staticmethod
    def NextLoop():
        console_utils.ClearScreen()
        print("[地图: Map]")
        print("你打开了地图.")
        console_utils.TypingEffectPrint("前面的区域, 以后再来探索吧!")
        page_switcher.SwitchTo(starting_area_page.StartingAreaPage.NextLoop)
        console_utils.Pause()
