from .. import db
from sqlalchemy.sql import func
from app_name.database.eventModel import Event

class Kehadiran(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_event = db.Column(db.Integer, db.ForeignKey(Event.id, ondelete='CASCADE'),nullable=False)
    kode_kehadiran = db.Column(db.String(7), nullable=False)
    nama_peserta = db.Column(db.String(255), nullable=False)
    email_peserta = db.Column(db.String(255), nullable=False)
    link_sertifikat = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    is_delete = db.Column(db.Integer, nullable=True, server_default='0', comment="1 = deleted, 0 = not deleted")

    def __repr__(self):
        return '<Kehadiran {}>'.format(self.name)