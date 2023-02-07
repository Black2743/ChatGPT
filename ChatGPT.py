import openai
import logging
import telegram
from telegram.update import Update
# Set up logging
logging.basicConfig(level=logging.INFO)
# Set up the OpenAI API client
openai.api_key = "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"
# Set up the Telegram API client
bot = Updater("5972044151:AAGocm3kJ1gWnbNi0dUhIaQIWobFNrC1M3c",use_context=True)

def handle_update(update):
  # Log the update
  logging.info("Received update: %s", update)
  # Get the message text and sender from the update
  text = update.message.text
  sender = update.message.from_user
  # Use the OpenAI API to generate a response
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
  )
  # Log the response
  logging.info("Generated response: %s", response.text)
  # Send the response back to the sender
  bot.send_message(chat_id=sender.id, text=response.text)
# Set the update handler to our function
bot.set_update_handler(handle_update)
# Start the bot
bot.start_polling()
