import pandas as pd
import matplotlib.pyplot as plt



def checkPassword(password):
    if password == "1234":
        print("The password is correct")
        return True
    else:
        print("The password is incorrect")
        return False


def plot_water_level(time, water_level):
    """Plot water level versus time."""
    plt.plot(time, water_level)
    plt.xlabel("Time")
    plt.ylabel("Water Level")
    plt.title("Water Level vs Time")
    plt.show()


def plot_pressure(time, pressure):
    """Plot pressure versus time."""
    plt.plot(time, pressure)
    plt.xlabel("Time")
    plt.ylabel("Pressure")
    plt.title("Pressure vs Time")
    plt.show()


def LogAll(initial_time, final_time):
    logs_df = pd.read_csv("Log.csv")
    for index, row in logs_df.iterrows():
        if initial_time <= row["Time"] <= final_time:
            client_df = pd.read_csv(f"{row['Client_ID']}.csv")
            water_level = client_df["Water Level"].astype(float)
            pressure = client_df["Pressure"].astype(float)
            time = client_df["Time"]
            plot_water_level(time, water_level)
            plot_pressure(time, pressure)


def LogEmployee(client_id):
    client_df = pd.read_csv(f"{client_id}.csv")
    water_level = client_df["Water Level"].astype(float)
    pressure = client_df["Pressure"].astype(float)
    time = client_df["Time"]
    plot_water_level(time, water_level)
    plot_pressure(time, pressure)


def LogDanger():
    logs_df = pd.read_csv("Log.csv")
    for index, log in logs_df.iterrows():
        client_df = pd.read_csv(f"{log['Client_ID']}.csv")
        danger_rows = client_df.query("Danger == 'True'")
        for danger_row in danger_rows.itertuples():
            print(
                f"Client ID: {log['Client_ID']} has danger settings values at {danger_row.Time}: Pressure={danger_row.Pressure}, Water Level={danger_row.WaterLevel}"
            )

def init():
    print("Welcome to the Version Control system")
    print("Please provide the password to proceed")
    password = input("Enter the password: ")
    if checkPassword(password):
        print("welcome to the system")
        print(
            " Please select option 1. To check the log details of all employees. 2. To check the log details of a specific employee, 3. To check log  Details of a danger settings"
        )
        option = input("Enter the option: ")
        if option == "1":
            print(
                "Please enter the initial time and final time to check the log details"
            )
            initial_time = input("Enter the initial time: ")
            final_time = input("Enter the final time: ")
            LogAll(initial_time, final_time)
        elif option == "2":
            print("Please enter the Client ID to check the log details")
            client_id = input("Enter the Client ID: ")
            LogEmployee(client_id)
        elif option == "3":
            LogDanger()
        else:
            print("Invalid option")
            exit()


#
