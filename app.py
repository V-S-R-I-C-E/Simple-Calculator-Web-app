from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        operation = request.form.get("Operation", "")
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
        except ValueError:
                result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
