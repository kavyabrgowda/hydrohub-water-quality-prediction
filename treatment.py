def get_treatment_suggestions(wqi):
    """
    Evaluate the Water Quality Index (WQI) and provide treatment recommendations.

    Parameters:
    wqi (float): The Water Quality Index value.

    Returns:
    tuple: A summary message and a detailed recommendation with treatment steps.
    """
    if wqi < 50:
        summary = "✅ Safe – Excellent water quality. Suitable for drinking without treatment."
        details = (
            "This water meets WHO standards and is completely safe for drinking. No additional purification is required. "
            "Regular testing ensures it remains free from biological and chemical hazards. It is also ideal for cooking, bathing, and other household uses.\n\n"
            "Maintaining such high-quality water requires proper protection of water sources. Avoid contamination from agricultural runoff, industrial waste, and household chemicals. "
            "Regular inspections and quality assessments can help maintain the purity of water.\n\n"
            "Although no immediate treatment is necessary, ensuring the integrity of your water source through sustainable practices is key. Rainwater harvesting, groundwater recharge, "
            "and responsible disposal of waste contribute significantly to maintaining excellent water quality."
        )
        link = "https://www.who.int/publications/i/item/9789241549950"

    elif wqi < 100:
        summary = "🔹 Moderate – Slight impurities, but still generally safe."
        details = (
            "Water is mostly safe, but it might contain minor impurities. Activated carbon filters can help remove residual taste and odors. "
            "Occasional microbial testing is recommended, especially for well water. Household filters like pitcher filters or faucet-mounted filters work well.\n\n"
            "At this level, water is generally safe for consumption but may have some aesthetic issues such as slight discoloration, mild odor, or a slightly altered taste. "
            "While these are usually harmless, it is advisable to test the water periodically for potential increases in contamination levels.\n\n"
            "To maintain good quality, consider using activated carbon filters, UV sterilization, or boiling before drinking. These methods effectively remove any minor bacterial presence or residual chemicals."
        )
        link ="https://www.epa.gov/ground-water-and-drinking-water/home-drinking-water-filtration-fact-sheet?utm_source=chatgpt.com"

    elif wqi < 250:
        summary = "⚠️ Acceptable – Minor contamination. Filtration recommended."
        details = (
            "The water may contain trace amounts of bacteria and contaminants. Sediments, chlorine, and mild chemical pollutants may be present. "
            "Boiling and UV treatment can reduce microbial risks. Reverse osmosis (RO) or carbon filtration improves taste and safety.\n\n"
            "In rural and semi-urban areas, groundwater contamination is a common concern. Agricultural chemicals, fertilizers, and untreated sewage can lead to increased microbial load. "
            "Regular water testing is crucial to ensure contaminants remain within acceptable limits.\n\n"
            "At this level, investment in water purification systems such as reverse osmosis (RO) or ultraviolet (UV) sterilization is highly recommended. These methods help eliminate both microbial threats and chemical residues, making the water safer for long-term consumption."
        )
        link = "https://www.cdc.gov/drinking-water/about/index.html"

    elif wqi < 500:
        summary = "❌ Poor – Visible contamination risk. Use RO filtration."
        details = (
            "Water contains higher levels of dissolved solids and microbial content. Reverse osmosis (RO) or distillation is necessary for safe consumption. "
            "Possible industrial pollution affects taste, smell, and color. Long-term consumption can lead to health complications.\n\n"
            "Such water is typically found near industrial regions, landfill sites, or areas with improper sewage disposal. Heavy metals such as lead, arsenic, and mercury may be present. "
            "These pose severe health risks, including organ damage and developmental disorders.\n\n"
            "Investing in advanced filtration systems such as multi-stage RO purification, ion exchange, or distillation is necessary. Additionally, regular government oversight and monitoring can help identify sources of contamination and mitigate risks."
        )
        link = "https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies?utm_source=chatgpt.com"

    elif wqi < 1000:
        summary = "⚠️ Unhealthy – High levels of contaminants detected. Avoid consumption."
        details = (
            "Water contains unsafe levels of chemicals, bacteria, and heavy metals. Long-term exposure leads to serious health risks. "
            "Filtration alone is not enough—ozonation and ion exchange are needed. It is not safe for any consumption without industrial-grade purification.\n\n"
            "At this contamination level, water is deemed hazardous for both human consumption and agricultural use. Prolonged exposure can cause neurological damage, kidney failure, and increased risk of cancers. "
            "Industrial runoff, mining activities, and excessive pesticide usage often contribute to such severe contamination.\n\n"
            "Emergency measures must be taken, including switching to alternative water sources and implementing large-scale decontamination efforts such as coagulation, flocculation, and activated carbon treatment."
        )
        link = "https://www.who.int/health-topics/water-sanitation-and-hygiene-wash?utm_source=chatgpt.com#tab=tab_1"

    elif wqi < 2000:
        summary = "☣️ Severely Polluted – Industrial waste possible. Needs heavy purification."
        details = (
              "This water may contain chemical spills, oil residues, and toxic metals. Reverse osmosis, activated carbon, and ion exchange are mandatory. Long-term use can lead to cancer, reproductive harm, and organ failure. It should be treated as potential hazardous waste\n\n."  
             " The pollutants in this category primarily originate from industrial discharge, mining operations, and improper waste disposal. Heavy metals such as lead, mercury, and arsenic can accumulate in the body over time, leading to irreversible health effects. Additionally, petroleum byproducts and volatile organic compounds (VOCs) may cause severe poisoning, skin burns, and respiratory distress upon exposure. The presence of pharmaceutical residues and pesticides further increases toxicity, making this water unsuitable for any use without extensive treatment\n\n."
              " Advanced purification is necessary to make this water safe. Reverse osmosis effectively removes dissolved inorganic substances, while activated carbon filtration helps eliminate organic contaminants and petroleum residues. Ion exchange is crucial for reducing heavy metal concentrations, and additional treatment, such as chemical coagulation or oxidation, may be required for full decontamination. Traditional filtration methods, such as boiling or household water filters, are ineffective at removing industrial toxins. Authorities must intervene to prevent public health risks\n\n."
            " Long-term exposure to this level of pollution is extremely hazardous. Consumption or prolonged contact with this water can cause neurological impairments, organ failure, and developmental disorders in children. Carcinogenic compounds such as benzene and polychlorinated biphenyls (PCBs) significantly increase the risk of cancer. The environmental impact is also devastating, as toxic runoff contaminates groundwater, destroys aquatic ecosystems, and leads to biodiversity loss. Immediate regulatory action is needed to prevent further contamination\n\n."
            ) 
        link = "https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies?utm_source=chatgpt.com"

    elif wqi < 3000:
        summary = "☠️ Toxic – Highly toxic with potential heavy metal poisoning."
        details = (
            "Water is heavily polluted with industrial chemicals and radioactive materials. Toxic exposure can cause neurological damage, immune disorders, and death. Specialized cleanup efforts are needed\n\n." 
             " This level of contamination often results from industrial waste discharge, mining runoff, and nuclear facility leaks. The presence of heavy metals such as lead, cadmium, and chromium poses severe risks to human health. Additionally, radioactive elements like uranium and cesium may be present, increasing the likelihood of radiation poisoning and genetic mutations. The water is unsafe for consumption, agriculture, or any direct human contact without advanced treatment\n\n."
            " Health effects of exposure to this toxic water are life-threatening. Heavy metal poisoning can cause irreversible damage to the nervous system, leading to cognitive impairment, memory loss, and paralysis. Prolonged ingestion can weaken the immune system, making individuals more susceptible to infections and chronic illnesses. Exposure to radioactive contamination significantly raises the risk of cancer, organ failure, and birth defects, making immediate intervention necessary\n\n."
            " Environmental damage caused by such toxic pollution is catastrophic. Aquatic ecosystems suffer from mass fish kills, genetic mutations in wildlife, and loss of biodiversity. Soil and groundwater contamination make agricultural activities impossible, affecting food security in surrounding areas. Specialized cleanup efforts, including bioremediation, chemical neutralization, and radiation containment, are essential to mitigate the long-term consequences. Strict industrial regulations and waste management policies must be enforced to prevent further deterioration\n\n."
            ) 
        link = "https://www.unep.org/topics/chemicals-management/pollution-and-health"

    elif wqi < 4000:
        summary = "⚠️ Hazardous – Chemical and biological hazards present."
        details = (
            "Water is highly contaminated with dangerous chemicals. Contains nuclear waste, arsenic, cyanide, and biohazards. It can cause irreversible health damage or immediate poisoning. Must be treated as hazardous waste\n\n." 
            " This level of water pollution is often linked to industrial accidents, improper hazardous waste disposal, and illegal chemical dumping. High concentrations of arsenic and cyanide make the water acutely toxic, leading to severe poisoning within minutes of ingestion. The presence of nuclear waste significantly increases radiation exposure risks, causing long-term genetic damage and immune suppression. Additionally, biological contaminants such as deadly bacteria, viruses, and biohazardous materials from medical waste pose serious infection threats\n\n."
            " Immediate health effects of exposure include severe respiratory distress, chemical burns, and organ failure. Even minor contact with the skin can lead to irritation, rashes, and toxic absorption into the bloodstream. Prolonged exposure increases the likelihood of neurological disorders, cardiovascular diseases, and cancers. Cyanide poisoning can cause rapid suffocation at the cellular level, leading to coma and death without immediate medical intervention. Arsenic contamination has been linked to chronic illnesses, including liver and kidney damage\n\n."
            " The environmental impact is equally devastating. Toxic runoff from such contaminated water infiltrates soil and groundwater reserves, making entire regions uninhabitable. Aquatic ecosystems suffer mass die-offs as fish and other organisms absorb lethal toxins. Bioaccumulation of heavy metals in the food chain threatens human and animal populations over generations. Cleanup efforts require advanced containment strategies, such as chemical neutralization, radioactive shielding, and extensive bioremediation. Authorities must enforce strict hazardous waste disposal regulations to prevent further ecological disasters\n\n."
            ) 
        link = "https://www.osha.gov/hazardous-waste"

    elif wqi < 5000:
        summary = "☢️ Critical – Water is highly toxic and unsafe."
        details =(
            "Water is classified as a critical environmental hazard. Contains radioactive isotopes, mercury, and chemical toxins. Immediate evacuation and containment required\n\n" 
            " This level of contamination results from severe industrial disasters, nuclear power plant leaks, and improper disposal of hazardous waste. Radioactive isotopes such as uranium, plutonium, and cesium persist in the environment for centuries, making cleanup efforts extremely complex. Mercury contamination, commonly originating from mining and chemical industries, leads to bioaccumulation in aquatic life, posing a severe risk to both wildlife and human populations. Exposure to these contaminants can cause widespread environmental devastation and render entire water sources permanently unsafe\n\n."
            " The health risks associated with this water are extreme. Even minimal exposure can cause acute radiation sickness, neurological damage, and organ failure. Mercury poisoning affects the brain and nervous system, leading to memory loss, speech impairment, and loss of motor functions. Long-term ingestion increases the risk of cancer, genetic mutations, and irreversible cellular damage. Pregnant women and children are particularly vulnerable, as exposure can cause severe birth defects and developmental disorders. Immediate decontamination is required for anyone exposed to this water\n\n."
            " The environmental consequences are catastrophic. Radioactive contamination can spread through groundwater and soil, making large regions uninhabitable for decades. Aquatic ecosystems suffer complete collapse as radiation and toxins disrupt reproductive cycles and cause mass die-offs. Heavy metals accumulate in the food chain, leading to long-term poisoning of humans and animals. Cleanup requires large-scale intervention, including radiation shielding, chemical neutralization, and government-regulated containment zones. Strict enforcement of environmental laws and emergency response plans is crucial to mitigate further damage\n\n."
            ) 
        link = "https://www.unep.org/resources/global-environment-outlook"

    elif wqi < 7500:
        summary = "⚠️ Extremely Dangerous – Must be treated as hazardous waste. Avoid any use."
        details =( 
            "Water contains highly toxic industrial waste, heavy metals, and pathogens. Direct contact can cause severe skin burns, poisoning, and infections. Consumption leads to organ failure and irreversible health effects\n\n." 
            " This level of water contamination is often caused by large-scale industrial accidents, unchecked dumping of hazardous waste, and chemical spills. It contains lethal concentrations of substances such as lead, cadmium, chromium, and benzene, which pose extreme health risks even at low exposure levels. Additionally, the presence of untreated sewage and dangerous pathogens increases the likelihood of widespread disease outbreaks. The water is not only unsuitable for drinking but also highly hazardous for any form of human or animal contact\n\n."
            " Exposure to this water can lead to immediate and severe symptoms, including chemical burns on the skin, respiratory distress, and systemic poisoning. Heavy metal contamination causes long-term health complications such as neurological disorders, kidney failure, and cardiovascular diseases. Ingestion of even small amounts can result in irreversible organ damage and a significantly increased risk of cancer. Direct contact with the water may introduce harmful bacteria, leading to life-threatening infections such as cholera, dysentery, and necrotizing fasciitis\n\n."
            " The environmental impact is equally devastating, as toxic runoff seeps into the soil and groundwater, rendering entire ecosystems uninhabitable. Aquatic life suffers mass die-offs due to bioaccumulation of heavy metals, leading to severe ecological imbalances. Crops irrigated with this water absorb toxic substances, making agricultural products unsafe for consumption. Cleanup requires extensive hazardous waste management, including advanced filtration, chemical neutralization, and large-scale bioremediation efforts. Governments and environmental agencies must enforce strict industrial regulations to prevent further contamination\n\n."
            ) 
        link = "https://sdgs.un.org/goals/goal6"

    elif wqi < 10000:
        summary = "☠️ Lethal Contamination – Contains lethal toxins. Potentially fatal on contact."
        details = (
            "Water is highly acidic, corrosive, and full of neurotoxins. Even touching it can cause serious burns and poisoning. Immediate government intervention is necessary for containment."
            " This level of contamination is typically caused by hazardous industrial discharge, uncontrolled chemical waste dumping, and mining runoff containing sulfuric acid and cyanide. The water may have dangerously high levels of arsenic, mercury, and polychlorinated biphenyls (PCBs), making it a direct threat to human life. Heavy exposure can lead to acute poisoning, paralysis, and multi-organ failure, requiring immediate medical attention and hospitalization\n\n."
            " The corrosive nature of this water can rapidly degrade infrastructure, including metal pipes, concrete foundations, and sewage systems. Communities near affected areas face structural hazards due to pipeline corrosion, leading to environmental disasters such as toxic gas leaks and chemical explosions. Inhalation of fumes from this contaminated water can cause lung damage, severe headaches, dizziness, and long-term neurological disorders\n\n."
            " Wildlife and aquatic ecosystems suffer catastrophic damage as bioaccumulative toxins spread through the food chain. Fish and amphibians experience mass die-offs, while birds and mammals that rely on contaminated water sources face genetic mutations and reproductive failures. Even indirect exposure through soil contamination can render agricultural land permanently infertile, making large areas uninhabitable and devastating local economies reliant on farming\n\n."
            " The severity of this pollution requires immediate large-scale intervention, including hazardous material containment, chemical neutralization, and international environmental disaster response. Specialized teams must assess the contamination level and implement emergency water treatment solutions such as advanced oxidation processes (AOPs) and nanofiltration systems. Governments and global organizations must impose strict regulatory policies and hold responsible parties accountable to prevent future occurrences\n\n."
            " Due to the presence of extreme pollutants, long-term monitoring of the affected region is essential. Contaminated zones must be cordoned off, and communities need to be relocated to prevent further exposure. Restoration efforts should include soil remediation, deep groundwater decontamination, and the implementation of green technologies to restore ecological balance. Failure to address this contamination can lead to irreversible damage, forcing entire populations to abandon their homes due to health risks and unlivable conditions\n\n."
            )
        link = "https://www.who.int/publications/i/item/9789241549950"


    elif wqi < 15000:
        summary = "🌍 Environmental Disaster – Severe pollution. Can cause ecological collapse."
        details = (
            "Water has destroyed local ecosystems due to oil spills, chemical waste, and industrial dumping. Drastic health risks and ecosystem destruction. Urgent cleanup and environmental restoration required\n\n."
            " This contamination level results from extreme industrial negligence, large-scale oil spills, and radioactive waste disposal. Toxic elements such as dioxins, polychlorinated biphenyls (PCBs), and microplastics have permanently altered the biological and chemical composition of the water. The surrounding soil and air may also be contaminated, posing severe health threats to nearby populations. Long-term exposure can lead to respiratory diseases, cancer, and genetic mutations\n\n."
            " The ecological impact is catastrophic, causing mass extinction of marine and freshwater species. Coral reefs, wetlands, and entire river systems become lifeless zones, disrupting food chains and accelerating biodiversity loss. Toxic water seeps into groundwater reserves, making entire regions uninhabitable for both humans and wildlife. The collapse of local fisheries and agricultural lands results in food shortages and economic crises\n\n."
            " Cleanup efforts require an international response, involving large-scale bioremediation, chemical neutralization, and deep-soil decontamination. Technologies such as oil skimmers, dispersants, and microbial treatments must be deployed to mitigate environmental damage. Long-term restoration may take decades, demanding government enforcement, industrial accountability, and sustainable development practices\n\n."
            )
        link = "https://www.unep.org/resources/global-environment-outlook"


    elif wqi < 20000:
        summary = "🚨 Uninhabitable – Extreme contamination levels. Long-term exposure fatal."
        details = (
            "Water is entirely unfit for human, animal, or plant use. Contains radioactive elements, cyanide, and neurotoxins. No known filtration or purification method can make it safe\n\n."
            " This level of pollution is typically caused by nuclear accidents, uncontrolled industrial waste disposal, and chemical warfare residues. The water is laden with hazardous compounds such as plutonium, uranium, and persistent organic pollutants (POPs), which have half-lives spanning decades or even centuries. The toxic composition makes any form of direct contact or inhalation of vapors extremely hazardous, leading to genetic mutations, aggressive cancers, and severe neurological damage\n\n."
            " Entire regions surrounding such contaminated water sources become wastelands, with massive biodiversity loss and soil sterilization. Water runoff poisons groundwater, rivers, and coastal ecosystems, leading to chain reactions of destruction in marine life. Vegetation withers due to toxic soil absorption, eliminating natural filtration and worsening the environmental crisis. Animal populations either flee or suffer widespread disease outbreaks and reproductive failures\n\n."
            " Due to the severity of contamination, conventional water treatment methods such as reverse osmosis or activated carbon are ineffective. Cleanup requires specialized intervention, including nuclear waste containment, deep-earth disposal, and large-scale bioremediation with genetically engineered microorganisms. Governments must enforce strict hazardous waste regulations, conduct long-term monitoring, and restrict human habitation in affected zones to prevent irreversible consequences\n\n."
            )
        link = "https://www.who.int/publications/i/item/9789241549950"


    else:
        summary = "☢️ Apocalyptic – Water is beyond hazardous. Catastrophic toxicity."
        details = (
            "Water contains nuclear waste, chemical warfare residues, and extreme biohazards. It is completely lethal and untreatable. "
            "Immediate government intervention is required for containment.\n\n"
            "At this point, the water is not only undrinkable but poses extreme risks even upon direct contact. Chemical burns, radiation poisoning, and severe health complications are inevitable. "
            "This level of contamination can arise from nuclear accidents, biological warfare, or extreme industrial waste dumping.\n\n"
            "Decontamination is virtually impossible. The only viable solution is complete isolation of the affected water body and large-scale remediation efforts involving global environmental agencies."
        )
        link = "https://www.unep.org/resources/global-environment-outlook"

    return summary, details, link

