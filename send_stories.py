import time
import requests

TOKEN = "8893826051:AAGLwe5hblnVCmhD4Iyv692jzs-6thqO7Ms"
CHAT_ID = "@cleopatramagnet"
DIR = "/Users/eldragon/git/el/cleopatramagnet/src/assets/darkfem/indo_image"

def send_story(photo_filename, teaser, story_text):
    photo_path = f"{DIR}/{photo_filename}"
    
    # 1. Send Photo
    print(f"Sending photo: {photo_filename}...")
    photo_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo_file:
        res = requests.post(photo_url, data={
            'chat_id': CHAT_ID,
            'caption': teaser,
            'parse_mode': 'HTML'
        }, files={
            'photo': photo_file
        })
    print("Photo response:", res.json())
    time.sleep(3)
    
    # 2. Send Text
    print("Sending text story...")
    text_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    res = requests.post(text_url, data={
        'chat_id': CHAT_ID,
        'text': story_text,
        'parse_mode': 'HTML',
        'disable_web_page_preview': 'true'
    })
    print("Text response:", res.json())
    time.sleep(5) # Delay before next story to ensure clear visual separation

stories = [
    # Story 1
    {
        "photo": "angle1-Silent_Power.webp",
        "teaser": "👑 <b>Pernah gak sih kamu merasa doi pelit banget perhatian? Ini rahasianya...</b>",
        "text": """Hai ladies, untuk kamu yang bermasalah dengan doi yang pelit banget perhatian, ini nih akarnya, tau gak?

Sebenarnya, pria itu bukan terlahir "cuek". Mereka hanya merespon frekuensi energi yang kamu pancarkan. Semakin kamu berusaha keras mengejar, membanjiri dia dengan chat, dan selalu <i>available</i> 24/7, semakin otaknya mengkategorikan kamu sebagai "sudah aman di tangan". Sesuatu yang selalu ada secara biologis tidak akan lagi diperjuangkan. Itulah kenapa kamu sering merasa <i>invisible</i> dan seakan mengemis cinta di dekatnya. Rasa sakitnya luar biasa saat pesanmu hanya dibaca, atau dibalas seadanya setelah berjam-jam, sementara dia asyik online.

Solusinya? Tarik energimu kembali dan bangun <b>Magnetic Presence</b>. Bukan dengan <i>silent treatment</i> yang manipulatif dan kekanak-kanakan, tapi dengan keanggunan. Di dalam <b>Ebook Dark Feminine</b> dan <b>Audio Workbook 30 Hari</b> Cleopatra Magnet, kamu akan dipandu step-by-step mencabut energimu dari dia dan mengalirkannya ke dirimu sendiri.

<b>Kisah Laras (26 th) - Dari "Invisible" Jadi Prioritas Utama:</b>
"Dulu aku yang selalu chat duluan, nanya 'lagi apa? udah makan?'. Gebetan cuma balas seadanya. Nyesek banget rasanya ngelihat dia online tapi chatku dianggurin. Aku capek nangis tiap malam. Lalu aku nemu <b>Ebook Dark Feminine</b> dan <b>Audio Workbook</b>. Aku dengerin audionya setiap pagi sambil siap-siap kerja. Aku mulai praktek <b>Jurus Jeda 3 Detik</b> dan <b>Orbit Detox</b> dari panduan ini. Aku stop inisiatif, stop stalking sosmednya. 

Minggu pertama, dia biasa aja. Aku sempat goyah, tapi aku buka lagi lembar evaluasi di Workbook. Masuk hari ke-14, keajaiban terjadi. Dia mulai panik! Tiba-tiba dia yang nge-spam chat, nanyain aku kemana aja kok ngilang. Puncaknya di hari ke-21, dia nyamperin ke kantorku bawain kopi favoritku sambil bilang, 'Aura kamu akhir-akhir ini beda banget, bikin aku kepikiran terus.' Sekarang, dia yang ngemis waktuku."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 2
    {
        "photo": "istritest3-Suami_Perhatian_HP.webp",
        "teaser": "👑 <b>Pernah gak sih kamu merasa suami berubah cuek dingin setelah menikah? Ini akarnya...</b>",
        "text": """Untuk kamu ladies yang bermasalah dengan suami yang cuek, dingin, dan lebih asyik dengan HP atau game daripada mengobrol denganmu, ini nih akarnya, tau gak?

Setelah menikah bertahun-tahun, rutinitas membunuh misteri. Kamu mengambil alih semua peran: istri, ibu, bahkan manajer rumah tangga yang selalu mengingatkan ini itu. Kamu terus ngomel meminta perhatiannya, menangis karena merasa tidak dihargai. Agitasi ini menyakitkan—tinggal satu atap, tidur di ranjang yang sama, tapi rasanya berjarak ribuan kilometer. Saat pria merasa kamu sudah 100% "dikuasai" dan kamu yang selalu merawat hubungan sendirian, insting mengejarnya mati total.

Solusinya adalah mengembalikan dinamika <i>tarik-ulur</i> elegan khas <b>Dark Feminine Istri</b>. Lewat <b>Ebook Dark Feminine</b> dan <b>Audio Workbook 30 Hari</b>, kamu akan dibimbing men-track tahapanmu menghentikan omelan, menciptakan ruang emosional, dan membuat dia merindukan kehadiranmu yang memudar.

<b>Kisah Mbak Vera (32 th) - Menyalakan Kembali Percikan:</b>
"Lima tahun nikah, suamiku pulang kerja langsung main HP atau mabar sampai tengah malam. Kalau ditegur malah marah. Aku depresi banget rasanya. Sampai aku nemuin paket <b>Ebook & Audio Workbook</b> Cleopatra Magnet. Aku rutin dengerin audionya sebelum tidur untuk menenangkan <i>anxiety</i> ku. Sesuai workbook, aku stop ngomel. Aku ubah fokusku. Hari ke-7, aku mulai dandan cuma buat nongkrong di ruang tamu sambil baca buku favoritku, pura-pura dia nggak ada. 

Masuk hari ke-15, dia mulai gelisah. Dia letakkan HP-nya dan terus curi-curi pandang. Di hari ke-20, tiba-tiba dia peluk aku dari belakang dan ngajak <i>date night</i> berdua <i>weekend</i> ini. Sesuatu yang udah 3 tahun nggak pernah dia lakuin! Dia bilang kangen ngobrol sama aku."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 3
    {
        "photo": "df06_fuckboy_cycle.webp",
        "teaser": "👑 <b>Tahukah kamu kenapa doi tiba-tiba ghosting padahal awalnya manis? Ini jawabannya...</b>",
        "text": """Halo ladies, untuk kamu yang bermasalah dengan doi yang tiba-tiba pelit banget perhatian, ghosting, dan menarik diri padahal awalnya super manis, ini nih akarnya, tau gak?

Saat seorang pria "maju mundur", itu karena di fase awal pendekatan kamu memberikan <i>segalanya</i>. Kamu terlalu cepat luluh, membalas pesannya dalam sedetik, mengiyakan semua ajakannya, dan menceritakan seluruh hidupmu. Rasa penasarannya habis sebelum waktunya. Sakit sekali rasanya ketika kemarin kalian ngobrol sampai pagi, tapi hari ini dia menghilang bak ditelan bumi tanpa penjelasan apapun, membuatmu overthinking dan menyalahkan diri sendiri.

Solusinya, jadilah wanita yang sangat sulit diprediksi dengan sistem <b>Anti-Ghosting</b>. Melalui <b>Ebook Dark Feminine</b> dan <b>Audio Workbook 30 Hari</b>, kamu akan mempraktekkan cara merestrukturisasi batas emosionalmu. Kamu akan belajar mengontrol laju percakapan dan <i>availability</i> mu.

<b>Kisah Anya (24 th) - Memutar Balik Keadaan Siklus Ghosting:</b>
"Ada cowok yang deketin aku intens banget. Tiap hari telponan. Terus minggu depannya dia ngilang, chat cuma dibaca. Hancur banget rasanya harga diriku. Untung aku langsung nemu <b>Ebook & Audio Workbook</b> ini. Aku dengerin panduan audionya buat nahan godaan pengen ngechat duluan. Aku isi jurnal di workbooknya tiap hari. 

Aku terapkan <b>Jurus Mirroring</b> dan memancarkan <b>Aura Misteri</b>. Aku sibukin diri dan posting pencapaian kerjaku tanpa ada galau-galaunya. Hari ke-10, dia muncul lagi nge-reply story aku, 'Hei, apa kabar?'. Dulu aku pasti langsung bales heboh. Tapi sesuai workbook, aku tahan. Aku baru bales besok paginya dengan sangat singkat. Masuk hari ke-18, dia panik dan mohon-mohon minta ketemu karena sadar dia hampir kehilanganku selamanya. Sekarang, dia yang terus ngejar-ngejar aku!"

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 4
    {
        "photo": "winner-Stop_Jadi_Opsi-SENT.webp",
        "teaser": "👑 <b>Pernah gak sih kamu merasa cuman dijadikan pilihan kedua oleh doi? Ini faktanya...</b>",
        "text": """Dear ladies, untuk kamu yang bermasalah dengan pasangan yang pelit banget perhatian padamu tapi justru "royal" ke orang lain atau wanita lain, ini nih akarnya, tau gak?

Ini adalah kenyataan psikologis yang sangat pahit: Pria tidak meremehkanmu karena ada wanita lain yang lebih cantik. Mereka menempatkanmu sebagai pilihan kedua karena kamu sendiri yang meletakkan dirimu di posisi itu. Saat kamu terus-terusan mengalah, berkorban habis-habisan (finansial dan emosional), dan mentolerir pengabaiannya, dia melihatmu sebagai <i>pasti</i> dan <i>tidak akan kemana-mana</i>. Hati siapa yang tidak hancur saat memergoki pasangan lebih antusias membalas pesan orang lain daripada mendengarkan keluh kesahmu?

Solusinya adalah kebangkitan kembali harga dirimu secara radikal. Bangun otoritas tak terbantahkan dengan <b>Proteksi Dark Feminine</b>. Di dalam <b>Ebook</b> dan <b>Audio Workbook 30 Hari</b>, kamu akan dibimbing penuh untuk menaikkan <i>self-worth</i> mu ke level tertinggi, menyadari nilaimu yang sebenarnya.

<b>Kisah Bunda Rini (35 th) - Mengambil Kembali Mahkota Pernikahannya:</b>
"Aku tahu suamiku punya wanita idaman lain. Dulu aku nangis-nangis di kakinya ngemis supaya dia berubah. Makin aku ngemis, dia makin semena-mena dan berani terang-terangan telponan di depanku. Mentalku hancur lebur. Lalu aku temukan sistem <b>Dark Feminine Ebook & Audio Workbook</b>. 

Hari 1 sampai 5 paling berat, tapi audionya bener-bener menguatkan aku. Aku berhenti bertanya dia kemana. Aku terapkan <b>Silent Treatment Berkelas</b>. Aku rawat diriku habis-habisan, beli baju baru, ikut kelas pilates, dan pulang malam dengan wajah ceria tanpa peduli dia ada di rumah atau nggak. Hari ke-14, perubahanku bikin dia ketakutan. Dia bingung kenapa aku nggak nangis lagi. Hari ke-25, dia mutusin selingkuhannya sendiri dan sujud di depanku minta ampun, takut banget aku bakal ninggalin dia."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 5
    {
        "photo": "angle6-Tidak_Pernah_Minta.webp",
        "teaser": "👑 <b>Tahukah kamu mengapa kamu selalu dapet pasangan yang pasif dan benalu? Ini penyebabnya...</b>",
        "text": """Hai ladies yang tangguh, untuk kamu yang selalu dapet pasangan yang pelit inisiatif, pasif, dan justru kamu yang malah jadi "provider" dalam hubungan, ini nih akarnya, tau gak?

Kamu mengadopsi energi maskulin yang terlalu kuat. Karena pengalaman masa lalu yang mengharuskanmu mandiri, kamu membangun tembok tebal. Pria di sekitarmu merasa tidak punya ruang untuk menjadi "pria". Kamu selalu inisiatif duluan, bayar kencan duluan, dan mengurus segalanya. Hasilnya? Kamu menarik pria-pria pasif dan benalu yang dengan senang hati menyerahkan tanggung jawab padamu. Capek dan muak kan rasanya berjuang sendirian sementara dia ongkang-ongkang kaki?

Solusinya adalah mengaktifkan mode <b>Softlife Protocol</b>. Kamu harus belajar merendahkan tembok pertahananmu dengan sangat anggun. Melalui <b>Ebook Dark Feminine</b> dan panduan harian di <b>Audio Workbook 30 Hari</b>, kamu akan mempraktekkan seni melepaskan kendali.

<b>Kisah Dina (28 th) - Dari Wanita Pekerja Keras Menjadi Ratu:</b>
"Aku wanita karir yang terbiasa mandiri. Tiap nge-date, aku selalu nawarin bayar. Ujung-ujungnya aku ditumpangin cowok pengangguran yang kerjaannya main PS doang. Putus dari dia, aku trauma. Terus aku mulai dengerin <b>Audio Workbook</b> Cleopatra Magnet tiap pagi di mobil. 

Aku ubah total caraku bersikap. Di hari ke-12, pas aku diajak jalan sama kenalan baru, aku praktek <b>The Art of Receiving</b>. Aku diam saja saat <i>bill</i> makanan datang, dan aku biarkan dia membukakan pintu mobil untukku. Awalnya aneh, tapi pria itu terlihat sangat bangga bisa melayaniku! Masuk hari ke-28, pria mapan ini makin gencar mengejarku. Dia bahkan ngirim makan siang premium ke kantorku karena takut aku telat makan. Aku sekarang diperlakukan murni seperti seorang Ratu."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 6
    {
        "photo": "df04_teman_curhat.webp",
        "teaser": "👑 <b>Pernah gak sih kamu terjebak friendzone dan cuman dijadikan teman curhat? Ini rahasianya...</b>",
        "text": """Untuk kamu ladies yang terjebak <i>friendzone</i> dengan doi yang pelit banget perhatian romantis dan cuma menganggapmu pendengar setia keluh kesahnya, ini nih akarnya, tau gak?

Kamu sedang memberikan <i>girlfriend privileges</i> (fasilitas pacar) secara cuma-cuma. Kamu selalu <i>available</i> saat dia butuh bahu untuk bersandar, kamu membawakan bekal, kamu jadi tempat sampah emosionalnya. Tapi saat dia butuh romansa? Dia mencarinya di wanita lain yang lebih "menantang". Rasa perihnya gak karuan saat melihat dia memuja wanita lain, sementara kamu yang selalu ada di saat dia jatuh justru dianggap "bro" saja.

Solusinya, putus siklus beracun itu dengan <b>Misteri Keterjangkauan</b>. Berhentilah menjadi ibu peri yang penurut. Gunakan <b>Ebook Dark Feminine</b> dan jadwal ketat dari <b>Audio Workbook 30 Hari</b> untuk mengurangi akses dia terhadap kebaikanmu secara drastis, menciptakan ruang yang memaksa otaknya memandangmu dari kacamata pria ke wanita.

<b>Kisah Sari (25 th) - Keluar Secara Ekstrem dari Zona Teman:</b>
"Tiga tahun aku cuma jadi bayang-bayangnya. Kalau dia diputusin pacarnya, aku yang ngehibur. Sakit banget dadaku tiap dengar dia sebut nama cewek lain. Sampai aku muak dan memutuskan beli paket <b>Ebook</b> dan <b>Audio Workbook</b> ini. 

Aku mulai program di hari pertama: <b>Access Denied</b>. Aku kurangi intensitas bales chatnya secara radikal. Aku stop ngasih saran dan bilang, 'Sorry aku lagi sibuk siap-siap mau keluar nih'. Di hari ke-10, pas kita nggak sengaja ketemu bareng temen-temen lain, aku tampil beda. Aku pakai <i>dress</i> yang memancarkan aura feminin dan lebih banyak senyum misterius ke orang lain dibanding ke dia. Matanya nggak bisa lepas dari aku. Hari ke-24, dia tiba-tiba cemburu buta pas ada cowok lain minta nomorku. Malam itu juga dia nembak aku karena sadar nggak bisa hidup tanpa eksistensiku."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 7
    {
        "photo": "winner-Satu_Perubahan-SENT.webp",
        "teaser": "👑 <b>Tahukah kamu mengapa omelanmu justru membuat suami semakin cuek dan menjauh? Ini jawabannya...</b>",
        "text": """Hai ladies, untuk kamu yang bermasalah dengan suami yang pelit perhatian dan setiap kali kamu memprotes sikap cueknya, dia malah semakin marah dan menjauh, ini nih akarnya, tau gak?

Pria memiliki ego setinggi gunung es. Saat kamu menuntut, menangis, dan melontarkan kalimat seperti "kamu nggak pernah merhatiin aku lagi!", otaknya mencerna itu sebagai serangan kompetisi. Rumah berubah menjadi medan perang. Dia tidak melihat tangisanmu sebagai permintaan cinta, melainkan sebagai beban tambahan yang membuatnya memilih untuk semakin menarik diri atau bekerja sampai larut malam. Sungguh membuat frustrasi saat semua usahamu berkomunikasi justru direspons dengan tembok kebisuan.

Solusinya adalah keheningan mutlak lewat teknik <b>Radiant Detachment</b>. Berhentilah mencoba memperbaikinya. Melalui ilmu di <b>Ebook Dark Feminine</b> dan pelacakan emosi harian di <b>Audio Workbook 30 Hari</b>, kamu akan memindahkan energi putus asamu menjadi energi kemandirian emosional yang bersinar terang.

<b>Kisah Mama Nindy (31 th) - Mengembalikan Cinta Suami yang Dingin:</b>
"Aku sering teriak-teriak dan banting barang saking stresnya dicuekin suami. Makin aku marah, dia makin sering pulang jam 11 malam. Keluarga kami di ujung tanduk. Lalu aku nemu solusi <b>Dark Feminine Ebook & Audio Workbook</b>. 

Aku dengar audionya tiap pagi untuk men-setting <i>mindset</i> ratu. Aku berhenti total mengirim pesan panjang lebar mempertanyakan dia di mana. Hari 1 sampai hari ke-7, rumah hening. Aku pakai waktu itu buat rawat diri, yoga, dan <i>enjoy</i> sama diriku sendiri. Pas dia pulang, aku senyum bahagia tapi sibuk dengan drakorku, seolah dia nggak ada efeknya ke bahagiaku. Di hari ke-14, keheninganku berhasil mengintimidasinya. Dia mulai nanya, 'Kamu kenapa? Kok seneng banget sekarang?'. Di hari ke-21, dia membatalkan jadwal kerjanya di <i>weekend</i> hanya untuk ngajak aku liburan berdua, persis kayak jaman pacaran dulu."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 8
    {
        "photo": "df09_wake_up_call.webp",
        "teaser": "👑 <b>Pernah gak sih kamu terjebak di lingkaran setan bersama pria toxic dan kasar? Ini penjelasannya...</b>",
        "text": """Untuk kamu ladies yang bermasalah karena selalu kembali ke pelukan pria toxic, manipulatif, dan sering menyiksamu dengan tarik-ulur emosional, ini nih akarnya, tau gak?

Pria toxic adalah predator insting yang mencari mangsa dengan <i>boundaries</i> (batasan) terendah. Mereka tahu persis bahwa dengan memberikan sedikit saja remah-remah cinta basi setelah mereka menyakitimu, kamu akan langsung luluh dan memaafkan seribu kesalahan fatal mereka. Kamu memancarkan ketakutan akan kesepian yang tercium sangat kuat oleh mereka. Terjebak dalam lingkaran ini merusak saraf dan kewarasanmu secara perlahan.

Solusinya, bangun perisai pertahanan <b>Standar Cleopatra</b>. Kamu harus menghancurkan rasa takut kehilangan itu dari akarnya. <b>Ebook Dark Feminine</b> dan sesi terapi <b>Audio Workbook 30 Hari</b> akan menampar kesadaranmu dan membimbingmu melalui fase detoksifikasi brutal untuk merombak total fondasi <i>self-love</i> mu.

<b>Kisah Maya (27 th) - Bangkit Menjadi Wanita yang Tak Tersentuh:</b>
"Mantan pacarku itu raja manipulatif. Dia sering maki-maki aku, terus besoknya nangis-nangis minta maaf bawa hadiah. Bodohnya aku selalu nerima dia selama 2 tahun penuh. Mentalku hancur. Waktu aku baca <b>Ebook Dark Feminine</b> dan praktekin <b>Workbook 30 Hari</b>, hari pertama sampai ketiga aku menggigil nahan godaan pengen angkat teleponnya.

Tapi audio workbooknya membimbingku mengaktifkan <b>No Contact Rule</b> ekstrem. Hari ke-10, dia nyamperin ke tempat kosku bawa bunga, nangis memohon. Dulu aku pasti nangis bareng dia. Tapi hari itu, auraku sedingin es. Aku tatap matanya tajam dan bilang, 'Tinggalkan bunga itu dan jangan pernah muncul di depanku lagi.' Wajahnya pucat pasi melihat ketegasanku. Di hari ke-30, energi baruku ini malah menarik seorang pria mapan, dewasa, dan <i>gentleman</i> yang langsung mengajak komitmen serius tanpa drama."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 9
    {
        "photo": "df02_2am_scroll.webp",
        "teaser": "👑 <b>Tahukah kamu mengapa hubunganmu selalu mandek di status 'jalani aja dulu'? Ini faktanya...</b>",
        "text": """Hai ladies, untuk kamu yang terjebak dalam hubungan tanpa status, mengambang, dan penuh ketidakpastian (HTS), ini nih akarnya, tau gak?

Pepatah lama ini benar: Pria tidak akan pernah mau membeli sapi jika dia bisa terus mendapatkan susunya secara gratis. Selama kamu dengan bodohnya memberikan seluruh komitmen, kesetiaan, perhatian penuh, bahkan hak-hak eksklusif suami-istri tanpa dia harus memberikan label atau cincin, dia tidak punya satupun alasan untuk membawamu ke pelaminan. Kecemasanmu di jam 2 pagi mempertanyakan "kita ini sebenarnya apa?" adalah hasil dari terlalu murahnya kamu memberi akses.

Solusinya, kuasai hukum <b>Paradoks Komitmen</b>. Tunjukkan melalui tindakan bahwa zona eksklusifmu sangat mahal harganya. Panduan <b>Ebook Dark Feminine</b> dan langkah harian <b>Audio Workbook 30 Hari</b> akan memaksamu merenggut kembali hak istimewa yang kamu berikan kepadanya secara prematur.

<b>Kisah Rara (27 th) - Memaksa Komitmen Tanpa Sepatah Kata Pun:</b>
"Dua tahun kami HTS-an. Tiap disinggung soal nikah, alasannya klasik: 'lagi fokus nabung', 'belum siap', 'jalani aja dulu'. Aku sering nangis semalaman ngerasa dipermainkan. Sampai aku temukan senjata di <b>Ebook & Audio Workbook</b> ini. 

Sesuai instruksi di hari ke-5, aku mulai menarik semua <i>privilege</i> pacar yang aku kasih. Aku berhenti masak buat dia, berhenti mau diajak <i>staycation</i>, dan batasi jam obrolan malam. Pas dia nanya, 'Kamu kenapa berubah?', aku pakai teknik verbal <b>Dark Feminine</b>: 'Aku sadar waktu remajaku udah habis. Aku lagi fokus investasi ke hal-hal yang ngasih <i>return</i> pasti'. Dia <i>shock</i> berat. Memasuki hari ke-20, karena takut aku dilamar orang lain, dia datang bawa kedua orang tuanya malam-malam untuk meresmikan ikatan kami!"

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    },
    
    # Story 10
    {
        "photo": "df08_secret_she_knows.webp",
        "teaser": "👑 <b>Pernah gak sih kamu merasa pasangan berani berkata kasar atau merendahkanmu? Ini rahasianya...</b>",
        "text": """Dear ladies, untuk kamu yang bermasalah dengan pasangan yang lidahnya tajam, sering merendahkan usahamu, membanding-bandingkanmu, dan berkata sangat dingin, ini nih akarnya, tau gak?

Saat seorang pria berani meremehkanmu di depan wajahmu, itu karena di masa lalu reaksi pertamamu selalu menguntungkannya. Pria dengan sifat <i>narcissistic</i> dan ego tinggi mendapatkan kepuasan absolut saat melihat kata-katanya berhasil merobek emosimu. Semakin kamu menangis, berdebat panjang lebar, dan membela diri, semakin dia merasa berkuasa menindasmu. Kepedihan saat dihina oleh orang yang paling kita cintai itu menusuk sampai ke tulang.

Solusinya adalah mengaktifkan <b>Emotional Shield</b> dan memakai mahkota <b>Dark Queen Aura</b>. Kamu harus mencabut kenikmatannya menyiksamu dengan reaksi yang tidak pernah dia duga. Di dalam <b>Ebook</b> dan pelacakan reaksi <b>Audio Workbook 30 Hari</b>, kamu akan berlatih keras mematikan reaktivitas emosional dan menguasai <b>silent power</b>.

<b>Kisah Citra (29 th) - Mengubah Hinaan Menjadi Ketakutan Kehilangan:</b>
"Sejak aku melahirkan, tubuhku berubah. Suami mulai sering nyindir kasar, 'kamu kok sekarang nggak keurus sih, malu aku diajak kondangan'. Hancur perasaanku dengernya, dulu aku pasti balas marah sambil nangis sesenggukan, dan berujung aku yang minta maaf. 

Lalu aku mulai dengerin <b>Audio Workbook 30 Hari</b>. Aku praktekin jurus <b>Cold Stare</b> (Tatapan Dingin). Minggu lalu pas dia nyindir kasar lagi saat makan malam, aku nggak balas sepatah kata pun. Aku hentikan kunyahanku, aku tatap matanya dalam-dalam dengan wajah sedatar tembok es selama 5 detik, aku senyum tipis, lalu aku berdiri dan masuk ke kamar meninggalkannya sendirian. Kekuatanku itu bikin mentalnya <i>down</i>. Malamnya, dia nggak bisa tidur, gedor kamarku nangis minta maaf karena merasa auraku begitu mengintimidasi dan takut aku pergi darinya."

Kamu siap membuat kisahmu sendiri mendapat pasangan yang ideal sesuai keinginanmu mu ?
Ingat yah ladies Semesta tidak memberikan pria yang kamu mau, tapi hanya memberikan pria yang selaras denganmu, saat kamu siap. Persiap disini 
https://cleopatramagnet.com/?pay"""
    }
]

for i, story in enumerate(stories, 1):
    print(f"\n--- Sending Story {i} ---")
    send_story(story["photo"], story["teaser"], story["text"])

print("Successfully sent all 10 stories!")
