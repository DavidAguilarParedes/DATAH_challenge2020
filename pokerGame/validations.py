def search_in_list(letter, list):

    answer = ["error", "correct format"]

    for s in list:
        if letter == s:
            answer = ["ok", "correct format"]

    return answer

    #validates that the input have the format we want
def validate_format(card):

    number = len(card)
    list1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    list2 = ["S", "H", "D", "C"]

    if number == 2:
        answer = search_in_list(card[0], list1)

        if answer[0] == "ok":
            answer = search_in_list(card[1], list2)

    else:
        answer = ["error", "More than 2 characters"]

    return answer


def validate_cards(list):

    analize_hand = []

    for s in list:

        answer = validate_format(s)
        analize_hand.append(answer[0])

    return analize_hand


