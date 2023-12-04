import telebot


bot = telebot.TeleBot('')


recipes = {'паста карбонара': 'ИНГРИДИЕНТЫ: (2 порции):\n 160 г Спагетти\n 2 яичных желтка\n 60 г сыра\n 80г сырокопченой грудинки\n соль и молотый черный перец по вкусу\n'
                              'РЕЦЕПТ:\n'
                              '1)В кипящей подсоленной воде отварите Спагетти 10 минут до состояния аль денте.\n'
                              '2)Отделите желтки от белков. Смешайте желтки с натертым на мелкой терке сыром и черным перцем, взбейте до однородной массы.\n'
                              '3)Обжарьте на небольшом количестве оливкового масла нарезанную кубиками грудинку.\n'
                              '4)Добавьте готовую пасту к грудинке, перемешайте.\n'
                              '5)Полейте пасту смесью желтков, сыра и черного перца, перемешайте.\n'
                              '6)Перед подачей посыпьте молотым черным перцем.',
    'суп борщ': 'ИНГИДИЕНТЫ: \n'
           'Говядина - 500 г\n'
           'Свёкла - 1 шт.\n'
           'Картофель - 2 шт.\n'
           'Капуста белокочанная - 200 г\n'
           'Морковь - 1 шт.\n'
           'Лук репчатый - 1 шт.\n'
           'Томатная паста - 1 ст. ложка\n'
           'Масло растительное - 2 ст. ложки\n'
           'Уксус - 1 ч. ложка\n'
           'Лавровый лист - 1 шт.\n'
           'Перец чёрный горошком - 2-3 шт.\n'
           'Соль - 2 ч. ложки (по вкусу)\n'
           'Вода - 1,5 л\n'
           'Зелень укропа и/или петрушки (для подачи) - 3-4 веточки\n'
           'Сметана (для подачи) - 2 ст. ложки\n'
           'РЕЦЕПТЫ:\n'
           '1)Подготовить продукты: нарезать мясо и овощи\n'
           '2)На сковороде разогреть растительное масло. Свёклу, морковь и лук выложить на сковороду и тушить на среднем огне (пассеровать), помешивая, 5-7 минут\n'
           '3)В конце добавить уксус и томатную пасту. Перемешать. Готовить овощи ещё 3-4 минуты, помешивая.\n'
           '4)В кипящий бульон выложить картофель и капусту, варить 10 минут. (Молодую капусту добавлять за 5 минут до окончания приготовления борща.)\n'
           '5)Затем добавить пассерованные овощи, лавровый лист и перец. Варить борщ с говядиной еще 5-7 минут.\n',
           'салат цезарь': 'ИНГРИДИЕНТЫ:\n'
                           'Грудка куриная - 1 шт. (400 г)\n'
                           'Капуста пекинская - 1 шт.\n'
                           'Помидоры черри - 150-200 г\n'
                           'Сыр твердый (желательно пармезан) - 50-70 г\n'
                           'Хлеб белый - 3-4 ломтика\n'
                           'Соль - по вкусу\n'
                           'Масло оливковое - 6 ст.л. (для жарки)\n'
                           'Перец черный молотый - 1 ч.л.\n'
                           'Чеснок - 4 зубчика\n'
                           'Майонез - 3-4 ст.л.\n'
                           'РЕЦЕПТ:\n'
                           'Помыть и очистить от пленок и лишнего жира куриную грудку. Нарезать ее на куски шириной 3 см поперек филе\n'
                           'Разогреть сковороду с 2 ст.л. оливкового масла. Обжарить с двух сторон курицу до готовности (7-10 минут).\n'
                           'Взять другую сковороду для обжаривания сухарей\n'
                           'Нарезать курицу, салат и помидоры\n'
                           'Смешать 2 измельченных зубчика чеснока, соль и майонез. Это и будет заправка для салата.\n'
                           'Все перемешать и можно есть\n'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я помощник по рецептам и приготовлению блюд. Пожалуйста, введите название блюда: '
                          'паста карбонара, '
                          'суп борщ, '
                          'салат цезарь.')




def browse_recipes(message):
    bot.reply_to(message, 'Список рецептов: паста карбонара, суп борщ, салат цезарь')

@bot.message_handler(func=lambda message: True)
def send_recipe(message):
    dish = message.text.lower()
    if dish in recipes:
        bot.reply_to(message, f'Рецепт для блюда "{dish}": {recipes[dish]}')
    else:
        bot.reply_to(message, f'Извините, рецепт для блюда "{dish}" не найден.')

bot.polling()
