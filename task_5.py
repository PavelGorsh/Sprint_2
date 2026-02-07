import inspect

class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'
    
    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'
    
    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'
    
    def total_points(self):
        total = 3*self.victories + self.draws
        return f'Общее количество очков: {total}'
    
class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Хоккейных побед: {self.victories}'
    
    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}'
    
    def number_of_losses(self):
        return f'Хоккейных поражений: {self.losses}'
    
    def total_points(self):
        total = 2*self.victories + self.draws
        return f'Общее количество очков: {total}'
    
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    team_methods = [m[0] for m in inspect.getmembers(team, predicate=inspect.ismethod)] # Сохранение списка методов ['__init__', 'number_of_draws', 'number_of_losses', 'number_of_wins', 'total_points']
    for i in range(1, len(team_methods)):
        print(getattr(team, team_methods[i])()) # Вызов методов, начиная со второго, чтобы пропустить конструктор