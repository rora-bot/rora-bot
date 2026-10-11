
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Rora FUHSI Biochemistry Class Of 2026 Bot is LIVE! 💚🧬"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
