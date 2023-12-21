from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api 

from models import HuaweiPhone

app = Flask(__name__)
api = Api(app)        

class Recommendation(Resource):

    def post(self):
        criteria = request.get_json()
        validCriteria = ['nama_produk','layar','prosesor','ram','penyimpanan','kamera_belakang','kamera_depan','baterai','harga']
        huawei_phone = HuaweiPhone()

        if not criteria:
            return 'criteria is empty', HTTPStatus.BAD_REQUEST.value

        if not all([v in validCriteria for v in criteria]):
            return 'criteria is not found', HTTPStatus.NOT_FOUND.value

        recommendations = huawei_phone.get_recs(criteria)

        return {
            'alternatif': recommendations
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
