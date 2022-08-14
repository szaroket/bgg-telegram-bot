import requests
import xmltodict


def get_all_gameid(response: dict) -> list:
    list_of_gameid = []
    for game in response["boardgames"]["boardgame"]:
        list_of_gameid.append(game["@objectid"])
    return list_of_gameid


def get_gameid_from_api(game_name: str) -> None:
    response = requests.get("https://api.geekdo.com/xmlapi/search?search=" + game_name)
    dict_searched_gamesid = xmltodict.parse(response.content)
    print(response.content)
    print(dict_searched_gamesid)
    print(get_all_gameid(dict_searched_gamesid))


get_gameid_from_api("Everdell")
