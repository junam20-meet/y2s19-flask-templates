from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	food=["mlokhieh","chocolate","pasta","wara2"]
	oppoeite_day = True
	least_foods=["fish","shrimp"]
	return render_template("index.html",foods = food, least = least_foods, oppoeite_day = oppoeite_day)



if __name__ == '__main__':
   app.run(debug = True)
