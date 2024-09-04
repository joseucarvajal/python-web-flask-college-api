from flask import Flask, request, jsonify

from models.course import Course

app = Flask(__name__)

@app.route('/course', methods=['POST'])
def create_course():
    data = request.json
    
    course = Course()
    course.name = data["name"]
    course.start_date = data["start_date"]
    course.end_date = data["end_date"]
    course.cut1_percentage = data["cut1_percentage"]
    course.cut2_percentage = data["cut2_percentage"]
    course.cut3_percentage = data["cut3_percentage"]

    
    #return jsonify(user.__dict__)
    return jsonify({
        "version": "0.0.1",
        "dato": course.name,
    })
