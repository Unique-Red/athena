api_key = "1905240420:AAEfKU7Pwf-VAAWoOLo4Q1JPl_EoQ-Agc-E"
from telegram.ext import *
import responses as r

print("Bot started...")

def start_command(update, context):
    update.message.reply_text("Hmm, Welcome!\nI was birthed out of an idea.\nAs the name implies 'Athena'. I am the greek goddess of knowledge, burdened with unending answers as regards Applied Psychology.\nHere to assist you with everything you may need to aid smooth learning.\n My creators the persons of Reddington & Chace built me to be your versatile friendly robot in 4 days!\n I can help you keep track of time and keep you up to date academically since that's what i was built for.\n \nSo, shall we begin?\nType your course code without space and without a slash'/'!")
def athena_command(update, context):
    update.message.reply_text("Hi, I'm Athena!\n Your versatile friendly robot.\nHere to assist you with everything you may need to aid smooth learning.\n \nSo, shall we begin?\nType your course code without space and with a (/)slash !")


def help_command(update, context):
    update.message.reply_text("If you need help! You should ask for it on Google!")

def crs146_command(update, context):
    update.message.reply_text("Introduction to African Traditional Religion.\nCOURSE OUTLINE\n146.01. What is ATR?\n- Why do we study ATR?\n146.02. Sources\n146.03. Terminologies used in describing ATR\n146.04. Problems facing the religion\n146.05. Structure of the religion\n-Features of ATR")
def crs120_command(update, context):
    update.message.reply_text("Introduction to Early Church.\nCOURSE OUTLINE\n120.01. Nature of the apostolic church\n120.02. Stages/phases of the history of the church (chronological)120.03. Stages 1 ad 30- ad 100(beginning and end of the apostolic church)\n120.04. Stage 2 ad 100- ad 313\n120.05. Stage 3 ad 313- ad 500")
def crs124_command(update, context):
    update.message.reply_text("Synoptic Gospels.\nCOURSE OUTLINE\n124.01. Introduction\n-Introduction of Synoptic Gospels\n124.02. Historical background to the life and teachings of Jesus Christ\n124.03. Preparation for the ministry\n124.04. Galilean ministry\n124.05. Teaching and preaching of Jesus Christ in Galilee\n124.06. Titles of Jesus Christ\n124.07. Parables of Jesus\n124.08. Miracles of Jesus\n124.09. Jesus and His disciples\n124.10. Passion of Narrative")

def edf123_command(update, context):
    update.message.reply_text("Psychoanalysis and measurement.\nCOURSE OUTLINE\n123.01. Definition of psychological test and impetus for psychological test.\n123.02. Arguments in favour and against the use of counselling \n123.03. General and specific uses of tests in counselling \n123.04. Classification of test\n-Achievement Test \n-Aptitude Test \n-Intelligence Test \n-Personality Test \nSocio metric Test\n123.05. Psychometric properties of tests \n(1)Reliability \n(2) validity \n(3) usability \n123.06. Test Administration: Definition, issues and guidelines \n123.07. Interpreting test results to clients \n123.08. Assessment of attitude and interest \n123.09. Ethical issues in psychological testing.")
def edf122_command(update, context):
    update.message.reply_text("Biological psychology.\nCOURSE OUTLINE\n122.01. The biological approach to behaviour\n-the fields of biological psychology.\n122.02.Nerve cells and nerve impulses\n-cells of the nervous system\n-the nerve impulse or impulses.\n122.03.Anatomy of the human brain\n-anatomy on psychology of man's brain.\n122.04. Genetics\n-evolution and development\n-medellian law of genetics\n-Gregory mendel, hereditary and environment.\n122.05. General principles of perception\n-anatomy of eyes\n-physiology of eyes and functions.\n122.06. Reproductive behaviour\n-childhood behaviour, organising sex hormones in male and female.\n122.07. Emotional behaviour\n-definition of emotion, function of emotion, emotion and moral decisions.\n122.08. Brain damage and its effects on human beings.\n122.09. Biology of learning and memory\n-defining of learning and types of memory.\n122.10. Psychological disorder\n-substance addiction and abuse, causes and its effects on young adults.")
def edf121_command(update, context):
    update.message.reply_text("Practices in Guidance and Counselling.\nCOURSE OUTLINE\n121.01. Conceptual definitions of guidance and counselling.\n121.02. The individual in situation.\n121.03. Psychoanalytic theory by Sigmund Freud.\n121.04. Person centered theory by Carl Rogers.\n121.05. Rational emotive behavioural theory by Herbert Ellis.\n121.06. Individual counselling \ individual therapy.\n121.07. Transactional analysis by Eric Ben.\n121.08. Traditional counselling or indigeneous counselling, and levels of counsellors participation.\n121.09. Case studies.")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("athena", athena_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("edf121", edf121_command))
    dp.add_handler(CommandHandler("edf122", edf122_command))
    dp.add_handler(CommandHandler("edf123", edf123_command))
    dp.add_handler(CommandHandler("crs120", crs120_command))
    dp.add_handler(CommandHandler("crs124", crs124_command))
    dp.add_handler(CommandHandler("crs146", crs146_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()