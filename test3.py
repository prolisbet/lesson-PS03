from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка - {str(e)}")


def translate_words(word, definition):
    try:
        rus_word = translator.translate(word, dest="ru").text.strip()
        rus_definition = translator.translate(definition, dest="ru").text.strip()

        return [rus_word, rus_definition]

    except Exception as e:
        print(f"Произошла ошибка - {str(e)}")
        return None


def word_game():
    print("Добро пожаловать в игру")
    win = 0
    fail = 0
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        rus_word, rus_word_definition = translate_words(word, word_definition)

        # print(f"\nWord definition - {word_definition}")
        print(f"\nЗначение слова - {rus_word_definition}")
        user = input("Что это за слово? ")
        if user == rus_word:
            print("Ответ верный")
            win += 1
        else:
            print(f"Ответ неверный, было загадоно слово - {rus_word}")
            # print(f"Wrong answer, the right word - {word}")
            fail += 1

        play_again = input("Хотите сыграть еще раз? д/н ")
        if play_again not in ("д", "Д"):
            print("Спасибо за игру!")
            print(f"Победы: {win}")
            print(f"Поражения: {fail}")
            break


word_game()
