import tornado.ioloop
import tornado.web
import database

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hi there!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.request)

    def post(self):
        print(self.request)
        item = self.get_argument('item')
        value = self.get_argument('value')
        con = database.Connection()
        con.add(item, value)


def make_app():
    return tornado.web.Application([
        (r"/hi", TestHandler),
        (r"/get", MainHandler),
        (r"/post", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
