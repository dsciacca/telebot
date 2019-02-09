import time, datetime
import RPi.GPIO as GO
import telepot
from telepot.loop import MessageLoop

green1 = 26
green2 = 19
red1 = 13
red2 = 6
booted = datetime.datetime.now()
GO.setmode(GO.BCM)
GO.setwarnings(False)

GO.setup(green1, GO.OUT)
GO.output(green1, 0)
GO.setup(green2, GO.OUT)
GO.output(green2, 0)
GO.setup(red1, GO.OUT)
GO.output(red1, 0)
GO.setup(red2, GO.OUT)
GO.output(red2, 0)

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()
    print 'Received: %s' % command

    if command == '/booted':
        #telegram_bot.sendMessage(chat_id, str(booted.hour) + str(":") + str(booted.minute))
        if booted.minute < 10:
            telegram_bot.sendMessage(chat_id, str(booted.hour) + str(":0") + str(booted.minute))
        else:
            telegram_bot.sendMessage(chat_id, str(booted.hour) + str(":") + str(booted.minute))
    elif command == '/current time':
        now = datetime.datetime.now()
        #telegram_bot.sendMessage(chat_id, str(now.hour) + str(":") + str(now.minute))
        if now.minute < 10:
            telegram_bot.sendMessage(chat_id, str(now.hour) + str(":0") + str(now.minute))
        else:
            telegram_bot.sendMessage(chat_id, str(now.hour) + str(":") + str(now.minute))
    elif command == '/hi':
        telegram_bot.sendMessage(chat_id, str("Hi! FirstBot"))
    elif command == '/logo':
        telegram_bot.sendPhoto(chat_id, photo = open('/home/pi/Pictures/robot.jpeg'))
        #"https://pbs.twimg.com/profile_images/535502528490655744/6N28C6iP.jpeg"
    elif command == '/file':
        telegram_bot.sendDocument(chat_id, document = open('/home/pi/telebot.py'))
    elif command == '/audio':
        telegram_bot.sendAudio(chat_id, audio = open('/home/pi/radioactive.mp3'))
    elif command == '/obstacle':
        telegram_bot.sendMessage(chat_id, str("sending obstacleAvoidingRobot.py..."))
        telegram_bot.sendDocument(chat_id, document = open('/home/pi/US-test.py'))

    if 'on' in command:
        message = "Turned on "
        if 'green1' in command:
            message = message + "green1 "
            GO.output(green1, 1)
        if 'green2' in command:
            message = message + "green2 "
            GO.output(green2, 1)
        if 'both green' in command:
            message = message + "both green "
            GO.output(green1, 1)
            GO.output(green2, 1)
        if 'red1' in command:
            message = message + "red1 "
            GO.output(red1, 1)
        if 'red2' in command:
            message = message + "red2 "
            GO.output(red2, 1)
        if 'both red' in command:
            message = message + "both red "
            GO.output(red1, 1)
            GO.output(red2, 1)
        if 'all' in command:
            message = message + "all "
            GO.output(green1, 1)
            GO.output(green2, 1)
            GO.output(red1, 1)
            GO.output(red2, 1)
        message = message + "light(s)"
        telegram_bot.sendMessage(chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'green1' in command:
            message = message + "green1 "
            GO.output(green1, 0)
        if 'green2' in command:
            message = message + "green2 "
            GO.output(green2, 0)
        if 'both green' in command:
            message = message + "both green "
            GO.output(green1, 0)
            GO.output(green2, 0)
        if 'red1' in command:
            message = message + "red1 "
            GO.output(red1, 0)
        if 'red2' in command:
            message = message + "red2 "
            GO.output(red2, 0)
        if 'both red' in command:
            message = message + "both red "
            GO.output(red1, 0)
            GO.output(red2, 0)
        if 'all' in command:
            message = message + "all "
            GO.output(green1, 0)
            GO.output(green2, 0)
            GO.output(red1, 0)
            GO.output(red2, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage(chat_id, message)

    if 'flash' in command:
        message = "Flashing "
        if 'green1' in command:
            message = message + "green1 "
            for x in range(10):
                time.sleep(1)
                GO.output(green1, 1)
                time.sleep(1)
                GO.output(green1, 0)
        if 'green2' in command:
            message = message + "green2 "
            for x in range(10):
                time.sleep(1)
                GO.output(green2, 1)
                time.sleep(1)
                GO.output(green2, 0)
        if 'both green' in command:
            message = message + "both green "
            for x in range(10):
                time.sleep(1)
                GO.output(green1, 1)
                GO.output(green2, 1)
                time.sleep(1)
                GO.output(green1, 0)
                GO.output(green2, 0)
        if 'red1' in command:
            message = message + "red1 "
            for x in range(10):
                time.sleep(1)
                GO.output(red1, 1)
                time.sleep(1)
                GO.output(red1, 0)
        if 'red2' in command:
            message = message + "red2 "
            for x in range(10):
                time.sleep(1)
                GO.output(red2, 1)
                time.sleep(1)
                GO.output(red2, 0)
        if 'both red' in command:
            message = message + "both red "
            for x in range(10):
                time.sleep(1)
                GO.output(red1, 1)
                GO.output(red2, 1)
                time.sleep(1)
                GO.output(red1, 0)
                GO.output(red2, 0)
        if 'all' in command:
            message = message + "all "
            for x in range(10):
                time.sleep(1)
                GO.output(green1, 1)
                GO.output(green2, 1)
                GO.output(red1, 1)
                GO.output(red2, 1)
                time.sleep(1)
                GO.output(green1, 0)
                GO.output(green2, 0)
                GO.output(red1, 0)
                GO.output(red2, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage(chat_id, message)

    if 'status' in command:
        message = "The following lights are on: "
        message2 = "\nAnd the following lights are off: "
        if GO.input(green1) == 1:
            message = message + "green1 "
        else:
            message2 = message2 + "green1 "
        if GO.input(green2) == 1:
            message = message + "green2 "
        else:
            message2 = message2 + "green2 "
        if GO.input(red1) == 1:
            message = message + "red1 "
        else:
            message2 = message2 + "red1 "
        if GO.input(red2) == 1:
            message = message + "red2 "
        else:
            message2 = message2 + "red2 "
        telegram_bot.sendMessage(chat_id, message + message2)


telegram_bot = telepot.Bot('616590850:AAFMw21-ffhxjY9HfM5axCMY0ICozmuJ3fA')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running.....'
while 1:
    time.sleep(10)
    
