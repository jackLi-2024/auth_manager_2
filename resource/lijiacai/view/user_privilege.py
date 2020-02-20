#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json
import graphene
from common.view import BaseApi
from resource.lijiacai.utils import utils
from sql import *
from sql.aggregate import *
from sql.functions import *
from sql.conditionals import *


class AddUserPrivilege(BaseApi, utils.MySQLCrud):
    name = "AddUserPrivilege"
    description = "为用户添加权限（基于用户组,支持多个用户绑定）"

    user_privilege = Table("user_privilege")

    class Argument:
        class ArgumentUserPrivilege(graphene.InputObjectType):
            user_id = graphene.String(description="用户id")
            user_no = graphene.String(description="用户编号")
            plat = graphene.String(description="指明平台", required=True)
            user_group_id = graphene.String(description="用户组数据id", required=True)
            user_detail = graphene.String(description="该记录的详细其他信息json传入")

        array = graphene.List(ArgumentUserPrivilege, description="参数列表")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        columns = [self.user_privilege.user_id,
                   self.user_privilege.user_no,
                   self.user_privilege.plat,
                   self.user_privilege.user_group_id,
                   self.user_privilege.user_detail]
        values = []
        for arg in self.arguments.get("array", []):
            values.append([f"'{arg.get('user_id')}'",
                           f"'{arg.get('user_no')}'",
                           f"'{arg.get('plat')}'",
                           f"'{arg.get('user_group_id')}'",
                           f"'{arg.get('user_detail', '{}')}'"])
        sql = self.deal_sql(self.user_privilege.insert(columns=columns, values=values))
        self.execute(sql)
        return {"succ": True}


class DeleteUserPrivilege(BaseApi, utils.MySQLCrud):
    name = "DeleteUserPrivilege"
    description = "为用户移除权限（基于用户组）"

    user_privilege = Table("user_privilege")
    eq_argument = {
        "user_id": user_privilege.user_id,
        "user_no": user_privilege.user_no,
        "plat": user_privilege.plat,
        "user_group_id": user_privilege.user_group_id
    }
    like_argument = {
        "user_detail": user_privilege.user_detail
    }

    class Argument:
        user_id = graphene.String(description="用户id")
        user_no = graphene.String(description="用户编号")
        plat = graphene.String(description="指明平台", required=True)
        user_group_id = graphene.String(description="用户组数据id", required=True)
        user_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sql = self.deal_sql(self.user_privilege.delete(where=self.where))
        self.execute(sql)
        return {"succ": True}


class SearchUserResourcePrivilege(BaseApi, utils.MySQLCrud):
    name = "SearchUserResourcePrivilege"
    description = "用户查资源权限"

    user_resource_privilege_view = Table("user_resource_privilege_view")

    eq_argument = {}
    like_argument = {}

    class Argument:
        user_id = graphene.String(description="用户id")
        user_no = graphene.String(description="用户编号")
        plat = graphene.String(description="指明平台")
        user_group_id = graphene.String(description="用户组数据id")
        user_detail = graphene.String(description="该记录的详细其他信息json传入")
        resource_privilege_id = graphene.String(description="资源权限id")
        resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
        log_id = graphene.Int(description="菜单目录id")
        log_name = graphene.String(description="目录菜单名称,例如“编辑”")
        log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
        parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
        identify = graphene.String(description="功能标识,用户自定义")
        status = graphene.String(description="菜单目录状态0停用-1启用")

    class Return:
        class ReturnUserResourcePrivilege(graphene.ObjectType):
            user_id = graphene.String(description="用户id")
            user_no = graphene.String(description="用户编号")
            plat = graphene.String(description="指明平台")
            user_group_id = graphene.String(description="用户组数据id")
            user_detail = graphene.String(description="该记录的详细其他信息json传入")
            resource_privilege_id = graphene.String(description="资源权限id")
            resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
            log_id = graphene.Int(description="菜单目录id")
            log_name = graphene.String(description="目录菜单名称,例如“编辑”")
            log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
            parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
            identify = graphene.String(description="功能标识,用户自定义")
            status = graphene.String(description="菜单目录状态0停用-1启用")

        rows = graphene.List(ReturnUserResourcePrivilege, description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        for k, v in self.arguments.items():
            self.eq_argument[k] = eval(f"self.user_resource_privilege_view.{v}")
        sql = self.deal_sql(self.user_resource_privilege_view.select(where=self.where))
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}


