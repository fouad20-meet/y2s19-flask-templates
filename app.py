from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	opposite_day = True
	pets = ["food1", "food2", "food3"] 
	foods = ["nofood1","nofood2","nofood3"]
	return render_template(
					"index.html",
					pets=pets, foods = foods)



if __name__ == '__main__':
   app.run(debug = True)
