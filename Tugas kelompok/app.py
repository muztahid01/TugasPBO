# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung_ipk', methods=['POST'])
def hitung_ipk():
    # Mendapatkan data dari formulir
    matkul1 = float(request.form['matkul1'])
    matkul2 = float(request.form['matkul2'])
    matkul3 = float(request.form['matkul3'])
    matkul4 = float(request.form['matkul4'])
    matkul5 = float(request.form['matkul5'])
    matkul6 = float(request.form['matkul6'])
    matkul7 = float(request.form['matkul7'])
    matkul8 = float(request.form['matkul8'])
    
    # Bobot SKS untuk setiap mata kuliah
    bobot_sks = {
        'matkul1': 3,
        'matkul2': 2,
        'matkul3': 2,
        'matkul4': 3,
        'matkul5': 3,
        'matkul6': 2,
        'matkul7': 2,
        'matkul8': 2,
    }

    # Menghitung total SKS
    total_sks = sum(bobot_sks.values())

    # Menghitung IPK dengan mempertimbangkan bobot SKS
    total_nilai = (matkul1 * bobot_sks['matkul1'] +
                   matkul2 * bobot_sks['matkul2'] +
                   matkul3 * bobot_sks['matkul3'] +
                   matkul4 * bobot_sks['matkul4'] +
                   matkul5 * bobot_sks['matkul5'] +
                   matkul6 * bobot_sks['matkul6'] +
                   matkul7 * bobot_sks['matkul7'] +
                   matkul8 * bobot_sks['matkul8'])

    ipk = round((total_nilai / total_sks), 2)  # Membulatkan hasil menjadi 2 angka desimal
    
    return render_template('hasil.html', ipk=ipk)

if __name__ == '__main__':
    app.run(debug=True)
