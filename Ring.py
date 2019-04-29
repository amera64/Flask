from ring_doorbell import Ring
from flask import Flask, render_template

myring = Ring('amera64@comcast.net', 'Malibu2515!')

app = Flask(__name__)

@app.route("/")
def home():
    for doorbell in myring.doorbells:
        # listing the last event of any kind
        for event in doorbell.history(limit=1):
            return render_template('index.html', id=event['id'], kind=event['kind'], answered=event['answered'], created_at=event['created_at'])

        # get a event list only the triggered by motion
        events = doorbell.history(kind='motion')


if __name__ == "__main__":
    app.run(host='0.0.0.0' debug=True)

