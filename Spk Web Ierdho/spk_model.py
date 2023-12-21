from settings import NAMA_SCALE, PROSESOR_SCALE

class BaseMethod():

    def __init__(self, data_hp, **setWeight):

        self.huawei_phone_data = data_hp

        # 1-9
        self.raw_weight = {
            'nama_produk': 8,
            'layar': 1,
            'prosesor': 2,
            'ram': 7,
            'penyimpanan': 6,
            'kamera_belakang': 5,
            'kamera_depan': 4,
            'baterai': 3,
            'harga': 9
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]]
                temp2 = {v: k for k, v in setWeight.items()}[item[1]]
                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': huawei['nama_produk'],
            'nama_produk': NAMA_SCALE[huawei['nama_produk']],
            'layar': float(huawei['layar'].replace(" inci", "")),
            'prosesor': PROSESOR_SCALE[huawei['prosesor']],
            'ram': huawei['ram'],
            'penyimpanan': huawei['penyimpanan'],
            'kamera_belakang': huawei['kamera_belakang'],
            'kamera_depan': huawei['kamera_depan'],
            'baterai': huawei['baterai'],
            'harga': huawei['harga']
        } for huawei in self.huawei_phone_data]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        nama_produk = [] # max
        layar = [] # max
        prosesor = [] # max
        ram = [] # max
        penyimpanan = [] # max
        kamera_belakang = [] # max
        kamera_depan = [] # max
        baterai = [] # max
        harga = [] # min

        for data in self.data:
            nama_produk.append(data['nama_produk'])
            layar.append(data['layar'])
            prosesor.append(data['prosesor'])
            ram.append(data['ram'])
            penyimpanan.append(data['penyimpanan'])
            kamera_belakang.append(data['kamera_belakang'])
            kamera_depan.append(data['kamera_depan'])
            baterai.append(data['baterai'])
            harga.append(data['harga'])

        max_nama_produk = max(nama_produk)
        max_layar = max(layar)
        max_prosesor = max(prosesor)
        max_ram = max(ram)
        max_penyimpanan = max(penyimpanan)
        max_kamera_belakang = max(kamera_belakang)
        max_kamera_depan = max(kamera_depan)
        max_baterai = max(baterai)
        min_harga = min(harga)

        return [{
            'id': data['id'],
            'nama_produk': data['nama_produk']/max_nama_produk,
            'layar': data['layar']/max_layar,
            'prosesor': data['prosesor']/max_prosesor,
            'ram': data['ram']/max_ram,
            'penyimpanan': data['penyimpanan']/max_penyimpanan,
            'kamera_belakang': data['kamera_belakang']/max_kamera_belakang,
            'kamera_depan': data['kamera_depan']/max_kamera_depan,
            'baterai': data['baterai']/max_baterai,
            'harga': min_harga/data['harga']
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    def __init__(self, huawei_phone_data, setWeight:dict):
        super().__init__(data_hp=huawei_phone_data, **setWeight)

    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['id']:
            round(
                row['nama_produk'] ** weight['nama_produk'] *
                row['layar'] ** weight['layar'] *
                row['prosesor'] ** weight['prosesor'] *
                row['ram'] ** weight['ram'] *
                row['penyimpanan'] ** weight['penyimpanan'] *
                row['kamera_belakang'] ** weight['kamera_belakang'] *
                row['kamera_depan'] ** weight['kamera_depan'] *
                row['baterai'] ** weight['baterai'] *
                row['harga'] ** (-weight['harga'])
                , 2
            )

            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))
