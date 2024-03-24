# input pressure -numeric  , SI unit and water level numeric and Si uint

import datetime
import csv
import hashlib
import secrets
import versionControl 
import pandas as pd
import json
import hashlib
import secrets

logID = 0


def hash_password(password, salt):
    """Hashes the password using SHA256 and a random salt."""
    salted_password = password.encode() + salt
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password


def check_password(client_id, password):
    with open("user_accounts.json") as file:
        user_accounts = json.load(file)

    if client_id in user_accounts:
        hashed_password_from_db = user_accounts[client_id]["password"]
        salt_from_db = bytes.fromhex(user_accounts[client_id]["salt"])

        hashed_input_password = hash_password(password, salt_from_db)

        if hashed_input_password == hashed_password_from_db:
            print("The password is correct")
            return True
        else:
            print("The password is incorrect")
            return False
    else:
        print("Client ID not found")
        return False


def add_user(client_id, password):
    with open("user_accounts.json") as file:
        user_accounts = json.load(file)

    if client_id in user_accounts:
        print("Client ID already exists")
        return False

    salt = secrets.token_hex(16)
    hashed_password = hash_password(password, bytes.fromhex(salt))

    user_accounts[client_id] = {"password": hashed_password, "salt": salt}

    with open("user_accounts.json", "w") as file:
        json.dump(user_accounts, file, indent=4)

    print("User account created successfully")
    return True


## 
def checkPassword_Setter(password):
    if password == "1234":
        print("The password is correct")
        return True
    else:
        print("The password is incorrect")
        return False


def CovertToStandardUnits(pressure, pressure_SI, water_level, water_level_SI):
    pressure_conversion = {"bar": 100000, "psi": 6894.76, "Pa": 1}

    length_conversion = {
        "m": 1,
        "ft": 0.3048,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "yd": 0.9144,
        "km": 1000,
        "mile": 1609.34,
    }

    if pressure_SI in pressure_conversion:
        pressure = pressure * pressure_conversion[pressure_SI]
    else:
        print("Invalid pressure unit")
        return False

    if water_level_SI in length_conversion:
        water_level = water_level * length_conversion[water_level_SI]
    else:
        print("Invalid water level unit")
        return False

    return pressure, water_level



def log_data(pressure, water_level, Client_ID, danger):
    data = {
        "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Pressure": pressure,
        "Water Level": water_level,
        "Danger": danger,
        "logID": logID
    }
    df = pd.DataFrame(data, index=[0])
    df.to_csv(f"{Client_ID}.csv", mode="a", header=not df.empty, index=False)



def check_limits(pressure, water_level):
    if pressure < 100 or pressure > 1000000:
        print("Pressure is out of limits")
        return False
    elif water_level < 10 or water_level > 100:
        print("Water level is out of limits")
        return False
    else:
        return True


def input_data(Client_ID):
    pressure = float(input("Enter the pressure: "))
    pressure_SI = input("Enter the pressure unit: ")
    water_level = float(input("Enter the water level: "))
    water_level_SI = input("Enter the water level unit: ")

    STD_pressure, STD_water_level = CovertToStandardUnits(
        pressure, pressure_SI, water_level, water_level_SI
    )

    if check_limits(STD_pressure, STD_water_level):
        print("The pressure and water level are within the limits")
        log_data(STD_pressure, STD_water_level, Client_ID, danger=False)
        Setter_function(STD_pressure, STD_water_level)
    else:
        print(
            "The pressure and water level are not within the limits, Please Provide Password to change"
        )
        password = input("Enter the password: ")
        if checkPassword_Setter(password):
            Setter_function(STD_pressure, STD_water_level, Client_ID)
            log_data(STD_pressure, STD_water_level, Client_ID, danger=True)
        else:
            print("The password is incorrect, Please try again")
            exit()


def User():
    print("Welcome to the system")
    print("May I know your name?")
    name = input("Enter your name: ")
    print("Hello", name)
    print("Please provide your Client ID")
    Client_ID = input("Enter your Client ID: ")
    print("Thank you for providing the Client ID")
    print("Please provide the password to proceed")
    password = input("Enter the password: ")
    if check_password(Client_ID, password):
        print("Welcome to the system")
        with open("Log.csv", mode="a") as log_file:
            log_writer = csv.writer(
                log_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_writer.writerow(
                [timestamp, Client_ID, logID]
            )  # Log check-in time and client ID
            logID += 1
        driver(Client_ID)
    else:
        print("The password is incorrect, Please try again")
        exit()


def version_control_Setter_function(logID=None, Client_ID=None):
    if logID is None and Client_ID is None:
        print("Please provide the Log ID or Client ID to set the previous setting")
        return False
    elif logID is not None:
        logs = pd.read_csv("Log.csv")
        for index, row in logs.iterrows():
            if logID == row["LogID"]:
                data = pd.read_csv(f"{row['Client_ID']}.csv")
                k = []
                for index, row in data.iterrows():
                    if row["LogID"] == logID:
                        print(
                            f"Client ID: {row['Client_ID']} has the following settings values"
                            + row["Time"]
                            + row["Pressure"]
                            + row["Water Level"]
                        )
                        k.append(row)
                return k if k else False
        print("Log ID not found")
        return False

    elif Client_ID is not None:
        data = pd.read_csv(f"{Client_ID}.csv")
        k = []
        for index, row in data.iterrows():
            if row["Client_ID"] == Client_ID:
                print(
                    f"Client ID: {Client_ID} has the following settings values"
                    + row["Time"]
                    + row["Pressure"]
                    + row["Water Level"]
                )
                k.append(row)
        return k if k else False


def driver(Client_ID):
    print(
        " Please Selection Option 1 for Input Data, 2 For using version control system , 3 for set to previous Setting based on LOG ID, 4 for log out"
    )
    option = input("Enter the option: ")
    if option == "1":
        input_data(Client_ID)
    elif option == "2":
        versionControl.init()
    elif option == "3":
        print("Please provide the Log ID to set the previous setting")
        logID = int(input("Enter the Log ID: "))
        version_control_Setter_function(logID)
    elif option == "4":
        print("Thank you for using the system")
        exit()
