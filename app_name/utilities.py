from flask import jsonify, make_response
import string
import random
import cv2
import base64
import numpy as np
import json
import requests
import os
import re
import uuid
import hashlib
from urllib.parse import urlparse
import pyqrcode
import base64
import io

def success(message, status_code=200):
    return make_response(jsonify({'status_code': status_code, 'message': message}), status_code)

def success_data(message, data, status_code=200):
    return make_response(jsonify({'status_code': status_code, 'message': message, 'data': data}), status_code)

def authorization_error():
    return make_response(jsonify({'error': 'Permission Denied', 'status_code': 403}), 403)

def invalid_params():
    return make_response(jsonify({'error': 'Invalid Parameters', 'status_code': 400}), 400)

def bad_request(description=""):
	return make_response(jsonify({'description':f"{description}",'error': 'Bad Request','status_code':400}), 400) #Production

def not_found_error():
    return make_response(jsonify({'error': 'Not Found', 'status_code': 404}), 404)

def defined_error(description, error="Defined Error", status_code=499):
	return make_response(jsonify({'description':description,'error': error,'status_code':status_code}), status_code)

def parameter_error(description, error= "Parameter Error", status_code=400):
	return make_response(jsonify({'description':description,'error': error,'status_code':status_code}), status_code)

def random_string_number_only(stringLength):
	letters = string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

def random_string(stringLength):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

def save(encoded_data, filename):
	encoded_data = encoded_data.split(',')[1]
	arr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
	img = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
	return cv2.imwrite(filename, img)

def validatepassword(password):
    message= []
    if len(password) < 8:
        message.append("Panjang Password setidaknya harus 8")
    if len(password) > 20:
        message.append("Panjang Password tidak boleh lebih dari 20")
    if not any(char.isdigit() for char in password):
        message.append("Password harus memiliki setidaknya satu angka")
    if any(char.isspace() for char in password):
        message.append("Password tidak boleh mengandung spasi")
    if not any(char.isupper() for char in password):
        message.append("Password harus memiliki setidaknya satu huruf besar")
    if not any(char.islower() for char in password):
        message.append("Password harus memiliki setidaknya satu huruf kecil")
    return message

#fungsi validasi email
def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def validateName(name):
    return name != '' and all(chr.isalpha() or chr.isspace() for chr in name)

def validateWhatsappContact(contact):
    if contact == None:
        return False
    if contact != "":
        if str(contact).find('/+') != -1:
            contactData = str(contact).split('/+')
            if contactData[0] == "wa.me" and contactData[1].isnumeric():
                return False
    return True

def url_validator(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def validatePhone(phone):
    return len(phone) > 5 and len(phone) <= 15 and all(chr.isdigit() for chr in (phone))

#fungsi untuk hashing password menggunakan salt
def hashPassword(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

#fungsi untuk komparasi password yang sudah di hash dengan password dari user
def checkPassword(hashedText, password):
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def send_email(penerima, judul, template):
    dataInput = {
        "pengirim" : "info@bisaai.com",
        "penerima" : penerima,
        "judul" : judul,
        "isi" : template
    }
    requests.request (
        method="POST",
        url=os.getenv("EMAIL_SERVICE_URL"),
        headers={
            "X-API-KEY" : os.getenv("EMAIL_API_KEY"),
            "Content-Type" : "application/json"
        },
        data=json.dumps(dataInput)
    )
    print(f'Berhasil mengirim email ke {penerima}')

def generate_qr_code(payload):
    data = pyqrcode.create(str(payload))
    s = io.BytesIO()
    data.png(s,scale=6)
    encoded = base64.b64encode(s.getvalue()).decode("ascii")
    return encoded
