# PRD Final v1.0 — 7 Sep 2026 (salinan)

   PRODUCT REQUIREMENTS DOCUMENT

     Tax Intelligence System

Sistem Analitik Potensi Pendapatan dan Deteksi Anomali
           Pajak PBJT Venue Padel Jakarta Barat

                     Progressive Web Application (PWA)

Atribut             Keterangan
Jenis Dokumen       Product Requirements Document (PRD)
Jenis Proyek        Proyek Magang (Internship Project)
Periode Proyek      1 September 2026 - 4 Desember 2026 (�14 Minggu)
Instansi Mitra      Badan Pendapatan Daerah (Bappenda)
Status Dokumen      Final - v1.0
Tanggal Penyusunan  7 September 2026

Daftar Isi

1. Product Overview
2. Problem Statement
3. Product Goals & Objectives
4. Product Scope
5. User Persona
6. User Journey Map
7. Functional Requirements
8. Machine Learning Requirements
9. Data Requirements
10. System Architecture
11. Database Design
12. UI/UX Requirement
13. Non-Functional Requirement
14. Development Roadmap
15. MVP Definition
16. Future Development

1. Product Overview

1.1 Nama Produk

Tax Intelligence System: Sistem Analitik Potensi Pendapatan dan Deteksi Anomali Pajak
PBJT Venue Padel Jakarta Barat.

1.2 Deskripsi Produk

Tax Intelligence System adalah Progressive Web Application (PWA) yang dirancang untuk
membantu Badan Pendapatan Daerah (Bappenda) dalam melakukan estimasi potensi
penerimaan Pajak Barang dan Jasa Tertentu (PBJT) pada sektor usaha venue padel di
wilayah Jakarta Barat. Sistem mengintegrasikan data operasional venue, data spasial Zona
Nilai Tanah (ZNT), model machine learning untuk estimasi omzet, mesin perhitungan PBJT,
mesin deteksi anomali pembayaran pajak, serta modul analitik keberlanjutan usaha
(business sustainability) berbasis tren historis. Seluruh hasil analisis disajikan melalui
dashboard interaktif berbasis peta (GIS) dan grafik untuk mendukung pengambilan
keputusan pengawasan pajak yang berbasis data (data-driven tax supervision).

1.3 Visi Produk

Menjadi sistem pendukung keputusan (decision support system) berbasis data spasial dan
machine learning yang membantu Bappenda mengoptimalkan pengawasan kepatuhan
pajak PBJT pada sektor usaha rekreasi olahraga, dimulai dari venue padel di Jakarta Barat,
dengan potensi replikasi ke sektor usaha sejenis dan wilayah lain di masa mendatang.

1.4 Masalah yang Diselesaikan

Sistem ini menjawab keterbatasan pengawasan pajak PBJT yang saat ini sangat
bergantung pada laporan mandiri (self-reported) wajib pajak, tanpa adanya mekanisme
verifikasi independen berbasis estimasi potensi ekonomi riil dari karakteristik operasional
dan lokasi usaha.

1.5 Target Pengguna

Target Pengguna               Peran dalam Sistem
Admin Bappenda
                              Mengelola data master, memantau ringkasan potensi pajak
Petugas Pengawasan Pajak      wilayah, dan mengambil keputusan strategis pengawasan.

Pimpinan/Pengambil Kebijakan  Menggunakan hasil anomaly score dan ranking wajib pajak
(Viewer)                      untuk memprioritaskan kunjungan/pemeriksaan lapangan.

                              Melihat ringkasan dashboard eksekutif untuk kebutuhan
                              pelaporan dan pengambilan kebijakan (akses terbatas,
                              read-only).

1.6 Value Proposition

Kondisi Sebelum Sistem                       Kondisi Setelah Implementasi Sistem
Estimasi potensi pajak dilakukan manual dan
tidak konsisten.                             Estimasi potensi omzet dan PBJT dihasilkan
                                             otomatis dari model machine learning berbasis
Tidak ada mekanisme deteksi dini             data operasional dan spasial.
ketidaksesuaian pembayaran pajak.
Prioritas pengawasan lapangan bersifat       Anomaly score dan risk category dihasilkan
subjektif.                                   otomatis untuk setiap wajib pajak.
Tidak ada visibilitas terhadap prospek
keberlanjutan usaha wajib pajak.             Ranking wajib pajak berbasis risiko membantu
                                             prioritisasi pengawasan yang objektif dan terukur.
Data venue, spasial, dan pajak tersebar dan
tidak terintegrasi.                          Sustainability Score dan business outlook
                                             memberi indikasi awal risiko penurunan usaha
                                             yang berdampak pada penerimaan pajak.

                                             Seluruh data terintegrasi dalam satu basis data
                                             dan disajikan melalui dashboard GIS interaktif.

2. Problem Statement

2.1 Kondisi Sistem Saat Ini
Pengawasan pajak PBJT pada sektor usaha venue padel saat ini masih bersifat administratif
dan pasif. Bappenda menerima laporan omzet dan pembayaran pajak dari wajib pajak tanpa
memiliki alat bantu independen untuk memvalidasi kewajaran nilai yang dilaporkan terhadap
potensi ekonomi riil usaha tersebut.

2.2 Masalah Utama

     � Tidak tersedia estimasi potensi omzet yang independen dari laporan wajib pajak.
     � Tidak ada integrasi antara lokasi usaha dengan data nilai ekonomi lokasi (Zona Nilai

         Tanah).
     � Tidak ada mekanisme sistematis untuk mendeteksi anomali/ketidaksesuaian

         pembayaran pajak.
     � Prioritas pengawasan lapangan ditentukan tanpa dasar data kuantitatif yang

         memadai.
     � Tidak ada visibilitas terhadap tren keberlanjutan usaha wajib pajak yang berdampak

         pada proyeksi penerimaan pajak jangka menengah.

2.3 Pain Point Pengguna

Pengguna                  Pain Point
Admin Bappenda
                          Kesulitan memantau potensi pajak seluruh wilayah secara
Petugas Pengawasan Pajak  agregat dan real-time; laporan manual memakan waktu.

                          Tidak memiliki daftar prioritas wajib pajak berisiko tinggi;
                          kunjungan lapangan dilakukan tanpa data pendukung yang
                          kuat.

