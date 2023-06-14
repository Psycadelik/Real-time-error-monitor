import vonage
from dotenv import dotenv_values

config = dotenv_values(".env")
client = vonage.Client(key=config["VONAGE_API_KEY"], secret=config["VONAGE_API_SECRET"])


def send_alert(message):
    return client.messages.send_message(
        {
            "channel": "sms",
            "message_type": "text",
            "from": config["VONAGE_SENDER"],
            "to": config["RECIPIENT"],
            "text": f"{message}",
        }
    )
