from app_name.dbFunctions import Database
from app_name.queries import *
import os

def create_log(log):
    query = QUERY_CREATE_LOG
    val = (log,)
    Database().insert_data(query,val)

def check_and_remove_file(appConfig,savedPath):
    if savedPath and  os.path.exists(os.path.join(appConfig, savedPath)):
        os.remove(os.path.join(appConfig, savedPath))

def format_portofolio_data(url,result,i=0):
    image_list = ['thumbnail','foto_1','foto_2','foto_3']

    for field in image_list:
        if result[i][field]:
            result[i][field] = f"{url}/media/{result[i][field]}"

    if result[i]["foto"]:
        result[i]["foto"] = f"{url[:-11]}/user/media/{result[i]['foto']}"

    status = "Sudah disetujui" if result[i]["approved"] == 1 else "Belum disetujui"

    return {
            "id" : result[i]["id"],
            "judul" : result[i]["judul"],
            "deskripsi_singkat" :  result[i]["deskripsi_singkat"],
            "deskripsi_lengkap" :  result[i]["deskripsi_lengkap"],
            "kategori" :  result[i]["kategori"],
            "approved" :  status,
            "thumbnail" :  result[i]["thumbnail"],
            "foto_1" :  result[i]["foto_1"],
            "foto_2" :  result[i]["foto_2"],
            "foto_3" :  result[i]["foto_3"],
            "owner" : {
                "nama":result[i]["nama"],
                "foto":result[i]["foto"],
                "linkedin":result[i]["linkedin"],
                "instagram":result[i]["instagram"],
            }
        }


