import pandas as pd
from spk_model import WeightedProduct

class HuaweiPhone():

    def __init__(self) -> None:
        self.huawei_phone = pd.read_csv('huaweiphone_202311010621.csv')

    def get_recs(self, kriteria):
        wp = WeightedProduct(self.huawei_phone.to_dict(orient="records"), kriteria)
        return wp.calculate

