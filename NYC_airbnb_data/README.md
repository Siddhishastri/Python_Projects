# NYC Airbnb Data Analysis

## Project Overview
This project analyzes the New York City Airbnb dataset to gain insights into the distribution of listings, price ranges, and availability of properties. The analysis leverages various statistical methods such as mean, median, mode, quantiles, and standard deviation to better understand the data and provide actionable insights. Additionally, visualizations are used to identify patterns and trends in the dataset.

## Dataset Information
The dataset contains detailed information about Airbnb listings in NYC, including:

+ id: Unique identifier for each listing.
+ name: Name of the listing.
+ host_id: Unique identifier for the host.
+ host_name: Name of the host.
+ neighbourhood_group: The general area in NYC (e.g., Manhattan, Brooklyn).
+ neighbourhood: Specific neighborhood where the listing is located.
+ latitude, longitude: Geographical coordinates of the listing.
+ room_type: Type of room (e.g., Entire home/apt, Private room).
+ price: Price per night in USD.
+ minimum_nights: Minimum number of nights required for booking.
+ number_of_reviews: Total number of reviews for the listing.
+ last_review: Date of the most recent review.
+ reviews_per_month: Average number of reviews per month.
+ calculated_host_listings_count: Number of listings a host has.
+ availability_365: Number of days the listing is available per year.

## Project Steps
### Data Loading
+ Objective: Load the dataset into the environment for analysis.
+ Action: Use pandas to read the CSV file and inspect the first few rows of the dataset for initial exploration.

### Data Preprocessing
+ Objective: Clean and preprocess the dataset to prepare it for analysis.
+ Actions:
  + Handle any missing values in key columns such as reviews_per_month.
  + Convert columns like last_review to datetime format for better time-based analysis.
  + Remove outliers in the price column (e.g., extremely high or low values).

### Exploratory Data Analysis (EDA) Using Statistics

1. Descriptive Statistics

+ Objective: Use statistical measures like mean, median, mode, quantiles, and standard deviation to summarize the data.
+ Actions:
  + Calculate the average (mean) price and compare it with the median price to check for skewness.
  + Use quantiles to understand the distribution of price and other numerical features.

2. Standard Deviation

+ Objective: Measure the dispersion of listings' prices around the mean.
+ Action: Use standard deviation to identify the variation in prices.

### Data Visualization
+ Histogram of Prices
Objective: Visualize the distribution of the price column to identify the common price ranges.
+ Action: Create a histogram to show how prices are distributed.

## Key Insights and Conclusions
1. Price Distribution:

+ The average price of an Airbnb listing in NYC is around X USD, with a median of Y USD, indicating a slight skew in the data.
+ Most listings fall within the [quantile ranges] for price, with outliers at both high and low ends.

2. Room Type and Pricing:

+ Entire homes/apartments generally have a higher price compared to private rooms or shared spaces, as expected.

3. Neighborhood Insights:

+ Certain neighborhoods, such as [Top Neighborhoods], have consistently higher prices and demand, making them premium locations for Airbnb listings.

4. Availability:

+ Listings are typically available for around [availability statistic] days per year, indicating that many properties are not rented year-round.

## Technologies and Tools Used
Python: Main language used for analysis.
Pandas: For data loading, cleaning, and preprocessing.
Seaborn & Matplotlib: For data visualization.
Statistics: For data insights (mean, median, mode, quantiles, standard deviation).

## Future Work
+ Explore deeper insights by performing a time-series analysis on booking trends.
+ Apply machine learning models to predict the optimal price for Airbnb listings based on location, room type, and availability.
+ Visualize neighborhood demand using geospatial analysis with latitude and longitude data.
