#!/bin/bash
TOKEN="8893826051:AAGLwe5hblnVCmhD4Iyv692jzs-6thqO7Ms"
CHAT_ID="@cleopatramagnet"
DIR="/Users/eldragon/git/el/cleopatramagnet/src/assets/darkfem/indo_image"

echo "Sending Photo..."
curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendPhoto?chat_id=${CHAT_ID}" \
  -F photo="@${DIR}/angle1-Silent_Power.webp" \
  -F caption="👑 <b>Mengapa Pria Menjadi Pelit Perhatian?</b>" \
  -F parse_mode="HTML"

sleep 2

echo -e "\nSending Text..."
curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendMessage" \
  -d chat_id="${CHAT_ID}" \
  -d text="Hai ladies, untuk kamu yang bermasalah dengan doi yang pelit banget perhatian, ini nih akarnya, tau gak?

Sebenarnya, pria itu bukan terlahir \"cuek\". Mereka hanya merespon frekuensi energi yang kamu pancarkan. Semakin kamu berusaha keras mengejar, membanjiri dia dengan chat, dan selalu <i>available</i> 24/7, semakin otaknya mengkategorikan kamu sebagai \"sudah aman di tangan\". Sesuatu yang selalu ada secara biologis tidak akan lagi diperjuangkan. Itulah kenapa kamu sering merasa <i>invisible</i> dan seakan mengemis cinta di dekatnya. Rasa sakitnya luar biasa saat pesanmu hanya dibaca, atau dibalas seadanya setelah berjam-jam, sementara dia asyik online.

Solusinya? Tarik energimu kembali dan bangun <b>Magnetic Presence</b>. Bukan dengan <i>silent treatment</i> yang manipulatif dan kekanak-kanakan, tapi dengan keanggunan. Di dalam <b>Ebook Dark Feminine</b> dan <b>Audio Workbook 30 Hari</b> Cleopatra Magnet, kamu akan dipandu step-by-step mencabut energimu dari dia dan mengalirkannya ke dirimu sendiri.

<b>Kisah Laras (26 th) - Dari \"Invisible\" Jadi Prioritas Utama:</b>
\"Dulu aku yang selalu chat duluan, nanya 'lagi apa? udah makan?'. Gebetan cuma balas seadanya. Nyesek banget rasanya ngelihat dia online tapi chatku dianggurin. Aku capek nangis tiap malam. Lalu aku nemu <b>Ebook Dark Feminine</b> dan <b>Audio Workbook</b>. Aku dengerin audionya setiap pagi sambil siap-siap kerja. Aku mulai praktek <b>Jurus Jeda 3 Detik</b> dan <b>Orbit Detox</b> dari panduan ini. Aku stop inisiatif, stop stalking sosmednya. 

Minggu pertama, dia biasa aja. Aku sempat goyah, tapi aku buka lagi lembar evaluasi di Workbook. Masuk hari ke-14, keajaiban terjadi. Dia mulai panik! Tiba-tiba dia yang nge-spam chat, nanyain aku kemana aja kok ngilang. Puncaknya di hari ke-21, dia nyamperin ke kantorku bawain kopi favoritku sambil bilang, 'Aura kamu akhir-akhir ini beda banget, bikin aku kepikiran terus.' Sekarang, dia yang ngemis waktuku.\"

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiapkan disini 
https://cleopatramagnet.com/?pay" \
  -d parse_mode="HTML" \
  -d disable_web_page_preview="true"
