from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

application = Flask(__name__)
api = Api(application)

URLS = {
    'url1': {'url': 'https://www.datatorrent.com/blog/fault-tolerant-file-processing/'},
    'url2': {'url': 'https://blogs.apache.org/hbase/entry/tuning_g1gc_for_your_hbase'},
    'url3': {'url': 'https://engineering.linkedin.com/blog/2016/05/kafkaesque-days-at-linkedin--part-1'}

}

def abort_if_url_doesnt_exist(url_id):
    if url_id not in URLS:
        abort(404, message = "URL {} doesnt exist".format(url_id))


parser = reqparse.RequestParser()
parser.add_argument('url')

#Todo
# shows a singlevtodo item and lets ou delete atodo item

class URL(Resource):
    def get(self, url_id):
        abort_if_url_doesnt_exist(url_id)
        return URLS[url_id]

    def delete(self, url_id):
        abort_if_url_doesnt_exist(url_id)
        del URLS[url_id]
        return '', 204

    def put(self, url_id):
        args = parser.parse_args()
        url = {'url': args['url']}
        URLS[url_id] = url
        return url, 201


class URLList(Resource):
    def get(self):
        return URLS

    def post(self):
        args = parser.parse_args()
        url_id = int(max(URLS.keys()).lstrip('url')) + 1
        url_id = 'url%i' % url_id
        URLS[url_id] = {'url': args['url']}
        return URLS[url_id], 201

# Actually setup the APi resource routing here

api.add_resource(URLList, '/url')
api.add_resource(URL, '/url/<url_id>')


if __name__ == '__main__':
    application.run(debug=True)
















