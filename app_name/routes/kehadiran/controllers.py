from flask import Blueprint, request, render_template, url_for
from flask import current_app as app
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, JWTManager

from ...queries import *
from ...dbFunctions import Database
from ...utilities import *

from app_name.helpers.validator import *
from app_name.helpers.function import *

kehadiran = Blueprint(
    name='kehadiran', 
    import_name=__name__, 
    url_prefix='/kehadiran'
)

@kehadiran.post('/<kode>')
def create_kehadiran(kode):
    try :
        # ===================================
        # ======== Handle Data Input ========
        # ===================================
        dataInput = request.json
        dataRequired = ["nama", "email"]
        for data in dataRequired:
            if dataInput == None:
                return bad_request("body request tidak boleh kosong")
            if data not in dataInput:
                return parameter_error(f"Missing {data} in Request Body")
            if dataInput[data] == None:
                dataInput[data] = ""
        # ====================================
        # ======== Data Preprocessing ========
        # ====================================

        # map dan sanitize input dengan trim 
        nama = dataInput["nama"].strip().title()
        email = dataInput["email"].strip().lower()
        kode_kehadiran = uuid.uuid4().hex[:6]  
        
        # =================================
        # ======== Data Validation ========
        # =================================
        query = QUERY_GET_EVENT_BY_KODE
        values = (kode,)
        result = Database().get_data(query, values)
        if len(result) == 0:
            return defined_error(f"event dengan kode:{kode} tidak ditemukan", 'Not Found', 404)

        id_event = result[0]["id"]

        
        #validasi apakah nama dan email sudah sesuai format
        error_list = kehadiran_validator(nama,email)
        if len(error_list) != 0:
            return defined_error(error_list,'Bad Request', 400)

        # cek apakah peserta telah mengisi kehadiran 
        query = QUERY_CHECK_DUPLICATE_KEHADIRAN
        values = (id_event,email,)
        kehadiran = Database().get_data(query, values)
        if len(kehadiran) != 0:
            return defined_error(f"email:{email} sudah menghadiri event dengan kode:{kode}", 'Bad Request', 400)

        # ========================
        # ======== Action ========
        # ========================
        # Insert data to database
        values = {
            "id_event":id_event,
            "nama_peserta" : nama,
            "email_peserta" : email,
            "kode_kehadiran": kode_kehadiran
        }
        Database().save(table="kehadiran", data=values)

        #membuat log
        create_log(f"peserta dengan email:{email} menghadiri event dengan id:{id} kode:{kode}")

        #return response
        return success(message=f"Berhasil menambahkan data kehadiran")

    except Exception as e:
        return bad_request(str(e))


@kehadiran.get('/kode/<kode>')
@jwt_required()
def get_kehadiran_by_event_kode(kode): 
    offset = request.args.get('page')
    limit = request.args.get('row')
    limit  = int(limit) if limit else 10
    offset  = (int(offset) - 1) * limit if offset else 0
    user_role = get_jwt()["role"]
    user_email = get_jwt()["email"]
    try :
        if user_role != "ADMIN":
            return defined_error("hanya admin yang dapat mengakses","Forbidden",403)   
        # =================================
        # ======== Data Validation ========
        # =================================
        query = QUERY_GET_EVENT_BY_KODE
        values = (kode,)
        result = Database().get_data(query, values)
        if len(result) == 0:
            return defined_error(f"event dengan kode:{kode} tidak ditemukan", 'Not Found', 404)

        id_event = result[0]["id"]
        # ========================
        # ======== Action ========
        # ========================
        query = QUERY_GET_ALL_KEHADIRAN_BY_EVENT
        values = (id_event,limit,offset)
        result = Database().get_data(query,values) 
        if len(result) == 0:
            return defined_error(f"belum ada yang menghadiri event dengan kode:{kode}", 'Not Found', 404)

        create_log(f"{user_role} dengan email:{user_email} mengambil data kehadiran dengan kode event:{kode}")

        return success_data(message=f"Success", data=result)

    except Exception as e:
        return bad_request(str(e))

@kehadiran.get('/id/<id>')
@jwt_required()
def get_kehadiran_by_event_id(id): 
    offset = request.args.get('page')
    limit = request.args.get('row')
    limit  = int(limit) if limit else 10
    offset  = (int(offset) - 1) * limit if offset else 0
    user_role = get_jwt()["role"]
    user_email = get_jwt()["email"]
    try :
        if user_role != "ADMIN":
            return defined_error("hanya admin yang dapat mengakses","Forbidden",403)   
        # =================================
        # ======== Data Validation ========
        # =================================
        query = QUERY_GET_EVENT_BY_ID
        values = (id,)
        result = Database().get_data(query, values)
        if len(result) == 0:
            return defined_error(f"event dengan id:{id} tidak ditemukan", 'Not Found', 404)

        id_event = result[0]["id"]
        # ========================
        # ======== Action ========
        # ========================
        query = QUERY_GET_ALL_KEHADIRAN_BY_EVENT
        values = (id_event,limit,offset)
        result = Database().get_data(query,values)
        if len(result) == 0:
            return defined_error(f"belum ada yang menghadiri event dengan id:{id}", 'Not Found', 404)

        create_log(f"{user_role} dengan email:{user_email} mengambil data kehadiran dengan id event:{id}")

        return success_data(message=f"Success", data=result)

    except Exception as e:
        return bad_request(str(e))

@kehadiran.get('/qrcode/id/<id>')
@jwt_required()
def get_QR_code_by_id(id): 
    user_role = get_jwt()["role"]
    user_email = get_jwt()["email"]
    try :
        if user_role != "ADMIN":
            return defined_error("hanya admin yang dapat mengakses","Forbidden",403)   
        # ========================
        # ======== Action ========
        # ========================
        query = QUERY_GET_KEHADIRAN_BY_ID
        values = (id,)
        result = Database().get_data(query,values)
        if len(result) == 0:
            return defined_error(f"kehadiran dengan id:{id} tidak ditemukan", 'Not Found', 404)

        payload = result[0]
        del payload["link_sertifikat"]
        data = {
            "qr_code": generate_qr_code(payload)
        }

        create_log(f"{user_role} dengan email:{user_email} mengambil data kehadiran dengan id:{id}")

        return success_data(message=f"Success", data=data)

    except Exception as e:
        return bad_request(str(e))

@kehadiran.get('/qrcode/kode/<kode>')
@jwt_required()
def get_QR_code_by_kode(kode): 
    user_role = get_jwt()["role"]
    user_email = get_jwt()["email"]
    try :
        if user_role != "ADMIN":
            return defined_error("hanya admin yang dapat mengakses","Forbidden",403)   
        # ========================
        # ======== Action ========
        # ========================
        query = QUERY_GET_KEHADIRAN_BY_KODE
        values = (kode,)
        result = Database().get_data(query,values)
        if len(result) == 0:
            return defined_error(f"kehadiran dengan kode:{kode} tidak ditemukan", 'Not Found', 404)

        payload = result[0]
        del payload["link_sertifikat"]
        data = {
            "qr_code": generate_qr_code(payload)
        }

        create_log(f"{user_role} dengan email:{user_email} mengambil data kehadiran dengan id:{id}")

        return success_data(message=f"Success", data=data)

    except Exception as e:
        return bad_request(str(e))

