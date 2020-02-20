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


class AddMenu(BaseApi, utils.MySQLCrud):
    name = "AddMenu"
    description = "添加菜单目录(done)"

    log = Table("log")

    class Argument:
        log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION",required=True)
        log_name = graphene.String(description="目录菜单名称,例如“编辑”",required=True)
        identify = graphene.String(description="功能标识,用户自定义")
        status = graphene.Int(description="菜单目录状态0停用-1启用",required=True)
        plat = graphene.String(description="指明平台",required=True)
        parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
        log_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        where = (self.log.log_id == self.arguments.get("parent_log_id")) & (self.log.log_type == "'MENU'")
        sql1 = self.deal_sql(self.log.select(where=where))

        self.execute(sql1)

        if self.arguments.get("parent_log_id") == 0:
            pass
        elif not self.read_all():
            raise Exception("不能创建子级菜单")
        else:
            pass
        args = {self.log.log_type: self.arguments.get("log_type"),
                self.log.log_name: self.arguments.get("log_name"),
                self.log.identify: self.arguments.get("identify"),
                self.log.status: self.arguments.get("status"),
                self.log.plat: self.arguments.get("plat", 1),
                self.log.parent_log_id: self.arguments.get("parent_log_id"),
                self.log.log_detail: self.arguments.get("log_detail", {})}
        columns, values = self.convert_insert_data(data=args)
        sql2 = self.deal_sql(self.log.insert(columns=columns, values=[values]))
        self.execute(sql2)
        return {"succ": True}

    def convert_insert_data(self, data: dict):
        cs = []
        vs = []
        for k, v in data.items():
            cs.append(k)
            vs.append(f"'{v}'")

        return cs, vs


class DeleteMenu(BaseApi, utils.MySQLCrud):
    name = "DeleteMenu"
    description = "删除菜单目录(done)"

    log = Table("log")

    class Argument:
        log_id = graphene.Int(description="菜单目录id", required=True)

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sql = self.deal_sql(self.log.delete())
        sql += f" WHERE FIND_IN_SET(log_id,queryChildren({self.arguments.get('log_id')}))"
        self.execute(sql)
        return {"succ": True}


class UpdateMenu(BaseApi, utils.MySQLCrud):
    name = "UpdateMenu"
    description = "更新菜单目录(暂时不支持)"

    class Argument:
        pass

    class Return:
        succ = graphene.Boolean(description="True: 操作成功 False:操作失败")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        pass


class SearchMenu(BaseApi, utils.MySQLCrud):
    name = "SearchMenu"
    description = "查询菜单目录(done)"

    log = Table("log")
    eq_argument = {
        'log_id': log.log_id,
        "log_type": log.log_type,
        "log_name": log.log_name,
        "identify": log.identify,
        "status": log.status,
        "plat": log.plat,
        "parent_log_id": log.parent_log_id,
        "log_detail": log.log_detail
    }

    class Argument:
        log_id = graphene.Int(description="菜单目录id")
        log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
        log_name = graphene.String(description="目录菜单名称,例如“编辑”")
        identify = graphene.String(description="功能标识,用户自定义")
        status = graphene.Int(description="菜单目录状态0停用-1启用")
        plat = graphene.String(description="指明平台")
        parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
        log_detail = graphene.String(description="该记录的详细其他信息json传入")

    class Return:
        class ReturnLog(graphene.ObjectType):
            log_id = graphene.Int(description="菜单目录id")
            log_type = graphene.String(description="菜单目录类型枚举值MENU/FUNCTION")
            log_name = graphene.String(description="目录菜单名称,例如“编辑”")
            identify = graphene.String(description="功能标识,用户自定义")
            status = graphene.Int(description="菜单目录状态0停用-1启用")
            plat = graphene.String(description="指明平台,")
            parent_log_id = graphene.Int(description="父级目录id,默认初级父级id为0")
            log_detail = graphene.String(description="该记录的详细其他信息json传入")

        rows = graphene.List(ReturnLog, description="返回列表")

    def deal(self, token, **kwargs):
        return self.run()

    def dealer(self):
        sele = self.log.select(where=self.where)
        sql = self.deal_sql(sele)
        self.execute(sql)
        rows = self.read_all()
        return {"rows": rows}
