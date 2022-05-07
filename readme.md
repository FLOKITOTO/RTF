We work with the following technologies:

- Microsoft Azure
- Python
- Pymysql
- Flask
- React
- React-Leaflet

An MVC architecture has been set up.


This project retrieves air traffic data from the [Airlabs API ](https://airlabs.co/) and stores it in a database to display it on a web map layer. 

Our database **rtap** is made of two tables **plane** & **flight**

**plane**

| name of column | type of value |
| --- | --- |
| reg_number  | varchar(255) |
| aircraft_icao | varchar(255) |
<details><summary>CLICK ME</summary>
<p>

#### plane

    ```sql
    CREATE TABLE plane 
    (
    
    reg_number int,
    aircraft_icao VARCHAR(255) 
    )
    ```

</p>
</details>


**flight**

| name of column | type of value |
| --- | --- |
| id  | int(11) | Primarykey
| flight_icao | varchar(255) |
| airline_icao | varchar(255) |
| status | varchar(255) |

<details><summary>CLICK ME</summary>
<p>

#### flight

    ```sql
    CREATE TABLE flight
    (
        id int,
        flight_icao VARCHAR(255),
        airline_icao  VARCHAR(255),
        status VARCHAR(255)
    )
    ```

</p>
</details>


