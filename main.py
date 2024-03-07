
from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)

elements = [
    {'id': 'button', 'type': 'button', 'text': 'Button'},
    {'id': 'text_field', 'type': 'text_field', 'placeholder': 'Enter text'},
    {'id': 'image', 'type': 'image', 'src': 'image.png'},
]

mockups = {}

@app.route('/')
def index():
    return render_template('index.html', elements=elements)

@app.route('/elements')
def get_elements():
    return jsonify(elements)

@app.route('/preview')
def preview():
    data = request.get_json()
    mockup = assemble_mockup(data)
    return render_template('preview.html', mockup=mockup)

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    mockup_id = str(uuid.uuid4())
    mockups[mockup_id] = data
    return jsonify({'mockup_id': mockup_id})

@app.route('/load/<mockup_id>')
def load(mockup_id):
    if mockup_id in mockups:
        data = mockups[mockup_id]
        return jsonify(data)
    else:
        return jsonify({'error': 'Mockup not found'})

@app.route('/delete/<mockup_id>', methods=['DELETE'])
def delete(mockup_id):
    if mockup_id in mockups:
        del mockups[mockup_id]
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'Mockup not found'})

def assemble_mockup(data):
    mockup = {}
    for element in data:
        element_id = element['id']
        element_type = element['type']
        element_attributes = element['attributes']
        if element_type == 'button':
            mockup[element_id] = {'type': 'button', 'text': element_attributes['text']}
        elif element_type == 'text_field':
            mockup[element_id] = {'type': 'text_field', 'placeholder': element_attributes['placeholder']}
        elif element_type == 'image':
            mockup[element_id] = {'type': 'image', 'src': element_attributes['src']}
    return mockup

if __name__ == '__main__':
    app.run(debug=True)
