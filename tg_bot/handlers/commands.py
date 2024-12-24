from aiogram import Router, types
from aiogram.filters import Command
from users import User

router = Router()
users = {}

@router.message(Command('start')) 
async def start(message: types.Message):
    await message.reply("Привет! Я бот для управления личным бюджетом."
                        '''
            Используйте команду /income для добавления дохода.
            Используйте команду /expense для добавления расходов.
            Используйте команду /balance для просмотра баланса.
            Используйте команду /report для просмотра трат.
    
    ''')                    

@router.message(Command('income'))  
async def income(message: types.Message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = User(user_id)

    try:
        
        args = message.text.split()[1:]  
        amount = float(args[0])  
        description = ' '.join(args[1:])  

        users[user_id].add_income(amount, description)
        await message.reply(f'Доход добавлен: {description} - {amount}.\nТекущий баланс: {users[user_id].get_balance()}')
    except (IndexError, ValueError):
        await message.reply('Пожалуйста, введите сумму и описание дохода в формате: /income "сумма" "описание".')

@router.message(Command('balance'))  
async def balance(message: types.Message):
    user_id = message.from_user.id
    if user_id in users:
        await message.reply(f'Ваш текущий баланс: {users[user_id].get_balance()}')
    else:
        await message.reply('Вы еще не добавили никакого дохода. Используйте команду /income.')


@router.message(Command('expense'))  
async def expense(message: types.Message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = User(user_id)

    try:

        args = message.text.split()[1:]
        amount = float(args[0])  
        description = ' '.join(args[1:])  

        users[user_id].add_expense(amount, description)  
        await message.reply(f'Расход добавлен: {description} - {amount}.\nТекущий баланс: {users[user_id].get_balance()}')
    except (IndexError, ValueError):
        await message.reply('Пожалуйста, введите сумму и описание расхода в формате: /expense "сумма" "описание".')

@router.message(Command('report'))  
async def report(message: types.Message):
    user_id = message.from_user.id
    if user_id in users:
        balance = users[user_id].get_balance()
        income_report = users[user_id].get_income_report()  
        expense_report = users[user_id].get_expense_report()  

        report_message = f'Ваш текущий баланс: {balance}\n\nДоходы:\n{income_report}\n\nРасходы:\n{expense_report}'
        await message.reply(report_message)
    else:
        await message.reply('Вы еще не добавили никаких доходов или расходов. Используйте команду /income для добавления дохода и /expense для добавления расхода.')