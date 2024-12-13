fieldsConfig = {
   "allCategoryList":[
      "employeeTravel",
      "businessTravel"
   ],
   "allCarbonKeysList":[
      "employeeTravel",
      "businessTravel",
      "energyFuels",
      "detailedCarbon"
   ],
   "allCarbonTDKeysList":[
      "businessTravel",
      "energyFuels"
   ],
   "allFieldsSummaryConfig":{
      "carTravel":{
         "label":"Car Travel",
         "unit":"miles"
      },
      "carbonDirectCarbon":{
         "label":"Direct Carbon"
      },
      "carbonElectricity":{
         "label":"Electricity",
         "unit":"kwh"
      },
      "carbonGas":{
         "label":"Gas",
         "unit":"kwh"
      },
      "carbonGreenElectricity":{
         "label":"Green Electricity",
         "unit":"kwh"
      },
      "carbonGreenGas":{
         "label":"Green Gas",
         "unit":"kwh"
      },
      "carbonSteam":{
         "label":"Steam",
         "unit":"kwh"
      },
      "compEmployees":{
         "label":"Employees"
      },
      "compOfficeSpace":{
         "label":"Office Space",
         "unit":"m2"
      },
      "compProductionSpace":{
         "label":"Production Space",
         "unit":"m2"
      },
      "compPupils":{
         "label":"Pupils"
      },
      "compTurnover":{
         "label":"Turnover",
         "prefix":"£"
      },
      "electricity":{
         "label":"Electricity",
         "unit":"kwh"
      },
      "gas":{
         "label":"Gas",
         "unit":"kwh"
      },
      "greenTravel":{
         "label":"Green Travel",
         "unit":"miles"
      },
      "hgvTravel":{
         "label":"HGV/Van Travel",
         "unit":"miles"
      },
      "otherTravel":{
         "label":"Other Travel",
         "unit":"miles"
      },
      "carPetrol":{
         "label":"Car - Petrol"
      }
   },
   "transmissionAndDistribution":{
      "unit":[
         "kwh"
      ]
   },
   "LABEL_TRANSMISSION_ELECTRICITY":{
      "unit":[
         "kwh"
      ]
   },
   "LABEL_TRANSMISSION_CAR_ELECTRIC":{
      "unit":[
         "km",
         "miles",
         "kwh",
         "kwh - Green (Grid)"
      ]
   },
   "CAR_ELECTRIC_GENERATED_ELECTRICITY_UNIT":{
      "unit":[
         "kwh - Green (Generated)"
      ]
   },
   "companyInfoFieldsList":[
      "compEmployees",
      "compOfficeSpace",
      "compProductionSpace",
      "compPupils",
      "compTurnover"
   ],
   "businessTravelFieldsList":[
      "carPetrol",
      "carAverage",
      "carDiesel",
      "carHybrid",
      "carElectric",
      "vans",
      "hgv",
      "hgvRefrigerated",
      "taxis",
      "bus",
      "rail",
      "ferry",
      "motorbike",
      "cycling",
      "walking",
      "plane",
      "iceCar",
      "greenCar",
      "vanTrucks",
      "otherTravel"
   ],
   "employeeTravelFieldsList":[
      "carPetrol",
      "carAverage",
      "carDiesel",
      "carHybrid",
      "carElectric",
      "taxis",
      "bus",
      "plane",
      "rail",
      "ferry",
      "motorbike",
      "cycling",
      "walking"
   ],
   "energyFuelsFieldsList":[
      "electricity",
      "gas",
      "greenElectricity",
      "greenGas",
      "fuelsLiquid",
      "bioFuels",
      "fuelsGaseous",
      "biomass",
      "biogas",
      "fugitiveEmissions",
      "steam"
   ],
   "detailedCarbonFieldsList":[
      "waterSupply",
      "waterTreatment",
      "materialUsed",
      "wasteDisposal"
   ],
   "energyFields":[
      "electricity",
      "greenElectricity",
      "gas",
      "greenGas",
      "steam"
   ],
   "meterEnergyFields":[
      "electricity",
      "greenElectricity",
      "gas",
      "greenGas"
   ],
   "meterElectricityFields":[
      "electricity",
      "greenElectricity"
   ],
   "meterGasFields":[
      "gas",
      "greenGas"
   ],
   "energyLocationFields":[
      "electricity",
      "greenElectricity"
   ],
   "totalEnergyFields":[
      "totalelectricity",
      "totalgreenElectricity",
      "totalgas",
      "totalgreenGas"
   ],
   "energyFuelsFields":{
      "electricity":{
         "label":"Electricity",
         "unit":[
            "kwh"
         ],
         "options":{
            "grid":{
               "unit":[
                  "kwh"
               ],
               "label":"Grid"
            },
            "nonGrid":{
               "unit":[
                  "kwh"
               ],
               "label":"Non-grid"
            }
         }
      },
      "greenElectricity":{
         "label":"Green Electricity",
         "unit":[
            "kwh"
         ],
         "options":{
            "grid":{
               "unit":[
                  "kwh"
               ],
               "label":"Grid",
               "source":[
                  "non-generated"
               ]
            },
            "pv":{
               "unit":[
                  "kwh"
               ],
               "label":"PV",
               "source":[
                  "generated"
               ]
            },
            "wind":{
               "unit":[
                  "kwh"
               ],
               "label":"Wind",
               "source":[
                  "generated"
               ]
            },
            "bio":{
               "unit":[
                  "kwh"
               ],
               "label":"Bio",
               "source":[
                  "generated"
               ]
            },
            "other":{
               "unit":[
                  "kwh"
               ],
               "label":"Other",
               "source":[
                  "generated"
               ]
            }
         }
      },
      "gas":{
         "carbonValue":0.18385,
         "label":"Gas",
         "unit":[
            "kwh"
         ],
         "options":{
            
         }
      },
      "greenGas":{
         "carbonValue":0.00021,
         "label":"Green Gas",
         "unit":[
            "kwh"
         ],
         "options":{
            
         }
      },
      "fuelsLiquid":{
         "label":"Fuels Liquid",
         "sheetLabel":"Fuels - Liquid",
         "optionsPlaceholder":"Fuel Type",
         "unit":[
            "tonnes",
            "litres"
         ],
         "options":{
            "aviationSpirit":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Aviation Spirit"
            },
            "dieselBioFuelBlend":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Diesel (Bio Fuel Blend)",
               "sheetLabel":"Diesel (Bio-Fuel Blend)"
            },
            "dieselMineralBlend":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Diesel (Mineral Blend)"
            },
            "fuelOil":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Fuel Oil"
            },
            "gasOil":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Gas Oil"
            },
            "lubricants":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Lubricants"
            },
            "petrolBioFuelBlend":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Petrol (Bio Fuel Blend)",
               "sheetLabel":"Petrol (Bio-Fuel Blend)"
            },
            "petrolMineralBlend":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Petrol (Mineral Blend)"
            },
            "wasteOils":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Waste Oils"
            },
            "custom":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Custom"
            }
         }
      },
      "bioFuels":{
         "label":"Bio Fuels",
         "sheetLabel":"Bio - Fuels",
         "optionsPlaceholder":"Fuel Type",
         "unit":[
            "tonnes",
            "litres"
         ],
         "options":{
            "bioEthanol":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Ethanol",
               "sheetLabel":"Bio-ethanol"
            },
            "bioDieselMe":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Diesel ME",
               "sheetLabel":"Bio-diesel ME"
            },
            "bioMethane":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Methane",
               "sheetLabel":"Bio-Methane"
            },
            "bioDieselMeUco":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Diesel ME (UCO)",
               "sheetLabel":"Bio-diesel ME (UCO)"
            },
            "bioDieselMeTallow":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Diesel ME (Tallow)",
               "sheetLabel":"Bio-diesel ME (Tallow)"
            },
            "bioDieselHvo":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Diesel HVO",
               "sheetLabel":"Bio-diesel HVO"
            },
            "bioPropane":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Propane",
               "sheetLabel":"Bio-propane"
            },
            "bioPetrol":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Bio Petrol",
               "sheetLabel":"Bio-petrol"
            },
            "renewablePetrol":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Renewable Petrol"
            },
            "custom":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Custom"
            }
         }
      },
      "fuelsGaseous":{
         "label":"Fuels Gaseous",
         "sheetLabel":"Fuels - Gaseous",
         "optionsPlaceholder":"Fuel Type",
         "unit":[
            "tonnes",
            "litres"
         ],
         "options":{
            "butane":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Butane"
            },
            "cng":{
               "label":"CNG",
               "unit":[
                  "tonnes"
               ]
            },
            "lng":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"LNG"
            },
            "lpg":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"LPG"
            },
            "naturalGas":{
               "unit":[
                  "kwh"
               ],
               "label":"Natural Gas"
            },
            "naturalGasMineralBlend":{
               "unit":[
                  "kwh"
               ],
               "label":"Natural Gas (Mineral Blend)"
            },
            "propane":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Propane"
            },
            "custom":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Custom"
            }
         }
      },
      "biomass":{
         "label":"Biomass",
         "optionsPlaceholder":"Fuel Type",
         "unit":[
            "tonnes",
            "litres"
         ],
         "options":{
            "woodLogs":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Wood Logs"
            },
            "woodChips":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Wood Chips"
            },
            "woodPellets":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Wood Pellets"
            },
            "grassStraw":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Grass/Straw"
            },
            "custom":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Custom"
            }
         }
      },
      "biogas":{
         "label":"Biogas",
         "optionsPlaceholder":"Fuel Type",
         "unit":[
            "tonnes",
            "litres"
         ],
         "options":{
            "biogas":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Biogas"
            },
            "landfillGas":{
               "label":"Landfill Gas",
               "unit":[
                  "tonnes",
                  "litres"
               ]
            },
            "custom":{
               "unit":[
                  "tonnes",
                  "litres"
               ],
               "label":"Custom"
            }
         }
      },
      "fugitiveEmissions":{
         "label":"Fugitive Emissions",
         "optionsPlaceholder":"Fuel Type",
         "unit":[
            "kg"
         ],
         "options":{
            "r404a":{
               "unit":[
                  "kg"
               ],
               "label":"R404A"
            },
            "r407a":{
               "unit":[
                  "kg"
               ],
               "label":"R407A"
            },
            "r407c":{
               "unit":[
                  "kg"
               ],
               "label":"R407C"
            },
            "r407f":{
               "unit":[
                  "kg"
               ],
               "label":"R407F"
            },
            "r408a":{
               "unit":[
                  "kg"
               ],
               "label":"R408A"
            },
            "r410a":{
               "unit":[
                  "kg"
               ],
               "label":"R410A"
            },
            "r507a":{
               "unit":[
                  "kg"
               ],
               "label":"R507A"
            },
            "r508b":{
               "unit":[
                  "kg"
               ],
               "label":"R508B"
            },
            "r403a":{
               "unit":[
                  "kg"
               ],
               "label":"R403A"
            },
            "hfc32r32":{
               "unit":[
                  "kg"
               ],
               "label":"HFC32 (R32)"
            },
            "custom":{
               "unit":[
                  "kg"
               ],
               "label":"Custom"
            }
         }
      },
      "steam":{
         "unit":[
            "tonnes"
         ],
         "label":"Steam"
      }
   },
   "companyInfoFields":{
      "compEmployees":{
         "label":"Employees"
      },
      "compOfficeSpace":{
         "label":"Office Space",
         "unit":"m2"
      },
      "compProductionSpace":{
         "label":"Production Space",
         "unit":"m2"
      },
      "compPupils":{
         "label":"Pupils"
      },
      "compTurnover":{
         "label":"Turnover",
         "unit":"£"
      }
   },
   "carOffTheRoadYearEquivalent":3420,
   "cowsPerYearEquivalent":2300,
   "homesPerYearEquivalent":3400,
   "treesPerYearEquivalent":10,
   "planePerYearEquivalent":1.23,
   "employeeTravelFields":{
      "carPetrol":{
         "label":"Car Petrol",
         "sheetLabel":"Car - Petrol",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.23877,
                  "litres":2.31467
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.30029,
                  "litres":2.31467
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.28052,
                  "litres":2.31467
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.44752,
                  "litres":2.31467
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carAverage":{
         "label":"Car Average",
         "sheetLabel":"Car - Average",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.23877,
                  "litres":2.31467
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.30029,
                  "litres":2.31467
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.28052,
                  "litres":2.31467
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.44752,
                  "litres":2.31467
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carDiesel":{
         "label":"Car Diesel",
         "sheetLabel":"Car - Diesel",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.22082,
                  "litres":2.68787
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.26775,
                  "litres":2.68787
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.32863,
                  "litres":2.68787
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.27108,
                  "litres":2.68787
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carHybrid":{
         "label":"Car Hybrid",
         "sheetLabel":"Car - Hybrid",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.16538,
                  "litres":0.16538
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.17216,
                  "litres":0.17216
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.23304,
                  "litres":0.23304
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.18601,
                  "litres":0.18601
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carElectric":{
         "label":"Car Electric",
         "sheetLabel":"Car - Electric",
         "unit":[
            "miles",
            "km",
            "kwh",
            "kwh - Green (Grid)",
            "kwh - Green (Generated)"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.03597
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.1128
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.1218
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.1126
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "taxis":{
         "label":"Taxis",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "regular":{
               "carbonValue":{
                  "km":0.20369
               },
               "label":"Regular"
            },
            "black":{
               "carbonValue":{
                  "km":0.31191
               },
               "label":"Black"
            }
         }
      },
      "bus":{
         "label":"Bus",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "localBus":{
               "carbonValue":{
                  "km":0.1195
               },
               "label":"Local Bus"
            },
            "localBusLondon":{
               "carbonValue":{
                  "km":0.07856
               },
               "label":"Local Bus (London)"
            },
            "average":{
               "carbonValue":{
                  "km":0.10312
               },
               "label":"Average"
            }
         }
      },
      "rail":{
         "label":"Rail",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Rail Type",
         "options":{
            "national":{
               "carbonValue":{
                  "km":0.03694
               },
               "label":"National"
            },
            "international":{
               "carbonValue":{
                  "km":0.00497
               },
               "label":"International"
            },
            "lightTram":{
               "carbonValue":{
                  "km":0.02991
               },
               "label":"Light/Tram"
            },
            "londonUnderground":{
               "carbonValue":{
                  "km":0.0275
               },
               "label":"London Underground"
            }
         }
      },
      "plane":{
         "label":"Plane",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Plane Type",
         "options":{
            "domestic":{
               "average":{
                  "carbonValue":{
                     "km":0.2443
                  },
                  "label":"Average"
               },
               "label":"Domestic"
            },
            "economy":{
               "average":{
                  "carbonValue":{
                     "km":0.2443
                  },
                  "label":"Average"
               },
               "label":"Economy"
            },
            "business":{
               "average":{
                  "carbonValue":{
                     "km":0.2443
                  },
                  "label":"Average"
               },
               "label":"Business"
            },
            "shortHaul":{
               "average":{
                  "carbonValue":{
                     "km":0.15553
                  },
                  "label":"Average"
               },
               "economy":{
                  "carbonValue":{
                     "km":0.15298
                  },
                  "label":"Economy"
               },
               "business":{
                  "carbonValue":{
                     "km":0.22947
                  },
                  "label":"Business"
               },
               "label":"Short Haul"
            },
            "longHaul":{
               "average":{
                  "carbonValue":{
                     "km":0.19085
                  },
                  "label":"Average"
               },
               "economy":{
                  "carbonValue":{
                     "km":0.14615
                  },
                  "label":"Economy"
               },
               "premiumEconomy":{
                  "carbonValue":{
                     "km":0.23385
                  },
                  "label":"Premium economy"
               },
               "business":{
                  "carbonValue":{
                     "km":0.42385
                  },
                  "label":"Business"
               },
               "first":{
                  "carbonValue":{
                     "km":0.58462
                  },
                  "label":"First"
               },
               "label":"Long Haul"
            },
            "international":{
               "average":{
                  "carbonValue":{
                     "km":0.18181
                  },
                  "label":"Average"
               },
               "economy":{
                  "carbonValue":{
                     "km":0.139245
                  },
                  "label":"Economy"
               },
               "premiumEconomy":{
                  "carbonValue":{
                     "km":0.22278
                  },
                  "label":"Premium economy"
               },
               "business":{
                  "carbonValue":{
                     "km":0.40379
                  },
                  "label":"Business"
               },
               "first":{
                  "carbonValue":{
                     "km":0.55695
                  },
                  "label":"First"
               },
               "label":"International"
            }
         }
      },
      "ferry":{
         "label":"Ferry",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Ferry Type",
         "options":{
            "footPassenger":{
               "carbonValue":{
                  "km":0.01874
               },
               "label":"Foot Passenger"
            },
            "carPassenger":{
               "carbonValue":{
                  "km":0.12952
               },
               "label":"Car Passenger"
            }
         }
      },
      "motorbike":{
         "label":"Motorbike",
         "unit":[
            "miles",
            "km"
         ],
         "carbonValue":{
            "miles":0.18245
         }
      },
      "cycling":{
         "label":"Cycling",
         "unit":[
            "miles",
            "km"
         ],
         "carbonValue":{
            "miles":0
         }
      },
      "walking":{
         "label":"Walking",
         "unit":[
            "miles",
            "km"
         ],
         "carbonValue":{
            "miles":0
         }
      }
   },
   "businessTravelFields":{
      "carPetrol":{
         "label":"Car Petrol",
         "sheetLabel":"Car - Petrol",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.23877,
                  "litres":2.31467
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.30029,
                  "litres":2.31467
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.396245,
                  "litres":2.31467
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.28502,
                  "litres":2.31467
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carAverage":{
         "label":"Car Average",
         "sheetLabel":"Car - Average",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.23877,
                  "litres":2.31467
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.30029,
                  "litres":2.31467
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.396245,
                  "litres":2.31467
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.28502,
                  "litres":2.31467
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carDiesel":{
         "label":"Car Diesel",
         "sheetLabel":"Car - Diesel",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.22082,
                  "litres":2.68787
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.26775,
                  "litres":2.68787
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.32863,
                  "litres":2.68787
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.27108,
                  "litres":2.68787
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carHybrid":{
         "label":"Car Hybrid",
         "sheetLabel":"Car - Hybrid",
         "unit":[
            "miles",
            "litres",
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.16538,
                  "litres":0.16538
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.17216,
                  "litres":0.17216
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.23304,
                  "litres":0.23304
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.18601,
                  "litres":0.18601
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "carElectric":{
         "label":"Car Electric",
         "sheetLabel":"Car - Electric",
         "unit":[
            "miles",
            "km",
            "kwh",
            "kwh - Green (Grid)",
            "kwh - Green (Generated)"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "carSmall":{
               "carbonValue":{
                  "miles":0.03597
               },
               "label":"Small Car",
               "sheetLabel":"Small"
            },
            "carMedium":{
               "carbonValue":{
                  "miles":0.1128
               },
               "label":"Medium Car",
               "sheetLabel":"Medium"
            },
            "carLarge":{
               "carbonValue":{
                  "miles":0.1218
               },
               "label":"Large Car",
               "sheetLabel":"Large"
            },
            "carAverage":{
               "carbonValue":{
                  "miles":0.1126
               },
               "label":"Average Car",
               "sheetLabel":"Average"
            }
         }
      },
      "vans":{
         "label":"Vans",
         "unit":[
            "litres",
            "miles",
            "km"
         ],
         "optionsPlaceholder":"Van Type",
         "options":{
            "class1":{
               "carbonValue":{
                  "miles":0.94,
                  "litres":2.68787
               },
               "label":"Class I",
               "sheetLabel":"Class 1"
            },
            "class2":{
               "carbonValue":{
                  "miles":1.19,
                  "litres":2.68787
               },
               "label":"Class II",
               "sheetLabel":"Class 2"
            },
            "class3":{
               "carbonValue":{
                  "miles":1.72,
                  "litres":2.68787
               },
               "label":"Class III",
               "sheetLabel":"Class 3"
            },
            "average":{
               "carbonValue":{
                  "miles":1.57,
                  "litres":2.68787
               },
               "label":"Average",
               "sheetLabel":"Average"
            }
         }
      },
      "hgv":{
         "label":"HGV",
         "unit":[
            "miles",
            "km",
            "litres"
         ],
         "optionsPlaceholder":"HGV Type",
         "options":{
            "rigid3575":{
               "carbonValue":{
                  "miles":0.77652
               },
               "label":"Rigid 3.5 - 7.5"
            },
            "rigid7517":{
               "carbonValue":{
                  "miles":0.94835
               },
               "label":"Rigid 7.5 - 17"
            },
            "rigid175":{
               "carbonValue":{
                  "miles":1.55192
               },
               "label":"Rigid > 17.5"
            },
            "average":{
               "carbonValue":{
                  "miles":1.28928
               },
               "label":"Average"
            }
         }
      },
      "hgvRefrigerated":{
         "label":"HGV Refrigerated",
         "sheetLabel":"HGV - Refrigerated",
         "unit":[
            "miles",
            "km",
            "litres"
         ],
         "optionsPlaceholder":"HGV Refrigerated Type",
         "options":{
            "rigid3575":{
               "carbonValue":{
                  "miles":0.92442
               },
               "label":"Rigid 3.5 - 7.5"
            },
            "rigid7517":{
               "carbonValue":{
                  "miles":1.12897
               },
               "label":"Rigid 7.5 - 17"
            },
            "rigid175":{
               "carbonValue":{
                  "miles":1.84749
               },
               "label":"Rigid > 17.5"
            },
            "average":{
               "carbonValue":{
                  "miles":1.53483
               },
               "label":"Average"
            }
         }
      },
      "taxis":{
         "label":"Taxis",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Car Type",
         "options":{
            "regular":{
               "carbonValue":{
                  "km":0.20369
               },
               "label":"Regular"
            },
            "black":{
               "carbonValue":{
                  "km":0.31191
               },
               "label":"Black"
            }
         }
      },
      "bus":{
         "label":"Bus",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Bus Type",
         "options":{
            "localBus":{
               "carbonValue":{
                  "km":0.1195
               },
               "label":"Local Bus"
            },
            "localBusLondon":{
               "carbonValue":{
                  "km":0.07856
               },
               "label":"Local Bus (London)"
            },
            "average":{
               "carbonValue":{
                  "km":0.10312
               },
               "label":"Average"
            }
         }
      },
      "rail":{
         "label":"Rail",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Rail Type",
         "options":{
            "national":{
               "carbonValue":{
                  "km":0.03694
               },
               "label":"National"
            },
            "international":{
               "carbonValue":{
                  "km":0.00497
               },
               "label":"International"
            },
            "lightTram":{
               "carbonValue":{
                  "km":0.02991
               },
               "label":"Light/Tram"
            },
            "londonUnderground":{
               "carbonValue":{
                  "km":0.0275
               },
               "label":"London Underground"
            }
         }
      },
      "ferry":{
         "label":"Ferry",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Ferry Type",
         "options":{
            "footPassenger":{
               "carbonValue":{
                  "km":0.01874
               },
               "label":"Foot Passenger"
            },
            "carPassenger":{
               "carbonValue":{
                  "km":0.12952
               },
               "label":"Car Passenger"
            }
         }
      },
      "motorbike":{
         "label":"Motorbike",
         "unit":[
            "miles",
            "km"
         ],
         "carbonValue":{
            "miles":0.18245
         }
      },
      "cycling":{
         "label":"Cycling",
         "unit":[
            "miles",
            "km"
         ],
         "carbonValue":{
            "miles":0
         }
      },
      "walking":{
         "label":"Walking",
         "unit":[
            "miles",
            "km"
         ],
         "carbonValue":{
            "miles":0
         }
      },
      "plane":{
         "label":"Plane",
         "unit":[
            "km"
         ],
         "optionsPlaceholder":"Plane Type",
         "options":{
            "domestic":{
               "average":{
                  "carbonValue":{
                     "km":0.2443
                  },
                  "label":"Average"
               },
               "label":"Domestic"
            },
            "shortHaul":{
               "average":{
                  "carbonValue":{
                     "km":0.15553
                  },
                  "label":"Average"
               },
               "economy":{
                  "carbonValue":{
                     "km":0.15298
                  },
                  "label":"Economy"
               },
               "business":{
                  "carbonValue":{
                     "km":0.22947
                  },
                  "label":"Business"
               },
               "label":"Short Haul"
            },
            "longHaul":{
               "average":{
                  "carbonValue":{
                     "km":0.19085
                  },
                  "label":"Average"
               },
               "economy":{
                  "carbonValue":{
                     "km":0.14615
                  },
                  "label":"Economy"
               },
               "premiumEconomy":{
                  "carbonValue":{
                     "km":0.23385
                  },
                  "label":"Premium economy"
               },
               "business":{
                  "carbonValue":{
                     "km":0.42385
                  },
                  "label":"Business"
               },
               "first":{
                  "carbonValue":{
                     "km":0.58462
                  },
                  "label":"First"
               },
               "label":"Long Haul"
            },
            "international":{
               "average":{
                  "carbonValue":{
                     "km":0.18181
                  },
                  "label":"Average"
               },
               "economy":{
                  "carbonValue":{
                     "km":0.139245
                  },
                  "label":"Economy"
               },
               "premiumEconomy":{
                  "carbonValue":{
                     "km":0.22278
                  },
                  "label":"Premium economy"
               },
               "business":{
                  "carbonValue":{
                     "km":0.40379
                  },
                  "label":"Business"
               },
               "first":{
                  "carbonValue":{
                     "km":0.55695
                  },
                  "label":"First"
               },
               "label":"International"
            }
         }
      },
      "iceCar":{
         "label":"ICE Cars",
         "options":{
            "carTravel":{
               "carSmall":{
                  "carbonValue":{
                     "miles":0.23802
                  },
                  "label":"Small"
               },
               "carMedium":{
                  "carbonValue":{
                     "miles":0.29202
                  },
                  "label":"Medium"
               },
               "carAverage":{
                  "carbonValue":{
                     "miles":0.28502
                  },
                  "label":"Average"
               },
               "carLarge":{
                  "carbonValue":{
                     "miles":0.396245
                  },
                  "label":"Large"
               },
               "label":"Car Travel"
            }
         },
         "unit":[
            "miles"
         ]
      },
      "greenCar":{
         "label":"Green Cars",
         "options":{
            "greenTravel":{
               "greenFullElectricAverage":{
                  "carbonValue":{
                     "miles":0.09612
                  },
                  "label":"Full Electric (Average Size)"
               },
               "greenHybridElectricAverage":{
                  "carbonValue":{
                     "miles":0.07115
                  },
                  "label":"Hybrid Electric (Average Size)"
               },
               "label":"Green Travel"
            }
         },
         "unit":[
            "miles"
         ]
      },
      "vanTrucks":{
         "label":"Vans/Trucks",
         "options":{
            "hgvTravel":{
               "hgvAverageVan":{
                  "carbonValue":{
                     "miles":0.40576
                  },
                  "label":"Average Van (upto 3.5 tonnes)"
               },
               "hgvRigidsDiesel":{
                  "carbonValue":{
                     "miles":1.28756
                  },
                  "label":"HGV Rigids (Diesel)"
               },
               "hgvRefrigeratedRigidsDiesel":{
                  "carbonValue":{
                     "miles":1.53294
                  },
                  "label":"HGV Refrigerated Rigids (Diesel)"
               },
               "label":"HGV Travel"
            }
         },
         "unit":[
            "miles"
         ]
      },
      "otherTravel":{
         "label":"Other Travel",
         "options":{
            "otherTravel":{
               "otherTrain":{
                  "carbonValue":{
                     "km":0.035995
                  },
                  "label":"Train"
               },
               "otherPlane":{
                  "carbonValue":{
                     "km":0.197413
                  },
                  "label":"Plane"
               },
               "label":"Other Travel"
            }
         },
         "unit":[
            "km"
         ]
      }
   },
   "detailedCarbonFields":{
      "waterSupply":{
         "carbonValue":0.2556,
         "label":"Water Supply",
         "unit":[
            "m3"
         ]
      },
      "waterTreatment":{
         "carbonValue":0.18385,
         "label":"Water Treatment",
         "unit":[
            "m3"
         ]
      },
      "materialUsed":{
         "label":"Material Used",
         "unit":[
            "tonnes"
         ],
         "optionsPlaceholder":"Material Used Type",
         "options":{
            "averageConstruction":{
               "carbonValue":{
                  "tonnes":0.23802
               },
               "label":"Average Construction"
            },
            "weeeMixed":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"WEEE Mixed"
            },
            "batteries":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Batteries"
            },
            "scrapMetal":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Scrap Metal"
            },
            "averagePlastics":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Average Plastics"
            },
            "paperBoardMixed":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Paper & Board Mixed"
            }
         }
      },
      "wasteDisposal":{
         "label":"Waste Disposal",
         "unit":[
            "tonnes"
         ],
         "optionsPlaceholder":"waste Dispoal Type",
         "options":{
            "averageConstruction":{
               "carbonValue":{
                  "tonnes":0.23802
               },
               "label":"Average Construction",
               "unit":[
                  "tonnes"
               ]
            },
            "household":{
               "carbonValue":{
                  "tonnes":0.23802
               },
               "label":"Household",
               "unit":[
                  "tonnes"
               ]
            },
            "commercialIndustrial":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Commercial & Industrial",
               "unit":[
                  "tonnes"
               ]
            },
            "weeeMixed":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"WEEE Mixed",
               "unit":[
                  "tonnes"
               ]
            },
            "scrapMetal":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Scrap Metal",
               "unit":[
                  "tonnes"
               ]
            },
            "averagePlastics":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Average Plastics",
               "unit":[
                  "tonnes"
               ]
            },
            "paperBoardMixed":{
               "carbonValue":{
                  "tonnes":0.23802,
                  "litres":0.23802
               },
               "label":"Paper & Board Mixed"
            }
         }
      }
   },
   "sectionLabel":{
      "companyInfo":"Intensity Metrics",
      "businessTravel":"Business Travel",
      "employeeTravel":"Employee Travel",
      "detailedCarbon":"Detailed Carbon",
      "energyFuels":"Energy Fuels",
      "totalEnergy":"Total Energy",
      "office":"Business Facility Energy",
      "home":"Working from Home Energy"
   },
   "commonLabel":{
      "massUpload":"massUpload"
   },
   "employeeTravelConfig":{
      "CAR":{
         "PETROL":{
            "label":"carPetrol",
            "SMALL":"carSmall",
            "MEDIUM":"carMedium",
            "LARGE":"carLarge",
            "AVERAGE":"carAverage"
         },
         "DIESEL":{
            "label":"carDiesel",
            "SMALL":"carSmall",
            "MEDIUM":"carMedium",
            "LARGE":"carLarge",
            "AVERAGE":"carAverage"
         },
         "HYBRID":{
            "label":"carHybrid",
            "SMALL":"carSmall",
            "MEDIUM":"carMedium",
            "LARGE":"carLarge",
            "AVERAGE":"carAverage"
         },
         "ELECTRIC":{
            "label":"carElectric",
            "SMALL":"carSmall",
            "MEDIUM":"carMedium",
            "LARGE":"carLarge",
            "AVERAGE":"carAverage"
         }
      },
      "LOCALBUS":{
         "label":"bus",
         "travelVehicle":"localBus"
      },
      "LONDONBUS":{
         "label":"bus",
         "travelVehicle":"localBusLondon"
      },
      "NATIONALRAIL":{
         "label":"rail",
         "travelVehicle":"national"
      },
      "LIGHTRAIL":{
         "label":"rail",
         "travelVehicle":"lightTram"
      },
      "UNDERGROUNDRAIL":{
         "label":"rail",
         "travelVehicle":"londonUnderground"
      },
      "FERRYCAR":{
         "label":"ferry",
         "travelVehicle":"carPassenger"
      },
      "FERRYFOOT":{
         "label":"ferry",
         "travelVehicle":"footPassenger"
      },
      "MOTORBIKE":{
         "label":"motorbike"
      },
      "WALKING":{
         "label":"walking"
      },
      "CYCLING":{
         "label":"cycling"
      }
   }
}