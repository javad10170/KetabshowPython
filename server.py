from libgenapi import Libgenapi
from flask import Flask, json

api = Flask(__name__)


@api.route('/', methods=['GET'])

def get_companies():
    lg = Libgenapi(["http://libgen.lc/", "http://gen.lib.rus.ec/"])
    return json.dumps(lg.search("python"))


if __name__ == '__main__':
    api.run()
