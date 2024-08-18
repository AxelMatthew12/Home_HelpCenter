from LoginService import login

class LoginDisplay():
    def execute(self):
        print("||    SELAMAT DATANG DI LOGIN PAGE    ||")
        print("||               LOGIN                ||")
        print("||             REGISTRASI             ||")
        print("========================================")
        inputLg= input("Jawaban: ")

class Perkenalan():
    def execute(self):
        print("\n")
        print("|| --Hallo Kami adalah Home_Help Center--                                                   ||")
        print("|| Kami dapat membantu anda untuk mengatur dan menjadwalkan setiap kebutuhan di dalam rumah ||")
        print("|| Tentu dengan efesiensi dan Kemudahan penggunaan yang akan membantu anda untuk lebih      ||")
        print("|| Produktif untuk melakukan kegiatan di luar Rumah, Kami dapat membantunya :)              ||")
        print("||==========================================================================================||")
        print("|| Lanjut ke next slide!. Berbagung dengan kami ")
        print("|| (1.Next / 2.Stay)")
        inputoption= input("Jawaban: ")

        try:
            inputoption = int(inputoption)
        except ValueError:
            inputoption = None
        if inputoption == 1:
            command=LoginDisplay()
            command.execute()
        elif inputoption ==2:
            command= Perkenalan()
            command.execute()


def MainIna():
    print("||    SELAMAT DATANG DI APLIKASI PINTAR   ||")
    print("|| 1. Mulai dengan Perkenalan             ||")
    print("|| 2. Sudah pernah Berkenalan             ||")
    input_value = input("||Jawaban: ")
    try:
        input_value = int(input_value)
    except ValueError:
        input_value = None

    if input_value == 1:
        command = Perkenalan()
        command.execute()