##用户查资源数据权限
class SearchUserDataPrivilege(BaseApi, utils.MySQLCrud):
    name = "SearchUserDataPrivilege"
    description = "用户查资源数据权限"

    table = Table("user_data_privilege_view")
    eq_argument = {}
    like_argument = {}

    class Argument:
        user_id = graphene.String(description="用户id")
        user_no = graphene.String(description="用户编号")
        plat = graphene.String(description="指明平台")
        user_group_id = graphene.String(description="用户组数据id")
        user_detail = graphene.String(description="该记录的详细其他信息json传入")
        resource_privilege_id = graphene.String(description="资源权限id")
        resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
        data_privilege_id = graphene.String(description="数据权限id")
        data_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
        data_group_id = graphene.String(description="数据组数据id")
        data_group_data = graphene.String(description="数据组具体数据")
        data_group_detail = graphene.String(description="该记录的详细其他信息json传入")
        data_group_name = graphene.String(description="数据组名称")
        data_group_type = graphene.String(description="数据组类型city/organization")
        log_id = graphene.Int(description="菜单目录id")
        log_name = graphene.String(description="目录菜单名称,例如“编辑”")
        log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
        parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
        identify = graphene.String(description="功能标识,用户自定义")
        status = graphene.String(description="菜单目录状态0停用-1启用")

    class Return:
        class ReturnUserDataPrivilege(graphene.ObjectType):
            user_id = graphene.String(description="用户id")
            user_no = graphene.String(description="用户编号")
            plat = graphene.String(description="指明平台")
            user_group_id = graphene.String(description="用户组数据id")
            user_detail = graphene.String(description="该记录的详细其他信息json传入")
            resource_privilege_id = graphene.String(description="资源权限id")
            resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
            data_privilege_id = graphene.String(description="数据权限id")
            data_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
            data_group_id = graphene.String(description="数据组数据id")
            data_group_data = graphene.String(description="数据组具体数据")
            data_group_detail = graphene.String(description="该记录的详细其他信息json传入")
            data_group_name = graphene.String(description="数据组名称")
            data_group_type = graphene.String(description="数据组类型city/organization")
            log_id = graphene.Int(description="菜单目录id")
            log_name = graphene.String(description="目录菜单名称,例如“编辑”")
            log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
            parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
            identify = graphene.String(description="功能标识,用户自定义")
            status = graphene.String(description="菜单目录状态0停用-1启用")

        rows = graphene.List(ReturnUserDataPrivilege, description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        for k, v in self.arguments.items():
            self.eq_argument[k] = eval(f"self.table.{v}")
        sql = self.deal_sql(self.table.select(where=self.where))
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}


##用户组的资源权限
class SearchUserGroupResourcePrivilege(BaseApi, utils.MySQLCrud):
    name = "SearchUserGroupResourcePrivilege"
    description = "用户组的资源权限"

    table = Table("user_group_resource_privilege")
    eq_argument = {}
    like_argument = {}

    class Argument:
        user_group_id = graphene.String(description="用户组数据id")
        user_group_type = graphene.String(description="用户组类型role/organazation")
        user_group_name = graphene.String(description="用户组名称")
        plat = graphene.String(description="指明平台")
        user_group_data = graphene.String(description="用户组具体数据")
        user_group_detail = graphene.String(description="该记录的详细其他信息json传入")
        resource_privilege_id = graphene.String(description="资源权限id")
        resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
        log_id = graphene.Int(description="菜单目录id")
        log_name = graphene.String(description="目录菜单名称,例如“编辑”")
        log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
        parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
        identify = graphene.String(description="功能标识,用户自定义")
        status = graphene.String(description="菜单目录状态0停用-1启用")

    class Return:
        class ReturnUserGroupResourcePrivilege(graphene.ObjectType):
            user_group_id = graphene.String(description="用户组数据id")
            user_group_type = graphene.String(description="用户组类型role/organazation")
            user_group_name = graphene.String(description="用户组名称")
            plat = graphene.String(description="指明平台")
            user_group_data = graphene.String(description="用户组具体数据")
            user_group_detail = graphene.String(description="该记录的详细其他信息json传入")
            resource_privilege_id = graphene.String(description="资源权限id")
            resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
            log_id = graphene.Int(description="菜单目录id")
            log_name = graphene.String(description="目录菜单名称,例如“编辑”")
            log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
            parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
            identify = graphene.String(description="功能标识,用户自定义")
            status = graphene.String(description="菜单目录状态0停用-1启用")

        rows = graphene.List(ReturnUserGroupResourcePrivilege, description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        for k, v in self.arguments.items():
            self.eq_argument[k] = eval(f"self.table.{v}")
        sql = self.deal_sql(self.table.select(where=self.where))
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}


