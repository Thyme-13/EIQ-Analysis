def data_screening(csv_list, names, sale_volumes):
    """
    对数据进行筛选并计算总销量
    :param names: 商品名所在列的索引
    :param sale_volumes: 商品销量所在列的索引
    :param csv_list: 需统计的二维列表
    :return: 由整理后的二维列表及总销量构成的元组
    """
    _names = ord(names)-65
    _sale_volumes = ord(sale_volumes)-65
    new_list = []
    total = 0
    l = len(csv_list)
    for i in range(1, l):
        val = csv_list[i]
        ls = [val[_names], val[_sale_volumes]]
        new_list.append(ls)
        total += float(val[_sale_volumes])
    return new_list, total


def sales_volumes(data_list):
    """
    统计将各商品的总销量并排序
    :param data_list: 由商品名和单笔销量构成的二维列表
    :return: 由商品名和销量构成的字典
    """
    sale_volumes = {}
    for i in data_list:
        if i[0] not in sale_volumes:
            sale_volumes[i[0]] = float(i[1])
        else:
            sale_volumes[i[0]] += float(i[1])
            if sale_volumes[i[0]] == 0:
                sale_volumes.pop(i[0])
    list_tuple = sorted(sale_volumes.items(), reverse=True, key=lambda x: x[1])
    sale_volumes = {}
    for i in list_tuple:
        sale_volumes[i[0]] = i[1]
    return sale_volumes


def proportion_calculation(sale_volumes, total, boundarys):
    if boundarys[1] == 1:
        a = boundarys[0][0]
        boundary1 = total * a / 100
        lists = [[], []]
        flag = 0
        for keys in sale_volumes:
            dicts = {keys: sale_volumes[keys]}
            if flag == 0:
                if sale_volumes[keys] <= boundary1:
                    lists[0].append(dicts)
                    boundary1 -= sale_volumes[keys]
                else:
                    flag = 1
                    lists[0].append(dicts)
            else:
                lists[1].append(dicts)
        sum_a = len(lists[0])
        sum_b = len(lists[1])
        sums = [sum_a, sum_b]
        return lists, sums
    elif boundarys[1] == 2:
        a, b = boundarys[0][0], boundarys[0][1]
        boundary1 = total * a / 100
        boundary2 = total * b / 100
        lists = [[], [], []]
        flag = 0
        for keys in sale_volumes:
            dicts = {keys: sale_volumes[keys]}
            if flag == 0:
                if sale_volumes[keys] <= boundary1:
                    lists[0].append(dicts)
                    boundary1 -= sale_volumes[keys]
                else:
                    flag = 1
                    boundary2 += boundary1
                    lists[0].append(dicts)
                    boundary2 -= sale_volumes[keys]
            elif flag == 1:
                if sale_volumes[keys] <= boundary2:
                    lists[1].append(dicts)
                    boundary2 -= sale_volumes[keys]
                else:
                    flag = 2
                    lists[1].append(dicts)
            else:
                lists[2].append(dicts)
        sum_a = len(lists[0])
        sum_b = len(lists[1])
        sum_c = len(lists[2])
        sums = [sum_a, sum_b, sum_c]
        return lists, sums
    else:
        a, b, c = boundarys[0][0], boundarys[0][1], boundarys[0][2]
        boundary1 = total * a / 100
        boundary2 = total * b / 100
        boundary3 = total * c / 100
        lists = [[], [], [], []]
        flag = 0
        for keys in sale_volumes:
            dicts = {keys: sale_volumes[keys]}
            if flag == 0:
                if sale_volumes[keys] <= boundary1:
                    lists[0].append(dicts)
                    boundary1 -= sale_volumes[keys]
                else:
                    flag = 1
                    boundary2 += boundary1
                    lists[0].append(dicts)
                    boundary2 -= sale_volumes[keys]
            elif flag == 1:
                if sale_volumes[keys] <= boundary2:
                    lists[1].append(dicts)
                    boundary2 -= sale_volumes[keys]
                else:
                    flag = 2
                    boundary3 += boundary2
                    lists[1].append(dicts)
                    boundary3 -= sale_volumes[keys]
            elif flag == 2:
                if sale_volumes[keys] <= boundary3:
                    lists[2].append(dicts)
                    boundary3 -= sale_volumes[keys]
                else:
                    flag = 3
                    lists[2].append(dicts)
            else:
                lists[3].append(dicts)
        sum_a = len(lists[0])
        sum_b = len(lists[1])
        sum_c = len(lists[2])
        sum_d = len(lists[3])
        sums = [sum_a, sum_b, sum_c, sum_d]
        return lists, sums

