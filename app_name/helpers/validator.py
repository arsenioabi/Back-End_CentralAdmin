from app_name.utilities import *

# Kumpulan fungsi untuk memvalidasi body request

def account_validator(nama,email,password):
    error_list =[]
    #validasi format nama
    validName = validateName(nama)
    if not validName:
        error_list.append("nama hanya boleh mengandung alphabet dan spasi")

    # Validasi format email
    validEmail = validateEmail(email)
    if not validEmail:
        error_list.append(f"format email tidak valid")

    # validasi password 
    invalid_password_list = validatepassword(password)
    if len(invalid_password_list) > 0:
        error_list += invalid_password_list

    return error_list 

def profile_validator(nama,jenis_kelamin, nomor_telepon,instagram,linkedin):
    error_list = []
    # validasi nama 
    validName = validateName(nama)
    if not validName:
        error_list.append(f"nama hanya boleh mengandung alphabet dan spasi")

    # validasi jenis_kelamin
    if jenis_kelamin and jenis_kelamin not in ["laki-laki","perempuan"]:
        error_list.append(f"jenis kelamin tidak valid")

    #validasi nomor telpon
    if nomor_telepon and not validatePhone(nomor_telepon):
        error_list.append(f"format nomor telepon tidak valid")

    #validasi url
    if instagram and not url_validator(instagram):
        error_list.append(f"format url instagram tidak valid")

    if linkedin and not url_validator(linkedin):
        error_list.append(f"format url linkedin tidak valid")

    return error_list


def update_password_validator(password_baru,confirm_password,password_lama,password_tersimpan):
    error_list = []
    if password_baru != confirm_password:
           error_list.append("password dan confirm password tidak sama")
    else:
        #cek apakah password lama sama dengan password yang tersimpan di database
        validPassword = checkPassword(password_tersimpan,password_lama)
        if not validPassword:      
               error_list.append("password lama salah")
                
        #cek apakah password baru sesuai format yang ditetapkan
        invalid_format_password_list = validatepassword(password_baru)
        if len(invalid_format_password_list) > 0:
            error_list += invalid_format_password_list 
            
    return error_list

def portofolio_validator(judul,deskripsi_singkat,deskripsi_lengkap):
    error_list = []
    if judul == "":
        error_list.append("Judul tidak boleh kosong")
    if deskripsi_singkat == "":
        error_list.append("deskripsi singkat tidak boleh kosong")
    if deskripsi_lengkap == "":
        error_list.append("deskripsi lengkap tidak boleh kosong")

    return error_list

def event_validator(nama,nama_pemateri,link_conference,contact_whatsapp=None):
    error_list = []
    if nama == "":
        error_list.append("nama tidak boleh kosong")
    if nama_pemateri == "":
        error_list.append("nama pemateri tidak boleh kosong")
    if link_conference == "" or not url_validator(link_conference):
        error_list.append("format url conference tidak valid")
    if validateWhatsappContact(contact_whatsapp):
        error_list.append("format penulisan kontak whatsapp tidak valid")

    return error_list

def kehadiran_validator(nama,email):
    error_list =[]
    #validasi format nama
    validName = validateName(nama)
    if not validName:
        error_list.append("nama hanya boleh mengandung alphabet dan spasi")

    # Validasi format email
    validEmail = validateEmail(email)
    if not validEmail:
        error_list.append(f"format email tidak valid")

    return error_list 

