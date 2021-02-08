import pymorphy2


morph = pymorphy2.MorphAnalyzer()


def word_agree_with_number(number: int, word: str) -> str:
    """Возвращает форму слова согласованную с числительным."""
    morph_word = morph.parse(word)[0]
    return morph_word.make_agree_with_number(number).word