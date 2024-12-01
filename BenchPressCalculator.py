from flask import Flask, render_template, request

BenchPressCalculator = Flask(__name__)


def calculate(weight, repetitions):
    epley = (weight * repetitions) / 30 + weight
    mattBrzycki = weight * (36 / (37 - repetitions))
    lander = (100 * weight) / (101.3 - 2.67123 * repetitions)
    oConner = weight *  (1 + 0.025 * repetitions)
    finalBenchPress = (epley + mattBrzycki + lander + oConner) / 4
    return epley, mattBrzycki, lander, oConner, finalBenchPress



@BenchPressCalculator.route("/", methods=["GET", "POST"])
@BenchPressCalculator.route("/index", methods=["GET", "POST"])


def index():
    result = {'epley': '-', 'mattBrzucki': '-', 'lander': '-', 'oConner': '-', 'finalBecnhPress': '-'}
    weight = "-"
    repetition = "-"

    if request.method == 'POST':
        try:
            weight = float(request.form["working-weight"])
            repetition = int(request.form["working-repetition"])
            epley, mattBrzycki, lander, oConner, finalBenchPress = calculate(weight, repetition)
            result = {'epley': int(epley), 'mattBrzucki': int(mattBrzycki), 'lander': int(lander), 'oConner':int(oConner), 'finalBecnhPress':int(finalBenchPress)}
            
        except:
            print("Произошла ошибка")
    
    # if request.method == 'GET':
    #     return render_template("index.html")

    return render_template("index.html", result=result, weight=weight, repetition=repetition)


if __name__ == "__main__":
    BenchPressCalculator.run(debug=True)
