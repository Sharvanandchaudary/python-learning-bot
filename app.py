from flask import Flask, render_template, request, redirect
from models import db, UserProgress
from flask_migrate import Migrate
from problem_generator import generate_problem
from algorithm_guide import get_algorithm
from data_structure_guide import get_data_structure
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///progress.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize migration
migrate = Migrate(app, db)

@app.route('/')
def home():
    problem = generate_problem()  # Generate the daily problem
    completion_status = "Not Completed"  # Set default completion status
    return render_template('index.html', problem=problem, completion_status=completion_status)

@app.route('/daily-challenge')
def daily_challenge():
    problem = generate_problem()  # Get the daily problem
    algorithm = get_algorithm()  # Get the algorithm of the day
    data_structure = get_data_structure()  # Get the data structure of the day
    completion_status = "Not Completed"  # Set default completion status
    return render_template('problem.html', 
                           problem=problem, 
                           algorithm=algorithm, 
                           data_structure=data_structure, 
                           completion_status=completion_status)

@app.route('/submit-progress', methods=['POST'])
def submit_progress():
    user = request.form['user']
    date = datetime.date.today()
    progress = UserProgress(user=user, date=date)
    db.session.add(progress)
    db.session.commit()
    return redirect('/progress')

@app.route('/progress')
def progress():
    all_progress = UserProgress.query.all()
    return render_template('progress.html', progress=all_progress)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

