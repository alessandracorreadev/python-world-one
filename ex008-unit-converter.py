distance = float(input("Enter a distance in meters: "))
km = distance/1000
hm = distance/100
dam = distance/10
dm = distance*10
cm = distance*100
mm = distance*1000

print(f"The meansurement of {distance} meters corresponds to: \n"
      f"{km}km. \n"
      f"{hm}hm. \n"
      f"{dam}dam. \n"
      f"{dm:.0f}dm. \n"
      f"{cm:.0f}cm. \n"
      f"{mm:.0f}mm.")