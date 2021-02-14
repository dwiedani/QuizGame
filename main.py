from game import Game


if __name__ == '__main__':
    game = Game()
    game_exit = False

    while not game_exit:
        print('*** Game-Options ***')
        if game.selected_quiz:
            print('(1). play Quiz "' + game.data.get_quiz_by_id(game.selected_quiz).title + '"')
        print('(2). select Quiz')
        print('(3). create Quiz')
        print('(4). create Question / add to Quiz')
        print('(0). exit')
        task = input()
        if task == '1':
            game.play_quiz()
        if task == '2':
            game.select_quiz()
        if task == '3':
            game.create_quiz()
        if task == '4':
            game.create_question()
        elif task == '0':
            game_exit = True
