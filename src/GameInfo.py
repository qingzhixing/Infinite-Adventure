import ConsoleUtils

GameName = "无尽的冒险 (Infinite Adventure)"
GameVersion = "v0.1.0"
VersionUpdate = "早期游戏开发中..."
Author = "@qingzhixing"


def PrintGameInfo():
    print(f"游戏名称: {GameName}\n")
    print(f"游戏版本: {GameVersion}\n")
    print(f"版本更新信息: {VersionUpdate}\n")
    ConsoleUtils.TypingEffectPrint(f"Made by: {Author}\n")
