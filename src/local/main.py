import keyboard
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        # (r"/ext", )
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# class Handler:
#     def is_active(self) -> bool:
#         pass
#
#     def handle(self, key):
#         pass
#
# from typing import List
#
# class KeyboardManager:
#     handlers: List[Handler]
#
#     def hook(self, key):
#         handler = self.res
#
#     def resolve_handler(self):
#         pass
