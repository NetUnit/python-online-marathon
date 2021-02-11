import re


def max_population(data):
    # done - info deletion
    del data[0]

    # done - is_capital removal
    data = [i[:-2] for i in data]

    # done - convert into string
    data = ' '.join(data)

    # pattern & return the prapared string
    pattern_list = (''.join(re.findall(
        r"\D{2}\S\w{1,}\s\d{5}", data.replace(',', ' ')))).strip().split()

    # slices for dict
    settlement = [i for i in pattern_list[::2]]
    population = [int(i) for i in pattern_list[1::2]]

    # creating dict
    zip_iterator = dict(zip(population, settlement))
    # print(zip_iterator)

    return zip_iterator[max(zip_iterator.keys())], max(zip_iterator.keys())


data = ["id,name,poppulation,is_capital",
        "3024,eu_kyiv,24834,y",
        "3025,eu_volynia,20231,n",
        "3026,eu_galych,23745,n",
        "4892,me_medina,18038,n",
        "4401,af_cairo,18946,y",
        "4700,me_tabriz,13421,n",
        "4899,me_bagdad,22723,y",
        "6600,af_zulu,09720,n"]

print(max_population(data))
