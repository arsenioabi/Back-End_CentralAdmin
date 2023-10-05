QUERY_UPDATE_PROFILE = '''
        UPDATE user
        SET nama=%s, tanggal_lahir=%s, foto=%s, jenis_kelamin=%s, nomor_telepon=%s, 
        linkedin=%s, instagram=%s, alamat=%s, riwayat_kerja=%s  
        WHERE is_delete=0 AND id=%s AND email=%s
        '''

QUERY_UPDATE_PASSWORD = '''
        UPDATE user
        SET password=%s  
        WHERE is_delete=0 AND id=%s AND email=%s 
        '''
                
QUERY_GET_ACCOUNT_USER = '''
        SELECT id, email, nama, password, foto 
        FROM user 
        WHERE is_delete=0 AND id=%s AND email=%s
        '''

QUERY_GET_PROFILE = '''
        SELECT id, email, nama, tanggal_lahir, foto, jenis_kelamin, nomor_telepon, linkedin, instagram, alamat, riwayat_kerja 
        FROM user 
        WHERE is_delete=0 AND id=%s 
        '''

QUERY_GET_CURRENT_PROFILE = '''
        SELECT id, email, nama, tanggal_lahir, foto, jenis_kelamin, nomor_telepon, linkedin, instagram, alamat, riwayat_kerja 
        FROM user 
        WHERE is_delete=0 AND id=%s AND email=%s
        '''

QUERY_CHECK_EMAIL = "SELECT id FROM user WHERE email=%s AND is_delete=0"

QUERY_CHECK_PASSWORD = "SELECT id, nama, password FROM user WHERE email=%s AND is_delete=0"

QUERY_CHECK_EMAIL_ADMIN = "SELECT id FROM admin WHERE email=%s AND is_delete=0"

QUERY_CHECK_PASSWORD_ADMIN = "SELECT id, nama, password FROM admin WHERE email=%s AND is_delete=0"

QUERY_CREATE_LOG = "INSERT INTO log (activity) VALUES (%s)"

QUERY_GET_KATEGORI = "SELECT * FROM kategori WHERE id=%s AND is_delete=0"

QUERY_GET_PORTOFOLIO_BY_ID = """
        SELECT portofolio.id, portofolio.id_user, portofolio.approved, portofolio.judul,
        portofolio.deskripsi_singkat, portofolio.deskripsi_lengkap, portofolio.id_kategori,
        portofolio.thumbnail, portofolio.foto_1, portofolio.foto_2, portofolio.foto_3,
        portofolio.created_at, user.id,user.nama,user.foto,user.linkedin,user.instagram,
        kategori.id,kategori.kategori
        FROM portofolio 
        JOIN user ON portofolio.id_user = user.id
        INNER JOIN kategori ON portofolio.id_kategori = kategori.id
        WHERE portofolio.id=%s AND portofolio.is_delete=0
        """

QUERY_GET_ALL_PORTOFOLIO= """
        SELECT portofolio.id, portofolio.id_user, portofolio.approved, portofolio.judul,
        portofolio.deskripsi_singkat, portofolio.deskripsi_lengkap, portofolio.id_kategori,
        portofolio.thumbnail, portofolio.foto_1, portofolio.foto_2, portofolio.foto_3,
        portofolio.created_at, user.nama,user.foto,user.linkedin,user.instagram,kategori.kategori
        FROM portofolio 
        JOIN user ON portofolio.id_user = user.id
        INNER JOIN kategori ON portofolio.id_kategori = kategori.id
        WHERE portofolio.judul LIKE %s AND portofolio.approved=%s AND portofolio.is_delete=0
        ORDER BY created_at DESC
        LIMIT %s
        OFFSET %s
        """

QUERY_GET_ALL_PORTOFOLIO_BY_USER_ID= """
        SELECT portofolio.id, portofolio.id_user, portofolio.approved, portofolio.judul,
        portofolio.deskripsi_singkat, portofolio.deskripsi_lengkap, portofolio.id_kategori,
        portofolio.thumbnail, portofolio.foto_1, portofolio.foto_2, portofolio.foto_3,
        portofolio.created_at, user.nama,user.foto,user.linkedin,user.instagram,kategori.kategori
        FROM portofolio 
        JOIN user ON portofolio.id_user = user.id
        INNER JOIN kategori ON portofolio.id_kategori = kategori.id
        WHERE portofolio.id_user=%s AND portofolio.approved=%s AND portofolio.is_delete=0
        ORDER BY created_at DESC
        LIMIT %s
        OFFSET %s
        """

QUERY_UPDATE_PORTOFOLIO = """
        UPDATE portofolio
        SET judul=%s, deskripsi_singkat=%s, deskripsi_lengkap=%s, id_kategori=%s, 
        thumbnail=%s, foto_1=%s, foto_2=%s, foto_3=%s
        WHERE is_delete=0 AND id=%s
        """

