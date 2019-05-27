import geoip2.database

reader = geoip2.database.Reader('D:/Swiper1/address_/GeoLite2-City.mmdb')


def ip_print_AddrInfo(ip):

    # 载入指定IP相关数据
    response = reader.city(ip)
    # 读取国家代码
    Country_IsoCode = response.country.iso_code
    # 读取国家名称
    Country_Name = response.country.name
    # 读取国家名称(中文显示)
    Country_NameCN = response.country.names['zh-CN']
    # 读取州(国外)/省(国内)名称
    Country_SpecificName = response.subdivisions.most_specific.name
    # 读取州(国外)/省(国内)代码
    Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
    # 读取城市名称
    City_Name = response.city.name
    # 读取邮政编码
    City_PostalCode = response.postal.code
    # 获取纬度
    Location_Latitude = response.location.latitude
    # 获取经度
    Location_Longitude = response.location.longitude

    data={
        'Country_Name':Country_Name,
        'Country_SpecificName':Country_SpecificName,
        'City_Name':City_Name
    }
    return data


