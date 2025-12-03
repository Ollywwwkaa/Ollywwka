def filter_logs(log_lst, keyword):
    for log_entry in log_lst:
        if keyword in log_entry:
            yield log_entry
logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: File not found"]
for error in filter_logs(logs, "ERROR"):
    print(error)