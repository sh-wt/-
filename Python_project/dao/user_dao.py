# 用户的数据访问层
"""传入相应的参数进行，通过父类（basedao）对数据库中`t_user`进行操作"""
from .base_dao import BaseDao

class UserDao(BaseDao):
    def add_user(self, conn, username, password):
        """添加用户"""
        sql = "INSERT INTO `t_user` (username, password) VALUES (%s, %s)"
        params = (username, password)
        return self.execute_insert_auto_id(conn, sql, params)

    def emp_list_user(self, conn, name):
        """查询用户"""
        sql = f"SELECT `username` FROM `t_user` WHERE `id` = (SELECT `user_id` FROM `t_emp` WHERE `name` = '{name}')"
        return self.execute_query(conn, sql, params=None)

    def modify_user(self, conn, info, new_date, hire_id):
        """修改用户"""
        sql = f"UPDATE `t_user` SET `{info}` = '{new_date}' WHERE `id` = {hire_id}"
        return self.execute_update(conn, sql, params=None)

    def sea_id_user(self, conn, hire_id):
        sql_1 = f"SELECT `username` FROM `t_user` WHERE `id` = {hire_id}"
        return self.execute_query(conn, sql_1, params=None)

    def del_user(self, conn, username):
        """根据user_id获取的username来删除信息"""
        sql = f"DELETE FROM `t_user` WHERE `username` = '{username}'"
        return self.execute_update(conn, sql, params=None)
