from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Application.builder().token("6964320831:AAFBM9kXZ5kSbY_1uGB_p-l92NHAJOORflo").build()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Запишите своего ребенка на вступительный экзамен и получите ответы на все вопросы!\n\n" 
        "В один клик! Просто заполните форму в чате, и мы сразу же зарезервируем место для вашего ребенка на экзамен и ответим на все ваши вопросы.\n\n"
        "Помощь --> Получите сопровождение ввиде сообщения"        
        )
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """
    /Помощь     --> Получите сопровождение ввиде сообщения
    /Инфо       --> Информация о учебном заведении и поступлении
    /Подача     --> Подайте документы своего сына в нашу школу
    /Контакты   --> Получите подробную консультацию
    """
        )
        

app.add_handler(CommandHandler("start", start))
app.run_polling()
