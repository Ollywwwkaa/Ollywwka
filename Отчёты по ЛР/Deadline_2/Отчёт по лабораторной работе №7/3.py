from typing import List, Dict, Any, Union
def calc_avg(numbers: List[Union[int, float]]):
    if not numbers:
        return 0.0 
    return sum(numbers) / len(numbers)
def fmt_fio(parts: List[str], capitalize: bool = True):
    fio = " ".join(parts)
    if capitalize:
        return fio.title()  
    return fio
def filter_scores(data_dict: Dict[str, Union[int, float]], min_value: Union[int, float]) -> Dict[str, Union[int, float]]:
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value 
    return result
def main():
    print("=" * 60)
    print("=" * 60)
    print("-" * 50)
    test1 = [10, 20, 30, 40]
    test2 = [15.5, 25.3, 10.2]
    test3 = []
    print(f"calc_avg({test1}) = {calc_avg(test1)}")
    print(f"calc_avg({test2}) = {calc_avg(test2)}")
    print(f"calc_avg({test3}) = {calc_avg(test3)}")
    print("-" * 50)
    fio1 = ["петров", "иван", "сергеевич"]
    fio2 = ["сидорова", "анна", "валерьевна"]
    fio3 = ["ИВАНОВ", "петр", "СЕРГЕЕВИЧ"]
    print(f'fmt_fio({fio1}) = "{fmt_fio(fio1)}"')
    print(f'fmt_fio({fio2}, capitalize=False) = "{fmt_fio(fio2, capitalize=False)}"')
    print(f'fmt_fio({fio3}) = "{fmt_fio(fio3)}"')
    print("-" * 50)
    scores = {"math": 95, "history": 78, "english": 88, "art": 92, "physics": 65}
    print(f"Исходные данные: {scores}")
    print(f"filter_scores(scores, 90) = {filter_scores(scores, 90)}")
    print(f"filter_scores(scores, 80) = {filter_scores(scores, 80)}")
    print(f"filter_scores(scores, 95) = {filter_scores(scores, 95)}")
    print("\n" + "=" * 60)
    print("=" * 60)
if "name" == "main":
    main()