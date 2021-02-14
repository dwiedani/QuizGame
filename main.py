from game import Game


if __name__ == '__main__':
    game = Game()
    game_exit = False

    while not game_exit:
        print('---------------------')
        print('*** Game-Options ***')
        if game.selected_quiz:
            print('(1). play Quiz "' + game.data.get_quiz_by_id(game.selected_quiz).title + '"')
        print('(2). select Quiz')
        if game.current_user:
            print('(3). create Quiz')
            print('(4). create Question / add to Quiz')
            print('(5). show statistics')
        print('*** User-Options ***')
        if not game.current_user:
            print('(6). login')
            print('(7). register')

        print('(0). exit')
        task = input()
        if task == '1':
            game.play_quiz()
        if task == '2':
            game.select_quiz()
        if task == '3':
            if game.current_user:
                game.create_quiz()
        if task == '4':
            if game.current_user:
                game.create_question()
        if task == '5':
            if game.current_user:
                stats = game.current_user.stats()
                print(stats)
        if task == '6':
            user = game.login()
        if task == '7':
            user = game.register()
        elif task == '0':
            game_exit = True
