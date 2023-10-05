from .. import db
from sqlalchemy.sql import func

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kode = db.Column(db.String(7), unique=True,nullable=False)
    
    nama = db.Column(db.String(255), nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    waktu_mulai = db.Column(db.DateTime, nullable=False)
    waktu_berakhir = db.Column(db.DateTime, nullable=False)
    
    nama_pemateri = db.Column(db.String(255), nullable=False)
    nama_pemateri_2 = db.Column(db.String(255), nullable=True)
    contact_whatsapp = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    
    poster = db.Column(db.String(255), nullable=False)
    deskripsi = db.Column(db.String(400), nullable=False)
    
    link_conference = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=True)
    
    is_published = db.Column(db.Integer, nullable=True, server_default='1', comment="1 = published, 0 = not published")
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    is_delete = db.Column(db.Integer, nullable=True, server_default='0', comment="1 = deleted, 0 = not deleted")

    def __repr__(self):
        return '<User {}>'.format(self.name)