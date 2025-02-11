import os
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('your_database.db')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
