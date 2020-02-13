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


class AddDataGroupData(BaseApi, utils.MySQLCrud):
    name = "AddDataGroupData"
    description = "添加数据组数据"

    data_group = Table("data_group")

    class Argument:
        data_group_type = graphene.String(description="数据组类型city/organization")
        data_group_name = graphene.String(description="数据组名称")
        data_group_data = graphene.String(description="数据组具体数据")
        plat = graphene.String(description="指明平台")
        data_group_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        args = self.arguments
        data = {}
        for k, v in args.items():
            data[eval(f"self.data_group.{k}")] = v
        columns, values = self.split_columns_values(data=data)
        sql = self.deal_sql(self.data_group.insert(columns=columns, values=[values]))
        self.execute(sql)
        return {"succ": True}


class DeleteDataGroupData(BaseApi, utils.MySQLCrud):
    name = "DeleteDataGroupData"
    description = "删除数据组数据"

    data_group = Table("data_group")
    in_argument = {
        "data_group_id": data_group.data_group_id
    }

    class Argument:
        data_group_id = graphene.List(graphene.Int, description="数据组数据id")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sql = self.deal_sql(self.user_group.delete(where=self.where))
        self.execute(sql)
        return {"succ": True}


class UpdateDataGroupData(BaseApi, utils.MySQLCrud):
    name = "UpdateDataGroupData"
    description = "更新数据组数据"

    data_group = Table("data_group")
    eq_argument = {
        "data_group_id": data_group.data_group_id
    }

    class Argument:
        data_group_id = graphene.Int(description="数据组数据id", required=True)
        data_group_type = graphene.String(description="数据组类型city/organization")
        data_group_name = graphene.String(description="数据组名称")
        data_group_data = graphene.String(description="数据组具体数据")
        plat = graphene.String(description="指明平台")
        data_group_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        data = {}
        for k, v in self.arguments.items():
            if k == "data_group_id":
                continue
            data[eval(f"self.data_group.{k}")] = v
        columns, values = self.split_columns_values(data=data)
        sql = self.deal_sql(self.data_group.update(columns=columns, values=values, where=self.where))
        self.execute(sql)
        return {"succ": True}


class SearchDataGroupData(BaseApi, utils.MySQLCrud):
    name = "SearchDataGroupData"
    description = "查询数据组数据"

    data_group = Table("data_group")
    eq_argument = {
        "data_group_id": data_group.data_group_id,
        "data_group_type": data_group.data_group_type,
        "data_group_name": data_group.data_group_name,
        "data_group_data": data_group.data_group_data,
        "data_group_detail": data_group.data_group_detail,
        "plat": data_group.plat
    }

    class Argument:
        data_group_id = graphene.Int(description="数据组数据id")
        data_group_type = graphene.String(description="数据组类型city/organization")
        data_group_name = graphene.String(description="数据组名称")
        data_group_data = graphene.String(description="数据组具体数据")
        plat = graphene.String(description="指明平台")
        data_group_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        class ReturnDataGroupData(graphene.ObjectType):
            data_group_id = graphene.Int(description="数据组数据id")
            data_group_type = graphene.String(description="数据组类型city/organization")
            data_group_name = graphene.String(description="数据组名称")
            data_group_data = graphene.String(description="数据组具体数据")
            plat = graphene.String(description="指明平台")
            data_group_detail = graphene.String(description="该记录的详细其他信息json传入")

        rows = graphene.List(ReturnDataGroupData, description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        self.reset_page_size()
        sql = self.deal_sql(self.data_group.select(where=self.where))
        print(sql)
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}
