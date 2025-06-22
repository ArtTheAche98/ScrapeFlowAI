# ScrapeFlow AI

ScrapeFlow AI is a Django-based web application for scheduling, scraping, and publishing content to social platforms like LinkedIn, Meta (Facebook, Threads), and Telegram.

## Features

- **No-Code Automation:** Easily set up and manage scrapers with an intuitive interface.
- **Smart Scheduling:** Automate content publishing with flexible scheduling.
- **Real-time Dashboard:** Monitor your scrapers and data in real-time.
- **Cloud Storage:** Securely store and access your data.
- **Multi-Platform Publishing:** Publish scraped content to LinkedIn, Meta, and Telegram.
- **Telegram Integration:** Send scraped and optimized content directly to Telegram channels or groups.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ArtTheAche98/ScrapeFlowAI.git
   cd personal
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create `.env` and fill in your API keys and secrets:
     ```
     LINKEDIN_CLIENT_ID=your_linkedin_client_id
     LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
     META_CLIENT_ID=your_meta_client_id
     META_CLIENT_SECRET=your_meta_client_secret
     DEEPSEEK_API_KEY=your_deepseek_api_key
     ```

5. **Apply migrations and collect static files:**
   ```sh
   python manage.py migrate
   python manage.py collectstatic
   ```

6. **Run Redis (for Celery):**
   ```sh
   brew services start redis
   # or
   redis-server
   ```

7. **Start Celery worker and beat:**
   ```sh
   celery -A personal worker --loglevel=info
   celery -A personal beat --loglevel=info
   ```

8. **Run the development server:**
   ```sh
   python manage.py runserver 8080
   ```

## Usage

- Register a new user or log in.
- Create scraping schedules from the dashboard.
- Connect your LinkedIn, Meta, and Telegram accounts in settings.

## Project Structure

```
personal/
├── personal/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── scraper/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tasks.py
│   ├── views.py
│   ├── templates/
│   │   └── scraper/
│   │       ├── dashboard.html
│   │       ├── index.html
│   │       ├── linkedin_settings.html
│   │       ├── telegram_settings.html
│   │       └── register.html
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## Environment Variables

| Variable                | Description                       |
|-------------------------|-----------------------------------|
| LINKEDIN_CLIENT_ID      | LinkedIn API client ID            |
| LINKEDIN_CLIENT_SECRET  | LinkedIn API client secret        |
| META_CLIENT_ID          | Meta (Facebook) API client ID     |
| META_CLIENT_SECRET      | Meta (Facebook) API client secret |
| DEEPSEEK_API_KEY        | DeepSeek API key                  |
| TELEGRAM_BOT_TOKEN      | Telegram bot token                |
| TELEGRAM_CHAT_ID        | Telegram chat/group ID(s)         |

## License

MIT License

---

**Note:** Telegram integration is now supported. You can connect your Telegram bot and chat IDs in the settings page to enable automated posting. Contributions are welcome!
