class Game:
    def __init__(self, title):
        self.title = title

    def results(self):
        return [result for result in Result.all() if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]
        return sum(player_results) / len(player_results) if player_results else 0


class Player:
    def __init__(self, username):
        self.username = username

    def results(self):
        return [result for result in Result.all() if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)


class Result:
    _all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result._all.append(self)

    @classmethod
    def all(cls):
        return cls._all
