from time import sleep
from adafruit_servokit import ServoKit

waktu_sleep = 0.2

kit1 = ServoKit(channels = 16, address = 0x41)
kit2 = ServoKit(channels = 16, address = 0x40)

#femur 1 3 5 ngangkat
for i in range(10, 41, 1):
    kit1.servo[7].angle = 140 + i #femur1
    kit1.servo[6].angle = 150 + (i-10) #tibia1
    kit1.servo[1].angle = 140 + i #femur3
    kit1.servo[0].angle = 150 + (i-10) #tibia3
    kit2.servo[11].angle = 45 -(i+5) #femur5
    kit2.servo[12].angle = 35 - (i-5) #tibia5
print("Femur 1 3 5 Ngangkat")
sleep(waktu_sleep)

try:
    while True:
        #coxa 1 3 5 maju
        kit1.servo[8].angle = 120 #coxa1
        kit1.servo[2].angle = 120 #coxa3
        kit2.servo[10].angle = 60 #coxa5
        print("Coxa 1 3 5 Maju")
        sleep(waktu_sleep)
        

        #femur 1 3 5 turun dan tibia turun sekalian adjust ngambil kaki
        for i in range (10, 41, 1):
            kit1.servo[7].angle = 180 - i #femur1
            kit1.servo[6].angle = 180 - (i-10) #tibia1
            kit1.servo[1].angle = 180 - i #femur3
            kit1.servo[0].angle = 180 - (i-10) #tibia3
            kit2.servo[11].angle = 0 + (i+5) #femur5
            kit2.servo[12].angle = 0 + (i-5) #tibia5
        print("Femur Tibia 1 3 5 Turun")
        sleep(waktu_sleep)
        #coxa femur tibia 1 3 5 balik ke posisi awal
        kit1.servo[8].angle = 90 #coxa1
        kit1.servo[7].angle = 140 #femur1
        kit1.servo[6].angle = 150 #tibia1

        kit1.servo[2].angle = 90 #coxa3
        kit1.servo[1].angle = 140 #femur3
        kit1.servo[0].angle = 150 #tibia3

        kit2.servo[10].angle = 90 #coxa5
        kit2.servo[11].angle = 45 #femur5
        kit2.servo[12].angle = 35 #tibia5
        print("Coxa Femur Tibia 1 3 5 Balik")
        #sleep(0.05)
        #femur 2 4 6 ngangkat
        for i in range (10, 41, 1):
            kit1.servo[4].angle = 140 + i #femur2
            kit1.servo[3].angle = 145 + (i-5) #tibia2
            kit2.servo[14].angle = 40 - i #femur4
            kit2.servo[15].angle = 35 - (i-5) #tibia4
            kit2.servo[8].angle = 40 - i #femur6
            kit2.servo[9].angle = 30 - (i-10) #tibia6
        print("Femur 2 4 6 Ngangkat")
        sleep(waktu_sleep)

        #coxa 2 4 6 maju
        kit1.servo[5].angle = 120 #coxa2
        kit2.servo[13].angle = 60 #coxa4
        kit2.servo[7].angle = 60 #coxa6
        print("Coxa 2 4 6 Maju")
        sleep(waktu_sleep)

        #femur 2 4 6 turun dan tibia turun sekalian adjust ngambil kaki
        for i in range (10, 41, 1):
            kit1.servo[4].angle = 180 - (i) #femur2
            kit1.servo[3].angle = 180 - (i-5) #tibia2
            kit2.servo[14].angle = 0 + i #femur4
            kit2.servo[15].angle = 0 + (i-5) #tibia4
            kit2.servo[8].angle = 0 + i #femur6
            kit2.servo[9].angle = 0 + (i-10) #tibia6
        
        print("Femur Tibia 2 4 6 Turun")
        sleep(waktu_sleep)
        #coxa femur tibia 2 4 6 balik ke poisi awal
        kit1.servo[5].angle = 90 #coxa2
        kit1.servo[4].angle = 140 #femur2
        kit1.servo[3].angle = 145 #tibia2


        kit2.servo[13].angle = 90 #coxa4
        kit2.servo[14].angle = 40 #femur4
        kit2.servo[15].angle = 35 #tibia4


        kit2.servo[7].angle = 90 #coxa6
        kit2.servo[8].angle = 40 #femur6
        kit2.servo[9].angle = 30 #tibia6
        print("Coxa Femur Tibia 2 4 6 Balik")
        #sleep(0.05)
        #femur 1 3 5 ngangkat
        for i in range(10, 41, 1):
            kit1.servo[7].angle = 140 + i #femur1
            kit1.servo[6].angle = 150 + (i-10) #tibia1
            kit1.servo[1].angle = 140 + i #femur3
            kit1.servo[0].angle = 150 + (i-10) #tibia3
            kit2.servo[11].angle = 45 -(i+5) #femur5
            kit2.servo[12].angle = 35 - (i-5) #tibia5
        print("Femur 1 3 5 Ngangkat")
        sleep(waktu_sleep)

except KeyboardInterrupt:
	kit1.servo[8].angle = 90 #coxa1
	kit1.servo[7].angle = 140 #femur1
	kit1.servo[6].angle = 150 #tibia1

	kit2.servo[7].angle = 90 #coxa6
	kit2.servo[8].angle = 40  #femur6
	kit2.servo[9].angle = 30 #tibia6

	kit1.servo[5].angle = 90 #coxa2
	kit1.servo[4].angle = 140 #femur2
	kit1.servo[3].angle = 145 #tibia2

	kit2.servo[10].angle = 90 #coxa5
	kit2.servo[11].angle = 45 #femur5
	kit2.servo[12].angle = 35 #tibia5

	kit1.servo[2].angle = 90 #coxa3
	kit1.servo[1].angle = 140 #femur3
	kit1.servo[0].angle = 150 #tibia3

	kit2.servo[13].angle = 90 #coxa4
	kit2.servo[14].angle = 40 #femur4
	kit2.servo[15].angle = 35 #tibia4




