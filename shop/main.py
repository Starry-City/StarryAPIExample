import requests
import json
from pprint import pprint


class ApiExample:
    def __init__(self, key) -> None:
        self.url_base = "https://api.starrycity.net/api/shop"
        self.key = key

    # 取得物品最近幾筆完整交易紀錄
    def getLastestTransaction(self, item: str, limit: int = 10):
        raw = requests.get(
            f"{self.url_base}/getTransation?limit={limit}&key={self.key}"
        ).text
        try:
            lastest_transaction = json.loads(raw)['result']
            return lastest_transaction
        except:
            return 'Error'

    # 取得特定物品時間範圍內完整交易紀錄
    def getTransactionByTime(self, item: str, ts: int, te: int):
        post_data = {
            "items": f'[{item}]',
            "ts": f'[{ts}]',
            "te": f'[{te}]',
            "key": self.key
        }
        raw = requests.post(
            f"{self.url_base}/getTransation",
            data=post_data
        ).text
        # print(raw)
        try:
            transation_by_time = json.loads(raw)['result']
            return transation_by_time
        except:
            return 'Error'

    # 取得物品總交易量排行榜
    def getLeaderBoard(self, limit: int = 10):
        raw = requests.get(
            f"{self.url_base}/getLeaderBoard?limit={limit}&key={self.key}"
        ).text
        try:
            leader_board = json.loads(raw)['result']
            return leader_board
        except:
            return 'Error'


if __name__ == "__main__":
    api = ApiExample('xxxx')
    print('取得銅錠最近10筆完整交易紀錄')
    pprint(api.getLastestTransaction('COPPER_INGOT', limit=10))

    print('取得銅錠在時間翻圍內的完整交易紀錄')
    pprint(api.getTransactionByTime('COPPER_INGOT', 1689865200, 1689951600))

    print('取得物品總交易量排行榜')
    pprint(api.getLeaderBoard(limit=10))
