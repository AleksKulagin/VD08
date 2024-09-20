from flask import Flask, render_template_string
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Выполняем запрос к API для получения случайной цитаты
    response = requests.get('https://api.quotable.io/random', verify=False)
    data = response.json()
    quote = data.get('content')
    author = data.get('author')

    # Создаем простую HTML-страницу с цитатой
    html_content = f"""
    <html>
    <head>
        <title>Случайная цитата</title>
    </head>
    <body>
        <h1>Случайная цитата</h1>
        <blockquote>
            <p>"{quote}"</p>
            <footer>- {author}</footer>
        </blockquote>
    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)