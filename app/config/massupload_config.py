EXTENSION = {".xlsx"}
FILE_UPLOAD_PATH = "app/files/"

labelIgnore = ['category','custom']
sectionVal = {
    "section_1": "Company Information",
    "section_2": "Employee Commuting",
    "section_3": "Business Travel",
    "section_4": "Energy",
    "section_5": "Fuels",
    "section_6": "Detailed Carbon",
}
monthArr = ['January','February','March','April','May','June','July','August','September','October','November','December']
carElectricLabel = "car - electric",
CAR_ELECTRIC_OBJECT = {
      "kwh": {
          "fuelType": "electricity",
          "fuelSubType": "grid",
          "unit":"kwh",
      },
      "kwh - green (grid)": {
          "fuelType": "greenElectricity",
          "fuelSubType": "grid",
          "unit":"kwh - Green (Grid)",
      },
      "kwh - green (generated)": {
          "fuelType": "greenElectricity",
          "fuelSubType": "nonGrid",
          "unit":"kwh - Green (Generated)",
      }
},
PURCHASE_ENERGY_LABEL = "purchasedEnergy",
GENERATED_ENERGY_LABEL = 'generatedElectricity',
CAR_ELECTRIC_GENERATED_ELECTRICITY_UNIT  = 'kwh - green (generated)'