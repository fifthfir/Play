import word_puzzle


def test_search_word():
    sheet1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]

    word_lst1 = ['a']
    word_lst2 = ['a', 'e']
    word_lst3 = ['e', 'i']
    word_lst4 = ['c', 'e']
    word_lst5 = ['i', 'h']

    assert word_puzzle.search_word_helper(sheet1, 0, 0, 0, 0, word_lst1) == [0, 0]
    assert word_puzzle.search_word(sheet1, word_lst2) == [[0, 0], [1, 1]]
    assert word_puzzle.search_word(sheet1, word_lst3) == [[1, 1], [2, 2]]
    assert word_puzzle.search_word(sheet1, word_lst4) == [[2, 0], [1, 1]]
    assert word_puzzle.search_word(sheet1, word_lst5) == [[2, 2], [1, 2]]