2.4 Keterbatasan Proses Manual

     � Proses estimasi dan verifikasi memakan waktu lama karena dilakukan satu per satu
         secara manual.

     � Rentan terhadap bias subjektif petugas dalam menentukan wajib pajak yang perlu
         diperiksa.

     � Tidak dapat melakukan analisis skala besar (puluhan-ratusan venue) secara efisien.
     � Tidak memiliki jejak audit (audit trail) yang terdokumentasi secara digital.

2.5 Dampak Bisnis

     � Potensi kebocoran penerimaan daerah (revenue leakage) akibat underreporting yang
         tidak terdeteksi.

     � Alokasi sumber daya pengawasan yang tidak efisien karena tidak berbasis prioritas
         risiko.
� Minimnya data pendukung untuk perencanaan kebijakan pajak daerah berbasis bukti
   (evidence-based policy).

3. Product Goals & Objectives

3.1 Business Goals

     � Meningkatkan kepatuhan pajak PBJT sektor venue padel melalui pengawasan
         berbasis data.

     � Mengoptimalkan potensi penerimaan daerah dengan mendeteksi selisih antara
         potensi dan realisasi pembayaran pajak.

     � Menyediakan dasar kuantitatif untuk prioritisasi pengawasan lapangan sehingga
         sumber daya petugas digunakan lebih efisien.

3.2 User Goals

     � Admin Bappenda dapat memantau kondisi potensi pajak seluruh venue dalam satu
         dashboard terintegrasi.

     � Petugas Pengawasan Pajak dapat memperoleh daftar wajib pajak berisiko tinggi
         beserta alasan/faktor pendukungnya secara cepat.

3.3 Technical Goals

     � Membangun pipeline machine learning yang dapat diulang (reproducible) untuk
         estimasi omzet dan deteksi anomali.

     � Mengintegrasikan data spasial (GIS/ZNT) dengan data operasional venue secara
         konsisten.

     � Membangun arsitektur modular (frontend, backend, ML service terpisah) agar mudah
         dikembangkan lebih lanjut pasca-magang.

3.4 Success Metrics

Indikator               Target pada Akhir Magang (Minggu Metode Pengukuran
                        ke-14)
Cakupan data venue
yang terintegrasi       Minimal 80% dari sampel venue      Jumlah baris data venue
Akurasi model prediksi  padel Jakarta Barat yang tersedia  tervalidasi pada database
omzet
                        MAE dan RMSE pada tingkat yang     Evaluasi model pada test set
Fungsi deteksi anomali  wajar sesuai skala data; R2 > 0,6
                        pada data uji

                        Sistem mampu mengklasifikasikan    Pengujian fungsional pada
                        seluruh venue ke dalam 3 kategori  seluruh data venue
                        risiko
Waktu respons      Halaman utama dashboard termuat        Pengujian performa (load
dashboard          dalam < 3 detik pada kondisi data uji  testing sederhana)

Kelengkapan modul  Seluruh fitur Must Have pada Section User Acceptance Test (UAT)
MVP
                   15 selesai dan lulus uji fungsional    internal

4. Product Scope

4.1 MVP Scope (Wajib Selesai dalam 14 Minggu)

     � Data Management -- pengelolaan data venue padel (input, edit, hapus, impor).
     � GIS Integration -- pemetaan lokasi venue dan integrasi Zona Nilai Tanah (ZNT).
     � Revenue Estimation -- estimasi potensi omzet bulanan berbasis machine learning.
     � PBJT Estimation -- perhitungan estimasi PBJT berdasarkan omzet hasil estimasi.
     � Anomaly Detection -- deteksi ketidaksesuaian antara potensi dan pembayaran

         aktual.
     � Dashboard -- visualisasi hasil analisis (ringkasan, grafik, peta, detail venue).
     � Business Sustainability Analytics (sederhana) -- Should Have, hanya

         diimplementasikan apabila data historis memadai; berbasis analisis tren, bukan
         model kompleks.

4.2 Future Development (Di Luar Cakupan Magang)

     � Integrasi langsung dengan API resmi Bappenda/Pemprov DKI Jakarta.
     � Real-time monitoring transaksi venue (mis. integrasi sistem booking venue).
     � AI assistant pajak berbasis conversational AI untuk petugas.
     � Model prediksi penerimaan pajak daerah tingkat agregat/wilayah.
     � Survival analysis formal untuk estimasi probabilitas keberlangsungan usaha.
     � Ekspansi ke sektor PBJT lain (mis. karaoke, kolam renang, gym, bioskop).

4.3 Prioritas Fitur (MoSCoW)

Prioritas          Fitur
Must Have
Should Have        Data management, GIS & ZNT integration, revenue estimation, PBJT
Could Have         estimation, anomaly detection, dashboard risiko

                   Business sustainability analytics sederhana (score, outlook, tren) --
                   hanya jika data historis memadai

                   Survival analysis dan prediksi time-to-event risiko penutupan usaha
5. User Persona

5.1 Persona 1: Admin Bappenda

Aspek             Deskripsi
Background
                  Pegawai struktural Bappenda yang bertanggung jawab atas
Aktivitas         administrasi data wajib pajak PBJT dan pelaporan kinerja penerimaan
Kebutuhan         daerah. Memiliki pemahaman regulasi pajak daerah namun
Pain Point        keterbatasan literasi teknis data science.
Goal
                  Mengelola data master venue, memantau ringkasan potensi pajak
                  wilayah, menyusun laporan berkala untuk pimpinan, serta
                  menugaskan petugas pengawasan berdasarkan hasil analisis sistem.

                  Dashboard ringkas yang mudah dipahami, kemampuan impor data
                  secara massal (bulk import), serta laporan yang dapat diekspor untuk
                  keperluan rapat/pelaporan.

                  Data venue dan pajak tersebar di berbagai sumber; sulit melihat
                  gambaran menyeluruh potensi pajak wilayah secara cepat.

                  Mendapatkan visibilitas menyeluruh atas potensi dan risiko pajak
                  PBJT venue padel di wilayah kerjanya untuk mendukung pengambilan
                  keputusan.

5.2 Persona 2: Petugas Pengawasan Pajak

Aspek             Deskripsi
Aktivitas Harian
                  Melakukan verifikasi lapangan terhadap wajib pajak, memeriksa
Workflow          kesesuaian laporan omzet, dan menindaklanjuti temuan indikasi
                  ketidaksesuaian pembayaran pajak.
