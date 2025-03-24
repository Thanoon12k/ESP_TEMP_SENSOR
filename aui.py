import os
from flask import Flask, render_template

from api import construct_lists, get_data_from_sheet
# from .api import construct_lists, get_data_from_sheet


app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_data():
    data = get_data_from_sheet()
    reconstructed_data = construct_lists(data)
   
    return render_template('main.html', temp_data=reconstructed_data)

@app.route('/json', methods=['GET'])
def show_json_data():
    data = get_data_from_sheet()
    print ("total data getted successfuly: ",len(data))
    if (len(data) > 0):
        reconstructed_data = construct_lists(data)
        return reconstructed_data
    else:
        return {"error": "Failed to fetch data"}


if __name__ == '__main__':
    app.run(debug=True)

