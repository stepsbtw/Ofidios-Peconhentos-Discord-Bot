import bot
from tensorflow.keras.models import load_model

if __name__ == '__main__':
    modelo = load_model("modelo1.h5")
    bot.run_discord_bot()

