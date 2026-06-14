from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Tüm kaynaklardan gelen isteklere izin ver
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/islem', methods=['POST', 'OPTIONS']) # OPTIONS metodunu ekledik!
def islem():
    if request.method == "OPTIONS": # Tarayıcının ön kontrol isteğini burada kabul ediyoruz
        return jsonify({}), 200
        
    data = request.json
    komut = data.get('komut')
    
    islemler = {
        'ai': 'AI Analiz Merkezi: Sistem taraması başlatıldı.',
        'egitim': 'Eğitim Modülü: Simülasyonlar yüklendi.',
        'temizlik': 'Sistem Temizliği: Önbellek temizlendi.',
        'reklam_engelle': 'Ad-Blocker: Reklamlar engellendi.',
        'mail_uyari': 'Mail Uyarı: Rapor gönderildi.',
        'anonim': 'Anonim İletişim: Tünel aktif.'
    }
    
    mesaj = islemler.get(komut, "Bilinmeyen Komut!")
    return jsonify({"mesaj": mesaj})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
