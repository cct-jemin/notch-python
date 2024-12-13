from app.config.v2ReportFieldsConfig import fieldsConfig
energyFuelsFields = fieldsConfig['energyFuelsFields']
employeeTravelFields = fieldsConfig['employeeTravelFields']
businessTravelFields = fieldsConfig['businessTravelFields']
detailedCarbonFields = fieldsConfig['detailedCarbonFields']

scopeConfig = {
    "1" :{
        "label":'Scope 1 - Direct Emissions',
        "companyFacilities":{
            "label":"Company Facilities",
            "attributeSubCategory":{
                "gas":{
                    "label":"Gas",
                    "section":"energyFuels",
                    "type":{
                        'gas':energyFuelsFields['gas'],
                        'greenGas':energyFuelsFields['greenGas']
                    }
                },
                "fuels":{
                    "label":"Fuels",
                    "section":"energyFuels",
                    "type":{
                        'fuelsGaseous':energyFuelsFields['fuelsGaseous'],
                        'fuelsLiquid':energyFuelsFields['fuelsLiquid'],
                        'bioFuels':energyFuelsFields['bioFuels'],
                        'biomass':energyFuelsFields['biomass'],
                        'biogas':energyFuelsFields['biogas']
                    }
                },
                "fugitiveEmissions":{
                    "label":"Fugitive Emissions",
                    "section":"energyFuels",
                    "type":{
                        'fugitiveEmissions':energyFuelsFields['fugitiveEmissions']
                    }
                }
            }
        },
        "companyVehicles":{
            "label":"Company Vehicles",
            "attributeSubCategory":{
                "cars":{
                    "label":"Cars",
                    "section":"businessTravel",
                    "type":{
                        'carPetrol':businessTravelFields['carPetrol'],
                        'carDiesel':businessTravelFields['carDiesel'],
                        'carAverage':businessTravelFields['carAverage'],
                        'carHybrid':businessTravelFields['carHybrid'],
                        'carElectric':businessTravelFields['carElectric']
                    }
                },
                "vans":{
                    "label":"Vans",
                    "section":"businessTravel",
                    "type" : {
                        'vans' : businessTravelFields['vans'],
                      }
                },
                "trucks":{
                    "label":"Trucks",
                    "section":"businessTravel",
                    "type":{
                        'hgv':businessTravelFields['hgv'],
                        'hgvRefrigerated':businessTravelFields['hgvRefrigerated']
                    }
                },
            }
        }
    },
    "2":{
        "label":'Scope 2 - Energy Indirect Emissions',
        "purchasedEnergy":{
            "label":"Purchased Energy",
            "attributeSubCategory":{
                "electricity":{
                    "label":"Electricity",
                    "section":"energyFuels",
                    "type":{
                        'electricity':energyFuelsFields['electricity']
                    }
                },
                "greenElectricity":{
                    "label":"Green Electricity",
                    "section":"energyFuels",
                    "type":{
                        'greenElectricity':energyFuelsFields['greenElectricity']
                    }
                },
                "gas":{
                    "label":"Gas",
                    "section":"energyFuels",
                    "type":{
                        'gas':energyFuelsFields['gas'],
                        'greenGas':energyFuelsFields['greenGas']
                    }
                },
                "steam":{
                    "label":"Steam",
                    "section":"energyFuels",
                    "type":{
                        'steam':energyFuelsFields['steam']
                    }
                },
                "fuels":{
                    "label":"Fuels",
                    "section":"energyFuels",
                    "type":{
                        'fuelsGaseous':energyFuelsFields['fuelsGaseous'],
                        'fuelsLiquid':energyFuelsFields['fuelsLiquid'],
                        'bioFuels':energyFuelsFields['bioFuels'],
                        'biomass':energyFuelsFields['biomass'],
                        'biogas':energyFuelsFields['biogas']
                    }
                },
                "fugitiveEmissions":{
                    "label":"Fugitive Emissions",
                    "section":"energyFuels",
                    "type":{
                        'fugitiveEmissions':energyFuelsFields['fugitiveEmissions']
                    }
                },
                "cars":{
                    "label":"Cars",
                    "section":"businessTravel",
                    "type":{
                        'carElectric':businessTravelFields['carElectric']
                    }
                },
            }
        },
        "generatedElectricity":{
            "label":"Generated Electricity",
            "attributeSubCategory":{
                "greenElectricity":{
                    "label":"Green Electricity",
                    "section":"energyFuels",
                    "type":{
                        'greenElectricity':energyFuelsFields['greenElectricity'],
                    }
                },
                "cars":{
                    "label":"Cars",
                    "section":"businessTravel",
                    "type":{
                        'carElectric':businessTravelFields['carElectric']
                    }
                },
            }
        }
    },
    "3":{
        "label":'Scope 3 - Other Indirect Emissions',
        "purchasedGoodsAndServices": {
            "label":"Purchased Goods & Services",
            "attributeSubCategory":{
                "waterSupply":{
                    "label":"Water Supply",
                    "section":"detailedCarbon",
                    "type":{
                        'waterSupply':detailedCarbonFields['waterSupply'],

                    }
                },
                "materialUsed":{
                    "label":"Material Used",
                    "section":"detailedCarbon",
                    "type":{
                        'materialUsed':detailedCarbonFields['materialUsed'],

                    }
                },
                "custom" : {
                    "label":"any custom sub-category",
                    "unit" : ['liters','kg']
                }
            },

        },
        "capitalGoods":{
            "label":"Capital Goods",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "fuelEnergyActivities":{
            "label":"Fuel & Energy Related Activities",
            "attributeSubCategory":{
                "electricity":{
                    "label":"Electricity",
                    "section":"energyFuels",
                    "type":{
                        'electricity':energyFuelsFields['electricity'],
                    }
                },
                "greenElectricity":{
                    "label":"Green Electricity",
                    "section":"energyFuels",
                    "type":{
                        'greenElectricity':energyFuelsFields['greenElectricity']
                    }
                },
                "steam":{
                    "label":"Steam",
                    "section":"energyFuels",
                    "type":{
                        'steam':energyFuelsFields['steam']
                    }
                },
                "gas":{
                    "label":"Gas",
                    "section":"energyFuels",
                    "type":{
                        'gas':energyFuelsFields['gas'],
                        'greenGas':energyFuelsFields['greenGas']
                    }
                },
                "fuels":{
                    "label":"Fuels",
                    "section":"energyFuels",
                    "type":{
                        'fuelsGaseous':energyFuelsFields['fuelsGaseous'],
                        'fuelsLiquid':energyFuelsFields['fuelsLiquid'],
                        'bioFuels':energyFuelsFields['bioFuels'],
                        'biomass':energyFuelsFields['biomass'],
                        'biogas':energyFuelsFields['biogas']
                    }
                },
                "fugitiveEmissions":{
                    "label":"Fugitive Emissions",
                    "section":"energyFuels",
                    "type":{
                        'fugitiveEmissions':energyFuelsFields['fugitiveEmissions']
                    }
                },
                "custom" : {
                    "label":"any custom sub-category",
                    "unit" : ['kg','tonnes']
                }
            },
        },
        "upstreamTransportationDistribution":{
            "label":"Upstream Transportation & Distribution",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "wasteGeneratedFromOperations":{
            "label":"Waste Generated From Operations",
            "attributeSubCategory":{
                "wasteDisposal":{
                    "label":"Waste Disposal",
                    "section":"detailedCarbon",
                    "type":{
                        'wasteDisposal':detailedCarbonFields['wasteDisposal'],

                    }
                },
                "waterTreatment":{
                    "label":"Water Treatment",
                    "section":"detailedCarbon",
                    "type":{
                        'waterTreatment':detailedCarbonFields['waterTreatment'],

                    }
                },
                "custom" : {
                    "label":"any custom sub-category",
                    "unit" : ['kg','tonnes']
                }

            }

        },
        "businessTravel":{
            "label":"Business Travel",
            "attributeSubCategory":{
                "cars":{
                    "label":"Cars",
                    "section":"businessTravel",
                    "type":{
                        'carPetrol':businessTravelFields['carPetrol'],
                        'carDiesel':businessTravelFields['carDiesel'],
                        'carAverage':businessTravelFields['carAverage'],
                        'carHybrid':businessTravelFields['carHybrid'],
                        'carElectric':businessTravelFields['carElectric'],
                    }
                },
                "rail":{
                    "label":"Rail",
                    "section":"businessTravel",
                    "type" : {
                        'rail':businessTravelFields['rail'],
                    }
                },
                "plane":{
                    "label":"Plane",
                    "section":"businessTravel",
                    "type" : {
                        'plane':businessTravelFields['plane'],
                    },
                },
                "taxis":{
                    "label":"Taxis",
                    "section":"businessTravel",
                    "type" : {
                        'taxis':businessTravelFields['taxis'],
                    }
                },
                "vans":{
                    "label":"Vans",
                    "section":"businessTravel",
                    "type" : {
                        'vans':businessTravelFields['vans'],
                    }
                },
                "hgv":{
                    "label":"HGV",
                    "section":"businessTravel",
                    "type" : {
                        'hgv':businessTravelFields['hgv'],
                    }
                },
                "hgvRefrigerated":{
                    "label":"HGV - Refrigerated",
                    "section":"businessTravel",
                    "type" : {
                        'hgvRefrigerated':businessTravelFields['hgvRefrigerated'],
                    }
                },
                "ferry":{
                    "label":"Ferry",
                    "section":"businessTravel",
                    "type" : {
                        'ferry':businessTravelFields['ferry'],
                    }
                },
                "motorbike":{
                    "label":"Motorbike",
                    "section":"businessTravel",
                    "type" : {
                        'motorbike':businessTravelFields['motorbike'],
                    }
                },
                "bus":{
                    "label":"Bus",
                    "section":"businessTravel",
                    "type" : {
                        'bus':businessTravelFields['bus'],
                    }
                },
                "walking":{
                    "label":"Walking",
                    "section":"businessTravel",
                    "type" : {
                        'walking':businessTravelFields['walking'],
                    }
                },
                "cycling":{
                    "label":"Cycling",
                    "section":"businessTravel",
                    "type" : {
                        'cycling':businessTravelFields['cycling'],
                    }
                },
                "custom" : {
                    "label":"any custom sub-category",
                    "unit" : ['kg','tonnes']
                }
            }
        },
        "employeeTravel":{
            "label":"Employee Commuting",
            "attributeSubCategory":{
                "cars":{
                    "label":"Cars",
                    "section":"employeeTravel",
                    "type":{
                        'carPetrol':employeeTravelFields['carPetrol'],
                        'carDiesel':employeeTravelFields['carDiesel'],
                        'carAverage':employeeTravelFields['carAverage'],
                        'carHybrid':employeeTravelFields['carHybrid'],
                        'carElectric':employeeTravelFields['carElectric'],
                    }
                },
                "bus":{
                    "label":"Bus",
                    "section":"employeeTravel",
                    "type" : {
                        'bus':employeeTravelFields['bus'],
                    }
                },
                "rail":{
                    "label":"Rail",
                    "section":"employeeTravel",
                    "type" : {
                        'rail':employeeTravelFields['rail'],
                    }
                },
                "taxis":{
                    "label":"Taxis",
                    "section":"employeeTravel",
                    "type" : {
                        'taxis':employeeTravelFields['taxis'],
                    }
                },
                "ferry":{
                    "label":"Ferry",
                    "section":"employeeTravel",
                    "type" : {
                        'ferry':employeeTravelFields['ferry'],
                    }
                },
                "motorbike":{
                    "label":"Motorbike",
                    "section":"employeeTravel",
                    "type" : {
                        'motorbike':employeeTravelFields['motorbike'],
                    }
                },
                "plane":{
                    "label":"Plane",
                    "section":"employeeTravel",
                    "type" : {
                        'plane':employeeTravelFields['plane'],
                    },
                },
                "walking":{
                    "label":"Walking",
                    "section":"employeeTravel",
                    "type" : {
                        'walking':employeeTravelFields['walking'],
                    }
                },
                "cycling":{
                    "label":"Cycling",
                    "section":"employeeTravel",
                    "type" : {
                        'cycling':employeeTravelFields['cycling'],
                    }
                },
                "custom" : {
                    "label":"any custom sub-category",
                    "unit" : ['kg','tonnes']
                }
            }
        },
        "upstreamLeasedAssets":{
            "label":"Upstream Leased Assets",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "downstreamTransportation":{
            "label":"Downstream Transportation & Distribution",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "processingOfSoldProducts":{
            "label":"Processing of Sold Products",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "useOfSoldProducts":{
            "label":"Use of Sold Products",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "endoflifeTreatmentOfSoldProducts":{
            "label":"End-of-Life Treatment of Sold Products",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "downstreamLeasedAssets":{
            "label":"Downstream Leased Assets",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "franchises":{
            "label":"Franchises",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
        "investments":{
            "label":"Investments",
            "attributeSubCategory":"userdefine",
            "unit":['liters','kg']
        },
    }
}









