# 📋 How To: Parameter Lengkap — Cleopatra Magnet

> Panduan standar untuk memastikan setiap parameter persona memiliki **semua section** yang dibutuhkan agar funnel konversi berjalan optimal.

---

## 🎯 Kenapa Ini Penting?

Parameter yang **tidak lengkap** menyebabkan:
- Copy **disconnect** (atas halaman bicara tentang persona X, bawah halaman jatuh ke default)
- Section penting **tidak muncul** (paramAgitation, paramHope, dll.)
- Visitor kehilangan **emotional momentum** saat scroll ke bawah
- Conversion rate rendah (contoh: `?perhatian` hanya 2.05% sebelum fix)

---

## ✅ 12 Section Wajib Per Parameter

Setiap parameter persona harus memiliki **semua** section berikut:

| # | Section | Key | Fungsi Konversi |
|---|---------|-----|-----------------|
| 1 | **Hero Badge** | `heroBadge` | Branding & persona identity |
| 2 | **Hero Headlines** | `heroH1a`, `heroH1b`, `heroSub` | Hook pertama — first 3 seconds |
| 3 | **Pain Label & Headlines** | `painLabel`, `painH2a`, `painH2b` | Framing rasa sakit |
| 4 | **Stories (Carousel)** | `stories[]` | Narasi emosional, identifikasi diri |
| 5 | **Pain Points** | `pains[]` | Bullet pain — quick scan |
| 6 | **Agitation Text** | `agitH2a`, `agitH2b`, `agitText` | Memperdalam rasa sakit |
| 7 | **Solution Text** | `solText` | Jawaban — dengan studi kasus/gambar |
| 8 | **Param Agitation** | `paramAgitation{}` | Section agitasi tambahan (deep cut) |
| 9 | **Param Hope** | `paramHope{}` | Visi masa depan — "bayangkan..." |
| 10 | **Param How It Works** | `paramHowItWorks{}` | 3 langkah konkret — menghilangkan ketidakpastian |
| 11 | **Param Objections** | `paramObjections{}` | FAQ — menjawab keraguan spesifik per persona |
| 12 | **Param Social Proof** | `paramSocialProof{}` | Before/After — 3 transformasi nyata |

### Section Tambahan (Filter & Cleanup):

| Section | Key | Fungsi |
|---------|-----|--------|
| **Wife Section Filter** | `wifeSection{}` | Hide gambar tidak relevan untuk persona |
| **Winning Gallery Filter** | `winningGallery{}` | Hide gambar winning yang tidak relevan |
| **Before/After Nullify** | `beforeAfterIstri: null`, `beforeAfterSingle: null` | Hide carousel BA yang off-brand |

---

## 📊 Audit Status Semua Parameter

> [!IMPORTANT]
> ✅ = Ada & lengkap | ⚠️ = Ada tapi partial | ❌ = Tidak ada (fallback ke default)

| Parameter | Hero | Stories | Pains | AgitText | SolText | paramAgit | paramHope | paramHow | paramObj | paramProof | wifeFilter | winFilter |
|-----------|------|---------|-------|----------|---------|-----------|-----------|----------|----------|------------|------------|-----------|
| **?presence** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **?ghosting** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **?perhatian** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **?istrifear** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **?istrilegacy** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **?istrivisible** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **?perubahan** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **?highvalue** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **?nongames** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **?softlife** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Default** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |

> [!WARNING]
> Parameter tanpa `agitText`/`solText` custom akan **fallback ke default**. Jika default copy tidak cocok dengan persona, visitor mengalami **cognitive disconnect** dan bounce.

---

## 🔧 Studi Kasus: Fix `?perhatian`

### Sebelum (2.05% conversion — 292 views):

```
?perhatian HANYA punya:
├── ✅ Hero (custom)
├── ✅ Stories (3 cerita)
├── ✅ Pains (6 bullets)
├── ❌ agitText → FALLBACK ke default "Magnetic Presence"
├── ❌ solText → FALLBACK ke default (gambar presence)
├── ❌ paramAgitation → TIDAK MUNCUL
├── ❌ paramHope → TIDAK MUNCUL
├── ❌ paramHowItWorks → TIDAK MUNCUL
├── ❌ paramObjections → TIDAK MUNCUL
├── ❌ paramSocialProof → TIDAK MUNCUL
├── ⚠️ wifeSection → Filter kurang ketat
└── ❌ winningGallery → Tidak di-filter
```

**Dampak:** Visitor masuk dari iklan "perhatian", tapi scroll ke bawah melihat copy tentang "Magnetic Presence" dan gambar yang tidak relevan → **disconnect → bounce.**

### Sesudah (Fix Applied — v1.0.31):

```
?perhatian SEKARANG punya:
├── ✅ Hero (custom)
├── ✅ Stories (3 cerita — tentang mengemis perhatian)
├── ✅ Pains (6 bullets — tentang diabaikan)
├── ✅ agitText — "Kenapa Semakin Kamu Perhatian, Semakin Dia Menjauh?"
├── ✅ solText — Studi Kasus Nadia + kekosongan strategis Cleopatra
├── ✅ paramAgitation — "Kamu Sudah Berikan Segalanya, Dia Tetap Tidak Menghargai"
├── ✅ paramHope — "Bayangkan Dia Yang Gelisah Menunggu Balasanmu"
├── ✅ paramHowItWorks — 3 Tahap: Detox → Orbit Baru → Calibrate
├── ✅ paramObjections — 3 FAQ (hilang selamanya, playing games, introvert)
├── ✅ paramSocialProof — 3 transformasi (Laras, Vera, Dina)
├── ✅ wifeSection — Filter ketat (hide newIstri2/6/8/9, singleC5S1)
└── ✅ winningGallery — Hide winnerCrAd
```

---

## 📝 Checklist Membuat Parameter Baru

Gunakan checklist ini setiap kali membuat parameter persona baru:

- [ ] **Hero**: `heroBadge`, `heroH1a`, `heroH1b`, `heroSub` — hook pertama
- [ ] **Pain Section**: `painLabel`, `painH2a`, `painH2b` — framing
- [ ] **Stories**: 3 cerita carousel dengan gambar relevan
- [ ] **Pains**: 6 bullet points emosional dengan icon
- [ ] **Agitation Text**: `agitH2a`, `agitH2b`, `agitText` — twist the knife
- [ ] **Solution Text**: `solText` — jawaban + studi kasus + gambar hasil
- [ ] **paramAgitation**: Deep agitation section dengan gambar
- [ ] **paramHope**: "Bayangkan..." section — visi setelah transformasi
- [ ] **paramHowItWorks**: 3 langkah konkret (Hari 1-7 → 8-21 → 22+)
- [ ] **paramObjections**: 3 FAQ menjawab keraguan spesifik persona
- [ ] **paramSocialProof**: 3 before/after transformasi relevan
- [ ] **wifeSection**: Filter gambar tidak relevan + null beforeAfter
- [ ] **winningGallery**: Filter gambar winning tidak relevan
- [ ] **WhatsApp text**: Pesan pendek di floating button sesuai persona
- [ ] **APP_VERSION**: Bump versi di `index.html` sebelum deploy
- [ ] **Build & Push**: `npm run build && git push origin main`

> [!TIP]
> Selalu pastikan **semua teks connect secara emosional dari atas ke bawah**. Jangan sampai hero bicara tentang "perhatian" tapi agitText bicara tentang "ghosting". Visitor harus merasa seluruh halaman ditulis **khusus untuk mereka**.
