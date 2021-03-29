from flask import Flask, jsonify, request

app = Flask(__name__)
Designs = [
    {
        'name' : 'My Home 1',
        'Models' : [
            {'Name' : 'Modele one',
             'Number OF Blocks' : 4,
             'Number OF Doors' : 3,
             'Number OF Windows' : 5
            
            },
           {'Name' : 'Modele Tow',
            'Number OF Blocks' : 4,
            'Number OF Doors' : 3,
            'Number OF Windows' : 5
         
        }
        ]
    }
]


@app.route('/')
def get_Designs():
   return jsonify({'Designs':Designs})

@app.route('/Design', methods=['POST'])
def create_Design():
  request_data = request.get_json()
  new_Design = {
    'name': request_data['My Home 2'],
    'Models': ['Modele three']
}
  Designs.append(new_Design)
  return jsonify(new_Design)


@app.route('/Design/<string:name>/Model', methods=['POST'])
def create_Model_in_Design(name):
  request_data = request.get_json()
  for Design in Designs:
    if Design['name'] == name:
      new_Model = {
        'name': request_data['name'],
        'Number OF Blocks': request_data['Number OF Blocks'],
        'Number OF Doors': request_data['Number OF Doors'],
        'Number OF Windows': request_data['Number OF Windows']
}
      Designs['Models'].append(new_Model)
      return jsonify(new_item)
    return jsonify({'message': 'Design not found'})

if __name__ =='__main__': 
  app.run(port=5000)