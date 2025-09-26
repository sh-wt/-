# 员工的数据访问层
"""传入相应的参数进行，通过父类（basedao）对数据库中`t_emp`进行操作"""
from .base_dao import BaseDao

class EmpDao(BaseDao):
    def add_emp(self, conn, emp_name, emp_gender, emp_age, user_id,hire_date):
        """添加员工并绑定用户"""
        sql = "INSERT INTO `t_emp` (`name`, `gender`, `age`, `user_id`,`hire_date`) VALUES (%s, %s, %s, %s, %s)"
        params = (emp_name, emp_gender, emp_age, user_id, hire_date)
        return self.execute_update(conn, sql, params)

    def emp_list_emp(self, conn, name):
        """根据姓名查询信息"""
        sql = f"SELECT * FROM `t_emp` WHERE `name` = '{name}'"
        return self.execute_query(conn, sql, params=None)


    def modify_emp(self, conn, info, new_date, hire_id):
        """修改信息"""
        sql = f"UPDATE `t_emp` SET `{info}` = '{new_date}' WHERE `user_id` = {hire_id}"
        return self.execute_update(conn, sql, params=None)

    def delete_emp(self, conn, hire_id):
        """根据user_id来查询是否成功删除"""
        sql = f"SELECT * FROM `t_emp` WHERE `user_id` = {hire_id}"
        return self.execute_update(conn, sql, params=None)