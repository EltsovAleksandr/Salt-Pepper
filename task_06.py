l = ["R", "P", "S"]  # P - бумага, S - ножницы, R - камень


def rps_game_winner(a):
    if len(a) != 2:
        raise Exception("WrongNumberOfPlayersError")
    elif a[0][1] not in l or a[1][1] not in l:
        raise Exception("NoSuchStrategyError")
    elif a[0][1] == a[1][1]:
        return f"{a[0][0]} {a[0][1]}"
    elif a[0][1].upper() == "P":  # первый игрок бумага
        if a[1][1].upper() == "S":  # второй игрок ножницы
            return f"{a[1][0]} {a[1][1]}"
        else:
            return f"{a[0][0]} {a[0][1]}"
    elif a[0][1].upper() == "S":  # перый игрок ножницы
        if a[1][1].upper() == "R":  # второй игрок камень
            return f"{a[1][0]} {a[1][1]}"
        return f"{a[0][0]} {a[0][1]}"
    elif a[0][1].upper() == "R":  # первый игрок камень
        if a[1][1].upper() == "P":  # второй игрок бумага
            return f"{a[1][0]} {a[1][1]}"
        return f"{a[0][0]} {a[0][1]}"


# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) # => WrongNumberOfPlayersError
# rps_game_winner([['player1', 'P'], ['player2', 'A']]) # => NoSuchStrategyError
# print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # => 'player2 S'
# print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  # => 'player1 P'
# print(rps_game_winner([['player1', 'P'], ['player2', 'R']]))  # => 'player1 P'
# print(rps_game_winner([['player1', 'R'], ['player2', 'P']]))  # => 'player2 P'
# print(rps_game_winner([['player1', 'R'], ['player2', 'S']]))  # => 'player1 R'
# print(rps_game_winner([['player1', 'R'], ['player2', 'R']]))  # => 'player1 R'
# print(rps_game_winner([['player1', 'S'], ['player2', 'R']]))  # => 'player2 R'
# print(rps_game_winner([['player1', 'S'], ['player2', 'P']]))  # => 'player1 S'
# print(rps_game_winner([['player1', 'S'], ['player2', 'S']]))  # => 'player1 S'
