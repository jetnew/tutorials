# Python Telegram Bot Tutorial

Telegram is a chat messenging app (similar to WhatsApp) that is popular due to its stickers, bots and developer experience.

Telegram bots can be created for all kinds of apps: Poll creation (before polls were an in-built feature), the Werewolf game, to name a few.

## Quickstart
1. Get the access token from [BotFather](https://telegram.me/botfather) through the Telegram app.
2. To BotFather, send `/newbot`, `[bot name]`, and your bot will be found at `t.me/[bot name]`.
3. Refer to `bot.py` for a template that accepts commands and normal messages.
4. Remember to save the token as environment secrets or a separate file noted under `.gitignore`.
5. For example, `config.json` is added to `.gitignore`, and `bot.py` contains:

    ```python
    with open('config.json') as f:
        token = json.load(f)['token']
    ```
