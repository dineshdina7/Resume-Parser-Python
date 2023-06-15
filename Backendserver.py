from flask import Flask, request, jsonify
from pyresparser import ResumeParser
import tempfile
app = Flask(__name__)
@app.route('/parse_resume', methods=['POST'])
def parse_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    try:
#         parser = ResumeParser(file)
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name+'.pdf'
        print( temp_file_path)
        file.save(temp_file_path)
        file_path=temp_file_path.replace('\\','\\\\')
        parser=ResumeParser(file_path)
        data = parser.get_extracted_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run(debug=True)