Informasi yang
Dibutuhkan        Menerima penugasan  meninjau profil dan skor risiko venue pada
Pain Point        sistem  melakukan kunjungan/verifikasi lapangan  mencatat hasil
Goal              temuan.

                  Ranking wajib pajak berisiko tinggi, faktor-faktor yang mendasari
                  anomaly score, lokasi venue pada peta, serta riwayat pembayaran
                  pajak.

                  Tidak memiliki dasar objektif untuk menentukan venue mana yang
                  perlu diprioritaskan untuk diperiksa lebih dahulu.

                  Memprioritaskan kunjungan pengawasan pada wajib pajak dengan
                  indikasi risiko tertinggi secara efisien dan berbasis data.

6. User Journey Map
Alur penggunaan sistem secara umum mengikuti tahapan berikut:

[Login]

  |

  v

[Dashboard Utama]

  |

  v

[Input / Import Data Venue]

  |

  v

[Integrasi ZNT (Spasial)]

  |

  v

[Estimasi Omzet (ML)]

  |

  v

[Perhitungan PBJT]

  |

  v

[Deteksi Anomali]

  |

  v

[Analisis Keberlanjutan Usaha]

  |

  v

[Dashboard Risiko & Sustainability]

  |

  v

[Prioritas Pengawasan Lapangan]

Tahap                           Penjelasan
Login
Dashboard Utama                 Pengguna melakukan autentikasi sesuai peran (Admin Bappenda /
Input/Import Data Venue         Petugas Pengawasan).
Integrasi ZNT
Estimasi Omzet                  Menampilkan ringkasan total venue, total potensi omzet, total
Perhitungan PBJT                potensi PBJT, dan jumlah anomali terdeteksi.

                                Admin menambahkan data venue baru secara manual atau melalui
                                impor berkas (CSV/Excel).

                                Sistem mencocokkan koordinat venue dengan data Zona Nilai
                                Tanah untuk memperoleh faktor ekonomi lokasi.

                                Model machine learning menghasilkan estimasi omzet bulanan
                                berdasarkan karakteristik venue dan lokasi.

                                Sistem menghitung estimasi PBJT dari hasil estimasi omzet
                                menggunakan tarif yang berlaku.
Deteksi Anomali         Sistem membandingkan estimasi PBJT dengan pembayaran aktual
                        dan menghasilkan anomaly score serta kategori risiko.
Analisis Keberlanjutan
Usaha                   Jika data historis memadai, sistem menghasilkan Sustainability
Dashboard Risiko &      Score dan business outlook berbasis tren.
Sustainability
Prioritas Pengawasan    Menyajikan hasil analisis anomali dan keberlanjutan usaha dalam
                        bentuk grafik dan peta interaktif.

                        Petugas menggunakan ranking risiko untuk menentukan urutan
                        prioritas kunjungan/pemeriksaan lapangan.

7. Functional Requirements

Module 1: Authentication & User Management

     � Login menggunakan username/email dan password, dengan mekanisme
         session/token (JWT).

     � Role management dengan minimal tiga peran: Admin Bappenda, Petugas
         Pengawasan Pajak, dan Viewer.

     � Authorization berbasis peran (Role-Based Access Control) yang membatasi akses
         fitur sesuai peran pengguna.

Module 2: Venue Data Management

Fitur

     � Input data venue baru.
     � Edit data venue yang sudah ada.
     � Hapus (delete) data venue, dengan mekanisme soft-delete untuk audit trail.
     � Impor dataset venue secara massal melalui berkas CSV/Excel.

Field Data Venue        Tipe Data          Keterangan
                        String             Nama usaha venue padel
 Field                  String             Alamat lengkap venue
 Nama Venue             Decimal            Koordinat lintang lokasi venue
 Lokasi                 Decimal            Koordinat bujur lokasi venue
 Latitude               Integer            Jumlah lapangan padel yang dioperasikan
 Longitude              Decimal            Harga sewa per jam/sesi (Rupiah)
 Jumlah Court           String/Time Range  Jam buka-tutup operasional harian
 Harga Sewa             String             Hari-hari operasional dalam seminggu
 Jam Operasional
 Hari Operasi
Module 3: GIS & ZNT Integration

     � Mapping lokasi venue pada peta interaktif berbasis koordinat latitude/longitude.
     � Integrasi koordinat venue dengan basis data spasial Zona Nilai Tanah (ZNT)

         menggunakan operasi spatial join.
     � Spatial analysis untuk menentukan wilayah administratif dan faktor ekonomi lokasi

         tempat venue berada.

Output Modul

Output                 Keterangan
Nilai ZNT              Nilai Zona Nilai Tanah pada lokasi venue (Rp/m�)
Wilayah                Kelurahan/kecamatan tempat venue berada
Faktor Ekonomi Lokasi  Indikator turunan (mis. kategori zona: premium/menengah/reguler)
                       berdasarkan ZNT

Module 4: Revenue Estimation Engine

Input

     � Jumlah court, harga sewa, jam operasional, hari operasi, nilai ZNT, dan
         lokasi/wilayah.

Proses

 Feature Engineering --> Machine Learning Model --> Prediction

Output

Estimasi omzet bulanan venue dalam satuan Rupiah, disertai rentang estimasi (confidence
interval sederhana) apabila memungkinkan.

Module 5: PBJT Estimation Engine

Formula

 PBJT = Estimasi Omzet Bulanan x Tarif PBJT

Parameter, Input, dan Output

Komponen               Keterangan

Parameter              Tarif PBJT sesuai regulasi daerah yang berlaku untuk sektor jasa
                       olahraga/rekreasi (dapat dikonfigurasi admin).

Input                  Estimasi omzet bulanan dari Revenue Estimation Engine (Module 4).

Output                 Nilai estimasi PBJT bulanan yang menjadi acuan pembanding
                       terhadap pembayaran aktual.
Module 6: Anomaly Detection System

Tujuan: mendeteksi ketidaksesuaian antara potensi PBJT hasil estimasi sistem dengan nilai
PBJT yang benar-benar dibayarkan oleh wajib pajak.

Input

     � Estimasi omzet, estimasi PBJT, dan PBJT aktual (dari laporan/pembayaran wajib
         pajak).

Output

     � Anomaly score (nilai numerik tingkat kejanggalan).
     � Risk category (kategori risiko).
     � Ranking wajib pajak berdasarkan tingkat risiko.

