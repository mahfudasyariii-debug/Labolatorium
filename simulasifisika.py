import math
import time
import os

# ==========================================
# SIMULASI RELATIVITAS KHUSUS
# "KECEPATAN MEMBENGKOKKAN WAKTU"
# ==========================================

C = 299_792_458  # kecepatan cahaya (m/s)

player_time = 0.0
world_time = 0.0

speed_percent = 0.0

running = True


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def gamma(v):
    """
    Lorentz factor:
    gamma = 1 / sqrt(1 - v²/c²)
    """
    beta = v / C

    if beta >= 1:
        return float("inf")

    return 1 / math.sqrt(1 - beta**2)


def format_time(seconds):
    years = seconds / (365.25 * 24 * 3600)

    if years >= 1:
        return f"{years:.6f} tahun"

    days = seconds / (24 * 3600)

    if days >= 1:
        return f"{days:.6f} hari"

    return f"{seconds:.6f} detik"


while running:

    clear()

    velocity = C * (speed_percent / 100)

    g = gamma(velocity)

    print("=" * 55)
    print("      SIMULASI: KECEPATAN MEMBENGKOKKAN WAKTU")
    print("=" * 55)

    print()
    print(f"Kecepatan kapal : {speed_percent:.6f}% c")
    print(f"Kecepatan       : {velocity:,.2f} m/s")
    print(f"Faktor gamma    : {g:.6f}")

    print()
    print("WAKTU")
    print("-" * 55)

    print(f"Waktu Budi      : {format_time(world_time)}")
    print(f"Waktu pemain    : {format_time(player_time)}")

    if g != float("inf"):
        print()
        print(
            f"1 detik pemain ≈ {g:.6f} detik Budi"
        )

    print()
    print("KONTROL")
    print("-" * 55)
    print("[+] Tambah kecepatan")
    print("[-] Kurangi kecepatan")
    print("[S] Simulasikan 1 detik")
    print("[R] Reset")
    print("[Q] Keluar")

    command = input("\n>>> ").lower()

    if command == "+":
        speed_percent += 1

        if speed_percent >= 99.999999:
            speed_percent = 99.999999

    elif command == "-":
        speed_percent -= 1

        if speed_percent < 0:
            speed_percent = 0

    elif command == "s":

        # 1 detik waktu pemain
        dt_player = 1.0

        # Dilatasi waktu:
        # dt_world = gamma * dt_player
        dt_world = g * dt_player

        player_time += dt_player
        world_time += dt_world

    elif command == "r":
        player_time = 0
        world_time = 0
        speed_percent = 0

    elif command == "q":
        running = False


print("\nSimulasi selesai.")