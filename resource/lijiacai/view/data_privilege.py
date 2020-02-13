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


class AddDataPrivilege(BaseApi, utils.MySQLCrud):
    name = "AddDataPrivilege"
    description = "资源权限与数据组绑定(支持批量)"

    data_privilege = Table("data_privilege")

    class Argument:
        class ArgumentDataPrivilege(graphene.InputObjectType):
            resource_privilege_id = graphene.Int(description="资源权限id", required=True)
            data_group_id = graphene.Int(description="数据组数据id", required=True)
            data_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")

        array = graphene.List(ArgumentDataPrivilege, description="参数列表")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        columns = [self.data_privilege.resource_privilege_id,
                   self.data_privilege.data_group_id,
                   self.data_privilege.data_privilege_detail]
        values = []
        for arg in self.arguments.get("array", []):
            values.append([f"'{arg.get('resource_privilege_id')}'",
                           f"'{arg.get('data_group_id')}'",
                           f"'{arg.get('data_privilege_detail', '{}')}'"])
        sql = self.deal_sql(self.data_privilege.insert(columns=columns, values=values))
        self.execute(sql)
        return {"succ": True}


class DeleteDataPrivilege(BaseApi, utils.MySQLCrud):
    name = "DeleteDataPrivilege"
    description = "资源权限与数据组解绑"

    data_privilege = Table("data_privilege")
    eq_argument = {
        "resource_privilege_id": data_privilege.resource_privilege_id,
        "data_privilege_id": data_privilege.data_privilege_id,
        "data_group_id": data_privilege.data_group_id
    }
    like_argument = {
        "data_privilege_detail": data_privilege.data_privilege_detail
    }

    class Argument:
        data_privilege_id = graphene.Int(description="数据权限id")
        resource_privilege_id = graphene.Int(description="资源权限id")
        data_group_id = graphene.Int(description="数据组数据id")
        data_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sql = self.deal_sql(self.data_privilege.delete(where=self.where))
        self.execute(sql)
        return {"succ": True}
