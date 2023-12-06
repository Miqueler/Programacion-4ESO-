gender=input()
red_blood_cells=float(input())
whithe_blood_cells=int(input())
palletes=int(input())
hemoglobin=float(input())
hematocrit_percentage=int(input())

if gender =="Male":
    if red_blood_cells>5.9 or red_blood_cells<4.3:
        print("Red blood cells: VISIT THE DOCTOR")
    if whithe_blood_cells<4500 or whithe_blood_cells>11000:
        pass
#es poner muchos if's