# Food-and-Agriculture-Exploratory-Analysis


## Table of Contents
- [Executive Summary](#Executive-Summary)
- [Project Background](#Project-Background)
- [Trends in Emissions and Changes in Land Temperatures](#Trends-in-Emissions-and-Changes-in-Land-Temperatures)
- [Trend in Total Agricultural Yield](#Trend-In-Total-Agricultural-Yield)
- [Explanation of Differences in Product Pricing](#Explanation-of-Differences-in-Product-Pricing)
- [Trends in Inflation and Affordability](#Trends-in-Inflation-and-Affordability)
- [Acknowledgements](#Acknowledgements)


## Executive Summary
This report provides an exploratory analysis of the effects of greenhouse emissions, land temperatures, agricultural yields, producer pricing, and affordability. The objective of this report is to identify trends representative of the sustainability of modern agricultural practices and to provide context for environmental and economic trends for Mexico, Canada, and the United States.

This report analyzes emission data, temperature data, producer pricing, and rates of unaffordability from 2016 to 2023. The accompanying Tableau dashboards provide an interactive comparison for different categories of foods and emissions across the studied countries.

### Key Findings

* **Land Temperatures:** Changes in land temperatures have seen a stark increase and are expected to continue rising for Canada and Mexico; currently, the increase for Canada is approximately 1 °C higher than that of the United States and Mexico.
* **Total Emissions:** The United States has the highest median emissions (approximately 400 kt higher than that of Canada and Mexico). U.S. emissions decreased to 38% of its value from 2021 to 2023. The emissions for Canada have shown a recent rise, while those of Mexico have seen a minimal decrease.
* **Emission Intensity:** Emission intensity is on a slight decline, but has generally remained constant; the exception to this are, "Cereals excluding rise", which had a 75% dropoff in value.
* **Agricultural Yields:** Overall, there is minimally observed variance in the agricultural yield, though some sources (i.e. green corn, potatoes) have shown gradual increases in yields.
* **Producer Prices:** The producer prices of Mexico heavily outweigh those of the United States and Canada combined across all agricultural products. Green coffee from the United States is the exception, with a higher producer price than that of Mexico by 36,000 units of standard local currency.
* **Affordability of a Healthy Diet:** Affordability of a healthy diet has declined for Mexico and the United States (more so by the latter); Canada experienced minimal increases.
*  **Inflation in Food Pricing:** From 2016 to 2022, inflation continued to increase, but began declining thereafter in the United States by as much as 52%.

Overall, agricultural yields for multiple products have remained at constant levels and even shown to increase for some products. The analysis performed did not demonstrate a sensitivity or a strong connection between rising emissions and increases in temperatures to changes in agricultural yield. In contrast, the costs of food and producer pricing have increased, likely as a result of influence from economic policies and market conditions.

## Project Background
This project used data from the Food and Agriculture Organization of the United Nations's publically available datasets, which provide standardized economic data and agricultural/environmental indicators. This project focuses specifically on data for Canada, Mexico, and the United States. The project made use of Excel, Tableau, and MySQL to prepare and visualize the provided data.

## Trends in Emissions and Changes in Land Temperatures
![tempemit.png](TableauDashScreenshots/tempemit.png)
*The overall emission, emission intensity, and temperature growth for Mexico, Canada, and the United States. temperature growth and total emissions are on a rising trend; emission intensity shows gradual decrease. Data taken from Faostat.*

From 2016 to 2021, land temperatures across all three countries experienced major variation; from 2016 to 2019, the median change in temperature was beginning to decrease at different rates for each country, but from 2019 to 2023, Mexico experienced a gradual increment in temperature, while Canada nearly doubled its median change in temperature (234.20% increment); on the other hand, the United States, which had the highest median value, has declined in temperature growth to a value 73.40% that of its value in 2016. This being said, however, despite the changes, all studied countries are expected to continue to rise in median temperatures, but at different rates.

The United States was the highest contributor for all emissions from 2016 to 2023. Despite the rise in emissions from 2016 to 2017 and 2019 to 2020, by 2023, total emissions were only 8% higher than those of 2016. By comparison, Mexico, which overall had the lowest emissions, saw an average increment of 31.73 kt from 2018 to 2020; after this period, however, Mexico has continued to decrease its emissions, reaching a value 88.62% that of 2016. On the other hand, Canada's growth in total emissions followed the same trend as it did in temperature growth: sharp growths from 2020 to 2021 and 2022 to 2023. Despite minimal growth from 2016 to 2019, by the end of the measuring period, Canada's total emissions rose from 245.4 in 2016 to 437.9 in 2023, a 178.44% increment.

Overall emission intensity has remained on a gradual decrease. Almost all sources either experience changes less than 10% from the previous years' value, with increments and decreases in intensity that are practically nominal. Only rice and cereals excluding rice experience sizable changes, with Canada dropping to 24.23% of its intensity measure in 2021 by 2023.

The performed analysis explains that land temperatures will continue to increase; although emissions are generally lower than they were in previous years, all three countries continue to release tens to hundreds of kilotons of emissions each year. It is important to note that this study does not measure the emissions of other countries, whose effect on rising temperatures cannot be denied. According to the European Union's Emissions Database for Global Atmospheric Research, China was responsible for approximately 30% of greenhouse emissions in 2023, with India being responsible for about 8% and Russia 5% of global greenhouse emissions. In studies done more in depth, these contributions to emissions in the atmosphere must be taken into account to obtain an accurate understanding of the relationship between greenhouse gases and the growth in land temperatures.

## Trend in Total Agricultural Yield

![yields.png](TableauDashScreenshots/yields.png)
*The total yield across all sources for Mexico, Canada, and the United States. Overall yields show consistent progress in increments. Data taken from Faostat.*

Agricultural yield has remained at consistent levels despite increases in changes in land temperature and total emissions. The release of greenhouse gases, the rises in global temperature, and the consequent effects this process has had on the environment is more nuanced and outside of the scope of this project.

The NASA article, "*Rising Carbon Dioxide Levels Will Help and Hurt Crops*" explores how the increases in the concentration of Carbon Dioxide in the atmosphere can have the effect of mitigating yield losses while also increasing water use efficiency through the increase in the rate in photosynthesis under certain conditions; this effect, however, does not overshadow any negative effects caused by increased Carbon Dioxide emissions.

In this dataset, yields displayed a low sensitivity with total emissions and rising land temperatures. The behavior of each of the mentioned quantities is likely to be a sum of other factors not included or portrayed by the data being used, such as increases in the quality of the soil being used, or advancements in irrigation, farming practices, and technology.


## Explanation of Differences in Product Pricing

![sampleproducerprices.png](TableauDashScreenshots/sampleproducerprices.png)
*Sample producer prices for Mexico, Canada, and the United States. Producer prices have only increased for all countries. Data taken from Faostat.*

Product prices for Mexico far exceed those of its northern neighbors. Not only that, but product pricing has continued to increase across all products. This result is due to a variety of factors: 
* Mexico imports materials like fertilizers and pesticides, both of which have a high cost because of the war between Russia and Ukraine
* Disruptions in the supply chain caused by COVID-19 impacted the cost of products
*  Mexican producers often receive higher prices because of export demand and high labor costs
*  In a few regions, producers report extortion from organized crime groups, adding to operational costs.

## Trends in Affordability and Inflation
![TableauDashScreenshots/newaffordability.png](TableauDashScreenshots/newaffordability.png)
*The Changes in Affordability and Inflation for Mexico, Canada, and the United States. Shown with changes in inflation is the prevalence of the affordability of a healthy diet. Recently, inflation underwent drastic decreases, while a healthy diet has generally decreased in affordability. Data taken from Faostat.*

Four different measurements were used to determine the affordability of a healthy diet based on the local currency, affordability of a healthy diet based on the purchasing power of an individual, prevalence of unaffordability, and a count for the number of people incapable of affording a healthy diet. Across all of metrics, Mexico had the highest costs of a healthy diet and the highest rates of individuals unable to afford a healthy diet, reaching a peak of about 37.10 million people in 2020, or approximately 30% of the population. Further review reveals that all countries show continuing trends of price increases of a healthy diet. Canada and the United States show marginal increments (1.10 to 1.20 and 16.20 to 16.30, respectively) in the amount of people incapable of affording a healthy diet, but Mexico, has reduced the amount of people by about 9 million.

Inflation rates grew from 2016 to 2022, at which point the inflation rate surged to its highest recorded local maxima, but since then, inflation has reduced been reduced by 66.39% for the United States, 41.89% for Mexico, and 10.90% for Canada. According to Mark Zandi of Moody Analytics, the rise in inflation for the mentioned countries is in part a result of the Russia-Ukraine war, which caused a spike in the price of commodities and oil, leading to higher gas prices and by extension, transport costs for consumer goods.

## Acknowledgements
I would like to thank the Food and Agriculture Organization of the United Nations for their provision of the data that made this project possible.