Kategori Risiko  Deskripsi

 Kategori        Selisih antara estimasi dan pembayaran aktual berada dalam rentang
 Normal          wajar.

 Monitoring      Terdapat selisih yang perlu dipantau namun belum mengindikasikan
                 pelanggaran signifikan.
 High Risk
                 Selisih signifikan yang mengindikasikan kemungkinan underreporting
                 dan perlu diprioritaskan untuk verifikasi lapangan.

Module 7: Business Sustainability Analytics (Should
Have)

Tujuan: memberikan indikasi prospek keberlanjutan usaha venue berdasarkan tren performa
yang tersedia -- bukan menjamin umur perusahaan secara pasti.

Input (Bergantung Ketersediaan Data Historis)

     � Estimasi omzet per periode dan omzet laporan per periode.
     � PBJT pembayaran per periode dan tren pertumbuhan/penurunan.
     � Jumlah court, harga sewa, jam operasional, lokasi dan ZNT.
     � Anomaly score historis.

Proses

 Historical Trend Analysis --> Feature Engineering --> Sustainability Scoring / Forecasting

Output

     � Sustainability Score (skala 0-100).
     � Business Outlook: Positif / Stabil / Waspada.
     � Tren performa usaha dan indikasi risiko penurunan.
     � Proyeksi jangka pendek-menengah (1-3 tahun), hanya jika kualitas dan panjang data
         historis memadai.

Catatan Penting

     � Sistem tidak boleh mengklaim secara deterministik bahwa suatu venue akan
         bertahan selama X tahun.

     � Jika data historis belum cukup, sistem menampilkan status "Data belum memadai
         untuk proyeksi" dan hanya menyajikan analisis tren/deskriptif.

     � Untuk MVP 14 minggu, modul ini diposisikan sebagai Should Have/prototype dan
         tidak boleh mengorbankan penyelesaian fitur inti (estimasi PBJT dan deteksi
         anomali).

Module 8: Dashboard Analytics

Dashboard Utama

     � Total venue terdaftar.
     � Total omzet potensial (agregat).
     � Total PBJT potensial (agregat).
     � Jumlah anomali terdeteksi.

Grafik

     � Tren omzet dari waktu ke waktu.
     � Distribusi risiko (Normal/Monitoring/High Risk).
     � Tren Sustainability Score / business outlook (jika tersedia).

Peta (Map)

     � Sebaran lokasi venue pada peta interaktif.
     � Visualisasi zona risiko berbasis warna (heat/choropleth sederhana).

Halaman Detail

     � Profil venue lengkap.
     � Hasil prediksi omzet dan estimasi PBJT.
     � Status risiko dan anomaly score.
     � Sustainability Score dan business outlook (jika tersedia).

8. Machine Learning Requirements

Model 1: Revenue Prediction Model

Tujuan: memprediksi estimasi omzet bulanan venue padel.

Komponen  Keterangan
Dataset              Data venue (karakteristik operasional) yang digabungkan dengan data
                     spasial ZNT; dilengkapi data omzet historis/proksi bila tersedia untuk
Feature              pelatihan awal.
Target Variable
Feature Engineering  Jumlah court, harga sewa, jam operasional, hari operasi, nilai ZNT,
Algoritma            wilayah/lokasi.
Training Workflow
Evaluation Metrics   Omzet bulanan venue (Rupiah).

                     Normalisasi harga sewa, encoding wilayah, perhitungan total jam
                     operasional mingguan, kategori zona ekonomi berbasis ZNT.

                     XGBoost Regression (direkomendasikan); dibandingkan dengan
                     baseline regresi linier untuk validasi kewajaran.

                     Split data train/test (mis. 80/20), cross-validation, hyperparameter
                     tuning, evaluasi pada data uji.

                     MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), R2
                     Score.

Model 2: Anomaly Detection Model

Tujuan: mendeteksi pembayaran pajak yang bersifat abnormal dibandingkan estimasi
potensi.

Komponen             Keterangan
Dataset
Feature              Selisih/rasio antara estimasi PBJT (Module 5) dan PBJT aktual per
Metode               wajib pajak.
Threshold
Output               Rasio pembayaran terhadap estimasi, selisih absolut, tren
                     pembayaran antar periode (jika tersedia).

                     Isolation Forest (direkomendasikan) untuk mendeteksi outlier tanpa
                     memerlukan label anomali eksplisit.

                     Ambang batas anomaly score ditentukan melalui analisis distribusi
                     skor pada data historis, dikalibrasi bersama tim/pembimbing.

                     Anomaly score, kategori risiko (Normal/Monitoring/High Risk), dan
                     ranking wajib pajak.

Model 3: Business Sustainability Model (Should Have /
Prototype)

Tujuan: mengestimasi sustainability score dan outlook keberlanjutan usaha berdasarkan
pola historis yang tersedia.

Komponen             Keterangan
Minimum Kebutuhan Data      Idealnya minimal beberapa periode (mis. bulanan) data omzet dan
Historis                    pembayaran pajak per venue; jika tidak tersedia, modul membatasi
Feature                     diri pada analisis deskriptif.
Target/Proxy Target
                            Tren pertumbuhan omzet, tren anomaly score, stabilitas jam
Metode Forecasting/Scoring  operasional, faktor lokasi/ZNT.

Validasi                    Tidak menggunakan target biner "tutup/tidak tutup" (data belum
Confidence/Uncertainty      tersedia); menggunakan skor komposit sebagai proksi kesehatan
Keterbatasan Interpretasi   usaha.

                            Trend analysis dan rule-based/weighted sustainability scoring yang
                            transparan sebagai pendekatan MVP; evaluasi model
                            forecasting/regresi sederhana hanya jika data mencukupi.

                            Pemeriksaan konsistensi skor terhadap tren historis yang diketahui;
                            review kualitatif bersama pembimbing/pemangku kepentingan.

                            Skor disertai indikator tingkat keyakinan (mis. tinggi/sedang/rendah)
                            berdasarkan panjang dan kelengkapan data historis yang tersedia.

                            Skor bersifat indikatif, bukan jaminan; sistem secara eksplisit
                            menghindari klaim deterministik terkait usia/keberlangsungan
                            usaha.

Output

     � Sustainability Score (skala 0-100).
     � Business Outlook (Positif/Stabil/Waspada).
     � Trend direction (naik/stabil/turun).
     � Confidence level.
     � Faktor utama yang memengaruhi skor.

9. Data Requirements

