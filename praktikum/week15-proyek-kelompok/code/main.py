import os
import cpu_scheduling
import page_replacement
import deadlock_detection


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_header():
    print("=" * 40)
    print(" SIMULASI SISTEM OPERASI ")
    print("=" * 40)


def show_main_menu():
    print("\nMenu Utama:")
    print("1. CPU Scheduling")
    print("2. Page Replacement")
    print("3. Deadlock Detection")
    print("0. Keluar")


def run_cpu_scheduling():
    clear_screen()
    show_header()
    print("\n--- CPU Scheduling ---")
    cpu_scheduling.main()
    input("\nTekan Enter untuk kembali ke menu utama...")


def run_page_replacement():
    clear_screen()
    show_header()
    print("\n--- Page Replacement ---")
    page_replacement.main()
    input("\nTekan Enter untuk kembali ke menu utama...")


def run_deadlock_detection():
    clear_screen()
    show_header()
    print("\n--- Deadlock Detection ---")
    deadlock_detection.main()
    input("\nTekan Enter untuk kembali ke menu utama...")


def main():
    while True:
        clear_screen()
        show_header()
        show_main_menu()

        choice = input("\nPilih menu: ")

        if choice == "1":
            run_cpu_scheduling()
        elif choice == "2":
            run_page_replacement()
        elif choice == "3":
            run_deadlock_detection()
        elif choice == "0":
            print("\nKeluar dari program. Terima kasih ")
            break
        else:
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk mencoba lagi...")


if __name__ == "__main__":
    main()
