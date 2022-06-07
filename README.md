# ecommercepipeline
# Motivation
Create a sucessful real-time data streaming pipeline that would help me learn data streaming platforms such as Apache Kafka and Spark.



# GENERAL OVERVIEW

Since our main purpose is to learn in this project and acesss to streaming APIs are often limited, I decided to make my own data generator that produces JSON files in order to act as data vendors. We push this data into kafka topics, and our consumer (Spark Streaminng) applies transformations. This transformed data is then put into our database and then analyzed using our dashboard.

# ARCHITECTURE
![Untitled presentation](https://user-images.githubusercontent.com/70300980/172266644-dc1a4d13-e18b-4f8c-8ef2-370c82bc22f8.png)

# DATABASE DESIGN


![Database ER diagram (crow's foot)](https://user-images.githubusercontent.com/70300980/171524814-20ed47c1-861c-484a-92df-08be518b9349.png)



# HOW TO USE
1 . Install Docker and Docker compose


2 . Clone repository in whatever folder









