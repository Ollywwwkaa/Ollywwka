def format_report(report_title: str, *data: str, **properties: str):
    print(f"{report_title.upper()}")
    if data:
        print("\nсодержание:")
        for i, item in enumerate(data, 1):
            print(f"{i}. {item}")
    if properties:
        print("\n метаданные:")
        for key, value in properties.items():
            print(f"  • {key}: {value}")
format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    "Возвратов: 2",
    author="Сидоров А.В.",
    date="2025-11-04",
    department="Отдел продаж")