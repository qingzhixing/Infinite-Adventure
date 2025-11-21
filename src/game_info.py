import console_utils

GameName = "无尽的冒险 (Infinite Adventure)"
GameVersion = "v0.1.0"
VersionUpdate = "早期游戏开发中..."
Author = "@qingzhixing"


def PrintGameInfo():
    console_utils.ClearScreen()
    print(f"游戏名称: {GameName}")
    print(f"游戏版本: {GameVersion}")
    print(f"版本更新信息: {VersionUpdate}")
    print(f"Made by: {Author}")
