# ML-Random_Forrest
Pohon keputusan memberi Anda keputusan yang sulit. Pohon yang dalam dengan banyak daun akan cocok karena setiap prediksi berasal dari data historis hanya dari beberapa rumah di daunnya. 
Tetapi pohon yang dangkal dengan sedikit daun akan berkinerja buruk karena gagal menangkap banyak perbedaan dalam data mentah.
Bahkan teknik pemodelan paling canggih saat ini menghadapi ketegangan antara underfitting dan overfitting. 
Namun, banyak model memiliki ide-ide cerdas yang dapat menghasilkan kinerja yang lebih baik. Kita akan melihat hutan acak (random forrest) sebagai contoh.

=>Hutan acak menggunakan banyak pohon, dan membuat prediksi dengan merata-ratakan prediksi setiap pohon komponen.
 
Ini umumnya memiliki akurasi prediksi yang jauh lebih baik daripada pohon keputusan tunggal dan bekerja dengan baik dengan parameter default.
Jika Anda terus membuat model, Anda dapat mempelajari lebih banyak model dengan kinerja yang lebih baik, tetapi banyak di antaranya yang sensitif untuk mendapatkan parameter yang tepat.
