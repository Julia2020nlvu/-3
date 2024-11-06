# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(participants_first_group: str, participants_second_group: str, separator: str = ",") -> list:

  first_group = participants_first_group.split(separator)
  second_group = participants_second_group.split(separator)
  common_participants = sorted(list(set(first_group).intersection(set(second_group))))
  return common_participants

print(f"Общие участники: {find_common_participants}")

