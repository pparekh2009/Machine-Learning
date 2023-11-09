from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# import model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():

    req_form = request.form

    print(req_form)

    int_features = []
    area = req_form.get("sq_mtr")
    no_of_rooms = req_form.get("no_of_rooms")
    hasYard = 1 if req_form.get("has_yard") == "on" else 0
    hasPool = 1 if req_form.get("has_pool") == "on" else 0
    noOfFloors = req_form.get("floors")
    noOfPrevOwners = req_form.get("no_of_prev_owners")
    made = req_form.get("made")
    isNewBuilt = 1 if req_form.get("is_new_built") == "on" else 0
    hasStormProtector = 1 if req_form.get("has_storm_protector") == "on" else 0
    basementArea = req_form.get("basement")
    atticArea = req_form.get("attic")
    garageArea = req_form.get("garage")
    hasStorageRoom = 1 if req_form.get("has_storage_room") == "on" else 0
    hasGuestRoom = 1 if req_form.get("has_guest_room") == "on" else 0

    int_features.append([area, no_of_rooms, hasYard, hasPool, noOfFloors, noOfPrevOwners, made, isNewBuilt, hasStormProtector, basementArea, atticArea, garageArea, hasStorageRoom, hasGuestRoom])

    print(int_features)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)