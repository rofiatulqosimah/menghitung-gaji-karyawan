def calculate_salary():
    # Input jumlah jam kerja dan tarif per jam
    try:
        hours_worked = float(input("Masukkan jumlah jam kerja: "))
        hourly_rate = float(input("Masukkan tarif per jam: "))
    except ValueError:
        print("Masukkan angka yang valid untuk jam kerja dan tarif per jam.")
        return

    # Konstanta untuk batas jam kerja normal dan tarif lembur
    regular_hours = 40
    overtime_rate_multiplier = 1.5

    if hours_worked <= regular_hours:
        total_salary = hours_worked * hourly_rate
    else:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * hourly_rate * overtime_rate_multiplier
        total_salary = (regular_hours * hourly_rate) + overtime_pay

    print(f"Gaji total karyawan: Rp{total_salary:,.2f}")

# Menjalankan fungsi
if __name__ == "__main__":
    calculate_salary()