##用户组的资源数据权限
class SearchUserGroupDataPrivilege(BaseApi, utils.MySQLCrud):
    name = "SearchUserGroupDataPrivilege"
    description = "用户组的资源数据权限"

    table = Table("user_group_data_privilege")
    eq_argument = {}
    like_argument = {}

    class Argument:
        user_group_id = graphene.String(description="用户组数据id")
        user_group_type = graphene.String(description="用户组类型role/organazation")
        user_group_name = graphene.String(description="用户组名称")
        plat = graphene.String(description="指明平台")
        user_group_data = graphene.String(description="用户组具体数据")
        user_group_detail = graphene.String(description="该记录的详细其他信息json传入")
        resource_privilege_id = graphene.String(description="资源权限id")
        resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
        data_privilege_id = graphene.String(description="数据权限id")
        data_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
        data_group_id = graphene.String(description="数据组数据id")
        data_group_data = graphene.String(description="数据组具体数据")
        data_group_detail = graphene.String(description="该记录的详细其他信息json传入")
        data_group_name = graphene.String(description="数据组名称")
        data_group_type = graphene.String(description="数据组类型city/organization")
        log_id = graphene.Int(description="菜单目录id")
        log_name = graphene.String(description="目录菜单名称,例如“编辑”")
        log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
        parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
        identify = graphene.String(description="功能标识,用户自定义")
        status = graphene.String(description="菜单目录状态0停用-1启用")

    class Return:
        class ReturnUserGroupDataPrivilege(graphene.ObjectType):
            user_group_id = graphene.String(description="用户组数据id")
            user_group_type = graphene.String(description="用户组类型role/organazation")
            user_group_name = graphene.String(description="用户组名称")
            plat = graphene.String(description="指明平台")
            user_group_data = graphene.String(description="用户组具体数据")
            user_group_detail = graphene.String(description="该记录的详细其他信息json传入")
            resource_privilege_id = graphene.String(description="资源权限id")
            resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
            data_privilege_id = graphene.String(description="数据权限id")
            data_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")
            data_group_id = graphene.String(description="数据组数据id")
            data_group_data = graphene.String(description="数据组具体数据")
            data_group_detail = graphene.String(description="该记录的详细其他信息json传入")
            data_group_name = graphene.String(description="数据组名称")
            data_group_type = graphene.String(description="数据组类型city/organization")
            log_id = graphene.Int(description="菜单目录id")
            log_name = graphene.String(description="目录菜单名称,例如“编辑”")
            log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
            parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
            identify = graphene.String(description="功能标识,用户自定义")
            status = graphene.String(description="菜单目录状态0停用-1启用")

        rows = graphene.List(ReturnUserGroupDataPrivilege, description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        for k, v in self.arguments.items():
            self.eq_argument[k] = eval(f"self.table.{v}")
        sql = self.deal_sql(self.table.select(where=self.where))
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}


##用户验证数据权限
class CheckUserDataPrivilege(BaseApi, utils.MySQLCrud):
    name = "CheckUserDataPrivilege"
    description = "用户验证数据权限"

    table = Table("user_data_privilege")
    eq_argument = {}
    like_argument = {}

    class Argument:
        user_id = graphene.String(description="用户id")
        user_no = graphene.String(description="用户编号")
        plat = graphene.String(description="指明平台", required=True)
        data_group_id = graphene.String(description="数据组数据id", required=True)
        data_group_data = graphene.String(description="数据组具体数据")
        log_id = graphene.Int(description="菜单目录id", required=True)

    class Return:
        exist = graphene.Boolean(description="True: 存在 False:不存在")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        for k, v in self.arguments.items():
            self.eq_argument[k] = eval(f"self.table.{v}")
        sql = self.deal_sql(self.count, self.table.select(where=self.where & (self.table.status == '1')))
        self.execute(sql)
        if self.read_all():
            return {"exist": True}
        else:
            return {"exist": False}


##用户验证资源权限
class CheckUserResourcePrivilege(BaseApi, utils.MySQLCrud):
    name = "CheckUserResourcePrivilege"
    description = "用户验证资源权限"

    eq_argument = {}
    like_argument = {}

    class Argument:
        user_id = graphene.String(description="用户id")
        user_no = graphene.String(description="用户编号")
        plat = graphene.String(description="指明平台", required=True)
        log_id = graphene.Int(description="菜单目录id", required=True)
        log_name = graphene.String(description="目录菜单名称,例如“编辑”")

    class Return:
        exist = graphene.Boolean(description="True: 存在 False:不存在")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        for k, v in self.arguments.items():
            self.eq_argument[k] = eval(f"self.table.{v}")
        sql = self.deal_sql(self.count, self.table.select(where=self.where & (self.table.status == '1')))
        self.execute(sql)
        if self.read_all():
            return {"exist": True}
        else:
            return {"exist": False}
