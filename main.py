from faceit_api import get_elo

nickname = input("닉네임 입력: ")
elo = get_elo(nickname)
print(f"{nickname}님의 FACEIT ELO: {elo}")