9.1 Venue Dataset           Tipe Data
                            String/UUID (Primary Key)
 Field                      String
 venue_id                   String
 nama                       Decimal
 lokasi                     Decimal
 latitude                   Integer
 longitude                  Decimal
 jumlah_court
 harga_sewa
jam_operasi          String/Time Range
rating               Decimal (opsional)

9.2 Spatial Dataset  Tipe Data
                     Decimal
 Field               Decimal
 latitude            String
 longitude           Geometry (PostGIS)
 wilayah             Decimal (Rp/m�)
 polygon
 ZNT

9.3 Tax Dataset

Field                Tipe Data              Keterangan
wajib_pajak          String/FK ke venue_id  Identitas wajib pajak
omzet_laporan        Decimal                Omzet yang dilaporkan wajib pajak
PBJT_pembayaran      Decimal                Nilai PBJT yang benar-benar dibayarkan
periode              Date/String            Periode pelaporan (bulanan)
status_usaha         String (opsional)      Status operasional usaha, jika tersedia
tanggal_mulai_usaha  Date (opsional)        Tanggal mulai operasional usaha
tanggal_tutup_usaha  Date (opsional)        Untuk pengembangan survival analysis di
                                            masa depan

10. System Architecture

10.1 Komponen Teknologi

Layer                Teknologi
Frontend             React (Progressive Web Application)
Backend              FastAPI (Python)
Database             PostgreSQL + ekstensi PostGIS
Machine Learning     Python, Scikit-learn, XGBoost
GIS                  GeoPandas (pemrosesan spasial), Leaflet (visualisasi peta)
10.2 Diagram Alur Sistem

[User: Admin / Petugas]

   |

   v

  [Frontend - React PWA]

   |

   v

  [Backend API - FastAPI]

   |  |

   v  v

[Database] [ML Service]

PostgreSQL (Scikit-learn,

+ PostGIS XGBoost)

   \  /

   v v

  [Dashboard Analytics]

Backend API bertindak sebagai orkestrator: menerima permintaan dari frontend, melakukan
query ke database (termasuk operasi spasial via PostGIS), memanggil ML service untuk
inferensi (estimasi omzet, anomaly score, sustainability score), lalu mengembalikan hasil
gabungan ke frontend untuk ditampilkan pada dashboard.

11. Database Design

11.1 Daftar Tabel Konseptual

Tabel                      Deskripsi Singkat
users
venues                     Menyimpan akun pengguna sistem beserta peran (role).
spatial_znt
revenue_prediction         Menyimpan data master venue padel.

tax_payment                Menyimpan data Zona Nilai Tanah per wilayah/polygon.

anomaly_result             Menyimpan hasil estimasi omzet dari model ML per venue per
                           periode.
sustainability_result
                           Menyimpan data laporan omzet dan pembayaran PBJT aktual per
                           periode.

                           Menyimpan anomaly score, kategori risiko, dan ranking per venue
                           per periode.

                           Menyimpan sustainability score, outlook, dan tren per venue (jika
                           data historis memadai).

11.2 Relasi Antar Tabel (ERD Konseptual)
Tabel           Primary Key       Foreign Key                              Relasi

users           user_id           -                                        1 users : N aktivitas audit
venues          venue_id          znt_id  spatial_znt                      (opsional, pengembangan
                                                                           lanjutan)
spatial_znt     znt_id            -
                                  venue_id  venues                         1 spatial_znt : N venues
revenue_prediction prediction_id                                           (banyak venue dapat
                                                                           berada dalam satu zona
tax_payment     payment_id        venue_id  venues                         ZNT)

anomaly_result  anomaly_id        venue_id  venues,                        Referensi wilayah/zona nilai
                                  payment_id                               tanah
                                  tax_payment
                                                                           1 venues : N
sustainability_result sustainability_id venue_id  venues                   revenue_prediction (satu
                                                                           venue punya banyak
                                                                           periode prediksi)

                                                                           1 venues : N tax_payment
                                                                           (riwayat pembayaran per
                                                                           periode)

                                                                           1 tax_payment : 1
                                                                           anomaly_result (hasil
                                                                           deteksi per periode
                                                                           pembayaran)

                                                                           1 venues : N
                                                                           sustainability_result (skor
                                                                           dapat dihitung ulang per
                                                                           periode evaluasi)

 spatial_znt (1) ---- (N) venues (1) ---- (N) revenue_prediction
                      |
                      |---- (N) tax_payment (1) ---- (1) anomaly_result
                      |
                      |---- (N) sustainability_result


  users (peran: admin, petugas, viewer) mengakses seluruh entitas di atas
  sesuai hak akses (RBAC) masing-masing.

12. UI/UX Requirement

12.1 Login Page

Aspek            Keterangan
Komponen
                 Form input email/username dan password, tombol login, pesan
                 kesalahan validasi.
Informasi yang    Logo/nama sistem, keterangan versi/instansi.
Ditampilkan
                  Validasi input real-time, redirect ke dashboard sesuai peran setelah
User Interaction  login berhasil.

12.2 Dashboard Page

Aspek             Keterangan
Komponen
                  Kartu ringkasan (total venue, total omzet potensial, total PBJT
Informasi yang    potensial, jumlah anomali), grafik tren, grafik distribusi risiko,
Ditampilkan       mini-map.
User Interaction
                  Ringkasan agregat seluruh venue serta tren performa dan risiko
                  secara keseluruhan.

                  Filter berdasarkan periode dan wilayah; klik pada elemen grafik/kartu
                  untuk melihat detail lanjutan.

12.3 Map Page

Aspek             Keterangan
Komponen
                  Peta interaktif (Leaflet) dengan marker venue, layer zona risiko,
Informasi yang    kontrol zoom/filter.
Ditampilkan
User Interaction  Sebaran lokasi venue, warna marker sesuai kategori risiko, informasi
                  singkat saat marker diklik (popup).

                  Klik marker untuk membuka ringkasan venue; filter peta berdasarkan
                  kategori risiko atau wilayah.

12.4 Venue Detail Page

Aspek             Keterangan
Komponen
                  Profil venue, kartu hasil prediksi omzet, kartu estimasi PBJT, indikator
Informasi yang    anomaly score, kartu sustainability score/outlook, grafik tren historis.
Ditampilkan
User Interaction  Seluruh data dan hasil analisis terkait satu venue tertentu secara
                  lengkap.

                  Navigasi antar-tab (profil, prediksi, pajak, risiko, sustainability); ekspor
                  ringkasan venue (opsional).

