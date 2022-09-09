from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-temp-secret-key"

debug = DebugToolbarExtension(app)


@app.route("/")
def show_home():
    return render_template("home.html", stories=stories.stories.keys())


@app.route("/form")
def show_form():
    story_code = request.args.get("story")
    story = stories.stories[story_code]
    return render_template("form.html", story=story)


@app.route("/story/<code>")
def show_story(code):
    story = stories.stories[code]
    generated_story = story.generate(request.args)
    return render_template("story.html", story=generated_story, code=code)
