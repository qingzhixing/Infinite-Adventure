import json
import PlayerInfo

SAVE_PATH = "game_save.json"


def SavePlayer(player: PlayerInfo.Player):
    with open(SAVE_PATH, "w", encoding="utf-8") as file:
        data = {
            "name": player.name,
            "level": player.level,
            "health": player.health,
            "max_health": player.max_health,
            "attack_damage": player.attack_damage,
            "experience": player.experience,
            "job": {
                "name": player.job.name,
                "en_name": player.job.en_name,
            },
        }
        json.dump(data, file, ensure_ascii=False, indent=4)


def LoadPlayer() -> PlayerInfo.Player | None:
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            player = PlayerInfo.Player()
            player.name = data["name"]
            player.level = data["level"]
            player.health = data["health"]
            player.max_health = data["max_health"]
            player.attack_damage = data["attack_damage"]
            player.experience = data["experience"]

            job_name = data["job"]["name"]
            for job in PlayerInfo.JobList:
                if job.name == job_name:
                    player.set_job(job)
                    break

            return player
    except FileNotFoundError:
        return None
