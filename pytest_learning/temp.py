dimensionCode = [
    {"code": "account_id"},
    {"code": "adgroup_id"},
    {"code": "adgroup_name"},
    {"code": "ad_id"},
    {"code": "ad_name"},
    {"code": "ad_type"},
    {"code": "age"},
    {"code": "audience_interests"},
    {"code": "audience_type"}
]

codelist = []  # 存放结果列表
try:
    if dimensionCode:
        for code in dimensionCode:
            if isinstance(code, dict):
                codelist.append(code.get("code"))
    else:
        codelist.append("dmn_cluster_id")
except Exception as err:
    import logging
    logging.info(f"获取失败{err}")
    codelist.append('dmn_cluster_id')

## 打印变量内存（memory）地址
print(f"dimensionCode 变量内存地址：{id(dimensionCode)}")
print(f"codelist 变量内存地址：{id(code)}")