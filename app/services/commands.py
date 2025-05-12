from app.chatbot import send_chat_message

COMMAND_PREFIX = "!"


async def handle_command(message: str, username: str):
    if not message.startswith(COMMAND_PREFIX):
        return  # Ignore nom commands

    command = message[len(COMMAND_PREFIX):].strip().lower()

    if command == "hello":
        await send_chat_message(
            f"Hi, @{username}! 👋"
        )
    elif command == "piada":
        await send_chat_message(
            "Put a good joke here."
        )
    else:
        await send_chat_message(
            f"Is !{command} not a command, @{username}."
        )
