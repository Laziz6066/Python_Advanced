from flask import Flask, request

app = Flask(__name__)


@app.route('/logs', methods=['POST'])
def receive_logs():
    log_data = request.get_json()
    # Process the log data as needed
    print(log_data)  # Example: Print the log data
    return 'Logs received successfully'


if __name__ == '__main__':
    app.run()
