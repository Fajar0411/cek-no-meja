from flask import Flask, render_template

# Membuat aplikasi Flask dengan template di folder yang sama
app = Flask(__name__, template_folder='.')

@app.route('/meja/<int:nomor_meja>')
def meja(nomor_meja):
    # Render template dengan nomor meja yang diteruskan ke halaman
    return render_template('meja.html', nomor_meja=nomor_meja)

if __name__ == '__main__':
    app.run(debug=True)
