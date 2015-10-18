from kazoo.exceptions import NoNodeError

__author__ = 'hiepsimu'


class ClientCommandHandler(object):
    def __init__(self, zk, cmd_path, client_path, client_name):
        self.cmd_path = cmd_path
        self.client_path = client_path
        self.client_name = client_name
        self.zk = zk
        self.client_version = None
        self.client_full_path = client_path + '/' + client_name

        self.init()

        @zk.ChildrenWatch(cmd_path)
        def my_listener(children):
            keys = sorted(children)
            for key in keys:
                if key <= self.client_version:
                    continue
                self.handle_command(key)

            # print commands

            return True

    def init(self):
        try:
            client_version, stat = self.zk.get(self.client_full_path)
        except NoNodeError:
            client_version = ""
            self.zk.create(self.client_full_path, "", makepath=True)

        self.client_version = client_version

    def update_version(self, version):
        self.zk.set(self.client_full_path, version.encode('utf-8'))
        self.client_version = version

    def handle_command(self, key):
        val, stat = self.zk.get(self.cmd_path + '/' + key)
        # Execute
        print 'execute %s' % val
        print key
        print key.__class__

        self.update_version(key)