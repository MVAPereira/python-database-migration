from bacteria_struct import BacteriaStruct


uri = "mongodb://localhost:27017"
database = "pathogensDB2"

bacteria_struct = BacteriaStruct(uri, database)

bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Bacillus", "Bacillus cereus")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Campy", "Campylobacter")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Clostridium", "Clostridium perfringens")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Listeria", "Listeria monocytogenes")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Salmonella", "Salmonella")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Staphy", "Staphylococcus aureus")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "STEC", "Shiga toxin-producing Escherichia coli")
bacteria_struct.update_key_collection("5f3160623d418525e0385fa8", "Yersinia", "Yersinia enterocolitica")

