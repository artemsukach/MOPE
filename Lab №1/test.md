/**
* @name Обробник
* Обробник події надсилання будь-якого повідомлення
* За допомогою метода .chat.id отримуємо ідентифікатор діалогу, щоб відповідати саме тому користувачеві, який нам щось надіслав
* @param chatId Ідентифікатор чату
*/

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
