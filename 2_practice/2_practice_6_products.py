# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть
# два элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

list_products = []
# for analitic
name_list = []
price_list = []
number_list = []
unit_list = []
# ------------
dict_product_base = {"название": None, "цена": None, "количество": None, "ед": None}
number_product = int(input("Введите количество товаров которое хотите внести => "))
for i in range(number_product):
    dict_product = {}
    dict_product.update(dict_product_base)
    print("---Занесите сведения о товаре №", i+1, sep="")
    name_prod = input("Введите наименование товара: ")
    dict_product["название"] = name_prod
    price_prod = int(input("Введите цену товара: "))
    dict_product["цена"] = price_prod
    number_prod = int(input("Введите количество товара: "))
    dict_product["количество"] = number_prod
    unit_prod = input("Введите единицы измерения продукта: ")
    dict_product["ед"] = unit_prod
    list_products.append((i+1, dict_product))
    # for_analitic
    name_list.append(name_prod)
    price_list.append(price_prod)
    number_list.append(number_prod)
    unit_list.append(unit_prod)
print("\n*Занесение сведений о товарах завершено!*")
print("\n___Список занесеных товаров:___\n", list_products)
dict_analitic = {"названия": name_list, "цена": price_list, "количество": name_list, "ед": unit_list}
print("\n___Аналитика занесеных товаров:___\n", dict_analitic)
