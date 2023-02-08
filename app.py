from flask import Flask, render_template, request, jsonify
from util import filter_names, to_mongo, range_slider

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/results', methods=['POST', 'GET'])
def results():
    filter_names()
    return render_template('index.html') 

@app.route('/mongo', methods=['POST', 'GET'])
def mongo(): 
    if request.form.get('options-outlined') == "json":
        if request.form.get('dropdown') and request.form.get('dropdown').isalnum():
            limit = int(request.form.get('dropdown')) 
            return jsonify(to_mongo(limit)) 
        elif request.form.get('input-field') and request.form.get('input-field').isalnum():
            limit = int(request.form.get('input-field'))
            return jsonify(to_mongo(limit)) 
        elif request.form.get('range-field') and request.form.get('range-field').isalnum():
            limit = int(request.form.get('range-field'))
            return jsonify(to_mongo(limit)) 
        elif request.form.get('range-start') and request.form.get('range-end'):
            start_range = int(request.form.get('range-start'))
            end_range = int(request.form.get('range-end'))
            return jsonify(range_slider(start_range-1, end_range))
    
    elif request.form.get('options-outlined') == "table":
        if request.form.get('dropdown') and request.form.get('dropdown').isalnum():
            limit = int(request.form.get('dropdown'))
            my_dict = to_mongo(limit)
            columnnames = ["ID", "Company name", "Country ISO", "City", "Nace", "Website"]
            return render_template("index.html", records=my_dict, colnames=columnnames)
        
        elif request.form.get('input-field') and request.form.get('input-field').isalnum():
            limit = int(request.form.get('input-field'))
            my_dict = to_mongo(limit)
            columnnames = ["ID", "Company name", "Country ISO", "City", "Nace", "Website"]
            return render_template("index.html", records=my_dict, colnames=columnnames)
         
        elif request.form.get('range-start') and request.form.get('range-end'):
            start_range = int(request.form.get('range-start'))
            end_range = int(request.form.get('range-end'))
            my_dict = range_slider(start_range-1, end_range)
            columnnames = ["ID", "Company name", "Country ISO", "City", "Nace", "Website"]
            return render_template("index.html", records=my_dict, colnames=columnnames)
 

if __name__ == '__main__':
    app.run(debug=True)