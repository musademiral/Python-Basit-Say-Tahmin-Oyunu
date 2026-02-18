import random
num_in_mind= random.randint(1,100)
print("SAYI TAHMİN OYUNUNA HOŞ GELDİNİZ. 5 ADET CAN HAKKINIZ BULUNMAKTA.")
can=0
while can<6:
    user_input= input("1 ile 100 arasında bir sayı giriniz (1 ve 100 dahil): ")
    if user_input.isdigit():
        user_input= int(user_input)
        if user_input < num_in_mind:
            print("Daha yüksek bir sayı giriniz.")
            can= can+1
        elif user_input > num_in_mind:
            print("Daha düşük bir sayı giriniz.")
            can= can+1
        elif user_input == num_in_mind:
            print("DOĞRU TAHMİN!")
            break
        if can>=5:
            print(f"Can hakkınız bitti... Geçerli sayı: {num_in_mind}")
            break
    else:
        print("Lütfen bir sayı giriniz")
        continue