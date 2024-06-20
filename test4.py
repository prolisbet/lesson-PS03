from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator


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
        translator = GoogleTranslator(source='en', target='ru')
        rus_word = translator.translate(word).strip()
        rus_definition = translator.translate(definition).strip()

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

        print(f"Значение слова - {rus_word_definition}")
        user = input("Что это за слово? ")
        if user == rus_word:
            print("Ответ верный")
            win += 1
        else:
            print(f"Ответ неверный, было загадано слово - {rus_word}")
            fail += 1

        play_again = input("Хотите сыграть еще раз? д/н ")
        if play_again not in ("д", "Д"):
            print("Спасибо за игру!")
            print(f"Победы: {win}")
            print(f"Поражения: {fail}")
            break


word_game()
