class Game:
    def __init__(self, title):
        self.title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) == 0:
            raise ValueError("Title must not be empty")
        self._title = value

    def results(self):
        return self._results

    def players(self):
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        return 0


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Username must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = value

    def results(self):
        return []

    def games_played(self):
        return []

    def played_game(self, game):
        return False

    def num_times_played(self, game):
        return 0


class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        game._results.append(self)
