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


class AddUserGroupData(BaseApi, utils.MySQLCrud):
    name = "AddUserGroupData"
    description = "添加用户组数据(done)"

    user_group = Table("user_group")

    class Argument:
        user_group_id = graphene.String(description="用户组数据id", required=True)
        user_group_type = graphene.String(description="用户组类型role/organazation", required=True)
        user_group_name = graphene.String(description="用户组名称", required=True)
        plat = graphene.String(description="指明平台", required=True)
        user_group_data = graphene.String(description="用户组具体数据", required=True)
        user_group_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        args = self.arguments
        data = {}
        for k, v in args.items():
            data[eval(f"self.user_group.{k}")] = v
        columns, values = self.convert_insert_data(data=data)
        sql = self.deal_sql(self.user_group.insert(columns=columns, values=[values]))
        self.execute(sql)
        return {"succ": True}

    def convert_insert_data(self, data: dict):
        cs = []
        vs = []
        for k, v in data.items():
            cs.append(k)
            vs.append(f"'{v}'")

        return cs, vs


class DeleteUserGroupData(BaseApi, utils.MySQLCrud):
    name = "DeleteUserGroupData"
    description = "删除用户组数据(done)"

    user_group = Table("user_group")
    in_argument = {
        "user_group_id": user_group.user_group_id
    }

    class Argument:
        user_group_id = graphene.List(graphene.String, description="用户组数据id", required=True)

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sql = self.deal_sql(self.user_group.delete(where=self.where))
        self.execute(sql)
        return {"succ": True}


class UpdateUserGroupData(BaseApi, utils.MySQLCrud):
    name = "UpdateUserGroupData"
    description = "更新用户组数据(done)"

    user_group = Table("user_group")

    eq_argument = {
        "user_group_id": user_group.user_group_id
    }

    class Argument:
        user_group_id = graphene.String(description="用户组数据id", required=True)
        user_group_type = graphene.String(description="用户组类型role/organazation", required=True)
        user_group_name = graphene.String(description="用户组名称", required=True)
        plat = graphene.String(description="指明平台", required=True)
        user_group_data = graphene.String(description="用户组具体数据", required=True)
        user_group_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        data = {}
        for k, v in self.arguments.items():
            if k == "user_group_id":
                continue
            data[eval(f"self.user_group.{k}")] = v
        columns, values = self.convert_insert_data(data=data)
        sql = self.deal_sql(self.user_group.update(columns=columns, values=values, where=self.where))
        self.execute(sql)
        return {"succ": True}

    def convert_insert_data(self, data: dict):
        cs = []
        vs = []
        for k, v in data.items():
            cs.append(k)
            vs.append(f"'{v}'")

        return cs, vs


class SearchUserGroupData(BaseApi, utils.MySQLCrud):
    name = "SearchUserGroupData"
    description = "查询用户组数据(done)"

    user_group = Table("user_group")
    eq_argument = {
        "user_group_id": user_group.user_group_id,
        "user_group_type": user_group.user_group_type,
        "user_group_name": user_group.user_group_name,
        "plat": user_group.plat,
        "user_group_data": user_group.user_group_data,
        "user_group_detail": user_group.user_group_detail,
    }

    class Argument:
        user_group_id = graphene.String(description="用户组数据id")
        user_group_type = graphene.String(description="用户组类型role/organazation")
        user_group_name = graphene.String(description="用户组名称")
        plat = graphene.String(description="指明平台")
        user_group_data = graphene.String(description="用户组具体数据")
        user_group_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        class ReturnUserGroupData(graphene.ObjectType):
            user_group_id = graphene.String(description="用户组数据id")
            user_group_type = graphene.String(description="用户组类型role/organazation")
            user_group_name = graphene.String(description="用户组名称")
            plat = graphene.String(description="指明平台")
            user_group_data = graphene.String(description="用户组具体数据")
            user_group_detail = graphene.String(description="该记录的详细其他信息json传入")

        rows = graphene.List(ReturnUserGroupData, description="返回列表")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        self.reset_page_size()
        sql = self.deal_sql(self.user_group.select(where=self.where))
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}


class SearchUserGroup(BaseApi, utils.MySQLCrud):
    name = "SearchUserGroup"
    description = "查询用户组(done)"

    user_group_view = Table("user_group_view")

    eq_argument = {
        "user_group_type": user_group_view.user_group_type,
        "user_group_name": user_group_view.user_group_name,
        "plat": user_group_view.plat
    }

    class Argument:
        user_group_type = graphene.String(description="用户组类型role/organazation")
        user_group_name = graphene.String(description="用户组名称")
        plat = graphene.String(description="指明平台")

    class Return:
        class ReturnUserGroup(graphene.ObjectType):
            user_group_type = graphene.String(description="用户组类型role/organazation")
            user_group_name = graphene.String(description="用户组名称")
            plat = graphene.String(description="指明平台")

        rows = graphene.List(ReturnUserGroup, description="返回列表")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        self.reset_page_size()
        sql = self.deal_sql(self.user_group_view.select(where=self.where))
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}
