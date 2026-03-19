# WhatsApp Message Bot

A simple Python bot that sends WhatsApp messages instantly using [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit). Configure the recipient and message in a separate text file—no need to edit the code.

## How It Works

- Reads the phone number and message from `config.txt`
- Opens WhatsApp Web in your browser and sends the message automatically
- Uses browser automation (no official WhatsApp API)

## Requirements

- Python 3.x
- Chrome browser
- WhatsApp account (logged in at [web.whatsapp.com](https://web.whatsapp.com))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/whatsapp-bot.git
   cd whatsapp-bot
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.txt` with your settings:

```
# Line 1: phone number (e.g. +54912345678)
# Line 2 onwards: message
# ----------------------------------

+54912345678
Hello, write your message here
```

- **Line 1:** Phone number with country code (e.g. `+54912345678`)
- **Lines 2+:** Message to send (supports multiple lines)
- Lines starting with `#` are ignored

## Usage

1. Make sure you're logged into WhatsApp Web in your browser (scan the QR code if needed)
2. Edit `config.txt` with the recipient number and message
3. Run the bot:
   ```bash
   python bot1.py
   ```

The script will open Chrome, navigate to WhatsApp Web, and send the message. Keep the machine on and don't minimize the browser until the message is sent.

## Project Structure

```
botwhatsapp1/
├── bot1.py       # Main script
├── config.txt    # Configuration (number + message)
└── README.md     # This file
```

## Limitations

- Works only with **WhatsApp Web** (browser), not the desktop or mobile app
- Uses your system's local timezone
- Keep the computer awake and the browser visible until the message is sent
- Suitable for low volume (recommended: 5–30 messages per day)

## License

MIT
