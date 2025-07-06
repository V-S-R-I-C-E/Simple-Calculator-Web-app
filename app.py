from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        operation = request.form.get("Operation", "")
        round_places = request.form.get("round_places")

        if operation == "Round":
            try:
                last_result = session.get("last_result")
                if last_result is not None and round_places != "":
                    last_result = float(last_result)
                    round_places = int(round_places)
                    result = round(last_result, round_places)
                    session["last_result"] = result
                else:
                    result = "Nothing to round."
            except (ValueError, TypeError):
                result = "Invalid rounding input."
        else:
            try:
                num1 = float(request.form["num1"])
                num2 = float(request.form["num2"])

                if operation == "Add":
                    result = num1 + num2
                elif operation == "Subtract":
                    result = num1 - num2
                elif operation == "Multiply":
                    result = num1 * num2
                elif operation == "Divide":
                    result = num1 / num2 if num2 != 0 else "Error (Divide by 0)"
                elif operation == "Power":
                    result = num1 ** num2

                if isinstance(result, (int, float)):
                    session["last_result"] = result
            except ValueError:
                result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
