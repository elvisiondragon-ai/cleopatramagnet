# 🔄 Backup Revert: Presence Optimization Details

File ini berisi detail perubahan yang dilakukan pada persona `?presence` dan sinkronisasi Default setelah commit `6f0fb83`.

> [!NOTE]
> Perubahan ini di-revert karena `?presence` versi lama memiliki Conversion Rate 6% yang sangat baik.

## Git Diff (6f0fb83 -> cb82013)

```diff
diff --git a/src/App.tsx b/src/App.tsx
index 8eac1ef..bcab07f 100755
--- a/src/App.tsx
+++ b/src/App.tsx
@@ -290,17 +290,6 @@ const assetsMap: any = {
 
 const contentData: any = {
     id: {
-        agitText: <>Kamu diajari bahwa untuk dicintai, kamu harus berkorban, harus selalu ada, dan harus "menunjukkan" ketertarikanmu. <strong>ITU ADALAH KEBOHONGAN TERBESAR.</strong><br /><br />Ketika kamu terlalu mudah ditebak, selalu tersedia, dan terlalu eager, otak pria memprosesmu sebagai "barang murah" yang tidak perlu diperjuangkan. Mereka tidak tertantang. Tidak ada misteri. <strong>Tidak ada Magnetic Presence.</strong><br /><br />Wanita dengan Magnetic Presence tidak pernah mencari validasi. Saat dia diam, ketenangannya membunuh ego pria. Saat dia memandang, pria merasa dihakimi sekaligus terpesona. Dia tidak mengejar—dia menarik.<br /><br />Dan kabar buruknya: selama kamu masih memancarkan energi "butuh perhatian", kamu akan terus menarik pria yang hanya ingin mempermainkanmu, atau lebih parah... <strong>diabaikan sepenuhnya.</strong></>,
-        solText: <>Ini bukan sekadar tips "cara balas chat" dari TikTok. Ini adalah <strong>sistem psikologi kelas atas</strong> yang disembunyikan oleh wanita-wanita elit yang selalu mendapatkan apapun yang mereka inginkan.<br /><br />Dengan mempraktekkan Magnetic Presence, kamu akan mengubah frekuensi internalmu. Kamu akan memancarkan energi yang membuat pria secara biologis <strong>terobsesi</strong> untuk memenangkan perhatianmu.<br /><br />
-        <div style={{background:'rgba(139,92,246,0.08)',border:'1px solid rgba(139,92,246,0.25)',borderRadius:'16px',padding:'20px 18px',marginTop:'24px', marginBottom: '24px'}}>
-            <div style={{fontSize:'13px',fontWeight:700,letterSpacing:'0.12em',textTransform:'uppercase',color:'var(--purple-light)',marginBottom:'12px'}}>HASIL AKHIR MAGNETIC PRESENCE</div>
-            <img src={p_presence_cleopatra_secret} alt="Cleopatra Secret" style={{width: '100%', borderRadius: '12px', marginBottom: '16px', border: '1px solid rgba(255,255,255,0.1)'}} />
-            <img src={p_presence_softlife_v2} alt="Softlife Result" style={{width: '100%', borderRadius: '12px', marginBottom: '16px', border: '1px solid rgba(255,255,255,0.1)'}} />
-            <p style={{marginBottom:'12px'}}>Pria yang tadinya cuek akan berbalik memohon waktumu. Pria mapan di ruangan akan langsung menoleh saat kamu masuk.</p>
-            <p style={{marginBottom:'0'}}>Mereka tidak akan mengerti kenapa. Yang mereka tahu hanyalah: <strong>"Aku harus mendapatkan wanita ini, atau aku akan kehilangannya selamanya."</strong></p>
-        </div>
-        Berhenti menjadi pengemis perhatian. Mulailah menjadi <strong>Piala yang Diperebutkan</strong>.
-        </>,
         checks: [
             <>Seni <strong>MISTERI</strong> — bagaimana jadi wanita yang tidak bisa ditebak</>,
             <><strong>PUSH-PULL</strong> Dynamics — menarik dan mendorong bersamaan</>,
@@ -312,6 +301,79 @@ const contentData: any = {
             <><strong>Text Game</strong> — membuat dia ketagihan dari chat</>,
         ],
         checksPlus: "+ 44 jurus lainnya...",
+        agitH2a: "Kenapa Kamu Selalu Transparan",
+        agitH2b: "Di Ruangan Penuh Orang?",
+        agitText: <>Kamu diajari bahwa untuk dicintai, kamu harus berkorban, harus selalu ada, dan harus "menunjukkan" ketertarikanmu. <strong>ITU ADALAH KEBOHONGAN TERBESAR.</strong><br /><br />Ketika kamu terlalu mudah ditebak, selalu tersedia, dan terlalu eager, otak pria memprosesmu sebagai "barang murah" yang tidak perlu diperjuangkan. Mereka tidak tertantang. Tidak ada misteri. <strong>Tidak ada Magnetic Presence.</strong><br /><br />Wanita dengan Magnetic Presence tidak pernah mencari validasi. Saat dia diam, ketenangannya membunuh ego pria. Saat dia memandang, pria merasa dihakimi sekaligus terpesona. Dia tidak mengejar—dia menarik.<br /><br />Dan kabar buruknya: selama kamu masih memancarkan energi "butuh perhatian", kamu akan terus menarik pria yang hanya ingin mempermainkanmu, atau lebih parah... <strong>diabaikan sepenuhnya.</strong></>,
+        solText: <>Ini bukan sekadar tips "cara balas chat" dari TikTok. Ini adalah <strong>sistem psikologi kelas atas</strong> yang disembunyikan oleh wanita-wanita elit yang selalu mendapatkan apapun yang mereka inginkan.<br /><br />Dengan mempraktekkan Magnetic Presence, kamu akan mengubah frekuensi internalmu. Kamu akan memancarkan energi yang membuat pria secara biologis <strong>terobsesi</strong> untuk memenangkan perhatianmu.<br /><br />
+        <div style={{background:'rgba(139,92,246,0.08)',border:'1px solid rgba(139,92,246,0.25)',borderRadius:'16px',padding:'20px 18px',marginTop:'24px', marginBottom: '24px'}}>
+            <div style={{fontSize:'13px',fontWeight:700,letterSpacing:'0.12em',textTransform:'uppercase',color:'var(--purple-light)',marginBottom:'12px'}}>HASIL AKHIR MAGNETIC PRESENCE</div>
+            <img src={p_presence_cleopatra_secret} alt="Cleopatra Secret" style={{width: '100%', borderRadius: '12px', marginBottom: '16px', border: '1px solid rgba(255,255,255,0.1)'}} />
+            <img src={p_presence_softlife_v2} alt="Softlife Result" style={{width: '100%', borderRadius: '12px', marginBottom: '16px', border: '1px solid rgba(255,255,255,0.1)'}} />
+            <p style={{marginBottom:'12px'}}>Pria yang tadinya cuek akan berbalik memohon waktumu. Pria mapan di ruangan akan langsung menoleh saat kamu masuk.</p>
+            <p style={{marginBottom:'0'}}>Mereka tidak akan mengerti kenapa. Yang mereka tahu hanyalah: <strong>"Aku harus mendapatkan wanita ini, atau aku akan kehilangannya selamanya."</strong></p>
+        </div>
+        Berhenti menjadi pengemis perhatian. Mulailah menjadi <strong>Piala yang Diperebutkan</strong>.
+        </>,
+        paramAgitation: {
+            label: "AGITASI — REALITA YANG MENYAKITKAN",
+            h2a: "Kenapa Kamu Selalu Terlihat,",
+            h2b: "Tapi Tidak Pernah Diinginkan?",
+            imgKey: 'p_presence_Campaign_Test_df_0412_g5',
+            body: <>Kamu selalu membalas chatnya dalam 3 detik. Kamu selalu siap sedia saat dia butuh teman curhat. Kamu membelikannya makanan kesukaannya, memberikan senyum terbaikmu, dan selalu <strong>mengalah demi dia</strong>.<br /><br /><strong>TAPI APA BALASANNYA?</strong><br /><br />Dia membalas chatmu 5 jam kemudian. Dia membatalkan janji di menit terakhir dengan alasan "sibuk". Dan yang paling menghancurkan... dia justru mati-matian mengejar wanita lain yang <strong>bahkan tidak peduli padanya</strong>.<br /><br />Kamu menangis di kamar, bertanya "Apa yang kurang dariku?"<br /><br />Kamu tidak kurang cantik. Kamu tidak kurang baik. <strong>Kamu hanya tidak punya KHARISMA.</strong> Kamu memancarkan energi "selalu ada" yang membuat otak pria memprosesmu sebagai barang obral yang tidak perlu diperjuangkan.</>,
+        },
+        paramHope: {
+            label: "VISI BARU — HIDUP YANG BISA MENJADI MILIKMU",
+            h2a: "Bayangkan Kamu Masuk Ruangan",
+            h2b: "Dan Semuanya Berubah.",
+            imgKey: 'p_presence_df_0424_ad07_single_sahabat',
+            body: <>Bayangkan: kamu masuk kafe Sabtu sore. Tidak ada outfit istimewa, tidak ada makeup mahal — tapi <strong>3 kepala otomatis menoleh.</strong> Barista pria yang biasanya datar tiba-tiba salah ketik orderan karena gugup. Pria di meja sebelah pura-pura sibuk dengan laptop, tapi matanya curi pandang setiap 30 detik.<br /><br />Bayangkan: pria yang <strong>dulu ghosting kamu</strong> — tiba-tiba muncul di DM bulan depan, "Hai, lama ga ngobrol. Apa kabar?" Kamu read, smile, tidak balas. Karena kamu sudah <strong>level berbeda</strong> sekarang.<br /><br />Bayangkan: di kantor, ada CEO baru. Selama 2 minggu pertama, dia tidak pernah benar-benar memandang siapapun. Sampai suatu hari, dia melewati meja kamu, berhenti sebentar, dan tanya: "Sudah lunch?" Itulah <strong>magnetic presence</strong> bekerja.</>,
+        },
+        paramHowItWorks: {
+            label: "BAGAIMANA INI BEKERJA",
+            h2a: "3 Tahap Membangun",
+            h2b: "Frekuensi Magnetic.",
+            imgKey: 'p_presence_presence_01_diam_membunuh_1777550881301',
+            steps: [
+                { num: '1', title: 'AUDIT KEBOCORAN ENERGI (Hari 1-7)', body: 'Kamu identifikasi 7 micro-leak yang menjatuhkan frekuensimu — tempo balas chat, eye contact yang terlalu lama, senyum yang terlalu cepat, "sorry" yang berlebihan, justifikasi yang tidak diminta. Kamu sadar persis di mana energi kamu "tumpah" setiap hari.' },
+                { num: '2', title: 'RESET POLA INTERNAL (Hari 8-21)', body: 'Kamu ganti micro habits dengan protokol baru: jeda 3 detik sebelum bicara, postur "high status", regulasi reaksi emosional. Otakmu mulai mengirim sinyal baru ke orang lain — tanpa kamu harus pura-pura.' },
+                { num: '3', title: 'ANCHORING — JADI OTOMATIS (Hari 22+)', body: 'Setelah 3 minggu, frekuensi baru sudah jadi default. Kamu tidak lagi "berusaha" magnetic. Auramu bicara duluan, sebelum kata-kapamu. Pria mulai mendekati tanpa kamu undang. Wanita mulai mengamati cara kamu duduk. Dunia menyesuaikan ke arahmu.' },
+            ],
+        },
+        paramObjections: {
+            label: "PERTANYAAN UMUM",
+            h2a: "Tapi Bagaimana",
+            h2b: "Kalau...?",
+            items: [
+                { q: "Saya introvert parah, bisa bicara saja sudah gugup. Apakah ini cocok untuk saya?", a: "Justru introvert adalah modal terbaik magnetic presence. Wanita introvert sudah memiliki 50% komponen alaminya: ketenangan, jeda, tidak butuh banyak validasi. Yang kamu pelajari hanya bagaimana mengarahkan kekuatan diam itu. Banyak pembaca paling sukses adalah introvert berat." },
+                { q: "Saya sudah 38 tahun. Apakah belum terlambat?", a: "Magnetic presence justru lebih powerful di usia 30+ karena didukung maturity yang tidak bisa difake oleh wanita 20-an. Banyak pengguna mendapat hasil terbaik di usia 35-45 — termasuk dilamar oleh pria 5-7 tahun lebih muda yang sebelumnya 'tidak menyadari mereka'." },
+                { q: "Apakah ini hanya teori? Saya sudah baca banyak self-help.", a: "Ini bukan teori 'love yourself first'. Ini 52 jurus konkret dengan langkah harian yang bisa kamu praktekkan langsung. Setiap jurus disertai contoh kalimat, contoh sikap, dan contoh skenario nyata. Bukan motivasi — protokol." },
+            ],
+        },
+        paramSocialProof: {
+            label: "BUKTI TRANSFORMASI — SEBELUM & SESUDAH",
+            h2a: "3 Wanita.",
+            h2b: "3 Frekuensi Yang Berubah.",
+            transformations: [
+                {
+                    name: 'Rini, 27 thn — Project Manager',
+                    imgKey: 'p_presence_presence_01_diam_membunuh_v2_1777550965342',
+                    before: 'Saya hidup di Slack & WhatsApp. Setiap pria yang approach, dalam 2 minggu pasti hilang. Saya pikir saya "terlalu sibuk untuk mereka". Padahal aslinya saya "terlalu kelihatan butuh validasi" — chat balasan 30 detik, follow back IG-nya hari pertama, like setiap story-nya.',
+                    after: 'Setelah 21 hari praktek, Senior Director kantor saya sendiri yang DM saya duluan — padahal 2 tahun cuek total. Yang berubah cuma satu: saya berhenti membalas dalam hitungan detik. Saya berhenti tertawa di setiap candaan. Saya jadi diam. Dan sekarang dia yang mengejar saya.',
+                },
+                {
+                    name: 'Mira, 32 thn — Dokter Gigi',
+                    imgKey: 'p_presence_presence_02_invisible_dunia_v2_1777550999292',
+                    before: 'Saya cantik (semua bilang gitu), karir bagus, mandiri secara finansial. Tapi setiap kali ke kondangan, saya selalu pulang sendirian. Pria-pria mapan tertarik 1-2 minggu lalu menghilang. Saya mulai berpikir mungkin saya "intimidating".',
+                    after: 'Bukan saya yang intimidating. Saya yang frekuensinya salah — terlalu mengejar percakapan. Setelah saya pelajari jeda dan eye contact yang tepat, dalam 3 bulan saya bertemu seorang pengusaha 38 tahun yang bilang "saya kira kamu tidak akan tertarik dengan saya, makanya saya nekat ngajak ngobrol duluan". Sekarang kami sudah tunangan.',
+                },
+                {
+                    name: 'Anya, 24 thn — Mahasiswa S2',
+                    imgKey: 'p_presence_Campaign_Test_df_0412_g5',
+                    before: 'Saya selalu jadi "teman dekat" — tidak pernah jadi yang mereka kejar. Dengar curhatan banyak pria, tapi tidak ada yang serius mendekati saya. Saya merasa transparan di kelas penuh wanita yang lebih "biasa" dari saya tapi punya pacar.',
+                    after: 'Saya sadar saya selalu memberi semua dalam percakapan pertama — bercerita panjang, tertawa keras, langsung memberi solusi atas masalah mereka. Setelah saya terapkan jurus mystery dan jeda, dosen pembimbing saya mengundang saya makan malam private (saya sopan menolak), dan dua teman lama tiba-tiba "menyadari" saya. Salah satunya sekarang pacar saya.',
+                },
+            ],
+        },
         testis: [
             { text: "Demi allah sis, baru 2 minggu praktekin jurus 7... cowok yang dulu ghosting gue TIBA-TIBA nge-DM lagi. Padahal gue ga ngapa-ngapain. Cuma DIEM. Ternyata itu ilmunya 😭🔥", name: "Anisa, 24 thn", time: "2 hari lalu" },
             { text: "Suami gue yang tadinya cuek, sekarang GELISAH kalau gue keluar rumah. Bukan karena posesif. Tapi karena dia mulai TAKUT KEHILANGAN. Jurus 1 doang udah sedahsyat ini.", name: "Sari, 31 thn", time: "5 hari lalu" },
@@ -397,15 +459,10 @@ const contentData: any = {
             items: [
                 { imgs: ['singleC2First','singleC2S2','singleC2S3','singleC2S4'], title: "Dulu vs Sekarang", desc: "Mengingat masa pacaran yang penuh bunga, sementara sekarang hanya ada rutinitas yang membosankan dan hambar." },
                 { imgs: ['singleC4First','singleC4S2','singleC4S3','singleC4S4'], title: "Bersaing dengan Layar HP", desc: "Lelah mencoba menarik perhatiannya, tapi dia lebih memilih scroll sosmed daripada menatap matamu." },
-                { imgs: ['singleC5S1','singleC5S2','singleC5S3','singleC5S4'], title: "Dia Pilih Segalanya, Kecuali Kamu", desc: "Hobi, teman, hingga pekerjaan selalu jadi prioritas. Kamu hanya ada di daftar terakhir waktu luangnya." },
-                { imgs: ['newIstri9', 'newIstri4', 'newIstri9'], title: "DIA SEDANG MENGHAPUSMU DARI HIDUPNYA", desc: "Kamu pikir dia khilaf? Dia sedang menghapus jejakmu dari rekeningnya, dari rencana masa depannya, dan dari hatinya." },
-                { imgs: ['newIstri2'], title: "BANGUN RUMAH DENGAN UANGMU", desc: "Setiap kali dia bilang uang diputar untuk bisnis, wanita itu sedang memilih furnitur untuk apartemen barunya." },
-                { imgs: ['newIstri6'], title: "HANYA KEWAJIBAN", desc: "Sentuhannya terasa mekanis. Di tempat tidur, dia ingin segalanya cepat selesai karena pikirannya terbang ke wanita lain." },
-                { imgs: ['newIstri8'], title: "ANAKMU SUDAH TAHU", desc: "Kamu pikir bertahan demi anak itu mulia? Di mata mereka, kamu hanya mengajarkan cara menjadi korban." },
                 { imgs: ['newIstri11'], title: "PILIHAN KEDUA", desc: "Kamu mengorbankan segalanya demi keluarga, tapi dia mengorbankan keluarganya demi wanita lain." }
             ],
-            beforeAfterSingle: { imgs: ['baS1','baS2','baS3','baS4'], title: "", body: "" },
-            beforeAfterIstri: { imgs: ['baI1','baI2','baI3','baI4'], title: "", body: "" },
+            beforeAfterSingle: null,
+            beforeAfterIstri: null,
         },
         angleSection: {
 
@@ -448,8 +505,6 @@ const contentData: any = {
         painLabel: "RASA SAKIT MENJADI INVISIBLE",
         painH2a: "Semakin Kamu Berusaha Menarik Perhatian,",
         painH2b: "Semakin Cepat Mereka Melupakanmu.",
-        agitH2a: "Kenapa Usahamu Selalu",
-        agitH2b: "Berakhir Dengan Penolakan?",
         solLabel: "JAWABANNYA",
         solH2a: "Dark Feminine",
         solH2b: "52 Jurus Rahasia",
@@ -1131,6 +1186,26 @@ const DarkFeminineTSX = () => {
             { icon: "🌑", text: <>Lelah melihat wanita yang kurang menarik darimu mendapatkan <strong>pria mapan dan perlakuan ratu</strong>.</> },
             { icon: "👑", text: <>Saatnya berhenti mengemis perhatian. Mulai <strong>mengendalikan ruangan tanpa bersuara</strong>.</> },
         ],
+        stories: [
+            {
+                imgs: ['p_presence_presence_01_diam_membunuh_1777550881301'],
+                title: 'Dia Diam. Tapi Setiap Pria Di Ruangan Itu Sadar Dia Ada.',
+                body: `Pernah lihat wanita seperti itu? Dia masuk ke kafe, ke kantor, ke ruang meeting — dan tanpa bicara, atmosfer ruangan berubah.\n\nDia tidak teriak. Tidak posting OOTD setiap hari. Tidak nge-flex apapun. Tapi setiap pria diam-diam mencuri pandang. Setiap wanita diam-diam menelaah caranya berdiri, caranya duduk, caranya melihat.\n\nDan kamu? Kamu sudah menyiapkan outfit terbaik, makeup paling rapi, caption paling clever — tapi tetap merasa transparan. Seperti tidak ada yang benar-benar melihatmu.\n\nMasalahnya bukan penampilanmu. Masalahnya frekuensi yang kamu pancarkan.`
+            },
+            {
+                imgs: ['p_presence_Campaign_Test_df_0412_g5'],
+                title: 'Berhenti Mengejar. Mulai Menjadi Yang Dikejar.',
+                body: `Berapa banyak energi yang sudah kamu buang untuk "berusaha menarik perhatian"?\n\nReply chat dalam hitungan detik. Selalu jadi yang inisiatif. Selalu jadi yang bilang "kapan kita ketemu lagi?" duluan. Selalu jadi yang menyesuaikan jadwal.\n\nDan hasilnya? Mereka anggap kamu "selalu available" — alias mudah. Otak pria didesain untuk MENGEJAR. Yang terlalu mudah didapat, kehilangan nilainya secara biologis.\n\nMagnetic presence adalah kebalikannya. Kamu bukan menjadi sulit dijangkau — kamu menjadi seseorang yang nilainya terasa setiap dia mendekatimu.`
+            },
+            {
+                imgs: ['p_presence_df_0424_ad07_single_sahabat'],
+                title: 'Aura Bukan Tentang Kecantikan. Tapi Tentang Sertifikasi Internal.',
+                body: `Wanita dengan aura magnetic tidak selalu yang paling cantik. Kadang kulitnya biasa. Kadang badannya tidak ideal. Kadang umurnya sudah 35+.\n\nTapi cara dia memegang gelas, cara dia tertawa, cara dia mendengarkan — semuanya seperti membawa pesan: "Aku tahu siapa diriku, dan aku tidak butuh persetujuan siapapun."\n\nItulah yang otak pria deteksi dalam 3 detik pertama. Sebelum percakapan. Sebelum kamu sempat menjelaskan apa-apa.\n\nDan itu yang akan kamu pelajari. Bukan "tips PDe murahan" — tapi protokol membangun frekuensi internal yang tidak bisa dipalsukan.`
+            }
+        ],
+        agitH2a: "Kenapa Kamu Selalu Transparan",
+        agitH2b: "Di Ruangan Penuh Orang?",
+        agitText: <>Kamu diajari bahwa untuk dicintai, kamu harus berkorban, harus selalu ada, dan harus "menunjukkan" ketertarikanmu. <strong>ITU ADALAH KEBOHONGAN TERBESAR.</strong><br /><br />Ketika kamu terlalu mudah ditebak, selalu tersedia, dan terlalu eager, otak pria memprosesmu sebagai "barang murah" yang tidak perlu diperjuangkan. Mereka tidak tertantang. Tidak ada misteri. <strong>Tidak ada Magnetic Presence.</strong><br /><br />Wanita dengan Magnetic Presence tidak pernah mencari validasi. Saat dia diam, ketenangannya membunuh ego pria. Saat dia memandang, pria merasa dihakimi sekaligus terpesona. Dia tidak mengejar—dia menarik.<br /><br />Dan kabar buruknya: selama kamu masih memancarkan energi "butuh perhatian", kamu akan terus menarik pria yang hanya ingin mempermainkanmu, atau lebih parah... <strong>diabaikan sepenuhnya.</strong></>,
         paramAgitation: {
             label: "AGITASI — REALITA YANG MENYAKITKAN",
             h2a: "Kenapa Kamu Selalu Terlihat,",
@@ -2877,7 +2952,7 @@ const DarkFeminineTSX = () => {
                     <section id="df-hero">
                         <div className="df-wrap">
                             <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '32px' }}>
-                                <img src="/cleo-nobg.png" alt="Cleopatra Logo" style={{ width: '120px', height: '120px', filter: 'drop-shadow(0 0 15px rgba(139,92,246,0.5))' }} />
+                                <img src="/cleo-nobg.webp" alt="Cleopatra Logo" style={{ width: '120px', height: '120px', filter: 'drop-shadow(0 0 15px rgba(139,92,246,0.5))' }} />
                             </div>
                             <div className="df-hero-badge">{sc.heroBadge}</div>
                             <h1 className="df-hero-h1">
```