13. Non-Functional Requirement
13.1 Performance

     � Response time: sebagian besar permintaan API selesai dalam < 2 detik pada kondisi
         data uji skala magang.

     � Scalability: arsitektur backend dan database dirancang modular agar dapat
         menampung penambahan jumlah venue dan wilayah tanpa perombakan besar.

13.2 Security

     � Authentication: login berbasis token (JWT) dengan masa berlaku sesi yang wajar.
     � Authorization: pembatasan akses fitur dan data berdasarkan peran pengguna

         (RBAC).
     � Data Protection: enkripsi password (hashing), koneksi HTTPS, dan validasi input

         untuk mencegah injeksi data.

13.3 Maintainability

     � Modular architecture: pemisahan jelas antara frontend, backend API, dan ML service
         agar mudah dipelihara/dikembangkan.

     � Documentation: dokumentasi API, skema database, dan panduan menjalankan
         model ML disusun sebagai bagian dari deliverable akhir magang.

13.4 Usability

     � Dashboard dirancang user-friendly bagi pengguna non-teknis (Admin Bappenda,
         Petugas Pengawasan) dengan istilah yang mudah dipahami dan visualisasi yang
         jelas.

14. Development Roadmap

14.1 Ringkasan Bulanan

Bulan           Fokus                    Output
September 2026  Research & Requirement
Oktober 2026    Database + Backend + ML  Requirement analysis, system design

November 2026   Frontend + Dashboard     Database, API, model ML utama,
Desember 2026   Integration              eksperimen sustainability scoring
                                         berbasis tren (jika data historis
                Testing + Deployment +   tersedia)
                Documentation
                                         Dashboard, visualisasi GIS, visualisasi
                                         sustainability score/business outlook
                                         (Should Have)

                                         Testing, deployment, laporan akhir
14.2 Rincian Sprint Mingguan (14 Minggu)

Sprint     Periode            Fokus Utama                Deliverable
Sprint 1   1-7 Sep 2026
Sprint 2   8-14 Sep 2026      Onboarding & analisis      Dokumen requirement awal,
                              kebutuhan                  akses data/sumber ZNT
Sprint 3   15-21 Sep 2026     Riset domain pajak PBJT &
Sprint 4   22-28 Sep 2026     studi literatur ML         Rangkuman regulasi PBJT,
                                                         referensi model estimasi
Sprint 5   29 Sep-5 Okt 2026  Perancangan sistem         omzet
Sprint 6   6-12 Okt 2026      (arsitektur & PRD)
Sprint 7   13-19 Okt 2026     Perancangan UI/UX          PRD final, diagram arsitektur,
Sprint 8   20-26 Okt 2026     (wireframe)                ERD awal

Sprint 9   27 Okt-2 Nov 2026  Setup database & skema     Wireframe/mockup Login,
Sprint 10  3-9 Nov 2026       tabel                      Dashboard, Map, Venue
Sprint 11  10-16 Nov 2026     Pengumpulan & pembersihan  Detail
Sprint 12  17-23 Nov 2026     data venue/ZNT
Sprint 13  24-30 Nov 2026     Pengembangan backend API   Database PostgreSQL +
                              dasar                      PostGIS terisi skema awal
Sprint 14  1-4 Des 2026       Pengembangan Revenue
                              Prediction Model           Dataset venue dan spasial
                                                         siap pakai
                              Pengembangan Anomaly
                              Detection Model            Endpoint CRUD venue &
                              Integrasi ML service ke    autentikasi
                              backend API
                              Pengembangan frontend      Model XGBoost terlatih +
                              (Login, Dashboard)         evaluasi awal
                              Pengembangan frontend      (MAE/RMSE/R2)
                              (Map & Venue Detail)
                              Eksperimen sustainability  Model Isolation Forest +
                              scoring & polishing UI     threshold awal

                              Testing, deployment, dan   Endpoint prediksi omzet &
                              dokumentasi akhir          anomaly score berfungsi

                                                         Halaman Login dan
                                                         Dashboard terhubung ke API

                                                         Halaman Map dan Venue
                                                         Detail berfungsi penuh

                                                         Prototipe sustainability
                                                         score/outlook (Should Have),
                                                         perbaikan UI

                                                         Hasil UAT, sistem ter-deploy,
                                                         laporan akhir magang

15. MVP Definition

Prioritas  Fitur
Must Have    Data management, GIS & ZNT integration, revenue estimation, PBJT
             estimation, anomaly detection, dashboard risiko

Should Have  Business Sustainability Analytics sederhana, Sustainability Score,
             business outlook dan tren performa, proyeksi 1-3 tahun (hanya jika data
             historis memadai)

Could Have   Survival analysis untuk estimasi probabilitas keberlangsungan usaha,
             prediksi time-to-event/risiko penutupan usaha (setelah tersedia dataset
             historis yang memadai)

Ruang lingkup di atas disusun agar realistis untuk diselesaikan dalam periode magang 14
minggu, dengan prioritas utama pada fitur inti (Must Have) yang menjadi nilai utama sistem:
estimasi potensi pajak dan deteksi anomali. Fitur Should Have dan Could Have akan
dikembangkan secara bertahap sepanjang kapasitas waktu dan ketersediaan data
memungkinkan, tanpa mengorbankan kualitas fitur inti.

16. Future Development

     � Integrasi API Bappenda untuk sinkronisasi data wajib pajak secara langsung.
     � Real-time monitoring transaksi dan okupansi venue.
     � AI assistant pajak untuk membantu petugas menjawab pertanyaan terkait regulasi

         dan hasil analisis.
     � Model prediksi penerimaan pajak daerah pada tingkat agregat/wilayah.
     � Model survival analysis untuk estimasi probabilitas keberlangsungan usaha

         berdasarkan data tanggal buka/tutup yang memadai.
     � Early warning system atas penurunan kesehatan usaha wajib pajak.
     � Ekspansi cakupan ke sektor pajak PBJT lain (mis. kolam renang, gym, karaoke,

         bioskop).

MASTER PROMPT PEMBUATAN PRD

Tax Intelligence System PBJT Venue
Padel Jakarta Barat

Project Context
Project Type: Internship Project
Periode: 1 September 2026 - 4 Desember 2026
Durasi: �14 Minggu
Bertindak sebagai:

     Senior Product Manager
     System Architect
     AI/ML Product Designer
     Business Analyst
     Software Engineering Lead
