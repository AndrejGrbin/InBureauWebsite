from flask import Flask, render_template
from wtfforms.widgets import TextArea


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# Create a blog post model

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Srting(255))
	content = db.Column(db.Text)
	author = db.Column(db.String(255))
	date_posted = db.Column(db.DateTime, default=datetime.utcnow)
	slug = db.Column(db.String(255))

# Create a Post Form
class PostForm(FlakForm):
	title = StringField("Title") #još fali kontrola
	content = StringField("Content")
	author = StringField("Author")
	slug = StringField()
	submit = SubmitField("Submit")





@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
	form = PostForm()






if __name__ == '__main__':
	app.run(debug=True)