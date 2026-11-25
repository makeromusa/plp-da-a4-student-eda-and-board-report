import numpy as np
import pandas as pd

# Generator 1: Duka Electronics
rng1 = np.random.default_rng(2026)
n1 = 1000
products = {
    "Phone": 15000,
    "Laptop": 65000,
    "Headphones": 2500,
    "Tablet": 28000,
    "Charger": 1200,
}

sales = pd.DataFrame({
    "order_id": range(1001, 1001 + n1),
    "order_date": pd.to_datetime("2026-01-01")
    + pd.to_timedelta(rng1.integers(0, 180, n1), unit="D"),
    "branch": rng1.choice(
        ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"],
        n1,
        p=[0.4, 0.2, 0.15, 0.15, 0.1],
    ),
    "product": rng1.choice(list(products), n1),
    "quantity": rng1.integers(1, 6, n1),
    "channel": rng1.choice(
        ["In-store", "Online", "Phone order"], n1, p=[0.55, 0.35, 0.10]
    ),
})
sales["unit_price"] = sales["product"].map(products)
sales.to_csv("duka_sales.csv", index=False)
print("duka_sales.csv generated successfully.")

# Generator 2: Student Performance
rng2 = np.random.default_rng(55)
n2 = 1200
students = pd.DataFrame({
    "student_id": range(1, n2 + 1),
    "county": rng2.choice(
        ["Nairobi", "Kisumu", "Nakuru", "Mombasa", "Nyeri", "Turkana"], n2
    ),
    "school_type": rng2.choice(["Public", "Private"], n2, p=[0.75, 0.25]),
    "gender": rng2.choice(["F", "M"], n2),
    "attendance_rate": rng2.beta(8, 2, n2).round(2),
    "study_hours": rng2.gamma(2.5, 2.0, n2).round(1),
})
base = (
    35
    + 30 * students["attendance_rate"]
    + 2.2 * students["study_hours"]
    + np.where(students["school_type"] == "Private", 6, 0)
)
students["math"] = (base + rng2.normal(0, 8, n2)).clip(0, 100).round(0)
students["english"] = (base + rng2.normal(3, 7, n2)).clip(0, 100).round(0)
students["science"] = (base + rng2.normal(-2, 9, n2)).clip(0, 100).round(0)
students.to_csv("student_performance.csv", index=False)
print("student_performance.csv generated successfully.")
