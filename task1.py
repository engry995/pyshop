from task import generate_game, OFFSET_MAX_STEP


def get_score(game_stamps: list[dict], offset: int) -> dict:
    """
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    """
    score = None
    max_offset = game_stamps[-1]['offset']

    if offset >= max_offset:
        score = game_stamps[-1]['score']

    elif offset <= 0:
        score = game_stamps[0]['score']

    else:
        left = offset // OFFSET_MAX_STEP
        right = min(offset, len(game_stamps))
        while left <= right:
            middle = (left + right)//2
            test_offset = game_stamps[middle]['offset']
            if offset == test_offset:
                score = game_stamps[middle]['score']
                break
            elif test_offset > offset:
                right = middle - 1
            else:
                left = middle + 1

        if not score:
            score = game_stamps[right]['score']

    return score


if __name__ == '__main__':
    game_stamps = generate_game()
    print(f'{get_score(game_stamps, 100000) = }')
