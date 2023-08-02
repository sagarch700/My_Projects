def calculate_score(cards):
    result = 0
    for i in cards:
        result += i

    if result == 21 and len(cards) == 2:
        return 0
    
    while result > 21 and 11 in cards:
            x = cards.index(11)
            cards[x] = 1
            result = result - 10
    return result