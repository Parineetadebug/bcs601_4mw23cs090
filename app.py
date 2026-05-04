from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


@app.route("/", methods=["GET", "POST"])
def home():
    result = {}

    if request.method == "POST":
        number = int(request.form["number"])
        text = request.form["text"]

        result["even_odd"] = "Even" if number % 2 == 0 else "Odd"
        result["prime"] = "Prime" if is_prime(number) else "Not Prime"
        result["reverse_number"] = str(number)[::-1]

        vowels = "aeiouAEIOU"
        count = sum(1 for ch in text if ch in vowels)

        result["vowel_count"] = count
        result["upper"] = text.upper()
        result["lower"] = text.lower()
        result["reverse_text"] = text[::-1]

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
