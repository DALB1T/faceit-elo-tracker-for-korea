import os
import requests
import pprint
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FACEIT_API_KEY")
BASE_URL = "https://open.faceit.com/data/v4"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_player_info(nickname):
    url = f"{BASE_URL}/players?nickname={nickname}"
    response = requests.get(url, headers=HEADERS)
    # print("DEBUG:", response.status_code, response.text)  # 응답 상태 출력
    return response.json()

def get_elo(nickname):
    data = get_player_info(nickname)
    try:
        return data['games']['cs2']#['faceit_elo']
    except KeyError:
        return "ELO 정보 없음 또는 유저 없음"
