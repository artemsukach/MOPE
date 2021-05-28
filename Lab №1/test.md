# Documentation

## `const answer = require('.`

 * **Alias:** Підключення бібліотек TG і wit.ai

     Підключаємо node-telegram-bot-api для роботи телеграм-бота

     Підключаємо node-wit для роботи з wit.ai

## `const TG_TOKEN = '1860742369:AAGgci2FYZxFTfhR3SParu8nXroVk_YSKP4'`

 * **Alias:** Включаємо бота
 * **Parameters:** `TG_TOKEN` — `string` — Токен телеграм-бота

## `const WIT_TOKEN = 'ITXQFSJKZ4752LRXHQ7YPMBZGB3CWAD7'`

З'єднання по токену з ботом WIT

 * **Alias:** З'єднання
 * **Parameters:** `WIT_TOKEN` — `string` — Токен wit.ai

## `bot.onText(`

Функція виклику допомоги

 * **Author:** Artem
 * **Parameters:** `msg` — фраза

## `const validator = function(user_text)`

 * **Alias:** Валідатор

     Перевірка на валідність введених значень

## `bot.on('message', (msg) =>`

 * **Alias:** Обробник

     Обробник події надсилання будь-якого повідомлення

     За допомогою метода .chat.id отримуємо ідентифікатор діалогу, щоб відповідати саме тому користувачеві, який нам щось надіслав
 * **Parameters:** `chatId` — чату

## `client.message(msg.text,`

 * **Alias:** Відправка

     Відправлення повідовлення на wit.ai для подальшої обробки та отримання результату аналізу

     JSON.parse () розбирає рядок JSON
