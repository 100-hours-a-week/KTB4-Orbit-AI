print("Orbit 첫 터미널 코딩")
print("터미널 챗봇")
print("==========")

name = input("이름을 적어주세요:")
feeling = input("기분을 적어주세요(굿,보통,나쁨):")
print("=============")

if "굿" in feeling:
	print(f"{name}님이 기분이 좋다고 하시니, 저도 기분이 좋네요!")
elif "보통" in feeling:
	print(f"{name}님이 기분이 보통이라고 하시니, 좋은일이 생기실 거에요!")
elif "나쁨" in feeling:
	print(f"{name}님이 기분이 안좋다고 하사니, 내일은 좋은일이 생길거에요!")
else:
	print("오타가 있는거 같아요 다시 작성해 주세요!")

print("------------")
