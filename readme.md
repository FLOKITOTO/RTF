We work with the following technologies:

- Microsoft Azure
- Python
- Pymysql
- Flask
- React
- React-Leaflet

An MVC architecture has been set up.


This project retrieves air traffic data from the [Airlabs API ](https://airlabs.co/) and stores it in a database to display it on a web map layer. 


In postman : 
http://localhost:5000/plane/update

```USAGE  :```

You need to execute [app.py](https://github.com/FLOKITOTO/RTF/blob/master/MVC/src/app.py) and [scrapper.py](https://github.com/FLOKITOTO/RTF/blob/master/MVC/src/scrapper.py)
In frontend run with npm start in another instance

Our database **rtap** is made of two tables **plane** & **flight**

**plane**

| name of column | type of value |
| --- | --- |
| id  | int(11) |
| reg_number  | varchar(255) |
| aircraft_icao | varchar(255) |
<details><summary>CLICK ME SQL</summary>
<p>

#### plane

    ```sql
    CREATE TABLE plane 
    (
     id int(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    reg_number VARCHAR(255),
    aircraft_icao VARCHAR(255) 
    )
    ```

</p>
</details>


**flight**

| name of column | type of value |
| --- | --- |
| id  | int(100) |
| id_plane  | int(100) |
| flight_icao | varchar(255) |
| airline_icao | varchar(255) |
| status | varchar(255) |

<details><summary>CLICK ME SQL</summary>
<p>

#### flight

    ```sql
    CREATE TABLE flight
    (
        id int(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
        id_plane int(100) FOREIGN KEY REFERENCES plane(id),
        flight_icao VARCHAR(255),
        airline_icao  VARCHAR(255),
        status VARCHAR(255)
    )
    ```

</p>
</details>


