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
        name = self.get_argument('name')
        quantity = self.get_argument('quantity')
        item = database.Items(name = name, quantity = quantity)
        database.add(item)


def make_app():
    return tornado.web.Application([
        (r"/hi", TestHandler),
        (r"/items", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
