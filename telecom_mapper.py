#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(",")

    if fields[0] == "Phone Number":
        continue

    try:
        phone = fields[0]

        day_mins = float(fields[3])
        eve_mins = float(fields[6])
        night_mins = float(fields[9])
        intl_mins = float(fields[12])

        day_calls = int(fields[4])
        eve_calls = int(fields[7])
        night_calls = int(fields[10])
        intl_calls = int(fields[13])

        custserv_calls = int(fields[15])
        churn = fields[16]

        total_duration = day_mins + eve_mins + night_mins + intl_mins
        total_calls = day_calls + eve_calls + night_calls + intl_calls

        # 1️⃣ Total Duration Per User
        print("UserDuration_" + phone + "\t" + str(total_duration))

        # 2️⃣ Peak Usage
        print("DayCalls\t" + str(day_calls))
        print("EveCalls\t" + str(eve_calls))
        print("NightCalls\t" + str(night_calls))
        print("IntlCalls\t" + str(intl_calls))

        # 3️⃣ Churn
        if churn == "TRUE":
            print("Churn\t1")
        else:
            print("NonChurn\t1")

        # 4️⃣ Fraud Detection
        if custserv_calls > 3 or intl_calls > 5:
            print("HighRisk\t1")

        # 5️⃣ Heavy Users
        if total_calls > 300:
            print("HeavyUsers\t1")

        # 6️⃣ Customer Service Load
        print("CustServCalls\t" + str(custserv_calls))

    except:
        continue
