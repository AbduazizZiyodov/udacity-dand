# Bay Wheels Data Exploration (2019 Feb.)

## by Abduaziz

<hr>

## **Dataset**

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/en/9/95/Bay_Wheels_logo.png">
</p>

Bay Wheels is a regional public bicycle sharing system in California's San Francisco Bay Area. It is operated by Motivate in a partnership with the Metropolitan Transportation Commission and the Bay Area Air Quality Management District. Bay Wheels is 'the first regional and large-scale bicycle sharing system deployed in California and on the West Coast of the United States. It was established as Bay Area Bike Share in August 2013. As of January 2018, the Bay Wheels system had over 2,600 bicycles in 262 stations across San Francisco, East Bay and San Jose.

# **Dataset**

The dataset used for this exploratory analysis consists of individual trip data. There were 16 columns and after the cleaning process, they are 12. There are 16 types of columns.
Dataset consists:

- Information about the trip (duration ...):
- Information about stations (its cords, name and id)
- Users data (type of their, age, gender ...)

# **Wrangling**

- Fix data type of start/end time. I converted them to DateTime.
- Created new columns using from start time:

  - start_time
  - start_hour_of_day
  - start_day_of_week
  - start_month

- Converted birth year to int from the float.
- Created member age column using member birth year

## **Summary of Findings**

There is no doubt that the number of subscribers is more than customers. Decreasing the number of subscribers on weekends shows us that they ride bikes only during workdays.

After looking dataset, I have brainstormed! I wanted to do something good with locations & prove that locations are also useful for the analysis process. And, it was a good moment for me to use geodata and create heatmaps according to this on my Jupiter notebook.
We can see that in Oakland, Berkeley and the centre of San Francisco (and near san Francisco's port) were many start stations. But in the below map you can see, there is also another region that was many trips despite its area (San Jose & Japantown).

Almost all trips were less than 60 min and most of them were between 1 to 20 minutes range. The maximum duration time is ~ 1400 minutes (almost one day)

We can see that Customer bikers absolutely ride longer than subscribers. Customers ride longer on weekends & I think it may leisure purpose.

## **Key Insights for Presentation**

Subscribers were on shorter trips compared with customers. Most subscribers use the system on their workdays. There was a lot of subscribers than customers on this system. Most of the trips were around 8 AM and 17 PM ( afternoon )