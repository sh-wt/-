#封装通用数据库操作，是所以dao的父类
"""运用连接池技术连接数据库、优化结构下的预编译SQL进行相关操作"""
from dbutils.pooled_db import PooledDB
import pymysql


class BaseDao:
    def __init__(self):
        # 创建连接池，默认自动提交
        self.pool = PooledDB(
            creator=pymysql,
            host='你的MySQL的ip地址',
            user='你的MySQL的名字',
            password='你的MySQL的密码',
            database='进行管理的数据库',
            autocommit=True,   #True为自动提交
            charset='根据你的设置选择编码',
            #后续的都可以自行修改
            cursorclass=pymysql.cursors.DictCursor,
            mincached=2,
            maxcached=5,
            maxshared=3,
            maxconnections=6,
            blocking=True
        )

    def get_connection(self, autocommit=True):
        """从连接池获取连接，可指定是否自动提交"""
        conn = self.pool.connection()
        conn.autocommit = autocommit
        return conn
    @staticmethod
    def execute_query(conn, sql, params=None):
        """执行查询语句"""
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"执行查询时出现错误: {e}")
            return []
    @staticmethod
    def execute_update(conn, sql, params=None):
        """执行更新语句（如 INSERT、UPDATE、DELETE）"""
        try:
            with conn.cursor() as cursor:
                rows_affected = cursor.execute(sql, params)
                return rows_affected
        except Exception as e:
            print(f"执行更新时出现错误: {e}")
            return 0
    @staticmethod
    def execute_insert_auto_id(conn, sql, params=None):
        """执行更新语句（如 INSERT"""
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.lastrowid
        except Exception as e:
            print(f"执行更新时出现错误: {e}")
            return 0