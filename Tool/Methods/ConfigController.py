import configparser, os


class ConfigController(object):
    """操作配置文件的类"""

    def __init__(self, path):
        self.path = path

        if not os.path.exists(self.path):
            raise IOError("File {} is not found!".format(self.path))

        try:
            self.con = configparser.ConfigParser()
            self.con.read(self.path)
        except Exception as e:
            raise IOError(str(e))

    def get(self, section: str, key: str):
        """读取配置文件数据"""
        return self.con.get(section, key)

    def set(self, section: str, key: str, value):
        """写配置文件数据"""
        self.con.set(section, key, value)
        with open(self.path, "w") as f:
            self.con.write(f)


con = ConfigController("../Tool/Settings/config.ini")
wRatio = int(con.get("main", "width")) / 1024
hRatio = int(con.get("main", "height")) / 768
