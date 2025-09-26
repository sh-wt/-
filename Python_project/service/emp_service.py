#业务逻辑处理
from .user_service import UserService
from dao.emp_dao import EmpDao
from datetime import datetime


class EmpService:
    def __init__(self):
        self.user_service = UserService()
        self.emp_dao = EmpDao()

    def create_emp_with_user(self, emp_name, emp_gender, emp_age):
        """在事务中创建员工并绑定用户"""
        conn = self.emp_dao.get_connection(autocommit=False)
        try:
            # 创建用户
            user_id, username = self.user_service.create_user(conn)
            if user_id is None:
                conn.rollback()
                print("用户创建失败，事务回滚")
                return
            # 创建员工并绑定用户
            hire_date = datetime.now().strftime("%Y-%m-%d")
            emp_rows = self.emp_dao.add_emp(conn, emp_name, emp_gender, emp_age, user_id, hire_date)
            if emp_rows <= 0:
                conn.rollback()
                print("员工创建失败，事务回滚")
                return
            # 手动提交事务
            conn.commit()
            print("员工和用户创建成功！")
            print(f"用户名: {username}，密码: 123456")
        except Exception as e:
            # 出现异常，回滚事务
            conn.rollback()
            print(f"出现异常，事务回滚，错误信息: {e}")
        finally:
            # 关闭连接
            if conn:
                conn.close()

    def sea_emp_with_user(self, name):
        """根据姓名查询用户信息"""
        conn = self.emp_dao.get_connection(autocommit=False, )
        try:
            # 查询t_emp信息
            t_emp_info = self.emp_dao.emp_list_emp(conn, name)
            #查询user信息
            t_user_info = self.user_service.sea_name_user(conn, name)
            # 手动提交事务
            conn.commit()
            # 判断是否存在
            if t_emp_info and t_user_info:
                print("-------------员工信息如下---------------")
                t_emp_info[0]['username'] = t_user_info[0]['username']
                print(t_emp_info)
                return
            print(f"{name}用户不存在")
            return t_emp_info and t_user_info
        except Exception as e:
            # 出现异常，回滚事务
            conn.rollback()
            print(f"出现异常，事务回滚，错误信息: {e}")
        finally:
            # 关闭连接
            if conn:
                conn.close()


    def mod_emp_with_user(self, info, new_date, hire_id):
        """修改用户信息"""
        conn = self.emp_dao.get_connection(autocommit=False)
        try:
            # 判断要处理的业务
            emp_info_list = ['name', 'gender', 'age']
            user_info_list = ['username', 'password']
            if info in emp_info_list:
                emp_rows = self.emp_dao.modify_emp(conn, info, new_date, hire_id)
                # 手动提交事务
                conn.commit()
                # 判断是否修改成功
                if emp_rows <= 0:
                    conn.rollback()
                    print("员工信息修改失败（可能user_id有误），事务回滚")
                    return
                print(f'已成功将{info}内容修改为{new_date}')
                return
            elif info in user_info_list:
                user_rows = self.user_service.mod_user(conn, info, new_date, hire_id)
                # 手动提交事务
                conn.commit()
                # 判断是否修改成功
                if user_rows <= 0:
                    conn.rollback()
                    print("员工信息修改失败（可能user_id有误），事务回滚")
                    return
                print(f'已成功将{info}内容修改为{new_date}')
                return
            else:
                print(f"{info}不在业务范围内")
        except Exception as e:
            # 出现异常，回滚事务
            conn.rollback()
            print(f"出现异常，事务回滚，错误信息: {e}")
        finally:
            # 关闭连接
            if conn:
                conn.close()

    def del_emp_with_user(self, hire_id):
        """根据user_id查找的username删除用户信息"""
        conn = self.emp_dao.get_connection(autocommit=False)
        try:
            username_dict = self.user_service.sea_id_user(conn, hire_id)
            # 手动提交事务
            conn.commit()
            if username_dict:
                username = username_dict[0].get('username')
                user_rows = self.user_service.del_id_user(conn, username)
                # 手动提交事务
                conn.commit()
                # 判断是否删除成功
                if user_rows <= 0 :
                    conn.rollback()
                    print("员工信息修改失败，事务回滚")
                    return
                else:
                    emp_info = self.emp_dao.delete_emp(conn, hire_id)
                    # 手动提交事务
                    conn.commit()
                    if emp_info:
                        conn.rollback()
                        print("员工信息修改失败，事务回滚")
                        return
                    else:
                        print(f"id为{hire_id}的员工已成功删除")
            else:
                conn.rollback()
                print("员工信息修改失败（可能user_id不存在），事务回滚")
        except Exception as e:
            # 出现异常，回滚事务
            conn.rollback()
            print(f"出现异常，事务回滚，错误信息: {e}")
        finally:
            # 关闭连接
            if conn:
                conn.close()





