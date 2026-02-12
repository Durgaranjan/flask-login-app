from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '123':
            session['user'] = username
            return redirect(url_for('welcome'))
        else:
            error = "Invalid username or password"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
            }}
            .login-box {{
                width: 350px;
                margin: 100px auto;
                padding: 25px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h2 {{
                text-align: center;
                margin-bottom: 20px;
            }}
            input[type=text], input[type=password] {{
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }}
            input[type=submit] {{
                width: 100%;
                padding: 10px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            input[type=submit]:hover {{
                background: #0056b3;
            }}
            .error {{
                color: red;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>Login</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Login">
            </form>
            <p class="error">{error}</p>
        </div>
    </body>
    </html>
    """


@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Welcome</title>
            <style>
                body {{
                    font-family: Arial;
                    background: #e9ecef;
                    text-align: center;
                    padding-top: 100px;
                }}
                .box {{
                    background: white;
                    display: inline-block;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                a {{
                    display: inline-block;
                    margin-top: 15px;
                    text-decoration: none;
                    color: white;
                    background: #dc3545;
                    padding: 10px 20px;
                    border-radius: 4px;
                }}
            </style>
        </head>
        <body>
            <div class="box">
                <h2>Welcome, {session['user']} 👋</h2>
                <a href="{url_for('logout')}">Logout</a>
            </div>
        </body>
        </html>
        """
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
