from pickle import *
profile_file = open("profile.pickle","wb")
profile = {"이름":"도현태","나이":30,"취미":["골프","코딩","축구"]}
print(profile)
pickle.dump(profile,profile_file)
profile_file.close()