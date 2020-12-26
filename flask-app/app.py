from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media1.popsugar-assets.com/files/thumbor/8xugn8tUReUIM-P_T8bkjdhe0xc/fit-in/728xorig/filters:format_auto-!!-:strip_icc-!!-/2019/06/05/869/n/43879538/e754d6485cf81d3d31bd40.89484858_/i/Dark-Sides-Zodiac-Signs.jpg",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
