from flask import Flask ,render_template

app= Flask(__name__ ,template_folder='thems_6')

@app.route('/')
def index():
    numbers = [i for i in range(20)]
    students = ['john','sara','mohammad','mahdi']
    return render_template('index_3.html',students=students,numbers=numbers)


