'''
Author: Logan Maupin

The purpose of this python script is to take a starting number and ending number and 
map out their english word representations then alphabetically sort those english words
in ascending order. God only knows why I'm doing this. It's honestly just for laughs, 
and serves no real practical purpose... I don't think... lol
'''
import inflect
from translate import Translator
from supported_languages import Supported_Languages 


def number_to_words(number: int) -> str:
    p = inflect.engine()
    return p.number_to_words(number)


def translate_number_to_language(number_word: str, target_language: str ='en') -> str:
    translator = Translator(to_lang=target_language)
    translation = translator.translate(number_word)
    return translation


def print_supported_languages(supported_languages: dict[str, str]) -> None:
    
    ''' WARNING: This is not necessarily a support list of languages that are
    supported by the translator service. It's just a possible list. Unfortunately, 
    I could not find a way to get the supported languages from this library. So 
    this is really just a catch-all list of languages that COULD be supported. '''

    for language_name, abbreviation in supported_languages.items():
        print(f"Language: {language_name}, Abbreviation: {abbreviation}")


def convert_language_name_to_abbreviation(language_name: str) -> str:
    return Supported_Languages.get(language_name.title())


def get_words_from_x_to_y(start: int, end: int, step: int, language: str ='en') -> list[str]:
    words = []
    for i in range(start, end + 1, step):
        if language != 'en':
            words.append((str(i), translate_number_to_language(number_to_words(i), target_language=language).lower()))
        else:
            words.append((str(i), number_to_words(i)))
    return words


def sort_words_alphabetically_ascending(words: list[str]) -> list[str]:
    return sorted(words, key=lambda x: x[1].lower())


def print_numbers_from_words(words) -> None:
    for i in range(len(words)):
        number = words[i][0]
        word = words[i][1]
        if i == len(words) - 1:
            print(number)
        else:
            print(number, end=', ')


def main():
    # first decide what your start, ends (inclusive), and steps will be.
    start = 0
    end = 10
    step = 1

    # we should also define the target language we want this to sort in too.
    target_language = "Italian"

    target_language_abbreviation = convert_language_name_to_abbreviation(target_language)

    # now call the get_words_from_x_to_y function with those values
    words = get_words_from_x_to_y(start, end, step, target_language_abbreviation)

    # now let's sort that list so that we can display our data properly in a meaningful way.
    words = sort_words_alphabetically_ascending(words)

    # now let's print the data
    print_numbers_from_words(words)


# only call main if the script is ran directly.
if __name__ == "__main__":
    main()
