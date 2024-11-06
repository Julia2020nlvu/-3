# TODO Напишите функцию для поиска индекса товара

def find_first_index(items_list: list, find_item: str) -> int:
    try:
        return items_list.index(find_item)
    except ValueError:
        return None

    items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

    find_item = find_first_index(find_item, items_list)
    for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, index_item)   # TODO Вызовите функцию, что получить индекс товара

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


