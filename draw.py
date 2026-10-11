from controller import resolution


def l_d2list(list_dict, boundary_quantity):
    if boundary_quantity == 1:
        list_a = []
        list_b = []
        for i in list_dict[0]:
            for key in i:
                list_a.append([key, i[key]])
        for i in list_dict[1]:
            for key in i:
                list_b.append([key, i[key]])
        return list_a, list_b
    elif boundary_quantity == 2:
        list_a = []
        list_b = []
        list_c = []
        for i in list_dict[0]:
            for key in i:
                list_a.append([key, i[key]])
        for i in list_dict[1]:
            for key in i:
                list_b.append([key, i[key]])
        for i in list_dict[2]:
            for key in i:
                list_c.append([key, i[key]])
        return list_a, list_b, list_c
    else:
        return [], [], []


def l_d2sum(list_dict, boundary_quantity, kinds):
    lists = []
    if boundary_quantity == 1:
        sa = 0
        sb = 0
        for i in list_dict[0]:
            for key in i:
                sa += i[key]
        lists.append(['A类(共' + str(kinds[0]) + '种)', sa])
        for i in list_dict[1]:
            for key in i:
                sb += i[key]
        lists.append(['B类(共' + str(kinds[1]) + '种)', sb])
    elif boundary_quantity == 2:
        sa = 0
        sb = 0
        sc = 0
        for i in list_dict[0]:
            for key in i:
                sa += i[key]
        lists.append(['A类(共' + str(kinds[0]) + '种)', sa])
        for i in list_dict[1]:
            for key in i:
                sb += i[key]
        lists.append(['B类(共' + str(kinds[1]) + '种)', sb])
        for i in list_dict[2]:
            for key in i:
                sc += i[key]
        lists.append(['C类(共' + str(kinds[2]) + '种)', sc])
    else:
        pass
    return lists


value = resolution()[2] / 2073600
font_size1 = 10 * (1 + value / 4)
font_size = font_size1 * 0.8
distance = 0.8 * (1 + value / 180)
distance2 = distance * 0.95
l_distance = 1.1 * (1 + value / 400)
l_distance2 = l_distance * 0.95
radius = 1.2 / (1 + value / 800)
radius2 = radius * 0.8


def draw_pie(tuple_lists, boundary_quantity):
    import matplotlib.pyplot as plt

    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.size'] = font_size
    plt.rcParams['axes.unicode_minus'] = False

    if boundary_quantity == 1:
        title_a = []
        value_a = []
        title_b = []
        value_b = []
        for i in tuple_lists[0]:
            title_a.append(i[0])
            value_a.append(i[1])
        for i in tuple_lists[1]:
            title_b.append(i[0])
            value_b.append(i[1])
        plt.subplot(121)
        plt.title('A类销量占比')
        plt.pie(
            value_a, labels=title_a,
            labeldistance=l_distance2,
            shadow=True,
            radius=radius,
            autopct='%3.3f%%',
            pctdistance=distance2,
            wedgeprops=dict(width=0.7)
        )

        plt.subplot(122)
        plt.title('B类销量占比')
        plt.pie(
            value_b, labels=title_b,
            labeldistance=l_distance2,
            shadow=True,
            radius=radius,
            autopct='%3.3f%%',
            pctdistance=distance2,
            wedgeprops=dict(width=0.7)
        )
        plt.show()
    elif boundary_quantity == 2:
        title_a = []
        value_a = []
        title_b = []
        value_b = []
        title_c = []
        value_c = []
        for i in tuple_lists[0]:
            title_a.append(i[0])
            value_a.append(i[1])
        for i in tuple_lists[1]:
            title_b.append(i[0])
            value_b.append(i[1])
        for i in tuple_lists[2]:
            title_c.append(i[0])
            value_c.append(i[1])
        plt.subplot(232)
        plt.title('A类销量占比')
        plt.pie(
            value_a, labels=title_a,
            labeldistance=l_distance2,
            shadow=True,
            radius=radius,
            autopct='%3.3f%%',
            pctdistance=distance2,
            wedgeprops=dict(width=0.7)
        )

        plt.subplot(234)
        plt.title('B类销量占比')
        plt.pie(
            value_b, labels=title_b,
            labeldistance=l_distance2,
            shadow=True,
            radius=radius,
            autopct='%3.3f%%',
            pctdistance=distance2,
            wedgeprops=dict(width=0.7)
        )

        plt.subplot(236)
        plt.title('C类销量占比')
        plt.pie(
            value_c, labels=title_c,
            labeldistance=l_distance2,
            shadow=True,
            radius=radius,
            autopct='%3.3f%%',
            pctdistance=distance2,
            wedgeprops=dict(width=0.7),
        )
        plt.show()
    else:
        pass


def all_pie(lists, boundary_quantity):
    import matplotlib.pyplot as plt

    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.size'] = font_size1
    plt.rcParams['axes.unicode_minus'] = False

    title = []
    value_ = []

    for i in lists:
        title.append(i[0])
        value_.append(i[1])
    if boundary_quantity == 1:
        plt.title('两类货物实际销量占比')
    elif boundary_quantity == 2:
        plt.title('三类货物实际销量占比')
    else:
        plt.title('三类货物实际销量占比')

    plt.pie(
        value_, labels=title,
        labeldistance=l_distance,
        shadow=True,
        radius=radius2,
        autopct='%2.2f%%',
        pctdistance=distance,
        wedgeprops=dict(width=0.7),
    )
    plt.show()