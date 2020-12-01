from adventure import Game, Hero, Villain

if __name__ == '__main__':
    game = Game(Hero('Derplander'), Villain())

    game.play()

    print(game)



