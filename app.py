from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# Arayüzün ile sunucunun konuşabilmesi için CORS'u açıyoruz
CORS(app)

@app.route('/islem', methods=['POST'])
def islem():
    data = request.json
    komut = data.get('komut')
    
    # İşlem mantığı
    islemler = {
        'ai': 'AI Analiz Merkezi: Sistem taraması başlatıldı, tüm portlar güvenli.',
        'egitim': 'Eğitim Modülü: Siber savunma simülasyonları başarıyla yüklendi.',
        'temizlik': 'Sistem Temizliği: Önbellek ve geçici dosyalar başarıyla imha edildi.',
        'reklam_engelle': 'Ad-Blocker: Zararlı reklam scriptleri devre dışı bırakıldı.',
        'mail_uyari': 'Mail Uyarı: Kritik durum raporu operasyon merkezine iletildi.',
        'anonim': 'Anonim İletişim: Şifreli tünel kuruldu, bağlantı gizlendi.'
    }
    
    # Eğer komut listede varsa mesajı dön, yoksa hata ver
    mesaj = islemler.get(komut, "Bilinmeyen Komut: İşlem gerçekleştirilemedi!")
    
    return jsonify({"mesaj": mesaj})

# Render veya herhangi bir sunucuda çalışması için standart port ayarı
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)