import speech_recognition as sr
import random
import playsound
import os
import re
import webbrowser
from gtts import gTTS


def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то >>> ")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        print(f"Вы сказали: {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return "ошибка распознание"
    except sr.RequestError:
        return "ошибка запроса"


def say(text):
    voice = gTTS(text, lang="ru")
    unique_file = "audio_" + str(random.randint(0, 10000)) + ".mp3"  # audio_10.mp3
    voice.save(unique_file)

    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f"Ассистент: {text}")


def handle_command(command):
    command = command.lower()

    if command == "привет":
        say("Привет-привет")
    elif command == "пока":
        stop()
    elif command == "какие пары в среду":
        say("Вторая и третья пара лекции по основам информационной безопасности.Четвертая пара английский язык.")
    elif command == "какие пары в понедельник":
        say("Вторая и третья пара лекции по интеллектуальным системам")
    elif command == "какие пары во вторник":
        say("Первая пара практика по вычислительным системам, сетям и телекоммуникациям.Вторая пара лекция по вычислительным ситемам.Третья пара английский язык")
    elif command == "какие пары в четверг":
        say("Пар нет, можно отдыхать")
    elif command == "какие пары в пятницу":
        say("Вторая пара английский язык. Третья пара практика по интеллектуальным системам. Четвертая пара практика по основам информационной безопасности")
    elif command == "какие пары в субботу":
        say("Пар нет, можно отдыхать")
    elif command == "какие пары в субботу":
        say("Пар нет, можно отдыхать")
    elif command == "кто ведет лекции по интеллектуальным системам":
        say("Гусев Андрей Леонидович")
    elif command == "кто ведет практики по интеллектуальным системам":
        say("Гусев Андрей Леонидович")
    elif command == "кто ведет английский язык":
        say("Широкова Ганна Атанасовна")
    elif command == "кто ведет  основы информационной безопасности":
        say("Карпов Михаил Юрьевич")
    elif command == "кто ведет лекции по вычислительным системам":
        say("Раевский Виктор Николаевич ")
    elif command == "кто ведет практики по вычислительным системам":
        say("Анисимова Светлана Игоревна")
    elif command == "где проходят лекции по интеллектуальным системам":
        say("Второй корупус,третий этаж,аудитория 422")
    elif command == "где проходят лекции по вычислительным сетям ":
        say("Второй корпус,первый этаж,аудитория 225,ваша любимая!")
    elif command == "где проходят практики по вычислительным сетям":
        say("Восьмой корпус,четвертый этаж,аудитория 401/8")
    elif command == "где проходит английский язык по вторникам":
        say("Пятый корпус,первый этаж,аудитория 165/5")
    elif command == "где проходит английский по средам":
        say("Пятый корпус,первый этаж,аудитория 162/5")
    elif command == "где проходят лекции по основам информационной безопасности ":
        say("Второй корпус,третий этаж,аудитория 419")
    elif command == "где проходят практики по основам информационнной безопасности":
        say("Второй корпус,второй этаж,аудитория 305")
    elif command == "где проходят практики по интеллектуальным системам":
        say("Второй корпус,четвертый этаж,аудитория 519")
    elif command == "где проходит англиский язык по пятницам":
        say("Пятый корпус,первый этаж,аудитория 162/5")
    elif command == "где находится деканат":
        say("Второй корпус,аудитория 410")
    elif command == "как зовут нашего декана":
        say("Кузнецов Андрей Геннадьевич")
    elif command == "как зовут нашу старосту":
	    say("Главатских Ксения")
    elif command == "скажи телефон деканата":
	    say("двести тридцать девять шестьдесят три двадцать шесть")
    elif 'открой наш сайт' in command:
        url = 'http://www.psu.ru/'
        webbrowser.open(url)
        say("Запрошенный вами сайт открыт для вас")
    elif 'открой етис' in command:
        url = 'https://student.psu.ru/pls/stu_cus_et/stu.teach_plan'
        webbrowser.open(url)
        say("Запрошенный вами сайт открыт для вас")
    else:
        say("Не понятно, повторите")
def stop():
    say("До скорого.Удачи вам в учебе!")
    exit()


def start():
    print("Запуск ассистента...")

    while True:
        command = listen()
        handle_command(command)



try:
    start()
except KeyboardInterrupt:
    stop()