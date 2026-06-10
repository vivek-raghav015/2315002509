from datetime import datetime

notifications = [
    {
        "ID": "01460958",
        "Type": "Result",
        "Message": "mid-sem",
        "Timestamp": "2026-04-22 17:51:30"
    },
    {
        "ID": "b283218f",
        "Type": "Placement",
        "Message": "CSX Corporation hiring",
        "Timestamp": "2026-04-22 17:51:18"
    },
    {
        "ID": "81589ada",
        "Type": "Event",
        "Message": "Farewell",
        "Timestamp": "2026-04-22 17:51:06"
    }
]

weights = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

for notification in notifications:
    timestamp = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    notification["priority_score"] = (
        weights[notification["Type"]] * 1000000000
        + timestamp.timestamp()
    )

top_notifications = sorted(
    notifications,
    key=lambda x: x["priority_score"],
    reverse=True
)[:10]

print("\nTOP PRIORITY NOTIFICATIONS\n")

for i, n in enumerate(top_notifications, start=1):
    print(
        f"{i}. [{n['Type']}] "
        f"{n['Message']} "
        f"({n['Timestamp']})"
    )