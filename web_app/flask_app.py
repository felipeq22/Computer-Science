#command:
#python3 -m flask --app flask_app.py run --debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about")
def home():
    return render_template(
        'about.html', 
        heading="Juan Felipe Quiñones",
        image_url="images/photo3.png",
        description=(
            "Hi, I'm Juan, a Data Scientist currently doing a Master's of Data Science at Hertie School in Berlin. "
            "I love generating data-driven insights for social and governmental issues. "
            "Passionate about Python, AWS, and applying machine learning in impactful ways."
        ),
        subtitle = ('I like Artificial Intelligence, Football and Drones. '
                    'Currently living in Berlin, Germany'           
        ),
        linkedin_url="https://www.linkedin.com/in/juan-quinones22/"
    )

if __name__ == '__main__':
    app.run(debug=True)