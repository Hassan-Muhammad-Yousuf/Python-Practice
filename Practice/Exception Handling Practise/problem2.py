class SocketError(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)


try:
    raise SocketError('socket connection failed')
except SocketError as e:
    print("caught error", e)