Buatkan Product Requirements Document (PRD) yang profesional, realistis,
dan siap digunakan sebagai dokumen perencanaan pengembangan software.
Dokumen harus mengikuti standar PRD perusahaan teknologi, namun
disesuaikan dengan kapasitas proyek magang selama 14 minggu.

Informasi Produk

Nama Produk

Tax Intelligence System:
Sistem Analitik Potensi Pendapatan dan Deteksi Anomali Pajak PBJT
Venue Padel Jakarta Barat

Jenis Produk

Progressive Web Application (PWA)
Kategori:

     Tax Intelligence System
     Geographic Information System (GIS)
     Machine Learning Analytics
     Business Intelligence Dashboard
     Business Sustainability Analytics
Latar Belakang

Badan Pendapatan Daerah (Bappenda) membutuhkan sistem analitik yang
dapat membantu melakukan estimasi potensi penerimaan Pajak Barang dan
Jasa Tertentu (PBJT), khususnya pada sektor usaha venue padel.

Saat ini pengawasan pajak masih banyak bergantung pada laporan wajib
pajak sehingga terdapat keterbatasan dalam mengetahui apakah pembayaran
pajak telah sesuai dengan potensi ekonomi usaha sebenarnya.

Sistem harus mampu mengintegrasikan:

     Data venue padel
     Karakteristik operasional bisnis
     Data spasial Zona Nilai Tanah (ZNT)
     Estimasi potensi omzet
     Perhitungan estimasi PBJT
     Data pembayaran pajak aktual
     Data historis performa usaha (jika tersedia)
     Machine Learning untuk prediksi dan deteksi anomali
     Analitik tren untuk proyeksi keberlanjutan usaha

Tujuan Produk

Sistem harus mampu:

    1. Mengelola data venue padel.
    2. Mengintegrasikan lokasi venue dengan Zona Nilai Tanah.
    3. Mengestimasi potensi omzet bulanan.
    4. Menghitung estimasi PBJT.
    5. Membandingkan estimasi sistem dengan pembayaran aktual.
    6. Menghasilkan anomaly score dan risk category.
    7. Menghasilkan Sustainability Score dan business outlook berdasarkan

         data historis yang tersedia.
    8. Menampilkan hasil analisis melalui dashboard interaktif.

Struktur PRD yang Harus Dibuat

1. Product Overview
Jelaskan:
     Nama produk
     Deskripsi produk
     Visi produk
     Masalah yang diselesaikan
     Target pengguna
     Value proposition

2. Problem Statement

Analisis:
     Kondisi sistem saat ini
     Masalah utama
     Pain point pengguna
     Keterbatasan proses manual
     Dampak bisnis

3. Product Goals & Objectives

Buat:

Business Goals

User Goals

Technical Goals

Success Metrics

Gunakan indikator yang dapat diukur.

4. Product Scope
Pisahkan:

MVP Scope

Fitur yang wajib selesai dalam 14 minggu:
     Data management
     GIS integration
     Revenue estimation
     PBJT estimation
     Anomaly detection
     Dashboard
     Sustainability analytics sederhana berbasis tren historis (Should
         Have; hanya jika data historis memadai)

Future Development

Fitur pengembangan lanjutan.
Buat prioritas:

     Must Have
     Should Have
     Could Have

5. User Persona

Buat minimal dua persona.

Persona 1: Admin Bappenda

Jelaskan:
     Background
     Aktivitas
     Kebutuhan
     Pain point
     Goal

Persona 2: Petugas Pengawasan Pajak

Jelaskan:
     Aktivitas harian
     Workflow
     Informasi yang dibutuhkan
     Pain point
     Goal

6. User Journey Map

Buat alur:
Login

Dashboard

Input/import data venue

Integrasi ZNT

Estimasi omzet

Perhitungan PBJT

Deteksi anomali

Analisis keberlanjutan usaha

Dashboard risiko & sustainability

Prioritas pengawasan
Jelaskan setiap tahap.

7. Functional Requirements

Buat detail modul berikut:

Module 1: Authentication & User
Management

Fitur:
     Login
     Role management
     Authorization

Module 2: Venue Data Management

Fitur:
     Input venue
     Edit venue
     Delete venue
     Import dataset

Data:
     Nama venue
     Lokasi
     Latitude
     Longitude
     Jumlah court
     Harga sewa
     Jam operasional
     Hari operasi
Module 3: GIS & ZNT Integration

Jelaskan:
     Mapping lokasi venue
     Integrasi koordinat
     Spatial analysis
     Informasi Zona Nilai Tanah

Output:
     Nilai ZNT
     Wilayah
     Faktor ekonomi lokasi

Module 4: Revenue Estimation Engine

Jelaskan:
Input:

     Jumlah court
     Harga sewa
     Jam operasional
     Hari operasi
     ZNT
     Lokasi
Proses:
Feature Engineering  Machine Learning  Prediction
Output:
Estimasi omzet bulanan.

Module 5: PBJT Estimation Engine

Jelaskan:
Formula:
PBJT = Estimasi Omzet � Tarif PBJT
Jelaskan:

     Parameter
     Input
     Output

Module 6: Anomaly Detection System

Tujuan:
Mendeteksi ketidaksesuaian antara potensi dan pembayaran.
Input:

     Estimasi omzet
     Estimasi PBJT
     PBJT aktual
Output:
     Anomaly score
     Risk category
     Ranking wajib pajak
Kategori:
     Normal
     Monitoring
     High Risk

Module 7: Business Sustainability
Analytics

Tujuan:
Memberikan indikasi prospek keberlanjutan usaha venue berdasarkan tren
performa yang tersedia, bukan menjamin umur perusahaan secara pasti.
Input (bergantung ketersediaan data historis):
     Estimasi omzet per periode
     Omzet laporan per periode
     PBJT pembayaran per periode
     Tren pertumbuhan/penurunan
     Jumlah court
     Harga sewa
     Jam operasional
     Lokasi dan ZNT
     Anomaly score historis

Proses:

Historical Trend Analysis  Feature Engineering  Sustainability Scoring
/ Forecasting

Output:

     Sustainability Score (0-100)
     Business Outlook: Positif / Stabil / Waspada
     Tren performa usaha
     Indikasi risiko penurunan
     Proyeksi jangka pendek-menengah (misalnya 1-3 tahun) hanya jika

         kualitas dan panjang data historis memadai

