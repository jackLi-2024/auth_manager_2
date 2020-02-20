--查询某用户功能树数据权限
SELECT
  *
FROM
  `user`,
  user_group,
  resource_privilege,
  data_privilege,
  data_group,
  log
WHERE
  `user`.user_group_id = user_group.user_group_id
  AND resource_privilege.user_group_id = user_group.user_group_id
  AND resource_privilege.log_id = log.log_id
  AND log.log_type = 'FUNCTION'
  AND data_privilege.resource_privilege_id = resource_privilege.resource_privilege_id
  AND data_privilege.data_group_id = data_group.data_group_id
  AND `user`.user_id = '1'

--查询菜单目录状态树
--查询数据组
--查询数据组数据
--查询用户组
--查询用户组数据
--查询用户各个功能状态
--查询用户特定功能状态
--新增菜单目录
--新增用户组数据
--新增数据组数据
--资源权限与用户组数据互绑
--资源权限与数据组数据互绑
--修改菜单目录
--修改用户组数据
--修改数据组数据
--修改绑定关系
--删除菜单目录
--删除用户组数据
--删除数据组数据
--删除绑定关系



