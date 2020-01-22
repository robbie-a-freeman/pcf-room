from flask import Flask
app = Flask(__name__)

isOpen = False

@app.route('/')
def home():
    answer = '<p style="color:red;">not right now. Check back later!</p>'
    if isOpen:
        answer = '<p style="color:green;">yes it is! Stop on by!</p>'
    return ' '.join(['<h1>','Is Spelman 43 open currently? The answer is:', answer, '</h1>'])

@app.route('/changeStatus')
def changeStatus():
    global isOpen
    current = not isOpen
    isOpen = current
    return 'Successfully changed status'
    
if __name__ == "__main__":
    app.run()