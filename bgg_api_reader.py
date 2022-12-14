import requests
import xmltodict


class BoardGame:
    def __init__(self, name, year_published, description):
        self.name = name
        self.year_published = year_published
        self.description = description
        # self.image = image


def get_all_gameid(response: dict) -> list:
    list_of_gameid = []
    for game in response["boardgames"]["boardgame"]:
        list_of_gameid.append(game["@objectid"])
    return list_of_gameid


def get_gameid_from_api(game_name: str) -> list:
    response = requests.get("https://api.geekdo.com/xmlapi/search?search=" + game_name)
    dict_searched_gamesid = xmltodict.parse(response.content)
    return get_all_gameid(dict_searched_gamesid)


# separate function to get board game name
# API can return name in dict or list of dicts
def get_board_game_name(list_of_names) -> str:
    if type(list_of_names) is dict and "@primary" in list_of_names.keys():
        return list_of_names["#text"]

    for name in list_of_names:
        if type(name) is dict and "@primary" in name.keys():
            return name["#text"]


def create_board_game_object(board_game_data) -> object:
    year_published = board_game_data["yearpublished"]
    description = board_game_data["description"]
    # image = board_game_data["image"]
    name = get_board_game_name(board_game_data["name"])
    return BoardGame(name, year_published, description)


def get_list_of_board_games(game_name: str) -> list:
    gameid_list = get_gameid_from_api(game_name)
    list_of_games = []
    for gameid in gameid_list:
        response = requests.get("https://boardgamegeek.com/xmlapi/boardgame/" + gameid)
        dict_searched_games = xmltodict.parse(response.content)
        list_of_games.append(
            create_board_game_object(dict_searched_games["boardgames"]["boardgame"])
        )
    return list_of_games
