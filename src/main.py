import ConsoleUtils
from DataReadWriter import LoadPlayer, SavePlayer
from GamePages.MenuPage import MenuPage
import PageSwitcher
import PlayerInfo

player = PlayerInfo.Player()


def InputPlayerInfo():
    name_check = False
    while not name_check:
        player.name = input("亲爱的玩家，请输入你的姓名: ").strip()
        if player.name == "":
            print("姓名不能为空，请重新输入.")
            continue

        confirm_name = (
            input(f"你输入的姓名是 '{player.name}'，确认无误吗？(y/n): ")
            .strip()
            .lower()
        )
        if confirm_name == "y":
            name_check = True
        else:
            print("请重新输入姓名.")

    print(f"你好，{player.name}! 你的冒险之旅即将开始!")


def SelectJob():
    print("请选择你的职业:")
    for index, job in enumerate(PlayerInfo.JobList, start=1):
        print(f"\n{index}. {job.name} ({job.en_name}) - {job.description}")
        print(f"\t最大生命值: {job.max_health}")
        print(f"\t攻击力: {job.attack_damage}")

    job_selected = False
    while not job_selected:
        try:
            choice = int(input("请输入对应的数字选择职业: "))
            if 1 <= choice <= len(PlayerInfo.JobList):
                selected_job = PlayerInfo.JobList[choice - 1]
                player.set_job(selected_job)
                print(f"你已选择职业: {selected_job.name} ({selected_job.en_name})")
                job_selected = True
            else:
                print("选择无效，请输入有效的数字.")
        except ValueError:
            print("输入无效，请输入数字.")


def CreateAccount():
    global player

    read_player = LoadPlayer()
    if read_player is None:
        InputPlayerInfo()
        ConsoleUtils.Pause()
        ConsoleUtils.ClearScreen()
        SelectJob()
        ConsoleUtils.Pause()
        ConsoleUtils.ClearScreen()
        SavePlayer(player)
    else:
        player = read_player
        print("已加载存档，欢迎回来!")

    PlayerInfo.PrintPlayerInfo(player)
    ConsoleUtils.Pause()


def GameLoop():
    while not PageSwitcher.IsGameOver():
        PageSwitcher.NextLoop()


def Initialize():
    ConsoleUtils.ClearScreen()
    print("欢迎来到 [无尽的冒险: Infinite Adventure]")
    CreateAccount()
    PageSwitcher.SwitchTo(MenuPage())


def main():
    Initialize()
    GameLoop()


if __name__ == "__main__":
    print("正在启动 Infinite Adventure...")
    main()
    print("Infinite Adventure 已退出。")
