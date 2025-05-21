if __name__ == "__main__":

    import schedule
    import time
    from app import WhatsAppBotApp

    def job():
        app = WhatsAppBotApp()
        text = app.get_top_deals()
        app.send_test_message(text)

    schedule.every().day.at("09:00").do(job)

    print("Bot agendado para enviar promoções todos os dias às 09:00.")

    while True:
        schedule.run_pending()
        time.sleep(60)