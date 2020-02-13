INSERT INTO log ( `log_type`, `log_name`, `plat`, `parent_log_id` )
VALUES
	( 'MENU', '平台设置', 'test', 0 ),
	( 'MENU', '系统设置', 'test', 1 ),
	( 'MENU', '用户设置', 'test', 1 ),
	( 'FUNCTION', '新增', 'test', 2 ),
	( 'FUNCTION', '查看', 'test', 3 );
INSERT INTO user_group ( `user_group_type`, `user_group_name`, `user_group_data`, `plat` )
VALUES
	( 'city', '城市权限', '重庆', 'test' ),
	( 'city', '城市权限', '成都', 'test' ),
	( 'city', '城市权限', '北京', 'test' ),
	( 'city', '城市权限', '上海', 'test' ),
	( 'role', '角色权限', '管理员', 'test' ),
	( 'role', '角色权限', '超级管理员', 'test' ),
	( 'role', '角色权限', '普通员工', 'test' );
INSERT INTO resource_privilege ( `log_id`, `user_group_id` )
VALUES
	( '4', '5' ),
	( '5', '5' );
INSERT INTO data_group ( `data_group_type`, `data_group_name`, `data_group_data`, `plat` )
VALUES
	( 'city', '城市权限', '重庆', 'test' ),
	( 'city', '城市权限', '成都', 'test' ),
	( 'city', '城市权限', '北京', 'test' ),
	( 'city', '城市权限', '上海', 'test' );
INSERT INTO data_privilege ( `resource_privilege_id`, `data_group_id` )
VALUES
	( '1', '5' ),
	( '2', '3' );
INSERT INTO `user_privilege` ( `user_id`, `user_group_id` )
VALUES
	( '1', '5' ),
	( '1', '4' );