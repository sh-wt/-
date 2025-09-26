# -
运用python和MySQL进行员工信息管理（用于初学者学习参考）
MySQL中需创建的表
-- 用户表
CREATE TABLE `t_user` (
 `id` INT NOT NULL AUTO_INCREMENT COMMENT '用户唯一ID',
  `username` VARCHAR(50) NOT NULL COMMENT '登录用户名',
  `password` VARCHAR(100) NOT NULL COMMENT '加密后的登录密码',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '账号创建时间', 
 
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`)  -- 确保用户名唯一
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='系统用户表（员工登录账号）';-- 员工表（关联用户表）
CREATE TABLE `t_emp` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '员工唯一ID',
  `name` VARCHAR(50) NOT NULL COMMENT '员工姓名',
  `gender` CHAR(2) NOT NULL COMMENT '员工性别（男/女/未知）',
  `age` INT(3) NOT NULL COMMENT '员工年龄',
  `user_id` INT NOT NULL COMMENT '关联系统用户ID',
  `hire_date` DATE NOT NULL COMMENT '入职日期',
  PRIMARY KEY (`id`),
  -- 外键约束：员工的user_id必须在t_user表中存在，且用户删除时联动处理
  FOREIGN KEY (`user_id`) REFERENCES `t_user` (`id`) ON DELETE CASCADE,
  -- 检查约束：性别和年龄的合法范围
  CHECK (`gender` IN ('男', '女', '未知')),
  CHECK (`age` BETWEEN 18 AND 60)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='员工信息表';
