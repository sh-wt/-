# 在新增员工 emp 的同时，往 user 里面插入一条数据
"""用户交互界面程序"""
from service.emp_service import EmpService

emp_service = EmpService()

def add_emp():
    emp_name = input("员工名称：")
    emp_gender = input('员工性别：')
    emp_age = int(input('员工年龄：'))
    emp_service.create_emp_with_user(emp_name, emp_gender, emp_age)
def emp_list():
    name = input("请输入您要查询用户的名字：")
    emp_service.sea_emp_with_user(name)
def modify_emp():
    hire_id = int(input("请输入您要修改员工的user_id："))
    info = input("请输入您需要修改的业务（如name、password等）：")
    new_date = input("请输入您修改的内容：")
    emp_service.mod_emp_with_user(info, new_date, hire_id)
def delete_emp():
    hire_id = int(input("请输入您需要删除的员工user_id："))
    emp_service.del_emp_with_user(hire_id)
def start_system():
    is_continue = True
    while is_continue:
        print('-------欢迎使用员工管理系统-------')
        print('1.添加员工')
        print('2.员工列表')
        print('3.修改员工')
        print('4.删除员工')
        print('0.退出系统')
        print('---------------------------------')
        item = input('请输入：')
        if item == '1':
            add_emp()
        elif item == '2':
            emp_list()
        elif item == '3':
            modify_emp()
        elif item == '4':
            delete_emp()
        elif item == '0':
            is_continue = False
        else:
            print('错误选项！')

if __name__ == '__main__':
    start_system()