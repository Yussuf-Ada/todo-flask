from app import app

@app.route('/')
def index():
    return "<h1>Todo index page</h1>"

@app.route('/tasks')
def all_tasks():
    return "<h1> List of all tasks </h1>"

@app.route('/task/<int:task_id>')
def task(task_id):
    return f"<h1>Task detail page for task {task_id}</h1>"

@app.route('/new-task')
def new_task():
    return "<h1>Enter your new task</h1>"

