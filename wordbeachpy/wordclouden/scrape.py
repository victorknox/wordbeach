
"""# A) Corpus Collection

"""

import requests
from bs4 import BeautifulSoup

# Used bash script to get a list of titles
# ,"Scientific_method", Measurement","International_System_of_Units","Subatomic_particle","Electron","Neutron","Former_Photon","Proton","Former_Quantum_mechanics",Radioactive_decay","Space","Vacuum","Delisted_Thermodynamics","Heat","Temperature","Theory_of_relativity","Speed_of_light","Wave","Delisted_Physics","Energy","Time","Day","Year","Classical_mechanics","Electromagnetic_radiation","Light","Color","Optics","Delisted_Sound","Biology","Life","Delisted_Cell","Death","Suicide","Abiogenesis","Evolution","Mass","Momentum","Motion","Newton's_laws_of_motion","Human_evolution","Failed_candidate_Natural_selection","Force","Electromagnetism","Gravity","Strong_interaction","Weak_interaction","Magnetism","Matter","State_of_matter","Organism","Archaea","Bacteria","Eukaryote","Animal","Zoology","Amphibian","Arthropod","Former_Atom_","Particle_physics","Standard_Model","Delisted_Insect","Bird","Fish","Mammal","Former_Cat","Cattle","Dog","Horse","Primate","Former_Human","Rodent","Reptile","Dinosaur","Plant","Botany","Flower","Seed","Tree","Algae","Fungus","Virus","Anatomy","Human_body","Circulatory_system","Blood","Heart","Lung","Digestion","Liver","Immune_system","Skin","Muscle","Nervous_system","Brain","Ear","Eye","Sense","Skeleton","Ecology","Biodiversity","Ecosystem","Extinction","Genetics","DNA","Former_Gene","Heredity","RNA","Metabolism","Molecular_biology","Start-Class_article_Hormone","Protein","Paleontology","Photosynthesis","Reproduction","Sex","Pregnancy","Sleep","Taxonomy","Species","Chemistry","Biochemistry","Inorganic_chemistry","Organic_chemistry","Physical_chemistry","Chemical_element","Periodic_table","Aluminium","Carbon","Copper","Gold","Hydrogen","Iron","Nitrogen","Oxygen","Phosphorus","Silicon","Failed_candidate_Silver","Sulfur","Start-Class_article_Chemical_compound","Delisted_Water","Delisted_Carbon_dioxide","Chemical_bond","Molecule","Chemical_reaction","Acid–base_reaction","Catalysis","Redox","Metal","Alloy","Bronze","Steel","Earth_science","History_of_Earth","Atmosphere_of_Earth","Structure_of_Earth","Season","Flood","Climate_","Climate_change","Weather","Cloud","Rain","Snow","Tornado","Symbol_question.svg_Former_Tropical_cyclone","Wind","Geology","Earthquake","Erosion","Mineral","Former_Plate_tectonics","Rock","Soil","Delisted_Volcano"
url_list = ["Science","Nature","Astronomy","Universe","Solar_System","Sun","Mercury","Venus","Earth","Moon","Mars","Former_Jupiter","Saturn","Uranus","Neptune","Delisted_Asteroid","Former_Big_Bang","Former_Black_hole","Former_Comet","Galaxy","Milky_Way","Natural_satellite","Orbit","Outer_space","Physical_cosmology","Planet","Star","Supernova"]
# url_list = ['Laptop']
print("List of articles: ")
for i in url_list:
  url = "https://en.wikipedia.org/wiki/" + i
  print(i)
  # ping a website or portal for information
  res = requests.get(url)
  html_page = res.content

  soup = BeautifulSoup(html_page, 'html.parser')
  # Python library that is used for web scraping purposes to pull the data out of HTML and XML files
  text = soup.find_all(text=True)

  output = ''
  extractlist = [
      'p',
      'h1',
      'h2',
      'h3',
      'h4',
      'h5',
      'h6',
      'b',
      'a'
  ]

  for t in text:
      if t.parent.name in extractlist:
          output += '{} '.format(t)
    
  # print(output)
  f = open("text.txt", "a")
  f.write(output)
  f.close()

