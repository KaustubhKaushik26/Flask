from flask import Flask, render_template, url_for
app = Flask(__name__)

# code snippets: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets

posts = [
    {
        'author': 'cory shafer',
        'title': 'Blog Post 1',
        'content': 'This is the content of the first blog post.',
        'date_posted': 'April 20, 2023'
    }, 
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is the content of the second blog post.',
        'date_posted': 'April 21, 2023'
    }
    
]


# home and normally / pe bhi chalega
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts) # posts variable is passed to the template

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)


