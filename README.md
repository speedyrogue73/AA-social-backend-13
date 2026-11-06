# AA Social Backend 13

A Django backend application for social features and user management.

## Project Structure

```text
AA-social-backend-13/
│
├── AA/
│   ├── accounts/           # User authentication and profile management
│   ├── AA/                 # Core project configuration (settings, urls, wsgi, asgi)
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Project dependencies
│
├── requirements.txt        # Environment dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/speedyrogue73/AA-social-backend-13.git
cd AA-social-backend-13
```

### 2. Create and activate a virtual environment
```bash
# On Windows
python -m venv env
.\env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python AA/manage.py migrate
```

### 5. Start the development server
```bash
python AA/manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

