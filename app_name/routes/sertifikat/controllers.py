from wsgiref.util import request_uri
from flask import Blueprint, request, render_template, url_for
from flask_jwt_extended import  get_jwt, jwt_required
from werkzeug.utils import secure_filename
from flask import current_app as app
from time import strftime
from ...dbFunctions import Database
from ...utilities import *
from ...queries import *
from app_name.helpers.validator import *
from app_name.helpers.function import *
import threading
from PyPDF2 import PdfFileWriter, PdfFileReader
import io, math
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor
from PIL import Image
import PIL

sertifikat = Blueprint(
    name='sertifikat',
    import_name=__name__,  
    static_folder = '../../static/pdf/sertifikat', 
    static_url_path="/media",
    url_prefix='/sertifikat'
)

@sertifikat.get('id/<id>')
@jwt_required()
def send_sertifikat_by_id_kehadiran(id):
    currentUser_role = get_jwt()["role"]
    url_list = request.url.split('/')[:-2]
    url = ('/').join(url_list)
    try:
        if currentUser_role != "ADMIN":
            return defined_error("hanya ADMIN yang dapat mengirimkan sertifikat","Forbidden",403)  
        # Ambil id_user dari jwt
        query = QUERY_GET_KEHADIRAN_BY_ID
        values = (id,)
        result = Database().get_data(query,values)

        if len(result) == 0:
            return defined_error(f"portofolio dengan id:{id} tidak ditemukan",'Not Found', 404)

        email_peserta = result[0]["email_peserta"]

        template_email = render_template(
            template_name_or_list="template_email.html",
            data={
                "showGambar" : True,
                "gambarURL" : app.config["BASE_URL"] + "/" + url_for("static", filename="icons/login.png"),
                "judul" : "SERTIFIKAT KEHADIRAN PESERTA",
                "deskripsi" : "Terima kasih telah Berpartisipasi pada event ini",
            }
        )

        # 📭 Fungsi untuk mengirim verfikasi email pengguna baru
        def send_email_verification():
            send_email(
                penerima=email_peserta, 
                judul="Verifikasi Akun Email Central POS", 
                template=template_email
            )
        
        thread = threading.Thread(target=send_email_verification)
        thread.start()

        return success_data(message="Berhasil", data=email_peserta)

    except Exception as e:
        return bad_request(str(e))

@sertifikat.route('/create', methods=['POST'])
def create_sertifikat():
    data = request.json
    namaPeserta = data['namaPeserta'].title()
    namaEvent = data['namaEvent'].title()
    kodeHadir = data['kodeHadir'].lower()
    jenisEvent = data['jenisEvent'].lower()
    qr = data['qr']

    existing_pdf = PdfFileReader(open(app.config['TEMPLATE_SERTIFIKAT'] + f'{jenisEvent}.pdf', "rb"))
    page = existing_pdf.pages[0]

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page.mediabox.width, page.mediabox.height))

    pdfmetrics.registerFont(TTFont('Bitter', app.config['FONTS']+'Bitter-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Archivo', app.config['FONTS']+'Archivo-Bold.ttf'))

    if jenisEvent == "softskill":
        # nama peserta
        can.setFont("Bitter", 54)
        can.setFillColor(HexColor('#87AAAA'))
        namaPeserta = simpleSplit(namaPeserta, "Bitter", 54, 564)
        y_axis = 215
        for words in namaPeserta:
            can.drawString(160, y_axis+(len(namaPeserta)*54), words)
            y_axis-=60
        
        # nama event
        can.setFont("Archivo", 18)
        can.setFillColor(HexColor('#171717'))
        namaEvent = simpleSplit(namaEvent, "Archivo", 18, 429)
        y_axis = 205
        for words in namaEvent:
            can.drawString(160, y_axis, words)
            y_axis-=18
        
        # gambar qr
        img = PIL.Image.open(io.BytesIO(base64.b64decode(qr)))
        img = img.resize((80, 80))
        img.save(app.config['SERTIFIKAT'] + f'{kodeHadir}.jpeg')
        can.drawImage(app.config['SERTIFIKAT'] + f'{kodeHadir}.jpeg', 619, 150, width=115, preserveAspectRatio=True, mask='auto')
        can.save()
        os.remove(app.config['SERTIFIKAT'] + f'{kodeHadir}.jpeg')
    
    elif jenisEvent == "hardskill":
        # nama peserta
        can.setFont("Bitter", 54)
        can.setFillColor(HexColor('#F4C06C'))
        namaPeserta = simpleSplit(namaPeserta, "Bitter", 54, 710)
        y_axis = 320
        for words in namaPeserta:
            w_namaPeserta = stringWidth(words,"Bitter", 54)
            can.drawString((float(page.mediabox.width)-w_namaPeserta)/2, y_axis, words)
            y_axis-=54
        
        # nama event
        can.setFont("Archivo", 18)
        can.setFillColor(HexColor('#E9EEF1'))
        namaEvent = simpleSplit(namaEvent, "Archivo", 18, 710)
        y_axis = 205
        for words in namaEvent:
            w_namaEvent = stringWidth(words,"Bitter", 18)
            can.drawString((float(page.mediabox.width)-w_namaEvent)/2, y_axis, words)
            y_axis-=18
        
        # gambar qr
        img = PIL.Image.open(io.BytesIO(base64.b64decode(qr)))
        img = img.resize((80, 80))
        img.save(app.config['SERTIFIKAT'] + f'{kodeHadir}.jpeg')
        can.drawImage(app.config['SERTIFIKAT'] + f'{kodeHadir}.jpeg', 651, 85, width=115, preserveAspectRatio=True, mask='auto')
        can.save()
        os.remove(app.config['SERTIFIKAT'] + f'{kodeHadir}.jpeg')
    
    new_pdf = PdfFileReader(packet)
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    outputStream = open(app.config['SERTIFIKAT'] + f'{kodeHadir}.pdf', "wb")
    output.write(outputStream)
    outputStream.close()

    return success_data("Berhasil membuat sertifikat", app.config['SERTIFIKAT'] + f'{kodeHadir}.pdf')

