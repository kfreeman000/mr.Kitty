from flask import Flask, request, render_template, jsonify
import objects
from openai import OpenAI

app = Flask(__name__)
a_list = []
api_key = ""
client = OpenAI(api_key=api_key)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.json
        user_input = data.get('user_input')
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot to assist with music and related questions. You "
                                              "specialize in the artist Mr. Kitty. A user can submit forms under the "
                                              "'engage' tab. Be friendly and silly. Kat Freeman is the creator of you "
                                              "and the website."},
                {"role": "user", "content": user_input}
            ]
        )
        bot_response = completion.choices[0].message.content
        return jsonify({'bot_response': bot_response})
    return render_template('mrkitty.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/engage')
def engage():
    return render_template('engage.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/songform')
def song():
    return render_template('songform.html')


@app.route('/feedbackform')
def fb():
    return render_template('feedbackform.html')


@app.route('/albumform')
def album():
    return render_template('albumform.html')


@app.route('/socialform')
def social():
    return render_template('socialform.html')


@app.route('/submission', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        name = request.form.get('name')
        album = request.form.get('album')
        song = request.form.get('song')
        email = request.form.get('email')
        form_comments = request.form.get('comments')
        like = request.form.get('like')
        dislike = request.form.get('dislike')
        some_data = objects.ReadUserData(name, email, form_comments, like, dislike, album, song)
        some_data.append_to_file()
    return render_template('submission.html')


if __name__ == '__main__':
    app.run(debug=True)     # after code is stopped, a list of students with an IC
    # email who submitted  form will print
    ic_students = objects.SearchAndSort.search_for_ic_students()
    print(ic_students)


