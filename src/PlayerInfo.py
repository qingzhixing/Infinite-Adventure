# 职业
class Job:
    def __init__(
        self,
        name: str = "",
        en_name: str = "",
        max_health: int = 100,
        attack_damage: int = 20,
        description: str = "",
    ):
        self.name = name
        self.en_name = en_name
        self.max_health = max_health
        self.attack_damage = attack_damage
        self.description = description


TANK_JOB = Job(
    "坦克", "Tank", max_health=400, attack_damage=20, description="可以开炮吗?"
)
MAGICIAN_JOB = Job(
    "法师",
    "Magician",
    max_health=100,
    attack_damage=10,
    description="憧憬成为魔法少女...",
)
UNEMPLOYED_JOB = Job(
    "无业游民",
    "Unemployed",
    max_health=1000,
    attack_damage=1,
    description="无职转生?",
)

JobList: list[Job] = [
    TANK_JOB,
    MAGICIAN_JOB,
    UNEMPLOYED_JOB,
]


class Player:
    def __init__(self):
        self.name: str = ""
        self.level: int = 1
        self.health: int = 100
        self.max_health: int = 100
        self.attack_damage: int = 20
        self.experience: int = 0

        self.set_job(UNEMPLOYED_JOB)

    def set_job(self, job: Job):
        self.job = job
        self.max_health = job.max_health
        self.attack_damage = job.attack_damage
        self.health = job.max_health


def PrintJobInfo(job: Job):
    print(f"职业名称: {job.name} ({job.en_name})")
    print(f"最大生命值: {job.max_health}")
    print(f"攻击力: {job.attack_damage}")
    print(f"职业描述: {job.description}")
    print("")


def PrintPlayerInfo(player: Player):
    print(f"玩家姓名: {player.name}  {player.job.name} ({player.job.en_name})")
    print(f"\t{player.job.description}")
    print(f"\t等级: {player.level}")
    print(f"\t生命值: {player.health}/{player.max_health}")
    print(f"\t攻击力: {player.attack_damage}")
    print(f"\t经验值: {player.experience}")
    print("")
