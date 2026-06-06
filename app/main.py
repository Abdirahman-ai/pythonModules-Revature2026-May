from models.airfryer import Airfryer

# Skipping fry() and set_tempearture() - nothign new here

fryer = Airfryer()
print(fryer.fry())


print(fryer.set_temperature(80))
try:
    print(fryer.set_temperature(200))
except ValueError as e:
    print(f"Error: {e}")


print(fryer.register_user("FryGuy"))
try:
    print(fryer.register_user("iLikeJavaScript"))
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("will always run")

print(fryer.calculate_tip(5))
print(fryer.calculate_tip(100))

# Invalid weight

try:
    fryer.calculate_tip(-5)
except ValueError as e:
    print(f"Error: {e}")
    print("Please dont put negative weight in the air fryer")


print(fryer.calculate_tip(50))


