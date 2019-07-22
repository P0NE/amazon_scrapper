import os
import csv
from flask import Flask, request
from dotenv import load_dotenv
from flask_restplus import Api, Resource, fields

load_dotenv()
app = Flask(__name__)
app_plus = Api(app=app, version="1.0", title="Scrapper Price API",
               description="APIs for add an URL to scrappe the price")

scrapp_model = app_plus.model("scrapper", {
    "email": fields.String("Email of the user"),
    "url": fields.Url("URL to scrappe"),
    "price": fields.Float("price to check")})


@app_plus.route('/scrapper')
class Scrapper(Resource):

    @app_plus.expect(scrapp_model)
    def post(self):
        """
        Receive scrapping info and adding to csv for the script
        """
        new_sc = app_plus.payload
        print(new_sc)
        with open('check.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(
                [new_sc['email'], new_sc['url'], new_sc['price']])
        return {'result': 'add for scrapping'}, 201


HOST = os.environ.get('SERVER_HOST', 'localhost')
PORT = os.environ.get('SERVER_PORT', '8000')
app.run(HOST, PORT, debug=True)
