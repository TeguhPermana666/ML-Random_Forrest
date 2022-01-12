"""
#INTRO
Pohon keputusan memberi Anda keputusan yang sulit. Pohon yang dalam dengan banyak daun akan cocok karena setiap prediksi berasal dari data historis hanya dari beberapa rumah di daunnya. 
Tetapi pohon yang dangkal dengan sedikit daun akan berkinerja buruk karena gagal menangkap banyak perbedaan dalam data mentah.
Bahkan teknik pemodelan paling canggih saat ini menghadapi ketegangan antara underfitting dan overfitting. 
Namun, banyak model memiliki ide-ide cerdas yang dapat menghasilkan kinerja yang lebih baik. Kita akan melihat hutan acak (random forrest) sebagai contoh.

=>Hutan acak menggunakan banyak pohon, dan membuat prediksi dengan merata-ratakan prediksi setiap pohon komponen.
 
Ini umumnya memiliki akurasi prediksi yang jauh lebih baik daripada pohon keputusan tunggal dan bekerja dengan baik dengan parameter default.
Jika Anda terus membuat model, Anda dapat mempelajari lebih banyak model dengan kinerja yang lebih baik, tetapi banyak di antaranya yang sensitif untuk mendapatkan parameter yang tepat.

Variabel contoh:
->train_X
->val_X
->train_y
->val_y
"""
import pandas as pd
#load data
file_path="intro to ml\melb_data.csv"
model_data=pd.read_csv(file_path)
#filttered rows missing data
model_data=model_data.dropna(axis=0)
print(model_data.columns)
#select target predictions and fitur
y=model_data.Price
fitur=['Rooms', 'Bathroom', 'Landsize', 'BuildingArea','YearBuilt', 'Lattitude', 'Longtitude']
X=model_data[fitur]
#define build model
from sklearn.model_selection import train_test_split 
train_x,val_x,train_y,val_y=train_test_split(X,y)
"""
proses pembuatan model random foresst hampir sama dengan dession tree namun yang membdekan adalah 
penggunaan librarynya
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
foorest_model=RandomForestRegressor(random_state=1)
#train model data
foorest_model=foorest_model.fit(train_x, train_y)
melb_predcs=foorest_model.predict(val_x)
mea=mean_absolute_error(val_y, melb_predcs)
print("MEA=>",mea)