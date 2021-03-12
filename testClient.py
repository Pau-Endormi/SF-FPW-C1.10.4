from main import Client, Volunteer

client1 = Client()
client1.set_name("Paul")
client1.set_money(1000)

print(client1)

volunteer1 = Volunteer()
volunteer1.set_name("Julia")
volunteer1.set_city("Saint Petersburg")
volunteer1.set_status("Mentor")

print(volunteer1)
print(volunteer1.get_name())
