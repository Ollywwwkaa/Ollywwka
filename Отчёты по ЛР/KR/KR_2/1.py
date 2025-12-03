logs = [
    "192.168.1.1 - GET /index.html 200",
    "192.168.1.5 - GET /about 404",
    "192.168.1.1 - POST /login 200",
    "10.0.0.1 - GET /admin 500",
    "192.168.1.5 - GET /contact 404",
    "192.168.1.5 - GET /profile 404",
    "192.168.1.1 - GET /home 200",
    "10.0.0.1 - POST /admin 500",
    "192.168.1.5 - GET /test 404",
    "10.0.0.1 - GET /dashboard 500",
    "192.168.1.10 - GET /index 200",
    "192.168.1.10 - GET /login 404",]
def analyze_server_logs(logs, error_threshold=3):
    status_counts = {"200": 0, "404": 0, "500": 0}
    ip_counts = {}
    error_counts = {}
    for log in logs:
        parts = log.split()
        if len(parts) >= 4:
            ip = parts[0]
            status = parts[-1]
            if status in status_counts:
                status_counts[status] += 1
            ip_counts[ip] = ip_counts.get(ip, 0) + 1
            if status in ("404", "500"):
                error_counts[ip] = error_counts.get(ip, 0) + 1
    top_ip = max(ip_counts, key=ip_counts.get, default=None)
    suspicious_ips = [ip for ip, count in error_counts.items() 
                      if count > error_threshold]
    return status_counts, top_ip, suspicious_ips
status_counts, top_ip, suspicious_ips = analyze_server_logs(logs, error_threshold=2)
print("1. Количество запросов по кодам ответов:")
for status, count in status_counts.items():
    print(f"  Код {status}: {count} запросов")
print(f"\n2. IP с наибольшим количеством запросов: {top_ip}")
print(f"\n3. Подозрительные IP (с ошибками 404/500 > 2 раз):")
if suspicious_ips:
    for ip in suspicious_ips:
        print(f"  {ip}")
else:
    print("Подозрительных IP не обнаружено")
print("Дополнительная статистика:")
all_ips = set()
for log in logs:
    parts = log.split()
    if parts:
        all_ips.add(parts[0])
print(f"Всего уникальных IP: {len(all_ips)}")
print("\nСтатистика по IP-адресам:")
for log in logs:
    parts = log.split()
    if len(parts) >= 4:
        ip = parts[0]
        status = parts[-1]
        print(f"{ip}: {log.split('-', 1)[-1].strip()}")