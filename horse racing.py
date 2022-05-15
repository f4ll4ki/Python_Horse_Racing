import random as r

print("예시: 1 or 2 or 3 or 4 or 5")
yc = int(input("예측을 적어주세요: "))

i = 0
h = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
while i <5:
  i+=1
  #버프 크기 0.8 ~ 1.1
  bf1 = (r.randint(8,11)/10)
  bf2 = (r.randint(8,11)/10)
  bf3 = (r.randint(8,11)/10)
  bf4 = (r.randint(8,11)/10)
  bf5 = (r.randint(8,11)/10)
  h += r.randint(5,10)*bf1
  h2 += r.randint(5,10)*bf2
  h3 += r.randint(5,10)*bf3
  h4 += r.randint(5,10)*bf4
  h5 += r.randint(5,10)*bf5
  print("═══════════════════════════════════════════════") 
  print("                                             ")
  print(" [%d 바퀴]   1번 말은 %d만큼 이동했습니다!    "%(i,h))
  print("                                             ")
  print("            2번 말은 %d만큼 이동했습니다!      "%h2)
  print("                                             ")
  print("            3번 말은 %d만큼 이동했습니다!     "%h3)
  print("                                          ")
  print("            4번 말은 %d만큼 이동했습니다!      "%h4)
  print("                                           ")
  print("            5번 말은 %d만큼 이동했습니다!      "%h5)
  print("                                             ")
  print("═══════════════════════════════════════════════") 
print("╔═════════════════════════════════════════════╗")
print("║                                             ║")
print("║ 골인! 1번 말은 총 %d만큼 이동했습니다!      ║"%h)
print("║      2번 말은 총 %d만큼 이동했습니다!       ║"%h2)
print("║      3번 말은 %d만큼 이동했습니다!          ║"%h3)
print("║      4번 말은 %d만큼 이동했습니다!          ║"%h4)
print("║      5번 말은 %d만큼 이동했습니다!          ║"%h5)
print("║                                             ║")
print("╚═════════════════════════════════════════════╝")

num = [h,h2,h3,h4,h5]
i = 0
max = 0

kun = num[0]
rank = "1번이 제일 빠르다"
while i < 4:
  if kun < num[i+1]:
    kun = num[i+1]
    rank = "%d번 말이 제일 빠르다."%(i+2)
  max = kun
  i+=1
print("당신의 예측 말")
print(yc)
print("═════════════════════════════")
print("")
print("[순위]")
print(rank)
print("═════════════════════════════")
