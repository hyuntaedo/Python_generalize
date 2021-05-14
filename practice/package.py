#하나의 패키지에 여러 모듈이 들어있음
#import travel.tiland #클래스나 함수는 임포트를 직접 할 수 없음 패키지만 가능
#trip_to = travel.tiland.ThailandPackage()
#trip_to.detail()

#from travle.tiland import ThailandPackage
#trip_to = ThailandPackage()
#trip_to.detail()

#from travel import vietnam
#trip_to = vietnam.VietnamPackage()
#trip_to.detail()

#from random import *
from travel import * 
# *을 쓴다는거는 모든것을 
# 가져오지만 실제로는 개발자가 문법상에서
# 공개범위를 설정 해줘야하는것
trip_to1 = vietnam.VietnamPackage()
trip_to1.detail()
trip_to2 = tiland.ThailandPackage()
trip_to2.detail()