QUERY_APPROVE_PORTOFOLIO = """
        UPDATE portofolio
        SET approved=%s
        WHERE is_delete=0 AND id=%s
        """
        
QUERY_DELETE_PORTOFOLIO = """
        UPDATE portofolio
        SET thumbnail=NULL, foto_1=NULL, foto_2=NULL, foto_3=NULL, is_delete=1
        WHERE id=%s
        """

QUERY_GET_KODE_EVENT = "SELECT kode FROM event WHERE kode=%s"

QUERY_PUBLISH_EVENT = '''
        UPDATE event
        SET is_published=1
        WHERE kode=%s
        '''

QUERY_UNPUBLISH_EVENT = '''
        UPDATE event
        SET is_published=0
        WHERE kode=%s
        '''

QUERY_GET_ALL_EVENT = """
        SELECT id, kode, nama, 
        tanggal, waktu_mulai, waktu_berakhir, nama_pemateri, 
        poster, deskripsi, link_conference, password, is_published
        FROM event
        WHERE nama LIKE %s AND is_delete=0
        ORDER BY created_at DESC
        LIMIT %s
        OFFSET %s
        """

QUERY_GET_ALL_PUBLISHED_EVENT = """
        SELECT id, kode, nama, 
        tanggal, waktu_mulai, waktu_berakhir, nama_pemateri, 
        poster, deskripsi, link_conference, password, is_published
        FROM event
        WHERE nama LIKE %s AND is_delete=0 AND is_published=1
        ORDER BY created_at DESC
        LIMIT %s
        OFFSET %s
        """

QUERY_GET_PUBLISHED_EVENT_BY_ID = """
        SELECT id, kode, nama, 
        tanggal, waktu_mulai, waktu_berakhir, nama_pemateri, 
        poster, deskripsi, link_conference, password, is_published
        FROM event
        WHERE id=%s AND is_delete=0 AND is_published=1
        """

QUERY_GET_PUBLISHED_EVENT_BY_KODE = """
        SELECT id, kode, nama, 
        tanggal, waktu_mulai, waktu_berakhir, nama_pemateri, 
        poster, deskripsi, link_conference, password, is_published
        FROM event
        WHERE kode=%s AND is_delete=0 AND is_published=1
        """

QUERY_GET_ALL_EVENT = """
        SELECT *
        FROM event
        WHERE nama LIKE %s AND is_delete=0
        ORDER BY created_at DESC
        LIMIT %s
        OFFSET %s
        """

QUERY_GET_EVENT_BY_ID = """
        SELECT * FROM event
        WHERE id=%s AND is_delete=0
        """

QUERY_GET_EVENT_BY_KODE = """
        SELECT * FROM event
        WHERE kode=%s AND is_delete=0
        """

QUERY_UPDATE_EVENT_BY_ID = """
        UPDATE event
        SET nama=%s, tanggal=%s, waktu_mulai=%s, waktu_berakhir=%s, nama_pemateri=%s, 
        poster=%s, deskripsi=%s, link_conference=%s, password=%s
        WHERE is_delete=0 AND id=%s
        """

QUERY_UPDATE_EVENT_BY_KODE = """
        UPDATE event
        SET nama=%s, tanggal=%s, waktu_mulai=%s, waktu_berakhir=%s, nama_pemateri=%s, 
        poster=%s, deskripsi=%s, link_conference=%s, password=%s
        WHERE is_delete=0 AND kode=%s
        """

QUERY_DELETE_EVENT_BY_KODE = """
        UPDATE event
        SET poster=NULL, is_delete=1
        WHERE kode=%s
        """

QUERY_DELETE_EVENT_BY_ID = """
        UPDATE event
        SET poster=NULL, is_delete=1
        WHERE id=%s
        """

QUERY_CHECK_DUPLICATE_KEHADIRAN = """
        SELECT * FROM kehadiran
        WHERE id_event=%s AND email_peserta=%s AND is_delete=0
        """

QUERY_GET_ALL_KEHADIRAN_BY_EVENT ="""
        SELECT id, email_peserta, nama_peserta, kode_kehadiran
        FROM kehadiran
        WHERE id_event=%s AND is_delete=0
        LIMIT %s
        OFFSET %s
        """

QUERY_GET_KEHADIRAN_BY_ID = """
        SELECT id, email_peserta, nama_peserta, kode_kehadiran, link_sertifikat
        FROM kehadiran
        WHERE id=%s AND is_delete=0
        """

QUERY_GET_KEHADIRAN_BY_KODE = """
        SELECT id, email_peserta, nama_peserta, kode_kehadiran, link_sertifikat
        FROM kehadiran
        WHERE kode_kehadiran=%s AND is_delete=0
        """


    