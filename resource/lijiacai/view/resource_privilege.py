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


class AddResourcePrivilege(BaseApi, utils.MySQLCrud):
    name = "AddResourcePrivilege"
    description = "资源与用户组权限绑定(支持批量)"

    resource_privilege = Table("resource_privilege")

    class Argument:
        class ArgumentResourcePrivilege(graphene.InputObjectType):
            resource_privilege_id = graphene.String(description="资源权限id", required=True)
            log_id = graphene.Int(description="目录功能id", required=True)
            user_group_id = graphene.String(description="用户组id", required=True)
            resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")

        array = graphene.List(ArgumentResourcePrivilege, description="参数列表")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        columns = [self.resource_privilege.log_id, self.resource_privilege.user_group_id,
                   self.resource_privilege.resource_privilege_detail]
        values = []
        for arg in self.arguments.get("array", []):
            values.append([arg.get("log_id"),
                           arg.get("user_group_id"),
                           f"'{arg.get('resource_privilege_detail', '{}')}'"])
        sql = self.deal_sql(self.resource_privilege.insert(columns=columns, values=values))
        self.execute(sql)
        return {"succ": True}


class DeleteResourcePrivilege(BaseApi, utils.MySQLCrud):
    name = "DeleteResourcePrivilege"
    description = "资源与用户组解绑"

    resource_privilege = Table("resource_privilege")
    eq_argument = {
        "resource_privilege_id": resource_privilege.resource_privilege_id,
        "log_id": resource_privilege.log_id,
        "user_group_id": resource_privilege.user_group_id
    }
    like_argument = {
        "resource_privilege_detail": resource_privilege.resource_privilege_detail
    }

    class Argument:
        resource_privilege_id = graphene.String(description="资源权限id")
        log_id = graphene.Int(description="目录功能id")
        user_group_id = graphene.String(description="用户组id", required=True)
        resource_privilege_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sql = self.deal_sql(self.user_group.delete(where=self.where))
        self.execute(sql)
        return {"succ": True}
