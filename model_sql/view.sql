DROP VIEW IF EXISTS  user_group_view;
CREATE VIEW user_group_view AS SELECT
user_group_name,
plat,
user_group_type
FROM
	user_group
GROUP BY
	user_group_name,
	plat,
	user_group_type;


DROP VIEW IF EXISTS  user_resource_privilege_view;
CREATE VIEW user_resource_privilege_view AS SELECT
user_privilege.*,
resource_privilege.resource_privilege_id,
resource_privilege.resource_privilege_detail,
log.log_id,
log.log_name,
log.log_type,
log.parent_log_id,
log.identify,
log.`status`
FROM
	user_privilege,
	resource_privilege,
	log
WHERE
	user_privilege.user_group_id = resource_privilege.user_group_id
	AND resource_privilege.log_id = log.log_id
	AND log.log_type = 'FUNCTION'
	AND log.plat = user_privilege.plat;



DROP VIEW IF EXISTS  user_data_privilege_view;
CREATE VIEW user_data_privilege_view AS SELECT
user_privilege.*,
resource_privilege.resource_privilege_id,
resource_privilege.resource_privilege_detail,
data_privilege.data_privilege_id,
data_privilege.data_privilege_detail,
data_group.data_group_id,
data_group.data_group_data,
data_group.data_group_detail,
data_group.data_group_name,
data_group.data_group_type,
log.log_id,
log.log_name,
log.log_type,
log.parent_log_id,
log.identify,
log.`status`
FROM
	user_privilege,
	resource_privilege,
	log,
	data_privilege,
	data_group
WHERE
	user_privilege.user_group_id = resource_privilege.user_group_id
	AND resource_privilege.log_id = log.log_id
	AND log.plat = user_privilege.plat
	AND log.log_type = 'FUNCTION'
	AND data_privilege.resource_privilege_id = resource_privilege.resource_privilege_id
	AND data_group.data_group_id = data_privilege.data_group_id
	AND data_group.plat = user_privilege.plat;


DROP VIEW IF EXISTS  user_group_data_privilege_view;
CREATE VIEW user_group_data_privilege_view AS SELECT
user_group.*,
resource_privilege.resource_privilege_id,
resource_privilege.resource_privilege_detail,
data_privilege.data_privilege_id,
data_privilege.data_privilege_detail,
data_group.data_group_id,
data_group.data_group_data,
data_group.data_group_detail,
data_group.data_group_name,
data_group.data_group_type,
log.log_id,
log.log_name,
log.log_type,
log.parent_log_id,
log.identify,
log.`status`
FROM
	user_group,
	resource_privilege,
	log,
	data_privilege,
	data_group
WHERE
	user_group.user_group_id = resource_privilege.user_group_id
	AND resource_privilege.log_id = log.log_id
	AND log.plat = user_group.plat
	AND log.log_type = 'FUNCTION'
	AND data_privilege.resource_privilege_id = resource_privilege.resource_privilege_id
	AND data_group.data_group_id = data_privilege.data_group_id
	AND data_group.plat = user_group.plat;



DROP VIEW IF EXISTS  user_group_resource_privilege_view;
CREATE VIEW user_group_resource_privilege_view AS SELECT
user_group.*,
resource_privilege.resource_privilege_id,
resource_privilege.resource_privilege_detail,
log.log_id,
log.log_name,
log.log_type,
log.parent_log_id,
log.identify,
log.`status`
FROM
	user_group,
	resource_privilege,
	log
WHERE
	user_group.user_group_id = resource_privilege.user_group_id
	AND resource_privilege.log_id = log.log_id
	AND log.log_type = 'FUNCTION'
	AND log.plat = user_group.plat;