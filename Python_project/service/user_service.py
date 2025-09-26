#业务逻辑处理
import random
import string
from dao.user_dao import UserDao

class UserService:
    def __init__(self):
        self.user_dao = UserDao()
    @staticmethod
    def generate_random_username(length=8):
        """生成指定长度的随机用户名"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    def create_user(self, conn):
        """创建用户，用户名随机生成，密码默认 123456"""
        username = self.generate_random_username()
        password = '123456'
        return self.user_dao.add_user(conn, username, password), username

    def sea_name_user(self, conn, name):
        """根据name查询信息"""
        return self.user_dao.emp_list_user(conn, name)

    def mod_user(self, conn, info, new_date, hire_id):
        """修改信息"""
        return self.user_dao.modify_user(conn, info, new_date, hire_id)

    def sea_id_user(self, conn, hire_id):
        """根据user_id查询username"""
        return self.user_dao.sea_id_user(conn, hire_id)

    def del_id_user(self, conn, username):
        """根据hire_id查找username来删除用户"""
        return self.user_dao.del_user(conn, username)
