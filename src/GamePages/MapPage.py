from GamePages.BaseGamePage import BaseGamePage
from GamePages import StartingAreaPage
import ConsoleUtils
import PageSwitcher


class MapPage(BaseGamePage):
    @staticmethod
    def NextLoop():
        ConsoleUtils.ClearScreen()
        print("[地图: Map]")
        print("你打开了地图.")
        ConsoleUtils.TypingEffectPrint("前面的区域, 以后再来探索吧!")
        PageSwitcher.SwitchTo(StartingAreaPage.StartingAreaPage.NextLoop)
        ConsoleUtils.Pause()
