import tornado.ioloop
import tornado.web
import database

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hi there!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #print(self.request)
        id = self.get_argument('id', default = None)
        if id == None:
            result = database.get_all()
            for r in result:
                self.write(dict(r.id, r.name, r.quantity))
        else:
            r = database.get(int(id))
            self.write(dict(r.id, r.name, r.quantity))

    def put(self):
        #print(self.request)
        name = self.get_argument('name')
        quantity = self.get_argument('quantity')
        item = database.Items(name = name, quantity = quantity)
        database.add(item)

    def delete(self):
        id = self.get_argument('id')
        database.delete(int(id))

    def patch(self):
        id = self.get_argument('id')
        name = self.get_argument('name', default = None)
        quantity = self.get_argument('quantity', default = None)
        if name == None and quantity == None:
            return
        database.update(int(id), name, quantity)

#returns vars as dictionary
def dict(id, name, quantity):
    return {'id':id, 'name':name, 'quantity':quantity}

def make_app():
    return tornado.web.Application([
        (r'/hi', TestHandler),
        (r'/items', MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
