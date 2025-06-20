# NOTE: AI GENERATED JUST TO PRACTICE RAILWAY

from flask import Flask, render_template_string
import sqlite3
import os

# Load environment variables
user = os.environ.get('user', 'not set')
password = os.environ.get('password', 'not set')

# Print to command line
print(f"User from env: {user}")
print(f"Password from env: {password}")

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Contestants</title>
    <style>
        table { border-collapse: collapse; width: 80%; margin: 20px auto; }
        th, td { border: 1px solid #000; padding: 8px; text-align: center; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">Contestant List</h2>
    <div style="text-align:center; margin-bottom: 20px;">
        <strong>User from env:</strong> {{ user }}<br>
        <strong>Password from env:</strong> {{ password }}
    </div>
    <table>
        <tr>
            {% for header in headers %}
                <th>{{ header }}</th>
            {% endfor %}
        </tr>
        {% for row in rows %}
        <tr>
            {% for item in row %}
                <td>{{ item }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def index():
    conn = sqlite3.connect('contests.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM contests")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    conn.close()
    return render_template_string(HTML_TEMPLATE,
                                  headers=headers,
                                  rows=rows,
                                  user=user,
                                  password=password)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
