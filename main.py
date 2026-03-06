print("sizinle bir oyun oynayacağız")
isim=input("\nlütfen öncelikle isminizi giriniz")
print(f"\noynayacağımız oyun, sayı tahmin oyunudur. hoşgeldiniz {isim} bey")
while True:
  try:
    sayı_gir= int(input("\nlütfen tahmini bir sayı giriniz ve doğru olana kadar pes etmeyiniz:"))
    if sayı_gir== 2026:
      print("\ntebrikler doğru sayıyı buldunuz")
      break
    elif 0<sayı_gir<500:
      print("\nsayınız çok küçük, lütfen daha büyük bir sayı giriniz")
  
    elif 500<=sayı_gir<1000:
      print("\nsayınız biraz küçük ama bu yoldan devam edin")
    
    elif 1000<=sayı_gir<2000:
      print("\nne çok uzak ne de çok yakın bir sayı girdiniz, biraz daha büyük bir sayı giriniz")
    
    elif 2000<=sayı_gir<2026:
      print("\nşuan sayının dibinde duruyorsunuz")
      print("size ipucu vereyim;hangi yıldayız?")
    
    elif 2026<sayı_gir<=2500:
      print("\nşuan sayıya öpücük veriyorsunuz, lütfen daha küçük bir sayı giriniz")
  
    elif 2500<sayı_gir<=3000:
      print("\nsaynız biraz büyükmüş! daha küçük bir sayı deeneyebilirsiniz")
    
    elif 3000<sayı_gir<=4000:
      print("\nsayınız çok büyük!!, lüten daha küçük bir sayı tuşlayınız")
    
    elif sayı_gir>4000:
      print("\nuupsss!!! uzaya çıktın resmen, biraz in be!")
    elif sayı_gir<0:
      print("lütfen pozitif bir sayı tuşlayınız!!")
    
  except ValueError:
    print(f"\n{sayı_gir} bir sayı değil!! lütfen bir sayı değeri giriniz. örn:123")