from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Remote',
    'salary': '35k-45k pounds'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': '35k-45k pounds'
}, {
    'id': 3,
    'title': 'Automation Engineer',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Data Engineer',
    'location': 'Remote',
    'salary': '35k-45k pounds'
}]


@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS, company_name='CodingBlues')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
