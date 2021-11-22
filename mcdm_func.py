
import pymongo
def mcdm_func(weight_dict,room_values):
#room_values={"clean"=1,"temp"=22,"humidity"=32,"comp"=30,"wifi"=8,"area"=4,"window"=2,"outlet"=5}):
    total_score=0
    if not weight_dict:
        print("User didn't provide any preference hence assigning default weights....")
        weight_dict["health_clean"]=50
        weight_dict["health_temp"]=30
        weight_dict["health_humidity"]=20
        weight_dict["facility_computer"]=40
        weight_dict["facility_wifi"]=30
        weight_dict["facility_area"]=10
        weight_dict["facility_window"]=10
        weight_dict["facility_outlet"]=10

    else:
        print(weight_dict["b"])
    
    #calculating clean weights
    if room_values["clean"]==7:
        clean_score=weight_dict["health_clean"]
        total_score+=weight_dict["health_clean"]
        print("clean_score=",clean_score)
    else:
        clean_score=weight_dict["health_clean"]-(((7-room_values["clean"])/7)*weight_dict["health_clean"])
        total_score+=clean_score
        print("clean_score=",clean_score)
    #calculating temp weights
    if (room_values["temp"]>=16 and room_values["temp"]<=24):
        temp_score=weight_dict["health_temp"]
        total_score+=temp_score
        print("temp_score=",temp_score)
    elif room_values["temp"]<16:
        temp_score=weight_dict["health_temp"]-(((16-room_values["temp"])/20)*weight_dict["health_temp"])
        total_score+=temp_score
        print("temp_score=",temp_score)
    else:
        temp_score=weight_dict["health_temp"]-(((room_values["temp"]-24)/20)*weight_dict["health_temp"])
        total_score+=temp_score
        print("temp_score=",temp_score)
    #calculating humidity weights
    if (room_values["humidity"]>=30 and room_values["humidity"]<=60):
        humidity_score=weight_dict["health_humidity"]
        total_score+=humidity_score
        print("humidity_score=",humidity_score)
    elif room_values["humidity"]<30:
        humidity_score=weight_dict["health_humidity"]-(((30-room_values["humidity"])/45)*weight_dict["health_humidity"])
        total_score+=humidity_score
        print("humidity_score=",humidity_score)
    else:
        humidity_score=weight_dict["health_humidity"]-(((room_values["humidity"]-60)/45)*weight_dict["health_humidity"])
        total_score+=humidity_score
        print("humidity_score=",humidity_score)
    #calculating computer weights
    if (room_values["computer"]>=room_values["student"]):
        computer_score=weight_dict["facility_computer"]
        total_score+=computer_score
        print("computer_score=",computer_score)
    else:
        computer_score=weight_dict["facility_computer"]-(((room_values["student"]-room_values["computer"])/room_values["student"])*weight_dict["facility_computer"])
        total_score+=computer_score
        print("computer_score=",computer_score)
    #calculating wifi weights
    if (room_values["wifi"]==1):
        wifi_score=weight_dict["facility_wifi"]
        total_score+=wifi_score
        print("wifi_score=",wifi_score)
    else:
        wifi_score=0
        #total_score+=computer_score
        print("wifi_score=",wifi_score)
    #calculating computer weights
    lowest_area=room_values["student"]*3
    highest_area=room_values["student"]*7
    if (room_values["area"]>=lowest_area and room_values["area"]<=highest_area):
        area_score=weight_dict["facility_area"]
        total_score+=area_score
        print("area_score=",area_score)
    elif room_values["area"]<lowest_area:
        area_score=weight_dict["facility_area"]-(((lowest_area-room_values["area"])/5)*weight_dict["facility_area"])
        total_score+=area_score
        print("area_score=",area_score)
    else:
        area_score=weight_dict["facility_area"]-(((room_values["area"]-highest_area)/5)*weight_dict["facility_area"])
        total_score+=area_score
        print("area_score=",area_score)
    #calculating window weights
    if room_values["window"]>=4:
        window_score=weight_dict["facility_window"]
        total_score+=weight_dict["facility_window"]
        print("window_score=",window_score)
    else:
        window_score=weight_dict["facility_window"]-(((4-room_values["window"])/4)*weight_dict["facility_window"])
        total_score+=window_score
        print("window_score=",window_score)
    #calculating outlet weights
    if (room_values["outlet"]>=room_values["student"]):
        outlet_score=weight_dict["facility_outlet"]
        total_score+=outlet_score
        print("outlet_score=",outlet_score)
    else:
        outlet_score=weight_dict["facility_outlet"]-(((room_values["student"]-room_values["outlet"])/room_values["student"])*weight_dict["facility_outlet"])
        total_score+=outlet_score
        print("outlet_score=",outlet_score)
    
    print("total score=",total_score)
    





#mcdm_func({"a": 1, "b":40})
'''print("enter clean value:")
clean1=int(input())
print("enter temp value:")
temp1=int(input())
print("enter humidity value:")
humid1=int(input())
print("enter computer value:")
comp1=int(input())
print("enter student value:")
stu1=int(input())
print("enter wifi value:")
wifi1=int(input())
print("enter area value:")
area1=int(input())
print("enter window value:")
win1=int(input())
print("enter outlet value:")
out1=int(input())
'''
#mcdm_func({},{"clean":clean1,"temp":temp1,"humidity":humid1,"computer":comp1,"student":stu1,"wifi":wifi1,"area":area1,"window":win1,"outlet":out1})
client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/aip_building?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)

db = client.aip_building
coll = db.aip_rooms
coll.find_one({"name":"room2"})
print(coll.find_one({"name":"room2"}))