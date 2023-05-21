from flask import Flask, request

from recognize import recognize_image
import base64

app = Flask(__name__)


@app.route('/recognize', methods=['POST'])
def recognize_faces():
    if 'image' in request.files:
        image = request.files['image']
        image.save("image.jpg")
        result = recognize_image()
        print(result[1])
        return base64.b64encode(result[0])
    return None


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
