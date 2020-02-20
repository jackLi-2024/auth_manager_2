CREATE TABLE
IF
	NOT EXISTS `log` (
		`log_id` INT ( 11 ) AUTO_INCREMENT COMMENT '菜单目录id',
		`log_type` VARCHAR ( 25 ) COMMENT '菜单目录类型枚举值MENU/FUNCTION',
		`log_name` VARCHAR ( 50 ) COMMENT '目录菜单名称,例如“编辑”',
		`identify` VARCHAR ( 50 ) COMMENT '功能标识,用户自定义',
		`status` INT (1) DEFAULT 1 COMMENT '菜单目录状态0停用-1启用',
		`plat` VARCHAR ( 255 ) NOT NULL COMMENT '指明平台,',
		`parent_log_id` INT ( 11 ) NOT NULL DEFAULT 0 COMMENT '父级目录id,默认初级父级id为0',
		`log_detail` json COMMENT '该记录的详细其他信息json传入',
		PRIMARY KEY ( `log_id` )
	) COMMENT = '菜单目录表' ENGINE = INNODB DEFAULT CHARSET = utf8;
CREATE TABLE
IF
	NOT EXISTS `user_group` (
		`user_group_id` VARCHAR ( 50 )  NOT NULL COMMENT '用户组数据id',
		`user_group_type` VARCHAR ( 50 ) COMMENT '用户组类型role/organazation',
		`user_group_name` VARCHAR ( 50 ) COMMENT '用户组名称',
		`plat` VARCHAR ( 50 ) COMMENT '指明平台',
		`user_group_data` VARCHAR ( 50 ) COMMENT '用户组具体数据',
		`user_group_detail` json COMMENT '该记录的详细其他信息json传入',
		PRIMARY KEY ( `user_group_id` )
	) COMMENT = '用户组数据' ENGINE = INNODB DEFAULT CHARSET = utf8;
CREATE TABLE
IF
	NOT EXISTS `resource_privilege` (
		`resource_privilege_id` VARCHAR ( 50 ) NOT NULL COMMENT '资源权限id',
		`log_id` INT ( 11 )  NOT NULL COMMENT '目录功能id',
		`user_group_id` VARCHAR ( 50 )  NOT NULL COMMENT '用户组id',
		`resource_privilege_detail` json COMMENT '该记录的详细其他信息json传入',
		PRIMARY KEY ( `resource_privilege_id` ),
		FOREIGN KEY (`log_id`) REFERENCES log(`log_id`) ON DELETE CASCADE ON UPDATE CASCADE,
		FOREIGN KEY (`user_group_id`) REFERENCES user_group(`user_group_id`) ON DELETE CASCADE ON UPDATE CASCADE
	) COMMENT = '资源权限' ENGINE = INNODB DEFAULT CHARSET = utf8;
CREATE TABLE
IF
	NOT EXISTS `data_group` (
		`data_group_id` VARCHAR ( 50 )  NOT NULL COMMENT '数据组数据id',
		`data_group_type` VARCHAR ( 50 ) COMMENT '数据组类型city/organization',
		`data_group_name` VARCHAR ( 50 ) COMMENT '数据组名称',
		`data_group_data` VARCHAR ( 50 ) COMMENT '数据组具体数据',
		`plat` VARCHAR ( 50 ) COMMENT '指明平台',
		`data_group_detail` json COMMENT '该记录的详细其他信息json传入',
		PRIMARY KEY ( `data_group_id` )
	) COMMENT = '数据组数据' ENGINE = INNODB DEFAULT CHARSET = utf8;
CREATE TABLE
IF
	NOT EXISTS `data_privilege` (
		`data_privilege_id` VARCHAR ( 50 ) NOT NULL  COMMENT '数据权限id',
		`resource_privilege_id` VARCHAR ( 50 )  NOT NULL COMMENT '资源权限id',
		`data_group_id` VARCHAR ( 50 )  NOT NULL COMMENT '数据组数据id',
		`data_privilege_detail` json COMMENT '该记录的详细其他信息json传入',
		PRIMARY KEY ( `data_privilege_id` ),
		FOREIGN KEY (`resource_privilege_id`) REFERENCES resource_privilege(`resource_privilege_id`) ON DELETE CASCADE ON UPDATE CASCADE,
		FOREIGN KEY (`data_group_id`) REFERENCES data_group(`data_group_id`) ON DELETE CASCADE ON UPDATE CASCADE
	) COMMENT = '数据权限' ENGINE = INNODB DEFAULT CHARSET = utf8;
CREATE TABLE
IF
	NOT EXISTS `user_privilege` (
		`user_id` VARCHAR ( 50 ) COMMENT '用户id',
		`user_no` VARCHAR ( 50 ) COMMENT '用户编号',
		`plat` VARCHAR ( 50 ) COMMENT '指明平台',
		`user_group_id` VARCHAR ( 50 )  NOT NULL COMMENT '用户组数据id',
	    `user_detail` json COMMENT '该记录的详细其他信息json传入',
	    FOREIGN KEY (`user_group_id`) REFERENCES user_group(`user_group_id`) ON DELETE CASCADE ON UPDATE CASCADE
	) COMMENT = '用户' ENGINE = INNODB DEFAULT CHARSET = utf8;