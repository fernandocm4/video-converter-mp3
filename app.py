import os
from flask import Flask, render_template, request, flash, send_from_directory, jsonify
import script as sc

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c507d8d94510bf6799707da6d106a1aa1af52bacb144d92'

@app.route("/", methods=('GET', 'POST'))
def home():
	#exclusão dos arquivos
	path = '/home/fernandocm4/PycharmProjects/flaskteste/diretorio/'
	for arquivo in os.listdir(path):
		if arquivo.endswith('.mp3'):
			os.remove(os.path.join(path, arquivo))
	return render_template('video_converter.html')

@app.route('/convert', methods=['GET', 'POST'])
def converter():
	if request.method == 'POST':
		link = request.form['link']
		if not link:
			flash('Voce precisa informar o link do video')
		else:
			flash('video converitdo')

		sc.converter(link)
	return render_template('video_download.html')

@app.route('/download', methods=['POST','GET'])
def download():

	title = ''
	for arquivo in os.listdir('/home/fernandocm4/PycharmProjects/flaskteste/diretorio/'):
		if arquivo.endswith('.mp3'):
			title = arquivo

	return send_from_directory('diretorio', title, as_attachment=True)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