Catatan:

     Sistem tidak boleh mengklaim secara deterministik bahwa perusahaan
         akan bertahan selama X tahun.

     Jika data historis belum cukup, tampilkan "Data belum memadai untuk
         proyeksi" dan gunakan analisis tren/deskriptif.

     Untuk MVP 14 minggu, fitur ini diposisikan sebagai Should
         Have/prototype dan tidak boleh mengorbankan fitur inti estimasi PBJT
         dan deteksi anomali.

Module 8: Dashboard Analytics

Buat rancangan:

Dashboard utama:

     Total venue
     Total omzet potensial
     Total PBJT potensial
     Jumlah anomali

Grafik:
     Trend omzet
     Distribusi risiko
     Tren Sustainability Score / business outlook (jika tersedia)
Map:
     Lokasi venue
     Zona risiko
Detail:
     Profil venue
     Prediksi
     Pajak
     Risiko
     Sustainability Score dan business outlook

8. Machine Learning Requirements

Buat desain ML profesional.

Model 1: Revenue Prediction Model

Tujuan:
Prediksi omzet bulanan venue.
Jelaskan:

     Dataset
     Feature
     Target variable
     Feature engineering
     Algoritma
     Training workflow
     Evaluation metrics
Gunakan rekomendasi:
XGBoost Regression
Metric:
     MAE
     RMSE
     R2 Score

Model 2: Anomaly Detection Model

Tujuan:
Mendeteksi pembayaran pajak abnormal.
Jelaskan:

     Dataset
     Feature
     Metode
     Threshold
     Output
Gunakan rekomendasi:
Isolation Forest

Model 3: Business Sustainability Model
(Should Have / Prototype)

Tujuan:
Mengestimasi sustainability score dan outlook keberlanjutan usaha
berdasarkan pola historis yang tersedia.
Jelaskan:

     Minimum kebutuhan data historis
     Feature
     Target/proxy target
     Metode forecasting atau scoring
     Validasi
     Confidence/uncertainty
     Keterbatasan interpretasi
Rekomendasi pendekatan MVP:
     Mulai dari trend analysis dan rule-based/weighted sustainability
         scoring yang transparan.

     Jika tersedia data historis yang cukup, evaluasi model
         forecasting/regression yang sesuai.

     Hindari klaim "venue akan bertahan X tahun" tanpa data
         survival/closure historis yang memadai.

     Untuk prediksi umur usaha secara formal pada pengembangan lanjutan,
         pertimbangkan survival analysis setelah tersedia data tanggal
         buka/tutup dan histori usaha yang cukup.

Output:

     Sustainability Score (0-100)
     Business Outlook
     Trend direction
     Confidence level
     Faktor utama yang memengaruhi skor

9. Data Requirements

Buat rancangan database.

Venue Dataset

Field:

     venue_id
     nama
     lokasi
     latitude
     longitude
     jumlah_court
     harga_sewa
     jam_operasi
     rating

Spatial Dataset

Field:

     latitude
     longitude
     wilayah
     polygon
     ZNT

Tax Dataset

Field:
     wajib_pajak
     omzet_laporan
     PBJT_pembayaran
     periode
     status_usaha (opsional, jika tersedia)
     tanggal_mulai_usaha (opsional)
     tanggal_tutup_usaha (opsional, untuk pengembangan survival analysis)

10. System Architecture

Gunakan:
Frontend:
React PWA
Backend:
FastAPI
Database:
PostgreSQL + PostGIS
Machine Learning:
Python
Scikit-learn
XGBoost
GIS:
GeoPandas
Leaflet
Buat diagram:
User

Frontend

Backend API

Database

ML Service

Dashboard

11. Database Design

Buat ERD konseptual:
Table:

     users
     venues
     spatial_znt
     revenue_prediction
     tax_payment
     anomaly_result
     sustainability_result
Jelaskan:
     Primary key
     Foreign key
     Relationship

12. UI/UX Requirement
Buat rancangan:

Login Page

Dashboard Page

Map Page

Venue Detail Page

Jelaskan:
     Komponen
     Informasi yang ditampilkan
     User interaction

13. Non Functional Requirement

Jelaskan:

Performance

     Response time
     Scalability

Security

     Authentication
     Authorization
     Data protection

Maintainability

     Modular architecture
     Documentation

Usability

     User friendly dashboard
14. Development Roadmap

Buat timeline:

September 2026

Research & Requirement
Output:

     Requirement analysis
     System design

Oktober 2026

Database + Backend + ML
Output:

     Database
     API
     Model ML utama
     Eksperimen sustainability scoring berbasis tren jika data historis

         tersedia

November 2026

Frontend + Dashboard Integration
Output:

     Dashboard
     GIS visualization
     Visualisasi sustainability score/business outlook (Should Have)

Desember 2026

Testing + Deployment + Documentation
Output:

     Testing
     Deployment
     Final report
Buat sprint mingguan.

15. MVP Definition

Tentukan:

Must Have

     Data management
     GIS & ZNT integration
     Revenue estimation
     PBJT estimation
     Anomaly detection
     Dashboard risiko

Should Have

     Business Sustainability Analytics sederhana
     Sustainability Score
     Business Outlook dan tren performa
     Proyeksi 1-3 tahun hanya jika data historis memadai

Could Have

     Survival analysis untuk estimasi probabilitas keberlangsungan usaha
     Prediksi time-to-event/risiko penutupan usaha setelah tersedia

         dataset historis yang memadai
Pastikan realistis selesai dalam 14 minggu.

16. Future Development

Berikan pengembangan:
     Integrasi API Bappenda
     Real-time monitoring
     AI assistant pajak
     Prediksi penerimaan pajak daerah
     Model survival analysis untuk probabilitas keberlangsungan usaha
     Early warning system penurunan kesehatan usaha
     Ekspansi sektor pajak lain

Output Format

Gunakan:

     Bahasa Indonesia formal profesional.
     Struktur heading jelas.
     Gunakan tabel jika membantu.
     Gunakan diagram ASCII bila diperlukan.
     Jangan membuat fitur terlalu besar.
     Fokus pada MVP yang dapat selesai dalam periode magang.
     Bedakan dengan jelas antara analisis potensi pajak, anomaly risk,

         dan business sustainability.
     Jangan menyatakan perusahaan pasti dapat bertahan X tahun kecuali

         tersedia data historis survival/closure yang memadai; gunakan
         sustainability score, outlook, probabilitas, dan confidence level.
