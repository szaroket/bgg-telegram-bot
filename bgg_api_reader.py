import requests
import xmltodict


class BoardGame:
    def __init__(self, name, year_published, description, image):
        self.name = name
        self.year_published = year_published
        self.description = description
        self.image = image


def get_all_gameid(response: dict) -> list:
    list_of_gameid = []
    for game in response["boardgames"]["boardgame"]:
        list_of_gameid.append(game["@objectid"])
    return list_of_gameid


def get_gameid_from_api(game_name: str) -> list:
    response = requests.get("https://api.geekdo.com/xmlapi/search?search=" + game_name)
    dict_searched_gamesid = xmltodict.parse(response.content)
    return get_all_gameid(dict_searched_gamesid)


def create_board_game_object(board_game_data) -> object:
    year_published = board_game_data["yearpublished"]
    description = board_game_data["description"]
    image = board_game_data["image"]
    game_name = None
    for name in board_game_data["name"]:
        if type(name) is dict and "@primary" in name.keys():
            game_name = name["#text"]
    return BoardGame(game_name, year_published, description, image)


def get_list_of_board_games(gameid_list: list) -> list:
    list_of_games = []
    for gameid in gameid_list:
        print(gameid)
        response = requests.get("https://boardgamegeek.com/xmlapi/boardgame/" + gameid)
        dict_searched_games = xmltodict.parse(response.content)
        print(dict_searched_games)
        list_of_games.append(
            create_board_game_object(dict_searched_games["boardgames"]["boardgame"])
        )
    return list_of_games


list_id = get_gameid_from_api("Everdell")
get_list_of_board_games(list_id)
