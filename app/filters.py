import pymorphy2


morph = pymorphy2.MorphAnalyzer()


def word_agree_with_number(number: int, word: str) -> str:
    """Возвращает форму слова согласованную с числительным."""
    morph_word = morph.parse(word)[0]
    return morph_word.make_agree_with_number(number).word


def base_limiter(tours: dict, field_name: str, postfix_word: str = '') -> str:
    """Базовый лимитер для туров."""
    values = list(map(lambda tour: tour.get(field_name), tours))
    postfix = word_agree_with_number(5, postfix_word)
    limiter_parts = ('от', str(min(values)), 'до', str(max(values)), postfix)
    return ' '.join(limiter_parts)


def price_limiter(tours: dict) -> str:
    return base_limiter(tours, 'price', 'рубль')


def nights_limiter(tours: dict) -> str:
    return base_limiter(tours, 'nights', 'ночь')
