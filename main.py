import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))
    if not secret_number:
        secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(secret))

    return response


@app.route("/success", methods=["POST"])
def success():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Correct! The secret number is " + str(secret_number)
        response = make_response(render_template("success.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif guess > secret_number:
        message = "Your guess is not correct...try something smaller."
        return render_template("success.html", message=message)
    elif guess < secret_number:
        message = "Your guess is not correct...try something bigger."
        return render_template("success.html", message=message)

    return render_template (success.html)


if __name__ == '__main__':
    app.run()

