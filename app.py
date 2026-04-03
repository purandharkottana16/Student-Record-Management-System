from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage (list)
students = []

@app.route('/')
def home():
    return render_template('home.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        course = request.form['course']
        
        students.append({
            'name': name,
            'roll': roll,
            'course': course
        })
        
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:index>')
def delete_student(index):
    students.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)