ScrapeFlow AI

ScrapeFlow AI is a Django-based web application designed for automated scraping, content scheduling, and multi-platform publishing. It allows users to collect data and seamlessly publish to LinkedIn, Meta (Facebook, Threads), and Telegram — all without writing a single line of code.

🚀 Features
	•	No-Code Automation: Create and manage web scrapers with a clean and intuitive UI.
	•	Smart Scheduling: Schedule publishing at optimal times with built-in Celery + Redis.
	•	Real-time Dashboard: View scraping status and publishing activity live.
	•	Cloud Storage: Save and access scraped content securely.
	•	Multi-Platform Publishing: Instantly publish content to LinkedIn, Meta, and Telegram.
	•	Telegram Integration: Send AI-enhanced content directly to Telegram channels or groups.
	•	AI-Powered Optimization: Use DeepSeek AI for summarization or enhancement before publishing.

🎥 Watch the demo: ScrapeFlow AI on YouTube

⸻

⚙️ Setup
	1.	Clone the repository:

git clone https://github.com/ArtTheAche98/ScrapeFlowAI.git
cd personal


	2.	Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate


	3.	Install dependencies:

pip install -r requirements.txt


	4.	Configure environment variables:
Create a .env file and add:

LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
META_CLIENT_ID=your_meta_client_id
META_CLIENT_SECRET=your_meta_client_secret
DEEPSEEK_API_KEY=your_deepseek_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id


	5.	Apply migrations and collect static files:

python manage.py migrate
python manage.py collectstatic


	6.	Run Redis (required for Celery):

brew services start redis
# or manually:
redis-server


	7.	Start Celery worker and beat scheduler:

celery -A personal worker --loglevel=info
celery -A personal beat --loglevel=info


	8.	Run the development server:

python manage.py runserver 8080



⸻

🧑‍💻 Usage
	•	Register or log in to your account.
	•	Set up scraping tasks and schedule them.
	•	Connect your LinkedIn, Meta, and Telegram accounts.
	•	Enable AI-enhancement (optional).
	•	View logs and results in the real-time dashboard.

⸻

🗂 Project Structure

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
├── manage.py
├── requirements.txt
└── README.md


⸻

🔐 Environment Variables

Variable	Description
LINKEDIN_CLIENT_ID	LinkedIn API Client ID
LINKEDIN_CLIENT_SECRET	LinkedIn API Client Secret
META_CLIENT_ID	Meta (Facebook/Threads) Client ID
META_CLIENT_SECRET	Meta Client Secret
DEEPSEEK_API_KEY	API key for DeepSeek (AI processing)
TELEGRAM_BOT_TOKEN	Telegram bot token
TELEGRAM_CHAT_ID	Chat/group ID(s) for Telegram posting


⸻

📢 Telegram Integration

ScrapeFlow AI supports full Telegram integration. Add your bot token and chat ID on the settings page to post scraped or AI-generated content to Telegram channels or groups in real time.

⸻

📄 License

MIT Licens

⸻

Let me know if you want to:
	•	Add contributor credits
	•	Include deployment instructions (e.g. Docker, Azure)
	•	Add badges (CI, license, stars)
	•	Link to your LinkedIn/GitHub profile
