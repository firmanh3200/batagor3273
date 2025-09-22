import pandas as pd
import openpyxl

data = pd.read_excel('gis-dukcapil2.xlsx')
df = pd.DataFrame(data)

pilihankab = df['Kabupaten/Kota'].unique()

datapenduduk = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 'Jumlah Penduduk', 
                     'Jumlah Kepala Keluarga']]

datapendudukkec = datapenduduk.groupby(['Provinsi', 'Kabupaten/Kota', 'Kecamatan'])[['Jumlah Penduduk', 'Jumlah Kepala Keluarga']].sum().reset_index()

dataagama = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 'Islam',	'Kristen',	
                  'Katholik',	'Hindu', 'Buddha', 'Konghuchu',	'Kepercayaan terhadap Tuhan YME']]
dataagama2 = dataagama.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'], 
                             value_vars=['Islam', 'Kristen', 'Katholik', 'Hindu', 
                                         'Buddha', 'Konghuchu', 'Kepercayaan terhadap Tuhan YME'],
                             var_name='Agama', value_name='Jumlah Penduduk')

datajeniskelamin = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 'Laki-laki', 'Perempuan']]
datajeniskelamin2 = datajeniskelamin.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                                          value_vars=['Laki-laki', 'Perempuan'], var_name='Jenis Kelamin',
                                          value_name='Jumlah Penduduk')

datastatuskawin = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 'Belum Kawin',	'Kawin', 
                    'Cerai Hidup',	'Cerai Mati']]
datastatuskawin2 = datastatuskawin.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                                        value_vars=['Belum Kawin', 'Kawin', 'Cerai Hidup', 'Cerai Mati'],
                                        var_name='Status Kawin', value_name='Jumlah Penduduk')

dataumur = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', '00 - 04', '05 - 09',	'10 - 14', 
             '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '45 - 49', '50 - 54',	
             '55 - 59',	'60 - 64', '65 - 69', '70 - 74', '75+']]
dataumur2 = dataumur.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                          value_vars=['00 - 04', '05 - 09',	'10 - 14', '15 - 19', '20 - 24', 
                                      '25 - 29', '30 - 34', '35 - 39', '40 - 44', '45 - 49', 
                                      '50 - 54', '55 - 59',	'60 - 64', '65 - 69', '70 - 74', '75+'],
                          var_name='Kelompok Umur', value_name='Jumlah Penduduk')

datausiadidik = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 
                      '03 - 04', '05', '06 - 11', '12 - 14', '15 - 17',	'18 - 22']]
datausiadidik2 = datausiadidik.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                                    value_vars=['03 - 04', '05', '06 - 11', '12 - 14', '15 - 17',	'18 - 22'],
                                    var_name='Usia Pendidikan', value_name='Jumlah Penduduk')


datapendidikan = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 
                       'Tidak/Belum Sekolah', 'Belum Tamat SD',	'Tamat SD', 'SLTP',	
                       'SLTA',	'D1 dan D2',	'D3',	'S1',	'S2',	'S3']]
datapendidikan2 = datapendidikan.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                                      value_vars=['Tidak/Belum Sekolah', 'Belum Tamat SD',	'Tamat SD', 'SLTP',	
                                                'SLTA',	'D1 dan D2', 'D3', 'S1', 'S2', 'S3'],
                                      var_name='Pendidikan', value_name='Jumlah Penduduk')

datagolongandarah = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 
                        'O', 'B-', 'B+', 'O+', 'AB-', 'A', 'Tidak Diketahui', 'AB+', 'A+', 'A-', 'O-', 'B', 'AB']]
datagolongandarah2 = datagolongandarah.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                                            value_vars=['O', 'B-', 'B+', 'O+', 'AB-', 'A', 'Tidak Diketahui', 'AB+', 
                                                        'A+', 'A-', 'O-', 'B', 'AB'],
                                            var_name='Golongan Darah', value_name='Jumlah Penduduk')

datapekerjaan = df[['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa', 
                      'Belum/Tidak Bekerja', 'Pensiunan', 'Mengurus Rumah Tangga',
                      'Perdagangan', 'Perawat',	'Nelayan', 'Pelajar dan Mahasiswa',
                      'Guru', 'Wiraswasta',	'Pengacara', 'Pekerjaan Lainnya']]
datapekerjaan2 = datapekerjaan.melt(id_vars=['Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'],
                                    value_vars=['Belum/Tidak Bekerja', 'Pensiunan', 'Mengurus Rumah Tangga',
                                            'Perdagangan', 'Perawat',	'Nelayan', 'Pelajar dan Mahasiswa',
                                            'Guru', 'Wiraswasta',	'Pengacara', 'Pekerjaan Lainnya'],
                                    var_name='Pekerjaan', value_name='Jumlah Penduduk')

