
from routes import app
app.secret_key = 'qazwsxedcrfv'

if __name__ == '__main__':
    app.run(debug=True)
