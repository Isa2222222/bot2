import telebot
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of TOKEN from the environment
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Google Sheets credentials setup
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Islam/Desktop/project/google_credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open("Telegram Bot Responses").sheet1

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        """
        В один клик! Просто заполните форму в чате, и мы сразу же зарезервируем место для вашего ребенка на экзамен и ответим на все ваши вопросы.
        
        /start     --> Получите сопровождение ввиде сообщения
        /help       --> Информация о учебном заведении и поступлении
        /apply     --> Подайте документы своего сына в нашу школу
        /contacts   --> Получите подробную консультацию
        """
        )

@bot.message_handler(commands=['apply'])
def ask_questions(message):
    bot.reply_to(message, 
        """
        Подайте документы своего сына в нашу школу
        
        Введите имя:
        """
    )
    bot.register_next_step_handler(message, process_name_step)

def process_name_step(message):
    message_name = message.text
    # Store the name in Google Sheet
    sheet.append_row(["Name", message_name])
    
    bot.reply_to(message, "Введите фамилию:")
    bot.register_next_step_handler(message, process_surname_step)

def process_surname_step(message):
    message_surname = message.text
    # Store the surname in Google Sheet
    sheet.append_row(["Surname", message_surname])
    
    bot.reply_to(message, "Введите дату рождения:")
    bot.register_next_step_handler(message, process_dob_step)

def process_dob_step(message):
    dob = message.text
    # Store the date of birth in Google Sheet
    sheet.append_row(["Date of Birth", dob])
    
    bot.reply_to(message, "Введите номер телефона:")
    bot.register_next_step_handler(message, process_phone_step)

def process_phone_step(message):
    phone = message.text
    # Store the phone number in Google Sheet
    sheet.append_row(["Phone Number", phone])
    
    bot.reply_to(message, "Спасибо! Ваши данные были успешно сохранены.")

bot.polling(none_stop=True)