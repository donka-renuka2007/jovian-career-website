from flask import Flask, render_template, jsonify

app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Banglore, India',
    'salary':'Rs. 10,00,000'
  },
  {
      'id':2,
      'title':'Frontend Engineer',
      'location':'Hyderabad, India',
      'salary':'Rs. 20,00,000'
    },
    {
        'id':1,
        'title':'Backend Engineer',
        'location':'Mumbai, India',
      },
    {
        'id':1,
        'title':'Data Scientist',
        'location':'Banglore, India',
        'salary':'Rs. 10,00,000'
      }
]
@app.route("/")
def home():
  return render_template("home.html",jobs=JOBS,company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ in "__main__":
  app.run(debug=True)